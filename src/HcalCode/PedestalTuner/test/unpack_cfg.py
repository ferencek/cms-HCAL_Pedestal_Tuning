import FWCore.ParameterSet.Config as cms

process = cms.Process("COPY")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.source = cms.Source("HcalTBSource",
    #streams = cms.untracked.vstring('HCAL_Trigger', 'HCAL_DCC700', 'HCAL_DCC701', 'HCAL_DCC702', 'HCAL_DCC703', 'HCAL_DCC704', 'HCAL_DCC705',
                                    #'HCAL_DCC706', 'HCAL_DCC707', 'HCAL_DCC708', 'HCAL_DCC709', 'HCAL_DCC710', 'HCAL_DCC711', 'HCAL_DCC712',
                                    #'HCAL_DCC713', 'HCAL_DCC714', 'HCAL_DCC715', 'HCAL_DCC716', 'HCAL_DCC717', 'HCAL_DCC718', 'HCAL_DCC719',
                                    #'HCAL_DCC720', 'HCAL_DCC721', 'HCAL_DCC722', 'HCAL_DCC723', 'HCAL_DCC724', 'HCAL_DCC725', 'HCAL_DCC726',
                                    #'HCAL_DCC727', 'HCAL_DCC728', 'HCAL_DCC729', 'HCAL_DCC730', 'HCAL_DCC731'
                                    #),
    fileNames = cms.untracked.vstring("file:/bigspool/usc/USC_096978.root")
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('USC_096978_unpacked.root')
)

process.out_step = cms.EndPath(process.output)


