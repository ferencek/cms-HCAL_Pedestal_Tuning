import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.default.limit = 10
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
   dump = cms.untracked.vstring(''),
   file = cms.untracked.string('')
)

process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    toGet = cms.untracked.vstring('Gains','GainWidths','Pedestals','PedestalWidths','QIEData', 'ChannelQuality','ZSThresholds','RespCorrs','L1TriggerObjects','TimeCorrs','LUTCorrs','PFCorrs')
)

process.es_ascii = cms.ESSource("HcalTextCalibrations",
    input = cms.VPSet(
        cms.PSet(
            object = cms.string('ElectronicsMap'),
            file = cms.FileInPath('HcalCode/PedestalTuner/data/version_C_emap.txt')
        )
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)

# process.source = cms.Source("PoolSource",
process.source = cms.Source("HcalTBSource",
    fileNames = cms.untracked.vstring(
        'file:/tmp/ferencek/USC_105458.root'
    )
)

process.options = cms.untracked.PSet( 
    wantSummary = cms.untracked.bool(True) ) ## default is false

# HCAL digis
process.hcalDigis = cms.EDFilter("HcalRawToDigi",
    # Flag to enable unpacking of ZDC channels (default = false)
    UnpackZDC = cms.untracked.bool(False),
    # Optional filter to remove any digi with "data valid" off, "error" on, 
    # or capids not rotating
    FilterDataQuality = cms.bool(True),
    # Do not complain about missing FEDs
    ExceptionEmptyData = cms.untracked.bool(False),
    InputLabel = cms.InputTag("source"),
    # Use the defaults for FED numbers
    # Do not complain about missing FEDs
    ComplainEmptyData = cms.untracked.bool(False),
    # Flag to enable unpacking of calibration channels (default = false)
    UnpackCalib = cms.untracked.bool(True),
    # At most ten samples can be put into a digi, if there are more
    # than ten, firstSample and lastSample select which samples
    # will be copied to the digi
    firstSample = cms.int32(0),
    lastSample = cms.int32(9)
)

process.pedTuner = cms.EDAnalyzer('PedestalTuner',
    tunePedestals      = cms.bool(True),
    pathToOldXMLBricks = cms.untracked.string('test_bricks_old'),
    xmlBricksOutputDir = cms.untracked.string('test_bricks_new'),
    uniformDACSettings = cms.bool(False),
    initialDACSetting  = cms.int32(4),
    SiPMRBXes          = cms.vstring('HO1P10', 'HO2P12'),
    SiPMDACSetting     = cms.int32(7),
    targetPedestal     = cms.double(3.0),
    dac2adc            = cms.double(0.6),
    tagName            = cms.string('test')
)

#Paths
process.raw2digi_step = cms.Path(process.hcalDigis)
process.tuning_step = cms.Path(process.pedTuner)

# Schedule
process.schedule = cms.Schedule(process.raw2digi_step,process.tuning_step)
