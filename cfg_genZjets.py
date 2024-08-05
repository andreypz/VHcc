# Local Variables:
# python-indent-offset: 4
# End:

from VHcc.workflows.genZjets import (
    NanoProcessor as zjets,
)


cfg = {
    "user": {"debug_level": 0,
             "cuts": {
                 "vpt": 0
             }
         },
    "dataset": {
        "jsons": [
            #"src/VHcc/metadata/genZjets_2016.json",
            "src/VHcc/metadata/genZjets_2017.json",
            "src/VHcc/metadata/genZjets_MLM_Herwig_PreUL.json",
            #"src/VHcc/metadata/test_samples_local_DY_UNLOPS.json",
        ],
        "campaign": "UL17",
        "year": "2017",
        "filter": {
            "samples": [
                "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
                "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                "DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos", #2017 sample 
                ###"DYJetsToMuMu_M-50_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos", # 2016 sample
                "DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
                "DYJetsToMuMu_M-50_TuneCP5_ZptWeighted_13TeV-powhegMiNNLO-pythia8-photos",
                "DYJetsToEE_M-50_TuneCP5_ZptWeighted_13TeV-powhegMiNNLO-pythia8-photos",
                #"DYJetsToMuMu_BornSuppressV3_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
                #"DYjetstomumu_01234jets_Pt-0ToInf_13TeV-sherpa", # NanoV7 2016 sample
                #"DYJetsToLL_M-50_TuneCH3_13TeV-madgraphMLM-herwig7",
                "DYToLL_NLO_5FS_TuneCH3_13TeV_matchbox_herwig7",
            ],
            "samples_exclude": [],
        },
    },
    # Input and output files
    "workflow": zjets,
    "output": "output/GenZjets",
    "run_options": {
        "executor": "parsl/condor", "workers": 1, "limit": None,
        #"executor": "futures", "workers": 10, "limit": 1,
        "scaleout": 100,
        "walltime": "01:00:00",
        "mem_per_worker": 2,  # GB
        "chunk": 5000000,
        "max": None,
        "skipbadfiles": None,
        "voms": None,
        "retries": 30,
        "splitjobs": False,
        "requirements": (
            '( TotalCpus >= 8) &&'
            '( Machine != "lx3a44.physik.rwth-aachen.de")'
        ),

    },
}
