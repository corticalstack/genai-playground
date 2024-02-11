Example from Eric Hartford
# https://discord.com/channels/1156064224225808488/1187525864372580424/1202717621422788608

merge_method: linear 
parameters:
  weight: 1.0 
slices:
  - sources:
      - model: cognitivecomputations/dolphin-2.2-70b 
        layer_range: [0, 1]
      - model: 152334H/miqu-1-70b-sf 
        layer_range: [0, 1]
        parameters:
          weight: 0
  - sources:
      - model: cognitivecomputations/dolphin-2.2-70b
        layer_range: [1, 20]
  - sources:
      - model: 152334H/miqu-1-70b-sf
        layer_range: [10, 30]
  - sources:
      - model: cognitivecomputations/dolphin-2.2-70b
        layer_range: [20, 40]
  - sources:
      - model: 152334H/miqu-1-70b-sf
        layer_range: [30, 50]
  - sources:
      - model: cognitivecomputations/dolphin-2.2-70b
        layer_range: [40, 60]
  - sources:
      - model: 152334H/miqu-1-70b-sf
        layer_range: [50, 70]
  - sources:
      - model: cognitivecomputations/dolphin-2.2-70b
        layer_range: [60, 79]
  - sources: 
      - model: cognitivecomputations/dolphin-2.2-70b
        layer_range: [79, 80]
      - model: 152334H/miqu-1-70b-sf
        layer_range: [79, 80]
        parameters:
          weight: 0
dtype: float16
tokenizer_source: model:cognitivecomputations/dolphin-2.2-70b 