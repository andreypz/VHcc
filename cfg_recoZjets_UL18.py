# Local Variables:
# python-indent-offset: 4
# End:

from VHcc.workflows.recoZjets import (NanoProcessor as zjets,)

cfg = {
    "user": {"debug_level": 0,
             "cuts": {
                 "vpt": 0
             },
             "trigger": "double"
             #"trigger": "single"
         },
    "dataset": {
        "jsons": [
            #"src/VHcc/metadata/run2UL18_files.json",
            "src/VHcc/metadata/Investigation_files.json",
            #"src/VHcc/metadata/run2UL18_files_PoCo_SingleMuon.json",
            #"src/VHcc/metadata/run2UL18_files_PoCo_EGamma.json",
        ],
        "campaign": "2018_UL",
        "year": "2018",
        "filter": {
            "samples": [
                "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
                "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                "SingleMuon_Run2018",
                "EGamma_Run2018"
                #"DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
                #"DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
                #"Run2UL18_DoubleMuon",
                #"Run2UL18_SingleMuon",
                #"Run2UL18_EGamma_GT36"
           ],

            "samples_exclude": [],
        },
    },

    "weights": {
        "common":{
            "inclusive":{
                #"lumiMasks": "Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                "PU": None,
                "JME": "jec_compiled.pkl.gz",
                #"BTV": { "DeepJetC": "DeepJet_ctagSF_Summer20UL17_interp.root"},
                "LSF": {
                    "ele_ID 2018": "wp80iso",
                    "ele_Reco 2018": "RecoAbove20",
                    "ele_Reco_low 2018": "RecoBelow20",
                    ###"mvaEleID-Fall17-noIso-V2-wp80", ??
                    "mu_Reco 2018_UL": "NUM_TrackerMuons_DEN_genTracks",
                    ##"mu_HLT 2017_UL": "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoTight",
                    "mu_ID 2018_UL": "NUM_TightID_DEN_TrackerMuons",
                    "mu_Iso 2018_UL": "NUM_TightRelIso_DEN_TightIDandIPCut",
                    "mu_ID_low NUM_TightID_DEN_TrackerMuons": "Efficiency_muon_trackerMuon_Run2018_UL_ID.histo.json",
                    "mu_Reco_low NUM_TrackerMuons_DEN_genTracks": "Efficiency_muon_generalTracks_Run2018_UL_trackerMuon.histo.json",
                },
            },
        },
    },
    "systematic": {
        "JERC": False,
        "weights": False,

    },
    "workflow": zjets,
    "output": "output/recoZjets_UL18",
    "run_options": {
        #"executor": "parsl/condor", "workers": 1,  "limit": None,
        "executor": "futures", "workers": 10,  "limit": 10,
        "scaleout": 350,
        "walltime": "01:00:00",
        "mem_per_worker": 2,  # GB
        "chunk": 500000,
        "max": None,
        "skipbadfiles": True,
        "voms": None,
        "retries": 20,
        "splitjobs": False,
        "requirements": (
            '( Machine != "lx3a44.physik.rwth-aachen.de")'
        ),
    },
}
