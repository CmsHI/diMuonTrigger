import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUESettings_cfi import *

hiSignal = cms.EDProducer("Pythia6PtYDistGun",
                      PGunParameters = cms.PSet(ParticleID = cms.vint32(443), 
                                                MaxY  = cms.double(2.5),
                                                MinY  = cms.double(-2.5),   
                                                MinPt = cms.double(0.0),
                                                MaxPt = cms.double(20.0),
                                                MinPhi = cms.double(-3.14159265359),
                                                MaxPhi = cms.double(3.14159265359), 
                                                YBinning = cms.int32(500),     
                                                PtBinning = cms.int32(100000),
                                                kinematicsFile = cms.FileInPath('GeneratorInterface/HiGenCommon/data/flatYPt.root')
                                                ),
                         PythiaParameters = cms.PSet(pythiaUESettingsBlock,
                                                     JpsiMuMuDecay = cms.vstring('BRAT(858) = 0 ! switch off',
                                                                                 'BRAT(859) = 1 ! switch on',
                                                                                 'BRAT(860) = 0 ! switch off',
                                                                                 'MDME(858,1) = 0 ! switch off',
                                                                                 'MDME(859,1) = 1 ! switch on',
                                                                                 'MDME(860,1) = 0 ! switch off'),
                                                     parameterSets = cms.vstring('pythiaUESettings', 
                                                                                 'JpsiMuMuDecay')
                                                     )
                      )

ProductionFilterSequence = cms.Sequence(hiSignal)
