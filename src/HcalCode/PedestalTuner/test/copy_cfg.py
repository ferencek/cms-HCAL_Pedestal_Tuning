import FWCore.ParameterSet.Config as cms

process = cms.Process("COPY")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # CRAFT Run 67977
        '/store/data/Commissioning08/MinimumBias/RAW/v1/000/067/977/6283A5A8-E7A5-DD11-B226-001D09F24FE7.root'
    )
)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('CRAFT_Run67977.root')
)

process.out_step = cms.EndPath(process.output)


