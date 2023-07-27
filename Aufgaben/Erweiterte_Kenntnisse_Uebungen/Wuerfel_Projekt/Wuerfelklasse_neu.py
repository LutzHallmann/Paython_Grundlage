from dataclasses import dataclass, field
from typing import ClassVar, List, Dict
import random
import json
import os


@dataclass
class Wuerfel():
    MIN_AUGEN: ClassVar[int] = 1
    MAX_AUGEN: ClassVar[int] = 6

    __min_augen: int
    __max_augen: int
    __wuerfe: int
    __ergebnisse: Dict
    __runde: int

    def __init__(self, min: int, max: int, wuerfe: int, ergebnisse: List = [], runde: int = 0):

        self.min_augen = min  # Calls setter method automatically
        self.max_augen = max  # Calls setter method automatically

        if (len(ergebnisse) == 0):
            self.__ergebnisse = {"results": []}
        else:
            self.__ergebnisse = {"results": ergebnisse}

        if self.__min_augen > self.__max_augen:
            raise ValueError("min_augen has to be smaller than max_augen.")

        if runde == 0:
            self.__runde = 1
        else:
            self.__runde = runde + 1

        if wuerfe < 10:
            raise ValueError("Die needs to be rolled at least 10 times.")

        self.__wuerfe = wuerfe

        for w in range(wuerfe):
            self.wuerfeln()

    # Getter/Setter min_augen
    @property
    def min_augen(self) -> int:
        # print("Getting min_augen")
        return self.__min_augen

    @min_augen.setter
    def min_augen(self, value: int):
        # print("Setting min_augen")
        try:
            self.__min_augen = int(value)
        except ValueError as e:
            # print(str(e))
            print(f"Value '{value}' for min could not be converted to int. " +
                  f"Using default value '{Wuerfel.MIN_AUGEN}' " +
                  f"for instanciation of {self.__class__.__name__} instead.")
            self.__min_augen = Wuerfel.MIN_AUGEN

    # Getter/Setter max_augen
    @property
    def max_augen(self) -> int:
        # print("Getting max_augen")
        return self.__max_augen

    @max_augen.setter
    def max_augen(self, value: int):
        # print("Setting max_augen")
        try:
            self.__max_augen = int(value)
        except ValueError as e:
            # print(str(e))
            print(f"Value '{value}' for max could not be converted to int. " +
                  f"Using default value'{Wuerfel.MAX_AUGEN}' " +
                  f"for instanciation of {self.__class__.__name__} instead.")
            self.__max_augen = Wuerfel.MAX_AUGEN

    def wuerfeln(self) -> int:
        result = random.randint(self.__min_augen, self.__max_augen)
        self.__ergebnisse["results"].append(result)
        return result

    def __str__(self):
        return (f"Lower Bound: {self.min_augen}; " +
                f"Upper Bound: {self.max_augen}")

    def summe(self) -> int:
        """
        Gesamtsumme der bisherigen Wuerfelergebnisse
        """
        return sum(self.__ergebnisse["results"])

    def durchschnitt(self) -> float:
        """
        Durchschnitt der bisherigen Wuerfelergebnisse
        """
        if (len(self.__ergebnisse["results"]) > 0):
            return sum(self.__ergebnisse["results"]) / len(self.__ergebnisse["results"])
        else:
            return 0

    def anzahl(self) -> int:
        """
        Gesamtzahl der bisherigen Wuerfe
        """
        return len(self.__ergebnisse["results"])

    def speichern(self, path: str) -> None:
        """
        Speichere als .json auf Festplatte
        """
        with(open(path, "w") as f):
            dct = self.__ergebnisse
            dct["min"] = self.__min_augen
            dct["max"] = self.__max_augen
            dct["wuerfe"] = self.__wuerfe
            dct["runde"] = self.__runde
            # dct["wuerfe"] = self.__wuerfe
            f.write(json.dumps(dct))

    @classmethod
    def laden(cls, path: str):
        with(open(path) as f):
            dct = json.load(f)
            w = Wuerfel(dct["min"], dct["max"], dct["wuerfe"], ergebnisse=dct["results"], runde=dct["runde"])

        return w

    def statistik(self) -> str:
        s = (
                f"Anzahl Wurfrunden: {self.__runde:>15} \n" +
                f"Gesamt gewürfelte Augenzahl: {self.summe():>5} \n" +
                f"Durchschnittliche Augenzahl: {self.durchschnitt():>5.4g}"
        )
        return s


if __name__ == "__main__":

    file = "historie.json"
    if file in os.listdir():
        wuerfel = Wuerfel.laden("historie.json")
    else:
        wuerfel = Wuerfel(min=1, max=20, wuerfe=10)

    print(wuerfel.statistik())
    wuerfel.speichern("historie.json")

    # for i in range(1000):
    #     wuerfel.wuerfeln()

    # print(f"min_augen: {wuerfel.min_augen}")
    # print(f"max_augen: {wuerfel.max_augen}")
    # print(f"anzahl: {wuerfel.anzahl()}")
    # print(f"summe: {wuerfel.summe()}")
    # print(f"durchschnitt: {wuerfel.durchschnitt()}")