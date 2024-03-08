``` mermaid
graph TD
  Zucc[Zuccini] --- |Companion| Ring[Ringelblume];
  Zucc --- |Companion| Mint[Minze];
  Zucc --- |Companion| Rosm[Rosmarin];
  Zucc --- |Companion| Lave[Lavendel];
  Zucc --- |Companion| Bohn;
  Zucc --- |Companion| Toma[Tomaten];
  Zucc --- |Companion| Pepp[Pepperoni];
  Zucc --- |Companion| Nasturtium;
  Zucc --- |Companion| Marigold;
  Zucc --- |Companion| Dill;
  Zucc --- |Companion| Thyme;
  Zucc --- |Companion| Garlic[Knoblauch];
  Zucc --- |Companion| Onio;
  Zucc --- |Companion| Borage;
  Zucc --- |Companion| Yarrow;
  Zucc --- |Companion| Peas;
  Zucc --- |Companion| Oregano;
  Zucc --- |Companion| Sage;
  Zucc --- |Companion| Corn;
  Zucc --- |Companion| Clover;
  Zucc --- |Companion| Alyssum;
  Zucc --- |Companion| Echinacea;
  Zucc --- |Companion| Zinnias;
  Zucc --- |Companion| Phacelia;

  Bohn --- |Companion| Rosm;
  Bohn --- |Companion| Toma;
  Bohn --- |Companion| Himb;
  Bohn --- |Nicht passend| Pepp;
  Bohn --- |Nicht passend| Onio[Zwiebeln];
  %%Bohn --- |Nicht passend| Sunf[Sonnenblume];
  %%Bohn --- |Nicht passend| Fennel;
  %%Bohn --- |Nicht passend| Pota[Kartoffel];
  %%Bohn --- |Companion| Corn[Mais];
  %%%Bohn --- |Companion| Kale[Kohl];
  %%%Bohn --- |Nicht passend| Pumpkin;
  %%%Bohn --- |Nicht passend| SweetPotatoes;

  Goji[Goji] --- |Companion| Spin[Spinat];
  Goji --- |Companion| Heid[Heidelbeeren];
  Goji --- |Companion| Himb[Himbeeren];
  Goji --- |Companion| Toma;

  Leek[Lauch] --- |Companion| Himb;
  Leek --- |Companion| Himb;
  Leek --- |Companion| Toma;
  Leek --- |Companion| Ring;
  Leek --- |Companion| Chill
  Leek --- |Nicht passend| Bohn;
  Leek --- |Companion| Pepp;
  Leek --- |Companion| Onio;
  Leek --- |Companion| Rosm;
  Leek --- |Companion| Thyme;
  Leek --- |Companion| Nasturtium;
  Leek --- |Companion| Marigold;
  Leek --- |Companion| Carrots;
  Leek --- |Companion| Parsnips;
  Leek --- |Companion| Celery;
  Leek --- |Companion| Beets;
  Leek --- |Companion| Brassicas;
  Leek --- |Companion| Chamomile;

  Himb --- |Companion| Spin;
  Himb --- |Companion| Garlic;
  Himb --- |Companion| Marigold;
  Himb --- |Companion| Thyme;
  Himb --- |Companion| Dill;
  Himb --- |Companion| Borage;
  Himb --- |Companion| Yarrow;
  Himb --- |Companion| Asparagus;
  Himb --- |Companion| Rhubarb;
  Himb --- |Companion| Lettuce;

  Toma --- |Companion| Basi[Basilikum];
  Toma --- |Companion| Ring;
  Toma --- |Companion| Lave;
  Toma --- |Companion| Mint;
  Toma --- |Nicht passend| Pepp;
  Toma --- |Nicht passend| Dill;
  Toma --- |Nicht passend| Rosm;
  Toma --- |Companion| Garlic;
  Toma --- |Companion| Marigold;
  Toma --- |Companion| Sunf;
  Toma --- |Companion| Borage;
  Toma --- |Nicht passend| Gurk;
  Toma --- |Companion| Chives;
  Toma --- |Companion| Asparagus;
  Toma --- |Companion| Carrots;
  Toma --- |Companion| Oregano;
  Toma --- |Companion| Sage;
  Toma --- |Companion| Parsley;
  Toma --- |Companion| Radishes;

  Pepp --- |Companion| Basi;
  Pepp --- |Companion| Dill;
  Pepp --- |Companion| Lave;
  Pepp --- |Companion| Garlic;
  Pepp --- |Companion| Onio;
  Pepp --- |Companion| Nasturtium;
  Pepp --- |Companion| Sunf;
  Pepp --- |Companion| Fennel;
  Pepp --- |Companion| Peas;
  Pepp --- |Companion| Clover;
  Pepp --- |Companion| Cowpeas;
  Pepp --- |Companion| PakChoi;
  Pepp --- |Companion| Radish;

  Heid --- |Companion| Erdb[Erdbeere]
  Heid --- |Companion| Thyme
  Heid --- |Companion| Farn
  Heid --- |Companion| Immergrüne
  Heid --- |Companion| Hartriegel
  Heid --- |Companion| Rhododendron
  Heid --- |Companion| Azalee
  Heid --- |Companion| Heidekraut
  Heid --- |Companion| Preiselbeersträucher
  Heid --- |Companion| Akelei
  Heid --- |Companion| Berglorbeer
  Heid --- |Companion| Stechpalme
  Heid --- |Companion| Hortensie
  Heid --- |Companion| Fliederbusch

  Chill[Chilli] --- |Companion| Basi
  Chill[Chilli] --- |Companion| Onio
  Chill[Chilli] --- |Companion| Leek
  Chill[Chilli] --- |Companion| Garlic
  Chill[Chilli] --- |Companion| Chives
  Chill[Chilli] --- |Companion| Scallions
  Chill[Chilli] --- |Companion| Shallots

  Zucc -->  Foli{Blätter};
  Zucc -->  Wuch{Wuchernd};
  Bohn --> Nitr{Stickstoff};
  Bohn -->  Wuch{Wuchernd};
  Leek -->  Repe{Insektenschutz};

  Basi --> Repe
  Garlic --> Repe
  Fennel --> Repe
  Lemongrass --> Repe
  Marigold --> Repe
  Mint --> Repe
  Chrysanthemum --> Repe
  Alliums  --> Repe


     classDef selected fill:#9f6,stroke:#333,stroke-width:2px;
     classDef planned fill:#f96,stroke:#333,stroke-width:4px;
     class Toma,Pepp,Heid,Chill,Zucc,Bohn,Stra,Goji,Leek,Mint,Basi,Erdb selected
     class Lave,Farn,Garlic,Spin,Rosm planned

    linkStyle 0 stroke-width:2px,fill:none,stroke:pink;
    linkStyle 1 stroke-width:2px,fill:none,stroke:blue;
    linkStyle 2 stroke-width:2px,fill:none,stroke:yellow;
    linkStyle 3 stroke-width:2px,fill:none,stroke:green;
```
[Companions](https://www.gardenersworld.com/plants/10-companion-plants-to-grow/)
