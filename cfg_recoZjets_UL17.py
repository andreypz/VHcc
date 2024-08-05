# Local Variables:
# python-indent-offset: 4
# End:

from VHcc.workflows.recoZjets import (NanoProcessor as zjets,)

cfg = {
    "user": {"debug_level": 0,
             "cuts": {
                 "vpt": 60
             },
             "trigger": "double"
             #"trigger": "single"
         },
    "dataset": {
        "jsons": [
            "src/VHcc/metadata/run2UL17_files_DATA.json",
            "src/VHcc/metadata/run2UL17_files_DYJets.json"
            #"src/VHcc/metadata/run2UL17_test.json"
        ],
        "campaign": "2017_UL",
        "year": "2017",
        "filter": {
            "samples": [
                "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
                "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8",
                "DYJetsToMuMu_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
                "DYJetsToEE_M-50_massWgtFix_TuneCP5_13TeV-powhegMiNNLO-pythia8-photos",
                "DoubleMuon_Run2017B-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleMuon_Run2017C-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleMuon_Run2017D-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleMuon_Run2017E-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleMuon_Run2017F-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleEG_Run2017B-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleEG_Run2017C-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleEG_Run2017D-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleEG_Run2017E-UL2017_MiniAODv2_NanoAODv9-v1",
                "DoubleEG_Run2017F-UL2017_MiniAODv2_NanoAODv9-v1",
           ]
        },
    },

    "weights": {
        "common":{
            "inclusive":{
                "lumiMasks":"Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                "PU": None,
                "JME": "jec_compiled.pkl.gz",
                #"BTV": { "DeepJetC": "DeepJet_ctagSF_Summer20UL17_interp.root"},
                "LSF": {
                    "ele_Reco 2017": "RecoAbove20",
                    "ele_Reco_low 2017": "RecoBelow20",
                    "ele_ID 2017": "wp80iso",
                    "mu_Reco 2017_UL": "NUM_TrackerMuons_DEN_genTracks",
                    "mu_HLT 2017_UL": "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoTight",
                    "mu_ID 2017_UL": "NUM_TightID_DEN_TrackerMuons",
                    "mu_Iso 2017_UL": "NUM_TightRelIso_DEN_TightIDandIPCut",
                    "mu_ID_low NUM_TightID_DEN_TrackerMuons": "Efficiency_muon_trackerMuon_Run2017_UL_ID.histo.json",
                    "mu_Reco_low NUM_TrackerMuons_DEN_genTracks": "Efficiency_muon_generalTracks_Run2017_UL_trackerMuon.histo.json",
                },

            },
        },
    },
    "systematic": {
        "JERC": False,
        "weights": False,
    },
    "workflow": zjets,
    "output": "output/recoZjets_UL17",
    "run_options": {
        "executor": "parsl/condor", "workers": 1,  "limit": None,
        #"executor": "futures", "workers": 10,  "limit": 1,
        "scaleout": 350,
        "walltime": "01:00:00",
        "mem_per_worker": 2,  # GB
        "chunk": 500000,
        "max": None,
        "skipbadfiles": False,
        "voms": None,
        "retries": 20,
        "splitjobs": False,
        "requirements": (
            '( Machine != "lx3a44.physik.rwth-aachen.de")'
        ),
    },
}
