
import json
import os
import base64
import asyncio
import aiohttp
import pprint
import urllib.parse
import datetime


url = "https://centralusdtapp34.epicorsaas.com/SaaS840/api/v1/"
b64 = base64.b64encode(('jgrissom:Nimsgotadoor!1').encode("ascii")).decode("ascii") 
creds = {'Authorization':'Basic ' + b64}

thingsToReplace = ["({","})",",","/","}","{","(",")","$","_____","____","___","__"]

list = [
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ABCCodeSvc/index.html" , "Erp.BO.ABCCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ACTTypeRevisionSvc/index.html" , "Erp.BO.ACTTypeRevisionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ACTTypeSvc/index.html" , "Erp.BO.ACTTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGAFIPCommDocTypeSvc/index.html" , "Erp.BO.AGAFIPCommDocTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGAFIPResponsibilitySvc/index.html" , "Erp.BO.AGAFIPResponsibilitySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGCAEASvc/index.html" , "Erp.BO.AGCAEASvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGCustomsSvc/index.html" , "Erp.BO.AGCustomsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGDestinationSvc/index.html" , "Erp.BO.AGDestinationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGEmissionPointSvc/index.html" , "Erp.BO.AGEmissionPointSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGIDDocTypeSvc/index.html" , "Erp.BO.AGIDDocTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGInvoicingPointSvc/index.html" , "Erp.BO.AGInvoicingPointSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGLocationSvc/index.html" , "Erp.BO.AGLocationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGProvinceSvc/index.html" , "Erp.BO.AGProvinceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGUserCompSvc/index.html" , "Erp.BO.AGUserCompSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AGWebServiceConfigSvc/index.html" , "Erp.BO.AGWebServiceConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APAdjustmentSvc/index.html" , "Erp.BO.APAdjustmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APAgingTrackerSvc/index.html" , "Erp.BO.APAgingTrackerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APAlcHedSvc/index.html" , "Erp.BO.APAlcHedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APBOEMultiGenSvc/index.html" , "Erp.BO.APBOEMultiGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APBankFileImportSvc/index.html" , "Erp.BO.APBankFileImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APChkGrpSvc/index.html" , "Erp.BO.APChkGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APInvDtlSearchSvc/index.html" , "Erp.BO.APInvDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APInvGrpSvc/index.html" , "Erp.BO.APInvGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APInvMscSearchSvc/index.html" , "Erp.BO.APInvMscSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APInvSearchSvc/index.html" , "Erp.BO.APInvSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APInvoiceLoadSvc/index.html" , "Erp.BO.APInvoiceLoadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APInvoiceSvc/index.html" , "Erp.BO.APInvoiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APLOCSvc/index.html" , "Erp.BO.APLOCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APPIWriteOffSvc/index.html" , "Erp.BO.APPIWriteOffSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APPromNoteGrpSvc/index.html" , "Erp.BO.APPromNoteGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APPromissoryNotesSvc/index.html" , "Erp.BO.APPromissoryNotesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.APTranSearchSvc/index.html" , "Erp.BO.APTranSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARAdjustmentSvc/index.html" , "Erp.BO.ARAdjustmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARAgingTrackerSvc/index.html" , "Erp.BO.ARAgingTrackerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARBOEMultiGenSvc/index.html" , "Erp.BO.ARBOEMultiGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARInvSearchSvc/index.html" , "Erp.BO.ARInvSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARInvcDtlSearchSvc/index.html" , "Erp.BO.ARInvcDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARInvoiceLoadSvc/index.html" , "Erp.BO.ARInvoiceLoadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARInvoiceSvc/index.html" , "Erp.BO.ARInvoiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARLOCSvc/index.html" , "Erp.BO.ARLOCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARPIStatusChgSvc/index.html" , "Erp.BO.ARPIStatusChgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARPIWriteOffSvc/index.html" , "Erp.BO.ARPIWriteOffSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARPromissoryNotesSvc/index.html" , "Erp.BO.ARPromissoryNotesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ARRecTrackerSvc/index.html" , "Erp.BO.ARRecTrackerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ATPSvc/index.html" , "Erp.BO.ATPSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AccountBudgetSvc/index.html" , "Erp.BO.AccountBudgetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ActualCostAllocationWorkbenchSvc/index.html" , "Erp.BO.ActualCostAllocationWorkbenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ActualCostingCategorySvc/index.html" , "Erp.BO.ActualCostingCategorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AddPartWhseSvc/index.html" , "Erp.BO.AddPartWhseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AdjustReturnContainerSvc/index.html" , "Erp.BO.AdjustReturnContainerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.Adjustment1099Svc/index.html" , "Erp.BO.Adjustment1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AgingCreditSvc/index.html" , "Erp.BO.AgingCreditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AgingRptFmtSvc/index.html" , "Erp.BO.AgingRptFmtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlcBatchSchedSearchSvc/index.html" , "Erp.BO.AlcBatchSchedSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlcHedSvc/index.html" , "Erp.BO.AlcHedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlcHedTgtStampSearchSvc/index.html" , "Erp.BO.AlcHedTgtStampSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlcHistorySvc/index.html" , "Erp.BO.AlcHistorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlertGroupSvc/index.html" , "Erp.BO.AlertGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlertLogSvc/index.html" , "Erp.BO.AlertLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AllocBatchSvc/index.html" , "Erp.BO.AllocBatchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AlternatePartSvc/index.html" , "Erp.BO.AlternatePartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AnalysisCodeSvc/index.html" , "Erp.BO.AnalysisCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ApplyCreditMemoSvc/index.html" , "Erp.BO.ApplyCreditMemoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ApplyDebitMemoSvc/index.html" , "Erp.BO.ApplyDebitMemoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AprvVendSvc/index.html" , "Erp.BO.AprvVendSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AssetAddEntrySvc/index.html" , "Erp.BO.AssetAddEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AssetClosePeriodSvc/index.html" , "Erp.BO.AssetClosePeriodSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AssetDispEntrySvc/index.html" , "Erp.BO.AssetDispEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AssetImpairSvc/index.html" , "Erp.BO.AssetImpairSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AttrBinSvc/index.html" , "Erp.BO.AttrBinSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AttrWhseGroupSvc/index.html" , "Erp.BO.AttrWhseGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AttributSvc/index.html" , "Erp.BO.AttributSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AutoBankRecSvc/index.html" , "Erp.BO.AutoBankRecSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.AutoTranReversalSvc/index.html" , "Erp.BO.AutoTranReversalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BENonAdmExpenseSvc/index.html" , "Erp.BO.BENonAdmExpenseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BESalesDomesticSvc/index.html" , "Erp.BO.BESalesDomesticSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BESalesIntracomSvc/index.html" , "Erp.BO.BESalesIntracomSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BOLGenerateSearchSvc/index.html" , "Erp.BO.BOLGenerateSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BOLSvc/index.html" , "Erp.BO.BOLSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankAcctSvc/index.html" , "Erp.BO.BankAcctSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankAdjEntrySvc/index.html" , "Erp.BO.BankAdjEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankBatchPayMethodSrchSvc/index.html" , "Erp.BO.BankBatchPayMethodSrchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankBatchSvc/index.html" , "Erp.BO.BankBatchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankBrnchSvc/index.html" , "Erp.BO.BankBrnchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankFeeSvc/index.html" , "Erp.BO.BankFeeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankFileImportSvc/index.html" , "Erp.BO.BankFileImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankFundTranSvc/index.html" , "Erp.BO.BankFundTranSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankPayMethodSearchSvc/index.html" , "Erp.BO.BankPayMethodSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BankTransactionCodeSvc/index.html" , "Erp.BO.BankTransactionCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BatchOpsSvc/index.html" , "Erp.BO.BatchOpsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BdnCdSvc/index.html" , "Erp.BO.BdnCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BdnSetActPctSvc/index.html" , "Erp.BO.BdnSetActPctSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BinSizeSvc/index.html" , "Erp.BO.BinSizeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BomSearchSvc/index.html" , "Erp.BO.BomSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BookOrdSvc/index.html" , "Erp.BO.BookOrdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BoxNumberSvc/index.html" , "Erp.BO.BoxNumberSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BudgetCodeSvc/index.html" , "Erp.BO.BudgetCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BurdenSetSvc/index.html" , "Erp.BO.BurdenSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BusEntitiesSvc/index.html" , "Erp.BO.BusEntitiesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BusinessCategorySvc/index.html" , "Erp.BO.BusinessCategorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.BuyerWorkbenchSvc/index.html" , "Erp.BO.BuyerWorkbenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCCountCycleSvc/index.html" , "Erp.BO.CCCountCycleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCDtlSearchSvc/index.html" , "Erp.BO.CCDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCHdrSearchSvc/index.html" , "Erp.BO.CCHdrSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCPartSelectUpdSvc/index.html" , "Erp.BO.CCPartSelectUpdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCPeriodDefnSvc/index.html" , "Erp.BO.CCPeriodDefnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCScheduleSvc/index.html" , "Erp.BO.CCScheduleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCSheetSearchSvc/index.html" , "Erp.BO.CCSheetSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CCTagSearchSvc/index.html" , "Erp.BO.CCTagSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CNCustomsDeclBillDtlSearchSvc/index.html" , "Erp.BO.CNCustomsDeclBillDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CNCustomsDeclarationBillSvc/index.html" , "Erp.BO.CNCustomsDeclarationBillSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CNCustomsHandbookSvc/index.html" , "Erp.BO.CNCustomsHandbookSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CNGLJrnAttachmentsSvc/index.html" , "Erp.BO.CNGLJrnAttachmentsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CNGoldenTaxInterfaceSvc/index.html" , "Erp.BO.CNGoldenTaxInterfaceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COAActCatSvc/index.html" , "Erp.BO.COAActCatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COABookSearchSvc/index.html" , "Erp.BO.COABookSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COAMapDataSvc/index.html" , "Erp.BO.COAMapDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COAPESvc/index.html" , "Erp.BO.COAPESvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COARefSearchSvc/index.html" , "Erp.BO.COARefSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COARefSegSearchSvc/index.html" , "Erp.BO.COARefSegSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COASegBalanceSvc/index.html" , "Erp.BO.COASegBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COASegValuesSvc/index.html" , "Erp.BO.COASegValuesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COASegmentSearchSvc/index.html" , "Erp.BO.COASegmentSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COASvc/index.html" , "Erp.BO.COASvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COMagneticMediaReportSvc/index.html" , "Erp.BO.COMagneticMediaReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COMagneticMediaSetupSvc/index.html" , "Erp.BO.COMagneticMediaSetupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.COOneTimeSvc/index.html" , "Erp.BO.COOneTimeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CORevelationSvc/index.html" , "Erp.BO.CORevelationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CRMCallSvc/index.html" , "Erp.BO.CRMCallSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CRMCompSvc/index.html" , "Erp.BO.CRMCompSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CalculatedFieldSvc/index.html" , "Erp.BO.CalculatedFieldSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CallTypeSvc/index.html" , "Erp.BO.CallTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CapPromiseSvc/index.html" , "Erp.BO.CapPromiseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CapabilitySvc/index.html" , "Erp.BO.CapabilitySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CarrierSvc/index.html" , "Erp.BO.CarrierSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CartonStageSvc/index.html" , "Erp.BO.CartonStageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashDtlSearchSvc/index.html" , "Erp.BO.CashDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashFlowSvc/index.html" , "Erp.BO.CashFlowSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashGrpSvc/index.html" , "Erp.BO.CashGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashHeadSearchSvc/index.html" , "Erp.BO.CashHeadSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashRecSearchSvc/index.html" , "Erp.BO.CashRecSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashRecSvc/index.html" , "Erp.BO.CashRecSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CashReceiptAdjustmentSvc/index.html" , "Erp.BO.CashReceiptAdjustmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ChangeImpactSvc/index.html" , "Erp.BO.ChangeImpactSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CheckDigitSvc/index.html" , "Erp.BO.CheckDigitSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CheckLstSvc/index.html" , "Erp.BO.CheckLstSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CheckRecSearchSvc/index.html" , "Erp.BO.CheckRecSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ClosePeriodSvc/index.html" , "Erp.BO.ClosePeriodSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CoaSegAcctSearchSvc/index.html" , "Erp.BO.CoaSegAcctSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.Code1099Svc/index.html" , "Erp.BO.Code1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CompanyLicenseInfoSvc/index.html" , "Erp.BO.CompanyLicenseInfoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CompanySvc/index.html" , "Erp.BO.CompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfigurationDesignSvc/index.html" , "Erp.BO.ConfigurationDesignSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfigurationRuntimeSvc/index.html" , "Erp.BO.ConfigurationRuntimeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfiguratorAssembliesSvc/index.html" , "Erp.BO.ConfiguratorAssembliesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfiguratorCodeEditorSvc/index.html" , "Erp.BO.ConfiguratorCodeEditorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfiguratorDefSvc/index.html" , "Erp.BO.ConfiguratorDefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfiguratorExpVarsSvc/index.html" , "Erp.BO.ConfiguratorExpVarsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfiguratorRuleSvc/index.html" , "Erp.BO.ConfiguratorRuleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConfiguratorUDFuncsSvc/index.html" , "Erp.BO.ConfiguratorUDFuncsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConsMonitorSvc/index.html" , "Erp.BO.ConsMonitorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConsTgtDefSvc/index.html" , "Erp.BO.ConsTgtDefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConsTypeSvc/index.html" , "Erp.BO.ConsTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ConsolidToParentSvc/index.html" , "Erp.BO.ConsolidToParentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ContactSvc/index.html" , "Erp.BO.ContactSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ContainerClassSvc/index.html" , "Erp.BO.ContainerClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ContainerTrackingSvc/index.html" , "Erp.BO.ContainerTrackingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ContractRenewalSearchSvc/index.html" , "Erp.BO.ContractRenewalSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ControlIDExtractSvc/index.html" , "Erp.BO.ControlIDExtractSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ControlIDSvc/index.html" , "Erp.BO.ControlIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CorrectiveActionSvc/index.html" , "Erp.BO.CorrectiveActionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CostAdjustmentSvc/index.html" , "Erp.BO.CostAdjustmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CostBurdenSearchSvc/index.html" , "Erp.BO.CostBurdenSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CostLaborSearchSvc/index.html" , "Erp.BO.CostLaborSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CostPartSearchSvc/index.html" , "Erp.BO.CostPartSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CostWorkBenchSvc/index.html" , "Erp.BO.CostWorkBenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CountTagSvc/index.html" , "Erp.BO.CountTagSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CountryPortSearchSvc/index.html" , "Erp.BO.CountryPortSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CountrySvc/index.html" , "Erp.BO.CountrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CourseRevisionSearchSvc/index.html" , "Erp.BO.CourseRevisionSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CourseSchSvc/index.html" , "Erp.BO.CourseSchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CourseSvc/index.html" , "Erp.BO.CourseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CreateIDNumbersSvc/index.html" , "Erp.BO.CreateIDNumbersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CreditCardProcSvc/index.html" , "Erp.BO.CreditCardProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CreditCardProcessorSvc/index.html" , "Erp.BO.CreditCardProcessorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CreditCardTypeSvc/index.html" , "Erp.BO.CreditCardTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CreditManagerSvc/index.html" , "Erp.BO.CreditManagerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CreditTranSvc/index.html" , "Erp.BO.CreditTranSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CrossDockSvc/index.html" , "Erp.BO.CrossDockSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CurrExRateSearchSvc/index.html" , "Erp.BO.CurrExRateSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CurrExRateSvc/index.html" , "Erp.BO.CurrExRateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CurrRateGrpSvc/index.html" , "Erp.BO.CurrRateGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CurrencySvc/index.html" , "Erp.BO.CurrencySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustBankSearchSvc/index.html" , "Erp.BO.CustBankSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustBillToSvc/index.html" , "Erp.BO.CustBillToSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustCntSvc/index.html" , "Erp.BO.CustCntSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustContImportSvc/index.html" , "Erp.BO.CustContImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustGrupSvc/index.html" , "Erp.BO.CustGrupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustPriceListSearchSvc/index.html" , "Erp.BO.CustPriceListSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustReminderSearchSvc/index.html" , "Erp.BO.CustReminderSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustShipSummarySvc/index.html" , "Erp.BO.CustShipSummarySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustShipSvc/index.html" , "Erp.BO.CustShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustXPrtSearchSvc/index.html" , "Erp.BO.CustXPrtSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustXPrtSvc/index.html" , "Erp.BO.CustXPrtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustomerPartXRefSvc/index.html" , "Erp.BO.CustomerPartXRefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.CustomerSvc/index.html" , "Erp.BO.CustomerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DBFieldSearchSvc/index.html" , "Erp.BO.DBFieldSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DEPartFIFOTranHistSvc/index.html" , "Erp.BO.DEPartFIFOTranHistSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DMRActnSearchSvc/index.html" , "Erp.BO.DMRActnSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DMRProcessingSvc/index.html" , "Erp.BO.DMRProcessingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DataCheckSvc/index.html" , "Erp.BO.DataCheckSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DataExportSvc/index.html" , "Erp.BO.DataExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DataFixSvc/index.html" , "Erp.BO.DataFixSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DefExpRecogSvc/index.html" , "Erp.BO.DefExpRecogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DeliveryTypeSvc/index.html" , "Erp.BO.DeliveryTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandCntDtlSearchSvc/index.html" , "Erp.BO.DemandCntDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandContractSvc/index.html" , "Erp.BO.DemandContractSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandEntrySvc/index.html" , "Erp.BO.DemandEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandFromOrdersSvc/index.html" , "Erp.BO.DemandFromOrdersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandImportEntrySvc/index.html" , "Erp.BO.DemandImportEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandLogSvc/index.html" , "Erp.BO.DemandLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandMassReviewSvc/index.html" , "Erp.BO.DemandMassReviewSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandPartSearchSvc/index.html" , "Erp.BO.DemandPartSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandReconcileSearchSvc/index.html" , "Erp.BO.DemandReconcileSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DemandReconcileSvc/index.html" , "Erp.BO.DemandReconcileSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DepSearchSvc/index.html" , "Erp.BO.DepSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DmdMassGrpSvc/index.html" , "Erp.BO.DmdMassGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DrawingsSvc/index.html" , "Erp.BO.DrawingsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DriverSvc/index.html" , "Erp.BO.DriverSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DropShipDtlSearchSvc/index.html" , "Erp.BO.DropShipDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DropShipSvc/index.html" , "Erp.BO.DropShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynAttrClassDtlSearchSvc/index.html" , "Erp.BO.DynAttrClassDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynAttrClassSvc/index.html" , "Erp.BO.DynAttrClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynAttrMasterDtlSvc/index.html" , "Erp.BO.DynAttrMasterDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynAttrValueSetLangDescSvc/index.html" , "Erp.BO.DynAttrValueSetLangDescSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynAttrValueSetSvc/index.html" , "Erp.BO.DynAttrValueSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynAttrValueSvc/index.html" , "Erp.BO.DynAttrValueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.DynCalSvc/index.html" , "Erp.BO.DynCalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EADSvc/index.html" , "Erp.BO.EADSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECCCustomerSvc/index.html" , "Erp.BO.ECCCustomerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECCExtensionSvc/index.html" , "Erp.BO.ECCExtensionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECCSupplierSvc/index.html" , "Erp.BO.ECCSupplierSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECCUDMapSvc/index.html" , "Erp.BO.ECCUDMapSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECCWebServiceSvc/index.html" , "Erp.BO.ECCWebServiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECOOprSearchSvc/index.html" , "Erp.BO.ECOOprSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECORevSearchSvc/index.html" , "Erp.BO.ECORevSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ECSalesReportSvc/index.html" , "Erp.BO.ECSalesReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EDIImportSvc/index.html" , "Erp.BO.EDIImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EInvOperatorSvc/index.html" , "Erp.BO.EInvOperatorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ETCAddrValidationSvc/index.html" , "Erp.BO.ETCAddrValidationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ElectronicInterfaceSvc/index.html" , "Erp.BO.ElectronicInterfaceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ElectronicReportSvc/index.html" , "Erp.BO.ElectronicReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmailTemplateSvc/index.html" , "Erp.BO.EmailTemplateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmpBasicSvc/index.html" , "Erp.BO.EmpBasicSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmpCourseSvc/index.html" , "Erp.BO.EmpCourseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmpExpenseGroupSvc/index.html" , "Erp.BO.EmpExpenseGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmpExpenseSvc/index.html" , "Erp.BO.EmpExpenseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmpRoleSearchSvc/index.html" , "Erp.BO.EmpRoleSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EmpYTDLoadSvc/index.html" , "Erp.BO.EmpYTDLoadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EngWorkBenchSvc/index.html" , "Erp.BO.EngWorkBenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EntityGLCSvc/index.html" , "Erp.BO.EntityGLCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EpicorAgentSvc/index.html" , "Erp.BO.EpicorAgentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EquipLocSvc/index.html" , "Erp.BO.EquipLocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EquipMeterSvc/index.html" , "Erp.BO.EquipMeterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EquipStatusSvc/index.html" , "Erp.BO.EquipStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EquipSvc/index.html" , "Erp.BO.EquipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.EquipTypeSvc/index.html" , "Erp.BO.EquipTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ErpMetaFxSvc/index.html" , "Erp.BO.ErpMetaFxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtCompanySvc/index.html" , "Erp.BO.ExtCompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtFinAnlsCdSvc/index.html" , "Erp.BO.ExtFinAnlsCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPREmpSvc/index.html" , "Erp.BO.ExtPREmpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPRHolidaySvc/index.html" , "Erp.BO.ExtPRHolidaySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPRLayoutSvc/index.html" , "Erp.BO.ExtPRLayoutSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPRPayClassSvc/index.html" , "Erp.BO.ExtPRPayClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPRPayTypeSvc/index.html" , "Erp.BO.ExtPRPayTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPRProcGrpSvc/index.html" , "Erp.BO.ExtPRProcGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtPlantSearchSvc/index.html" , "Erp.BO.ExtPlantSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ExtWarehouseSearchSvc/index.html" , "Erp.BO.ExtWarehouseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAClassSvc/index.html" , "Erp.BO.FAClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAGroupSvc/index.html" , "Erp.BO.FAGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAMethodSvc/index.html" , "Erp.BO.FAMethodSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAReportCatSvc/index.html" , "Erp.BO.FAReportCatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FARevalueRegSearchSvc/index.html" , "Erp.BO.FARevalueRegSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FARevalueSvc/index.html" , "Erp.BO.FARevalueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FASpreadCodeSvc/index.html" , "Erp.BO.FASpreadCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FATranSearchSvc/index.html" , "Erp.BO.FATranSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAssetFieldsSearchSvc/index.html" , "Erp.BO.FAssetFieldsSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAssetRegSvc/index.html" , "Erp.BO.FAssetRegSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FAssetSvc/index.html" , "Erp.BO.FAssetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FOBSvc/index.html" , "Erp.BO.FOBSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSAInstallationTypeSvc/index.html" , "Erp.BO.FSAInstallationTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSASyncWbSvc/index.html" , "Erp.BO.FSASyncWbSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSAssetClassSvc/index.html" , "Erp.BO.FSAssetClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSAssetConditionSvc/index.html" , "Erp.BO.FSAssetConditionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSCallCdSvc/index.html" , "Erp.BO.FSCallCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSCallDtSearchSvc/index.html" , "Erp.BO.FSCallDtSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSContCdSvc/index.html" , "Erp.BO.FSContCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSContDtSearchSvc/index.html" , "Erp.BO.FSContDtSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSContSNSearchSvc/index.html" , "Erp.BO.FSContSNSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSTechSearchSvc/index.html" , "Erp.BO.FSTechSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FSWarrCdSvc/index.html" , "Erp.BO.FSWarrCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FinChargeSvc/index.html" , "Erp.BO.FinChargeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FinReportConfigSvc/index.html" , "Erp.BO.FinReportConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FirstArtSvc/index.html" , "Erp.BO.FirstArtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FiscalCalSvc/index.html" , "Erp.BO.FiscalCalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FiscalPerSearchSvc/index.html" , "Erp.BO.FiscalPerSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FiscalYrSearchSvc/index.html" , "Erp.BO.FiscalYrSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ForecastSvc/index.html" , "Erp.BO.ForecastSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.Form1099Svc/index.html" , "Erp.BO.Form1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FormTypeSvc/index.html" , "Erp.BO.FormTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.FreightServiceSvc/index.html" , "Erp.BO.FreightServiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLAccountMassDelSvc/index.html" , "Erp.BO.GLAccountMassDelSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLAccountMassUpdSvc/index.html" , "Erp.BO.GLAccountMassUpdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLAccountSvc/index.html" , "Erp.BO.GLAccountSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLAcctDispSvc/index.html" , "Erp.BO.GLAcctDispSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLAlcHedSvc/index.html" , "Erp.BO.GLAlcHedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBCOASegValuesSvc/index.html" , "Erp.BO.GLBCOASegValuesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBCOASegmentSearchSvc/index.html" , "Erp.BO.GLBCOASegmentSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBCOASvc/index.html" , "Erp.BO.GLBCOASvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBGLAccountSvc/index.html" , "Erp.BO.GLBGLAccountSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBGLAcctDispSvc/index.html" , "Erp.BO.GLBGLAcctDispSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBGLBookSvc/index.html" , "Erp.BO.GLBGLBookSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBGLCOARefAcctSvc/index.html" , "Erp.BO.GLBGLCOARefAcctSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBGLCOARefTypeSvc/index.html" , "Erp.BO.GLBGLCOARefTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBJrnlCodeSvc/index.html" , "Erp.BO.GLBJrnlCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBookPerSearchSvc/index.html" , "Erp.BO.GLBookPerSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLBookSvc/index.html" , "Erp.BO.GLBookSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCOARefAcctSvc/index.html" , "Erp.BO.GLCOARefAcctSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCOARefTypeSvc/index.html" , "Erp.BO.GLCOARefTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCTAcctCntxtSvc/index.html" , "Erp.BO.GLCTAcctCntxtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCTEntitySearchSvc/index.html" , "Erp.BO.GLCTEntitySearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCntrlSvc/index.html" , "Erp.BO.GLCntrlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCntrlTypeSvc/index.html" , "Erp.BO.GLCntrlTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCntrlTypeSysSvc/index.html" , "Erp.BO.GLCntrlTypeSysSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLCostTransSvc/index.html" , "Erp.BO.GLCostTransSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLDailyBalanceSvc/index.html" , "Erp.BO.GLDailyBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLJournalEntrySvc/index.html" , "Erp.BO.GLJournalEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLJrnDtlSvc/index.html" , "Erp.BO.GLJrnDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLJrnGrpSvc/index.html" , "Erp.BO.GLJrnGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLJrnSrcSearchSvc/index.html" , "Erp.BO.GLJrnSrcSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLPeriodBalSearchSvc/index.html" , "Erp.BO.GLPeriodBalSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLPurchSvc/index.html" , "Erp.BO.GLPurchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLRptColSetSearchSvc/index.html" , "Erp.BO.GLRptColSetSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLTrackerSvc/index.html" , "Erp.BO.GLTrackerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GLTransMatchSvc/index.html" , "Erp.BO.GLTransMatchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GUIBatchAssignLNSvc/index.html" , "Erp.BO.GUIBatchAssignLNSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GUIGroupSearchSvc/index.html" , "Erp.BO.GUIGroupSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GUINumSvc/index.html" , "Erp.BO.GUINumSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GUITaxDeclareSvc/index.html" , "Erp.BO.GUITaxDeclareSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GUIVendDfltDocTypeSvc/index.html" , "Erp.BO.GUIVendDfltDocTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GetAmortizationSvc/index.html" , "Erp.BO.GetAmortizationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GetContractRenewalSvc/index.html" , "Erp.BO.GetContractRenewalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GetRequestSvc/index.html" , "Erp.BO.GetRequestSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlRptMasSvc/index.html" , "Erp.BO.GlRptMasSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbAlertSvc/index.html" , "Erp.BO.GlbAlertSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbCurrRateGrpSvc/index.html" , "Erp.BO.GlbCurrRateGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbCurrencySvc/index.html" , "Erp.BO.GlbCurrencySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbCustomerSearchSvc/index.html" , "Erp.BO.GlbCustomerSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbForecastSvc/index.html" , "Erp.BO.GlbForecastSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbPartSearchSvc/index.html" , "Erp.BO.GlbPartSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbPerConSearchSvc/index.html" , "Erp.BO.GlbPerConSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbTableSvc/index.html" , "Erp.BO.GlbTableSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlbVendorSearchSvc/index.html" , "Erp.BO.GlbVendorSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.GlobalInputVarsSvc/index.html" , "Erp.BO.GlobalInputVarsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.HXProjectSearchSvc/index.html" , "Erp.BO.HXProjectSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.HelpDeskSvc/index.html" , "Erp.BO.HelpDeskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.HelpDeskTopicSvc/index.html" , "Erp.BO.HelpDeskTopicSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ICReceiptSearchSvc/index.html" , "Erp.BO.ICReceiptSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ICommCodeSvc/index.html" , "Erp.BO.ICommCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IDNumbersSvc/index.html" , "Erp.BO.IDNumbersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMABCCodeSvc/index.html" , "Erp.BO.IMABCCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMCashHeadSvc/index.html" , "Erp.BO.IMCashHeadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMCompanySvc/index.html" , "Erp.BO.IMCompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMCustomerSvc/index.html" , "Erp.BO.IMCustomerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMEmpBasicSvc/index.html" , "Erp.BO.IMEmpBasicSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMEmpExpenseSvc/index.html" , "Erp.BO.IMEmpExpenseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMExtSysChunkDefSvc/index.html" , "Erp.BO.IMExtSysChunkDefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMFSCallhdSvc/index.html" , "Erp.BO.IMFSCallhdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMFSContCdSvc/index.html" , "Erp.BO.IMFSContCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMFSContHdSvc/index.html" , "Erp.BO.IMFSContHdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMFSWarrCdSvc/index.html" , "Erp.BO.IMFSWarrCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMInvTransferSvc/index.html" , "Erp.BO.IMInvTransferSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMInvcHeadSvc/index.html" , "Erp.BO.IMInvcHeadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMInventoryQtyAdjSvc/index.html" , "Erp.BO.IMInventoryQtyAdjSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMLaborHedSvc/index.html" , "Erp.BO.IMLaborHedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMMiscChrgSvc/index.html" , "Erp.BO.IMMiscChrgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMMoveRequestSvc/index.html" , "Erp.BO.IMMoveRequestSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMMscShpHdSvc/index.html" , "Erp.BO.IMMscShpHdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMMtlQueueSvc/index.html" , "Erp.BO.IMMtlQueueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMPartBinSvc/index.html" , "Erp.BO.IMPartBinSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMPartSvc/index.html" , "Erp.BO.IMPartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMPlantSvc/index.html" , "Erp.BO.IMPlantSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMPurMiscSvc/index.html" , "Erp.BO.IMPurMiscSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMRMAHeadSvc/index.html" , "Erp.BO.IMRMAHeadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMSalesTaxSvc/index.html" , "Erp.BO.IMSalesTaxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMSerialNoSvc/index.html" , "Erp.BO.IMSerialNoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMShipDtlSvc/index.html" , "Erp.BO.IMShipDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMWarehseSvc/index.html" , "Erp.BO.IMWarehseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IMWhseBinSvc/index.html" , "Erp.BO.IMWhseBinSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.INGSTR1ReportSvc/index.html" , "Erp.BO.INGSTR1ReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.INGSTR2ReportExportSvc/index.html" , "Erp.BO.INGSTR2ReportExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.INGSTR2ReportImportSvc/index.html" , "Erp.BO.INGSTR2ReportImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.INLUTBondSvc/index.html" , "Erp.BO.INLUTBondSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.INMaterialBurdenSvc/index.html" , "Erp.BO.INMaterialBurdenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IRWarehseSearchSvc/index.html" , "Erp.BO.IRWarehseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IStatTrnSvc/index.html" , "Erp.BO.IStatTrnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImageCategorySvc/index.html" , "Erp.BO.ImageCategorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImageDefaultCategorySvc/index.html" , "Erp.BO.ImageDefaultCategorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImageLayerSvc/index.html" , "Erp.BO.ImageLayerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImageSubCategorySearchSvc/index.html" , "Erp.BO.ImageSubCategorySearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImageSvc/index.html" , "Erp.BO.ImageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImportGrpSvc/index.html" , "Erp.BO.ImportGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImportLaborAndSchedParamsSvc/index.html" , "Erp.BO.ImportLaborAndSchedParamsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ImportSubsidSvc/index.html" , "Erp.BO.ImportSubsidSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IncotermsSvc/index.html" , "Erp.BO.IncotermsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IndClassCodeSearchSvc/index.html" , "Erp.BO.IndClassCodeSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IndirectSvc/index.html" , "Erp.BO.IndirectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IndustryClassSvc/index.html" , "Erp.BO.IndustryClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspAttrSvc/index.html" , "Erp.BO.InspAttrSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspDataTrackerSvc/index.html" , "Erp.BO.InspDataTrackerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspPlanRevSearchSvc/index.html" , "Erp.BO.InspPlanRevSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspPlanSvc/index.html" , "Erp.BO.InspPlanSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspProcessingSvc/index.html" , "Erp.BO.InspProcessingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspResultsSvc/index.html" , "Erp.BO.InspResultsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InspectrSvc/index.html" , "Erp.BO.InspectrSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InternalPartCrossRefSvc/index.html" , "Erp.BO.InternalPartCrossRefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IntgWorkbenchSvc/index.html" , "Erp.BO.IntgWorkbenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IntraStatReportSvc/index.html" , "Erp.BO.IntraStatReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InvTransferSvc/index.html" , "Erp.BO.InvTransferSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InvcGrpSvc/index.html" , "Erp.BO.InvcGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InventoryAdvisorSvc/index.html" , "Erp.BO.InventoryAdvisorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InventoryAttributeSearchSvc/index.html" , "Erp.BO.InventoryAttributeSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InventoryQtyAdjSvc/index.html" , "Erp.BO.InventoryQtyAdjSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InvoiceIStatTrnSvc/index.html" , "Erp.BO.InvoiceIStatTrnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.InvoiceReceiptMatchSvc/index.html" , "Erp.BO.InvoiceReceiptMatchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.IssueReturnSvc/index.html" , "Erp.BO.IssueReturnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JCDeptSvc/index.html" , "Erp.BO.JCDeptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JCShiftSvc/index.html" , "Erp.BO.JCShiftSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JPAPPerBillStmtSvc/index.html" , "Erp.BO.JPAPPerBillStmtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JPAPPerBillSvc/index.html" , "Erp.BO.JPAPPerBillSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JPPerBillStmtSvc/index.html" , "Erp.BO.JPPerBillStmtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JPPerBillSvc/index.html" , "Erp.BO.JPPerBillSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobAddlInfoSvc/index.html" , "Erp.BO.JobAddlInfoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobAdjustmentSvc/index.html" , "Erp.BO.JobAdjustmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobAsmSearchSvc/index.html" , "Erp.BO.JobAsmSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobAsmblCostsSvc/index.html" , "Erp.BO.JobAsmblCostsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobClosingCdSvc/index.html" , "Erp.BO.JobClosingCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobClosingSvc/index.html" , "Erp.BO.JobClosingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobEntrySvc/index.html" , "Erp.BO.JobEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobLogViewerSvc/index.html" , "Erp.BO.JobLogViewerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobManagerSvc/index.html" , "Erp.BO.JobManagerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobMtlSearchSvc/index.html" , "Erp.BO.JobMtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobOperSearchSvc/index.html" , "Erp.BO.JobOperSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobPartSvc/index.html" , "Erp.BO.JobPartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobProdSearchSvc/index.html" , "Erp.BO.JobProdSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobSchedSvc/index.html" , "Erp.BO.JobSchedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JobStatusSvc/index.html" , "Erp.BO.JobStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JournalTrackerDetailSvc/index.html" , "Erp.BO.JournalTrackerDetailSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.JrnlCodeSvc/index.html" , "Erp.BO.JrnlCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.KBMaxSvc/index.html" , "Erp.BO.KBMaxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.KanBanTypeSvc/index.html" , "Erp.BO.KanBanTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.KanbanPartSearchSvc/index.html" , "Erp.BO.KanbanPartSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.KanbanReceiptsSvc/index.html" , "Erp.BO.KanbanReceiptsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LabExpCdSvc/index.html" , "Erp.BO.LabExpCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LaborApprovalSvc/index.html" , "Erp.BO.LaborApprovalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LaborDtlGroupSvc/index.html" , "Erp.BO.LaborDtlGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LaborDtlSearchSvc/index.html" , "Erp.BO.LaborDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LaborDtlSvc/index.html" , "Erp.BO.LaborDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LaborSvc/index.html" , "Erp.BO.LaborSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LbrPrjRoleSvc/index.html" , "Erp.BO.LbrPrjRoleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LegalNumCnfgSvc/index.html" , "Erp.BO.LegalNumCnfgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LegalNumGenOptsSvc/index.html" , "Erp.BO.LegalNumGenOptsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LegalNumHistorySvc/index.html" , "Erp.BO.LegalNumHistorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LegalNumPrefixSvc/index.html" , "Erp.BO.LegalNumPrefixSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LifecycleSvc/index.html" , "Erp.BO.LifecycleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LinkQuoteSearchSvc/index.html" , "Erp.BO.LinkQuoteSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.Local001SearchSvc/index.html" , "Erp.BO.Local001SearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LocationInventoryMtlSearchSvc/index.html" , "Erp.BO.LocationInventoryMtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LocationInventorySearchSvc/index.html" , "Erp.BO.LocationInventorySearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LocationMgmtSvc/index.html" , "Erp.BO.LocationMgmtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LockboxGroupSvc/index.html" , "Erp.BO.LockboxGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LockboxLayoutRecordTypeSvc/index.html" , "Erp.BO.LockboxLayoutRecordTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LockboxLayoutSvc/index.html" , "Erp.BO.LockboxLayoutSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LogAPInvSvc/index.html" , "Erp.BO.LogAPInvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LogInvAprvVoidSvc/index.html" , "Erp.BO.LogInvAprvVoidSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LogInvGrpSvc/index.html" , "Erp.BO.LogInvGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LookupDataSvc/index.html" , "Erp.BO.LookupDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LotSelectUpdateSvc/index.html" , "Erp.BO.LotSelectUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LotSeqSvc/index.html" , "Erp.BO.LotSeqSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.LotTraceSvc/index.html" , "Erp.BO.LotTraceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MESMenuSearchSvc/index.html" , "Erp.BO.MESMenuSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MESMenuSvc/index.html" , "Erp.BO.MESMenuSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MICRPrinterSvc/index.html" , "Erp.BO.MICRPrinterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MLSupplyDemandSvc/index.html" , "Erp.BO.MLSupplyDemandSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MPSSvc/index.html" , "Erp.BO.MPSSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MXAPInvFolioImportSvc/index.html" , "Erp.BO.MXAPInvFolioImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MXAPPaymentFolioImportSvc/index.html" , "Erp.BO.MXAPPaymentFolioImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MXGLJournalFolioImportSvc/index.html" , "Erp.BO.MXGLJournalFolioImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MXPACConfigurationSvc/index.html" , "Erp.BO.MXPACConfigurationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MXTaxRegimeSvc/index.html" , "Erp.BO.MXTaxRegimeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MXWHTaxCertificateSvc/index.html" , "Erp.BO.MXWHTaxCertificateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MaintReqSvc/index.html" , "Erp.BO.MaintReqSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MaintResourceSvc/index.html" , "Erp.BO.MaintResourceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MangCustSearchSvc/index.html" , "Erp.BO.MangCustSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ManufacturerSvc/index.html" , "Erp.BO.ManufacturerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MassIssueToMfgSvc/index.html" , "Erp.BO.MassIssueToMfgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MassOperationReplaceSvc/index.html" , "Erp.BO.MassOperationReplaceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MassPartReplaceDeleteSvc/index.html" , "Erp.BO.MassPartReplaceDeleteSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MassRscGrpReplaceSvc/index.html" , "Erp.BO.MassRscGrpReplaceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MasterPackSvc/index.html" , "Erp.BO.MasterPackSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MaterialQueueSvc/index.html" , "Erp.BO.MaterialQueueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MaterialQueueTranTypesSvc/index.html" , "Erp.BO.MaterialQueueTranTypesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MetaUIHarnessSvc/index.html" , "Erp.BO.MetaUIHarnessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MetaUISharedSvc/index.html" , "Erp.BO.MetaUISharedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MeterReadSvc/index.html" , "Erp.BO.MeterReadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MfgPartSvc/index.html" , "Erp.BO.MfgPartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MinMaxSfyMassUpdSvc/index.html" , "Erp.BO.MinMaxSfyMassUpdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MiscChrgSvc/index.html" , "Erp.BO.MiscChrgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MiscShipSvc/index.html" , "Erp.BO.MiscShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MiscShipToSearchSvc/index.html" , "Erp.BO.MiscShipToSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MktgActSvc/index.html" , "Erp.BO.MktgActSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MktgAdvSvc/index.html" , "Erp.BO.MktgAdvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MktgCampSvc/index.html" , "Erp.BO.MktgCampSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MktgEvntSvc/index.html" , "Erp.BO.MktgEvntSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MktgLstSvc/index.html" , "Erp.BO.MktgLstSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MktgPubSvc/index.html" , "Erp.BO.MktgPubSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileAttachmentSvc/index.html" , "Erp.BO.MobileAttachmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileCRMSvc/index.html" , "Erp.BO.MobileCRMSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileEmpExpenseSvc/index.html" , "Erp.BO.MobileEmpExpenseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileLaborSvc/index.html" , "Erp.BO.MobileLaborSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileSettingsSvc/index.html" , "Erp.BO.MobileSettingsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileUserNotificationOptionSvc/index.html" , "Erp.BO.MobileUserNotificationOptionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MobileUserNotificationSvc/index.html" , "Erp.BO.MobileUserNotificationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MoveRequestSvc/index.html" , "Erp.BO.MoveRequestSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MrpProcQueueSvc/index.html" , "Erp.BO.MrpProcQueueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MrpProcSvc/index.html" , "Erp.BO.MrpProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MrpQueueSvc/index.html" , "Erp.BO.MrpQueueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MsgIDCounterSvc/index.html" , "Erp.BO.MsgIDCounterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.MultiShipSearchSvc/index.html" , "Erp.BO.MultiShipSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NARelationshipSvc/index.html" , "Erp.BO.NARelationshipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NLICPReportSvc/index.html" , "Erp.BO.NLICPReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NLVATDeclarationSvc/index.html" , "Erp.BO.NLVATDeclarationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NaturalAcctCurrSearchSvc/index.html" , "Erp.BO.NaturalAcctCurrSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NettingSvc/index.html" , "Erp.BO.NettingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NonConfSvc/index.html" , "Erp.BO.NonConfSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.NonFinBalDirectSvc/index.html" , "Erp.BO.NonFinBalDirectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OTSSearchSvc/index.html" , "Erp.BO.OTSSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OpMasterSvc/index.html" , "Erp.BO.OpMasterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OpStdSvc/index.html" , "Erp.BO.OpStdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OpTextSvc/index.html" , "Erp.BO.OpTextSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderAllocSvc/index.html" , "Erp.BO.OrderAllocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderDtlSearchSvc/index.html" , "Erp.BO.OrderDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderHistSvc/index.html" , "Erp.BO.OrderHistSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderJobWizSvc/index.html" , "Erp.BO.OrderJobWizSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderLineStatusSvc/index.html" , "Erp.BO.OrderLineStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderRelPlantSearchSvc/index.html" , "Erp.BO.OrderRelPlantSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OrderRelSearchSvc/index.html" , "Erp.BO.OrderRelSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.OverrideSchedOrdersSvc/index.html" , "Erp.BO.OverrideSchedOrdersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PAPlanSvc/index.html" , "Erp.BO.PAPlanSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PAScheduleSvc/index.html" , "Erp.BO.PAScheduleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PAWeekSvc/index.html" , "Erp.BO.PAWeekSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PBGInvoiceSvc/index.html" , "Erp.BO.PBGInvoiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PBSchWrkSearchSvc/index.html" , "Erp.BO.PBSchWrkSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PBillSchSearchSvc/index.html" , "Erp.BO.PBillSchSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCIDCustomerSearchSvc/index.html" , "Erp.BO.PCIDCustomerSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCIDJobOperSearchSvc/index.html" , "Erp.BO.PCIDJobOperSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCWarehseSearchSvc/index.html" , "Erp.BO.PCWarehseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCashCloseDaySvc/index.html" , "Erp.BO.PCashCloseDaySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCashDeskSvc/index.html" , "Erp.BO.PCashDeskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCashEntrySvc/index.html" , "Erp.BO.PCashEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PCashOprTypeSvc/index.html" , "Erp.BO.PCashOprTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PIStatusSvc/index.html" , "Erp.BO.PIStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PITypeSvc/index.html" , "Erp.BO.PITypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PLJPKVATReportSvc/index.html" , "Erp.BO.PLJPKVATReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.POApvMsgSvc/index.html" , "Erp.BO.POApvMsgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PODetailSearchSvc/index.html" , "Erp.BO.PODetailSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PODetailTrackerSearchSvc/index.html" , "Erp.BO.PODetailTrackerSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PORelSearchSvc/index.html" , "Erp.BO.PORelSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.POScheduleSvc/index.html" , "Erp.BO.POScheduleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.POSuggChgSvc/index.html" , "Erp.BO.POSuggChgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.POSuggSvc/index.html" , "Erp.BO.POSuggSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.POSvc/index.html" , "Erp.BO.POSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.POWorkbenchSvc/index.html" , "Erp.BO.POWorkbenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRChkGrpSvc/index.html" , "Erp.BO.PRChkGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRClassSvc/index.html" , "Erp.BO.PRClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRDeductSvc/index.html" , "Erp.BO.PRDeductSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PREmployeeSvc/index.html" , "Erp.BO.PREmployeeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRHoldySvc/index.html" , "Erp.BO.PRHoldySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRTaxDtlSearchSvc/index.html" , "Erp.BO.PRTaxDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRW2DtlSvc/index.html" , "Erp.BO.PRW2DtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PRWrkCmpSvc/index.html" , "Erp.BO.PRWrkCmpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PWLocHisSearchSvc/index.html" , "Erp.BO.PWLocHisSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PackClssSvc/index.html" , "Erp.BO.PackClssSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PackOutSearchSvc/index.html" , "Erp.BO.PackOutSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PackingMtlTypeSvc/index.html" , "Erp.BO.PackingMtlTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PackingSvc/index.html" , "Erp.BO.PackingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PackingTypeSvc/index.html" , "Erp.BO.PackingTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ParsingParamsSvc/index.html" , "Erp.BO.ParsingParamsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartAdvisorSvc/index.html" , "Erp.BO.PartAdvisorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartAllocRuleClassSvc/index.html" , "Erp.BO.PartAllocRuleClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartAllocRuleMasterDtlSvc/index.html" , "Erp.BO.PartAllocRuleMasterDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartAllocTemplateSvc/index.html" , "Erp.BO.PartAllocTemplateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartAttributeSetSearchSvc/index.html" , "Erp.BO.PartAttributeSetSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartBinSearchSvc/index.html" , "Erp.BO.PartBinSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartClassSvc/index.html" , "Erp.BO.PartClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartClassWhseSearchSvc/index.html" , "Erp.BO.PartClassWhseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartCostSearchSvc/index.html" , "Erp.BO.PartCostSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartDimSvc/index.html" , "Erp.BO.PartDimSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartFIFOCostSvc/index.html" , "Erp.BO.PartFIFOCostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartLangDescSvc/index.html" , "Erp.BO.PartLangDescSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartLotIncludeAttributesSvc/index.html" , "Erp.BO.PartLotIncludeAttributesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartOnHandWhseSvc/index.html" , "Erp.BO.PartOnHandWhseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartPlantSearchSvc/index.html" , "Erp.BO.PartPlantSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartPlantWhseSearchSvc/index.html" , "Erp.BO.PartPlantWhseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartRevSearchSvc/index.html" , "Erp.BO.PartRevSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartSchedSearchSvc/index.html" , "Erp.BO.PartSchedSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartSchedSvc/index.html" , "Erp.BO.PartSchedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartSchedVendSearchSvc/index.html" , "Erp.BO.PartSchedVendSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartSvc/index.html" , "Erp.BO.PartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartTranHistSvc/index.html" , "Erp.BO.PartTranHistSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartTranSvc/index.html" , "Erp.BO.PartTranSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartTranTranTypeSearchSvc/index.html" , "Erp.BO.PartTranTranTypeSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartWhseFullSearchSvc/index.html" , "Erp.BO.PartWhseFullSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartWhseSearchSvc/index.html" , "Erp.BO.PartWhseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartWipSearchSvc/index.html" , "Erp.BO.PartWipSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartXRefMfgSvc/index.html" , "Erp.BO.PartXRefMfgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PartXRefSelectSvc/index.html" , "Erp.BO.PartXRefSelectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PayMethodSearchSvc/index.html" , "Erp.BO.PayMethodSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PayMethodSvc/index.html" , "Erp.BO.PayMethodSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PayTypeSvc/index.html" , "Erp.BO.PayTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PaymentEntrySvc/index.html" , "Erp.BO.PaymentEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PayrollCheckEntrySvc/index.html" , "Erp.BO.PayrollCheckEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PayrollTaxSvc/index.html" , "Erp.BO.PayrollTaxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcConDataSvc/index.html" , "Erp.BO.PcConDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcConTypeSvc/index.html" , "Erp.BO.PcConTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcECCSvc/index.html" , "Erp.BO.PcECCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcImageLayerIDWhereUsedSvc/index.html" , "Erp.BO.PcImageLayerIDWhereUsedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcInputsSearchSvc/index.html" , "Erp.BO.PcInputsSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcLookupColSetHedSearchSvc/index.html" , "Erp.BO.PcLookupColSetHedSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcLookupTblSvc/index.html" , "Erp.BO.PcLookupTblSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PcPropBagDefSvc/index.html" , "Erp.BO.PcPropBagDefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PeLogViewerSvc/index.html" , "Erp.BO.PeLogViewerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PerConLnkSearchSvc/index.html" , "Erp.BO.PerConLnkSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PerConSvc/index.html" , "Erp.BO.PerConSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PeriodicAvgCostingWorkbenchSvc/index.html" , "Erp.BO.PeriodicAvgCostingWorkbenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PeriodicitySvc/index.html" , "Erp.BO.PeriodicitySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PersonSvc/index.html" , "Erp.BO.PersonSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PickedOrdersSvc/index.html" , "Erp.BO.PickedOrdersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PipeLineSvc/index.html" , "Erp.BO.PipeLineSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlConfigSvc/index.html" , "Erp.BO.PkgControlConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlGenPCIDSvc/index.html" , "Erp.BO.PkgControlGenPCIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlIDBuildSplitMergeSvc/index.html" , "Erp.BO.PkgControlIDBuildSplitMergeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlIDGeneratorSvc/index.html" , "Erp.BO.PkgControlIDGeneratorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlIDMaintSvc/index.html" , "Erp.BO.PkgControlIDMaintSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlIDSvc/index.html" , "Erp.BO.PkgControlIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlJobOutputByPCIDSvc/index.html" , "Erp.BO.PkgControlJobOutputByPCIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlLabelTypeSvc/index.html" , "Erp.BO.PkgControlLabelTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlLabelValueSvc/index.html" , "Erp.BO.PkgControlLabelValueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlParentPCIDMasterSvc/index.html" , "Erp.BO.PkgControlParentPCIDMasterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlRepackReclassPCIDSvc/index.html" , "Erp.BO.PkgControlRepackReclassPCIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlResourcePrinterSvc/index.html" , "Erp.BO.PkgControlResourcePrinterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlStationSvc/index.html" , "Erp.BO.PkgControlStationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlTranRoutingPrinterSvc/index.html" , "Erp.BO.PkgControlTranRoutingPrinterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlTranRoutingSvc/index.html" , "Erp.BO.PkgControlTranRoutingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgControlVoidPCIDSvc/index.html" , "Erp.BO.PkgControlVoidPCIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgCtrlOverlayPCIDValidateSvc/index.html" , "Erp.BO.PkgCtrlOverlayPCIDValidateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PkgCtrlTranRoutPrinterSearchSvc/index.html" , "Erp.BO.PkgCtrlTranRoutPrinterSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlanContractSvc/index.html" , "Erp.BO.PlanContractSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlanningWBSvc/index.html" , "Erp.BO.PlanningWBSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlantConfCtrlSvc/index.html" , "Erp.BO.PlantConfCtrlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlantCostSvc/index.html" , "Erp.BO.PlantCostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlantFromSearchSvc/index.html" , "Erp.BO.PlantFromSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlantSvc/index.html" , "Erp.BO.PlantSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlantTranSearchSvc/index.html" , "Erp.BO.PlantTranSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlantWhseSearchSvc/index.html" , "Erp.BO.PlantWhseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PlasticPackagingTaxReportSvc/index.html" , "Erp.BO.PlasticPackagingTaxReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PostingRulesGLTranTypeSvc/index.html" , "Erp.BO.PostingRulesGLTranTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PostingRulesPackageSvc/index.html" , "Erp.BO.PostingRulesPackageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PrefSchemeSvc/index.html" , "Erp.BO.PrefSchemeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PriceGroupSvc/index.html" , "Erp.BO.PriceGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PriceListInquirySvc/index.html" , "Erp.BO.PriceListInquirySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PriceLstGroupsSvc/index.html" , "Erp.BO.PriceLstGroupsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PriceLstHedSvc/index.html" , "Erp.BO.PriceLstHedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PriceLstPartsSvc/index.html" , "Erp.BO.PriceLstPartsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PriceLstSvc/index.html" , "Erp.BO.PriceLstSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProdActDaySvc/index.html" , "Erp.BO.ProdActDaySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProdActivitySvc/index.html" , "Erp.BO.ProdActivitySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProdCalSvc/index.html" , "Erp.BO.ProdCalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProdCalWkSvc/index.html" , "Erp.BO.ProdCalWkSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProdGrupSvc/index.html" , "Erp.BO.ProdGrupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProdTeamSvc/index.html" , "Erp.BO.ProdTeamSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProjAnalysisSvc/index.html" , "Erp.BO.ProjAnalysisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProjChkLstTypeSvc/index.html" , "Erp.BO.ProjChkLstTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProjMultiSvc/index.html" , "Erp.BO.ProjMultiSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProjPhaseSearchSvc/index.html" , "Erp.BO.ProjPhaseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProjSummarySvc/index.html" , "Erp.BO.ProjSummarySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ProjectSvc/index.html" , "Erp.BO.ProjectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PropertyValueSearchSvc/index.html" , "Erp.BO.PropertyValueSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PurAgentSvc/index.html" , "Erp.BO.PurAgentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PurAuthSearchSvc/index.html" , "Erp.BO.PurAuthSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PurMiscSvc/index.html" , "Erp.BO.PurMiscSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PurTermsSvc/index.html" , "Erp.BO.PurTermsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.PurchaseAdvisorSvc/index.html" , "Erp.BO.PurchaseAdvisorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QMarkUpSvc/index.html" , "Erp.BO.QMarkUpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuickEntrySearchSvc/index.html" , "Erp.BO.QuickEntrySearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuickEntrySvc/index.html" , "Erp.BO.QuickEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuickJobEntrySvc/index.html" , "Erp.BO.QuickJobEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuoteAdtSvc/index.html" , "Erp.BO.QuoteAdtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuoteAnalysisExpSvc/index.html" , "Erp.BO.QuoteAnalysisExpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuoteAsmSearchSvc/index.html" , "Erp.BO.QuoteAsmSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuoteAsmSvc/index.html" , "Erp.BO.QuoteAsmSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuoteDtlSearchSvc/index.html" , "Erp.BO.QuoteDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.QuoteSvc/index.html" , "Erp.BO.QuoteSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RASchedCdSvc/index.html" , "Erp.BO.RASchedCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RFQDecisionWizardSvc/index.html" , "Erp.BO.RFQDecisionWizardSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RFQEntryJobSearchSvc/index.html" , "Erp.BO.RFQEntryJobSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RFQEntryQuoteSearchSvc/index.html" , "Erp.BO.RFQEntryQuoteSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RFQEntrySvc/index.html" , "Erp.BO.RFQEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RFQSuggSvc/index.html" , "Erp.BO.RFQSuggSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RFQVendSvc/index.html" , "Erp.BO.RFQVendSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RMADispSvc/index.html" , "Erp.BO.RMADispSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RMADtlSearchSvc/index.html" , "Erp.BO.RMADtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RMAProcSvc/index.html" , "Erp.BO.RMAProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RateTypeSvc/index.html" , "Erp.BO.RateTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RatingSvc/index.html" , "Erp.BO.RatingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RcvDtlSearchSvc/index.html" , "Erp.BO.RcvDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReasonSvc/index.html" , "Erp.BO.ReasonSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RebateSvc/index.html" , "Erp.BO.RebateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RebateTransSvc/index.html" , "Erp.BO.RebateTransSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReceiptSvc/index.html" , "Erp.BO.ReceiptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReceiptsFromMfgSvc/index.html" , "Erp.BO.ReceiptsFromMfgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReclassCodeSvc/index.html" , "Erp.BO.ReclassCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RecurBookListSearchSvc/index.html" , "Erp.BO.RecurBookListSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RecurringCycleSvc/index.html" , "Erp.BO.RecurringCycleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RecurringJournalSvc/index.html" , "Erp.BO.RecurringJournalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RefCategorySvc/index.html" , "Erp.BO.RefCategorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RegionSvc/index.html" , "Erp.BO.RegionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReminderGroupSvc/index.html" , "Erp.BO.ReminderGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReminderLetterSvc/index.html" , "Erp.BO.ReminderLetterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RenewalCodeSvc/index.html" , "Erp.BO.RenewalCodeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReplenishmentSvc/index.html" , "Erp.BO.ReplenishmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReportQtySvc/index.html" , "Erp.BO.ReportQtySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReqActsSvc/index.html" , "Erp.BO.ReqActsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReqSvc/index.html" , "Erp.BO.ReqSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReservePriSvc/index.html" , "Erp.BO.ReservePriSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ResourceCollectionSvc/index.html" , "Erp.BO.ResourceCollectionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ResourceGroupSvc/index.html" , "Erp.BO.ResourceGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ResourceSvc/index.html" , "Erp.BO.ResourceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ResourceTypeSvc/index.html" , "Erp.BO.ResourceTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RestrictFctsSvc/index.html" , "Erp.BO.RestrictFctsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReturnRequestSvc/index.html" , "Erp.BO.ReturnRequestSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReverseCashReceiptSvc/index.html" , "Erp.BO.ReverseCashReceiptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ReviewJrnSvc/index.html" , "Erp.BO.ReviewJrnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RevisionCompareSvc/index.html" , "Erp.BO.RevisionCompareSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RlsClassSvc/index.html" , "Erp.BO.RlsClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RoleCdSvc/index.html" , "Erp.BO.RoleCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RoughCutParamSvc/index.html" , "Erp.BO.RoughCutParamSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.RunGLAllocSearchSvc/index.html" , "Erp.BO.RunGLAllocSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SNTranSearchSvc/index.html" , "Erp.BO.SNTranSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SOPOLinkSvc/index.html" , "Erp.BO.SOPOLinkSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SRTSearchSvc/index.html" , "Erp.BO.SRTSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SaleAuthSearchSvc/index.html" , "Erp.BO.SaleAuthSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesCatSvc/index.html" , "Erp.BO.SalesCatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesOrdHedDtlSvc/index.html" , "Erp.BO.SalesOrdHedDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesOrderSvc/index.html" , "Erp.BO.SalesOrderSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesPersonWBSvc/index.html" , "Erp.BO.SalesPersonWBSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesRepQuotaSvc/index.html" , "Erp.BO.SalesRepQuotaSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesRepSvc/index.html" , "Erp.BO.SalesRepSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesTRCSearchSvc/index.html" , "Erp.BO.SalesTRCSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesTaxSvc/index.html" , "Erp.BO.SalesTaxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SalesTerSvc/index.html" , "Erp.BO.SalesTerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SchedPriSvc/index.html" , "Erp.BO.SchedPriSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ScheduleEngineSvc/index.html" , "Erp.BO.ScheduleEngineSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SchedulingBoardSvc/index.html" , "Erp.BO.SchedulingBoardSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SelectedSerialNumbersSvc/index.html" , "Erp.BO.SelectedSerialNumbersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SerialMatchSvc/index.html" , "Erp.BO.SerialMatchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SerialMatchingSvc/index.html" , "Erp.BO.SerialMatchingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SerialNoAssignSvc/index.html" , "Erp.BO.SerialNoAssignSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SerialNoSvc/index.html" , "Erp.BO.SerialNoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SerialNumMaskingSvc/index.html" , "Erp.BO.SerialNumMaskingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SerialNumberSearchSvc/index.html" , "Erp.BO.SerialNumberSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ServiceCallCenterSvc/index.html" , "Erp.BO.ServiceCallCenterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ServiceContractDtSearchSvc/index.html" , "Erp.BO.ServiceContractDtSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ServiceContractSearchSvc/index.html" , "Erp.BO.ServiceContractSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ServiceContractSvc/index.html" , "Erp.BO.ServiceContractSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SetupGrpSvc/index.html" , "Erp.BO.SetupGrpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ShipDtlSearchSvc/index.html" , "Erp.BO.ShipDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ShipToSvc/index.html" , "Erp.BO.ShipToSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ShipViaSvc/index.html" , "Erp.BO.ShipViaSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ShipWhseSearchSvc/index.html" , "Erp.BO.ShipWhseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ShopLoadSvc/index.html" , "Erp.BO.ShopLoadSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.ShopWrnSvc/index.html" , "Erp.BO.ShopWrnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SkipLotCtlSvc/index.html" , "Erp.BO.SkipLotCtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SpecRevSearchSvc/index.html" , "Erp.BO.SpecRevSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SpecificationSvc/index.html" , "Erp.BO.SpecificationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SplitJobSvc/index.html" , "Erp.BO.SplitJobSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SplitMergeUOMSvc/index.html" , "Erp.BO.SplitMergeUOMSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.StageNoSvc/index.html" , "Erp.BO.StageNoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.StageShipConfirmSvc/index.html" , "Erp.BO.StageShipConfirmSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.StatUOMSvc/index.html" , "Erp.BO.StatUOMSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.StockProvisionFormatSvc/index.html" , "Erp.BO.StockProvisionFormatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SubConShipEntrySvc/index.html" , "Erp.BO.SubConShipEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SubstanceRestrictionSvc/index.html" , "Erp.BO.SubstanceRestrictionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SubstanceSearchSvc/index.html" , "Erp.BO.SubstanceSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SubstanceSvc/index.html" , "Erp.BO.SubstanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SupplierPartSvc/index.html" , "Erp.BO.SupplierPartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.SupplierXRefSvc/index.html" , "Erp.BO.SupplierXRefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TEApprovalTaskSvc/index.html" , "Erp.BO.TEApprovalTaskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TFOrdDtlSearchSvc/index.html" , "Erp.BO.TFOrdDtlSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.THLocAPTaxReceiptSvc/index.html" , "Erp.BO.THLocAPTaxReceiptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TWSellerAuthorizationSvc/index.html" , "Erp.BO.TWSellerAuthorizationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TWVoidAndBlankGUINumsSvc/index.html" , "Erp.BO.TWVoidAndBlankGUINumsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TariffSvc/index.html" , "Erp.BO.TariffSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaskMastSvc/index.html" , "Erp.BO.TaskMastSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaskSetSearchSvc/index.html" , "Erp.BO.TaskSetSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaskSetSvc/index.html" , "Erp.BO.TaskSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaskStatSvc/index.html" , "Erp.BO.TaskStatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaskSvc/index.html" , "Erp.BO.TaskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaskTypeSvc/index.html" , "Erp.BO.TaskTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxAlgrmSvc/index.html" , "Erp.BO.TaxAlgrmSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxAuthorityCdSvc/index.html" , "Erp.BO.TaxAuthorityCdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxBoxDefaultSvc/index.html" , "Erp.BO.TaxBoxDefaultSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxBoxReportConfigSvc/index.html" , "Erp.BO.TaxBoxReportConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxCatDSearchSvc/index.html" , "Erp.BO.TaxCatDSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxCatSvc/index.html" , "Erp.BO.TaxCatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxCentSvc/index.html" , "Erp.BO.TaxCentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxCertSearchSvc/index.html" , "Erp.BO.TaxCertSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxConnectCertificatesSvc/index.html" , "Erp.BO.TaxConnectCertificatesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxExemptSearchSvc/index.html" , "Erp.BO.TaxExemptSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxJurisSvc/index.html" , "Erp.BO.TaxJurisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxReconciliationSvc/index.html" , "Erp.BO.TaxReconciliationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxResultsSvc/index.html" , "Erp.BO.TaxResultsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxRgnSvc/index.html" , "Erp.BO.TaxRgnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxRptCatSvc/index.html" , "Erp.BO.TaxRptCatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxRptDtlSvc/index.html" , "Erp.BO.TaxRptDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxSvcConfigSvc/index.html" , "Erp.BO.TaxSvcConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxTextSvc/index.html" , "Erp.BO.TaxTextSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TaxValidationSvc/index.html" , "Erp.BO.TaxValidationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TermsSvc/index.html" , "Erp.BO.TermsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TimeExpenseSharedSvc/index.html" , "Erp.BO.TimeExpenseSharedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TimePhasSvc/index.html" , "Erp.BO.TimePhasSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TimeTypeSvc/index.html" , "Erp.BO.TimeTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TopicChildSearchSvc/index.html" , "Erp.BO.TopicChildSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TrackingDtlSvc/index.html" , "Erp.BO.TrackingDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TranDocTypeSvc/index.html" , "Erp.BO.TranDocTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TranGLCDetailSvc/index.html" , "Erp.BO.TranGLCDetailSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TranGLCJournalSvc/index.html" , "Erp.BO.TranGLCJournalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TranTypeSearchSvc/index.html" , "Erp.BO.TranTypeSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TransOrderReceiptSvc/index.html" , "Erp.BO.TransOrderReceiptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TransOrderShipSvc/index.html" , "Erp.BO.TransOrderShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TransSugSearchSvc/index.html" , "Erp.BO.TransSugSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TransferChgSugSvc/index.html" , "Erp.BO.TransferChgSugSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TransferOrderEntrySvc/index.html" , "Erp.BO.TransferOrderEntrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.TransferWorkBenchSvc/index.html" , "Erp.BO.TransferWorkBenchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UOMClassSvc/index.html" , "Erp.BO.UOMClassSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UOMSearchSvc/index.html" , "Erp.BO.UOMSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UOMStkSearchSvc/index.html" , "Erp.BO.UOMStkSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UOMSvc/index.html" , "Erp.BO.UOMSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.USStateSvc/index.html" , "Erp.BO.USStateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.USTINValidationResultSvc/index.html" , "Erp.BO.USTINValidationResultSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.USTINValidationSvc/index.html" , "Erp.BO.USTINValidationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UnpickTransactionSvc/index.html" , "Erp.BO.UnpickTransactionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UserCompSearchSvc/index.html" , "Erp.BO.UserCompSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.UserFileSvc/index.html" , "Erp.BO.UserFileSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VATTaxSvc/index.html" , "Erp.BO.VATTaxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VNTGLRptMasSvc/index.html" , "Erp.BO.VNTGLRptMasSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendBankSearchSvc/index.html" , "Erp.BO.VendBankSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendCntSearchSvc/index.html" , "Erp.BO.VendCntSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendGrupSvc/index.html" , "Erp.BO.VendGrupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendPartRestrictionSvc/index.html" , "Erp.BO.VendPartRestrictionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendPartSvc/index.html" , "Erp.BO.VendPartSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendorPPSearchSvc/index.html" , "Erp.BO.VendorPPSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VendorSvc/index.html" , "Erp.BO.VendorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VoidPRCheckSvc/index.html" , "Erp.BO.VoidPRCheckSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.VoidPaymentSvc/index.html" , "Erp.BO.VoidPaymentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WFGroupSvc/index.html" , "Erp.BO.WFGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WFStageSvc/index.html" , "Erp.BO.WFStageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WHTPaymentSubmitSvc/index.html" , "Erp.BO.WHTPaymentSubmitSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WHTPaymentSvc/index.html" , "Erp.BO.WHTPaymentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WarehseSearchSvc/index.html" , "Erp.BO.WarehseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WarehseSvc/index.html" , "Erp.BO.WarehseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WarningSvc/index.html" , "Erp.BO.WarningSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WaveSvc/index.html" , "Erp.BO.WaveSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WebLogSvc/index.html" , "Erp.BO.WebLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WhseBinSvc/index.html" , "Erp.BO.WhseBinSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WhseGroupEmpSearchSvc/index.html" , "Erp.BO.WhseGroupEmpSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WhseGroupSvc/index.html" , "Erp.BO.WhseGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WhsePartWhseSearchSvc/index.html" , "Erp.BO.WhsePartWhseSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WhseSysPrinterSearchSvc/index.html" , "Erp.BO.WhseSysPrinterSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WhseZoneSvc/index.html" , "Erp.BO.WhseZoneSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WorkQueueSvc/index.html" , "Erp.BO.WorkQueueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WorkStationSvc/index.html" , "Erp.BO.WorkStationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.WorkforceSearchSvc/index.html" , "Erp.BO.WorkforceSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.BO.glaccountmassaddSvc/index.html" , "Erp.BO.glaccountmassaddSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.APIKeySvc/index.html" , "Ice.BO.APIKeySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.APITraceSvc/index.html" , "Ice.BO.APITraceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AccessScopeSvc/index.html" , "Ice.BO.AccessScopeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AccountLockoutPolicySvc/index.html" , "Ice.BO.AccountLockoutPolicySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AdminCompanySvc/index.html" , "Ice.BO.AdminCompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AdminLicensingSvc/index.html" , "Ice.BO.AdminLicensingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AdminSessionSvc/index.html" , "Ice.BO.AdminSessionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AnnotationSvc/index.html" , "Ice.BO.AnnotationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AppRegistrationSvc/index.html" , "Ice.BO.AppRegistrationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AttachmentSvc/index.html" , "Ice.BO.AttachmentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AttachmentTransferSvc/index.html" , "Ice.BO.AttachmentTransferSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AutoPrintSearchSvc/index.html" , "Ice.BO.AutoPrintSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AutoRptSvc/index.html" , "Ice.BO.AutoRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.AzureADConfigSvc/index.html" , "Ice.BO.AzureADConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BAQDesignerSvc/index.html" , "Ice.BO.BAQDesignerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BAQExtDBSearchSvc/index.html" , "Ice.BO.BAQExtDBSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BAQExtDatasourceSvc/index.html" , "Ice.BO.BAQExtDatasourceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BAQExtDsMetadataSvc/index.html" , "Ice.BO.BAQExtDsMetadataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BAQExtDsTypeSvc/index.html" , "Ice.BO.BAQExtDsTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BORelationSearchSvc/index.html" , "Ice.BO.BORelationSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BpHoldsSvc/index.html" , "Ice.BO.BpHoldsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BpInstanceCounterSvc/index.html" , "Ice.BO.BpInstanceCounterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BpMethodSvc/index.html" , "Ice.BO.BpMethodSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BpTableDependSearchSvc/index.html" , "Ice.BO.BpTableDependSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.BpTextStorageSvc/index.html" , "Ice.BO.BpTextStorageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ChgLogSvc/index.html" , "Ice.BO.ChgLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ChglogDirectiveSearchSvc/index.html" , "Ice.BO.ChglogDirectiveSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.CnvProgsSvc/index.html" , "Ice.BO.CnvProgsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.CompanySvc/index.html" , "Ice.BO.CompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ConfigCheckSvc/index.html" , "Ice.BO.ConfigCheckSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ContextMenuDataSvc/index.html" , "Ice.BO.ContextMenuDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ConversionSetSvc/index.html" , "Ice.BO.ConversionSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DOCAssocSvc/index.html" , "Ice.BO.DOCAssocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DashBoardSvc/index.html" , "Ice.BO.DashBoardSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DashboardMaintSvc/index.html" , "Ice.BO.DashboardMaintSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DataDiscoverySvc/index.html" , "Ice.BO.DataDiscoverySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DigitalCertificateStoreSvc/index.html" , "Ice.BO.DigitalCertificateStoreSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DmsStorageTypeSvc/index.html" , "Ice.BO.DmsStorageTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DocTypeSvc/index.html" , "Ice.BO.DocTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DynamicQuerySvc/index.html" , "Ice.BO.DynamicQuerySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.DynamicReportSvc/index.html" , "Ice.BO.DynamicReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ESConfigSvc/index.html" , "Ice.BO.ESConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ESSearchSvc/index.html" , "Ice.BO.ESSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ESignatureSvc/index.html" , "Ice.BO.ESignatureSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ElementSvc/index.html" , "Ice.BO.ElementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ExportPackageSvc/index.html" , "Ice.BO.ExportPackageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ExtCompanySvc/index.html" , "Ice.BO.ExtCompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ExtServiceRegistrationSvc/index.html" , "Ice.BO.ExtServiceRegistrationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ExtSystemSvc/index.html" , "Ice.BO.ExtSystemSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ExtensionSvc/index.html" , "Ice.BO.ExtensionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.FavoriteSvc/index.html" , "Ice.BO.FavoriteSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.GenxDataSvc/index.html" , "Ice.BO.GenxDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.HealthCheckSvc/index.html" , "Ice.BO.HealthCheckSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IPFormCustomSvc/index.html" , "Ice.BO.IPFormCustomSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ImportMgmtSvc/index.html" , "Ice.BO.ImportMgmtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ImportSvc/index.html" , "Ice.BO.ImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.InfoPromptFormSvc/index.html" , "Ice.BO.InfoPromptFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IntegrationFieldMapSvc/index.html" , "Ice.BO.IntegrationFieldMapSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IoTConfigSvc/index.html" , "Ice.BO.IoTConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IoTDeviceEventSvc/index.html" , "Ice.BO.IoTDeviceEventSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IoTDeviceGroupSvc/index.html" , "Ice.BO.IoTDeviceGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IoTDeviceSvc/index.html" , "Ice.BO.IoTDeviceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.IoTRuleSvc/index.html" , "Ice.BO.IoTRuleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.KineticErpSvc/index.html" , "Ice.BO.KineticErpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.LangNameSvc/index.html" , "Ice.BO.LangNameSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.LangOrgSvc/index.html" , "Ice.BO.LangOrgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.LangProgSvc/index.html" , "Ice.BO.LangProgSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.LangTranSvc/index.html" , "Ice.BO.LangTranSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.LangXrefSvc/index.html" , "Ice.BO.LangXrefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MailLogSvc/index.html" , "Ice.BO.MailLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MailSettingSvc/index.html" , "Ice.BO.MailSettingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MemoCatSvc/index.html" , "Ice.BO.MemoCatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MemoSvc/index.html" , "Ice.BO.MemoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MenuProgramSvc/index.html" , "Ice.BO.MenuProgramSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MenuSvc/index.html" , "Ice.BO.MenuSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MenuTabSvc/index.html" , "Ice.BO.MenuTabSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.MessageTemplateSvc/index.html" , "Ice.BO.MessageTemplateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.NCChgLogSvc/index.html" , "Ice.BO.NCChgLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.NamedSearchSvc/index.html" , "Ice.BO.NamedSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ObjectSecuritySvc/index.html" , "Ice.BO.ObjectSecuritySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PDFFormSvc/index.html" , "Ice.BO.PDFFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PDFFormTemplateSvc/index.html" , "Ice.BO.PDFFormTemplateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PasswordPolicySvc/index.html" , "Ice.BO.PasswordPolicySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PatchFldSvc/index.html" , "Ice.BO.PatchFldSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PlantSvc/index.html" , "Ice.BO.PlantSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PredictiveSearchSvc/index.html" , "Ice.BO.PredictiveSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ProcessSetSvc/index.html" , "Ice.BO.ProcessSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ProcessTaskSvc/index.html" , "Ice.BO.ProcessTaskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ProductVersionSvc/index.html" , "Ice.BO.ProductVersionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.PublishedViewSvc/index.html" , "Ice.BO.PublishedViewSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.QueryConversionSvc/index.html" , "Ice.BO.QueryConversionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.QuickSearchSvc/index.html" , "Ice.BO.QuickSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ReportCriteriaSetSvc/index.html" , "Ice.BO.ReportCriteriaSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ReportMonitorSvc/index.html" , "Ice.BO.ReportMonitorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ReportStyleSearchSvc/index.html" , "Ice.BO.ReportStyleSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ReportSvc/index.html" , "Ice.BO.ReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ReportTypeSvc/index.html" , "Ice.BO.ReportTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.RptDataDefSvc/index.html" , "Ice.BO.RptDataDefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.RptStylePrintersListSvc/index.html" , "Ice.BO.RptStylePrintersListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.RptSubmissionSvc/index.html" , "Ice.BO.RptSubmissionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SchemaAttributeSvc/index.html" , "Ice.BO.SchemaAttributeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SchemaSvc/index.html" , "Ice.BO.SchemaSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SecColumnSvc/index.html" , "Ice.BO.SecColumnSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SecGroupSvc/index.html" , "Ice.BO.SecGroupSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SecuritySvc/index.html" , "Ice.BO.SecuritySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ShellLayoutSvc/index.html" , "Ice.BO.ShellLayoutSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SolutionTypeSvc/index.html" , "Ice.BO.SolutionTypeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SsrsReportDesignSvc/index.html" , "Ice.BO.SsrsReportDesignSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.StructuredOutputDefinitionSvc/index.html" , "Ice.BO.StructuredOutputDefinitionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysActivityLogSvc/index.html" , "Ice.BO.SysActivityLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysActivityTrackerSvc/index.html" , "Ice.BO.SysActivityTrackerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysAgentSvc/index.html" , "Ice.BO.SysAgentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysConfigSvc/index.html" , "Ice.BO.SysConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysCubeDefSvc/index.html" , "Ice.BO.SysCubeDefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysMonitorSvc/index.html" , "Ice.BO.SysMonitorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysMonitorTasksSvc/index.html" , "Ice.BO.SysMonitorTasksSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysPrinterSvc/index.html" , "Ice.BO.SysPrinterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysTagSvc/index.html" , "Ice.BO.SysTagSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysTaskAgentRuleSvc/index.html" , "Ice.BO.SysTaskAgentRuleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysTaskLogSvc/index.html" , "Ice.BO.SysTaskLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysTaskSvc/index.html" , "Ice.BO.SysTaskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.SysUserMenuPreferenceSvc/index.html" , "Ice.BO.SysUserMenuPreferenceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ThemeSvc/index.html" , "Ice.BO.ThemeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.TipSvc/index.html" , "Ice.BO.TipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD01Svc/index.html" , "Ice.BO.UD01Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD02Svc/index.html" , "Ice.BO.UD02Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD03Svc/index.html" , "Ice.BO.UD03Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD04Svc/index.html" , "Ice.BO.UD04Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD05Svc/index.html" , "Ice.BO.UD05Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD06Svc/index.html" , "Ice.BO.UD06Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD07Svc/index.html" , "Ice.BO.UD07Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD08Svc/index.html" , "Ice.BO.UD08Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD09Svc/index.html" , "Ice.BO.UD09Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD100Svc/index.html" , "Ice.BO.UD100Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD101Svc/index.html" , "Ice.BO.UD101Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD102Svc/index.html" , "Ice.BO.UD102Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD103Svc/index.html" , "Ice.BO.UD103Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD104Svc/index.html" , "Ice.BO.UD104Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD105Svc/index.html" , "Ice.BO.UD105Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD106Svc/index.html" , "Ice.BO.UD106Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD107Svc/index.html" , "Ice.BO.UD107Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD108Svc/index.html" , "Ice.BO.UD108Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD109Svc/index.html" , "Ice.BO.UD109Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD10Svc/index.html" , "Ice.BO.UD10Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD110Svc/index.html" , "Ice.BO.UD110Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD11Svc/index.html" , "Ice.BO.UD11Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD12Svc/index.html" , "Ice.BO.UD12Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD13Svc/index.html" , "Ice.BO.UD13Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD14Svc/index.html" , "Ice.BO.UD14Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD15Svc/index.html" , "Ice.BO.UD15Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD16Svc/index.html" , "Ice.BO.UD16Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD17Svc/index.html" , "Ice.BO.UD17Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD18Svc/index.html" , "Ice.BO.UD18Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD19Svc/index.html" , "Ice.BO.UD19Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD20Svc/index.html" , "Ice.BO.UD20Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD21Svc/index.html" , "Ice.BO.UD21Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD22Svc/index.html" , "Ice.BO.UD22Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD23Svc/index.html" , "Ice.BO.UD23Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD24Svc/index.html" , "Ice.BO.UD24Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD25Svc/index.html" , "Ice.BO.UD25Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD26Svc/index.html" , "Ice.BO.UD26Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD27Svc/index.html" , "Ice.BO.UD27Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD28Svc/index.html" , "Ice.BO.UD28Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD29Svc/index.html" , "Ice.BO.UD29Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD30Svc/index.html" , "Ice.BO.UD30Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD31Svc/index.html" , "Ice.BO.UD31Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD32Svc/index.html" , "Ice.BO.UD32Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD33Svc/index.html" , "Ice.BO.UD33Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD34Svc/index.html" , "Ice.BO.UD34Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD35Svc/index.html" , "Ice.BO.UD35Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD36Svc/index.html" , "Ice.BO.UD36Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD37Svc/index.html" , "Ice.BO.UD37Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD38Svc/index.html" , "Ice.BO.UD38Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD39Svc/index.html" , "Ice.BO.UD39Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UD40Svc/index.html" , "Ice.BO.UD40Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UDMapSvc/index.html" , "Ice.BO.UDMapSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UserCodesSvc/index.html" , "Ice.BO.UserCodesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UserDefinedDataSvc/index.html" , "Ice.BO.UserDefinedDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UserFileSvc/index.html" , "Ice.BO.UserFileSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.UserTracingSvc/index.html" , "Ice.BO.UserTracingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.XAttachMetaDataSvc/index.html" , "Ice.BO.XAttachMetaDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.XDocTypeCtrlSvc/index.html" , "Ice.BO.XDocTypeCtrlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.XFileRefSvc/index.html" , "Ice.BO.XFileRefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ZBODefSvc/index.html" , "Ice.BO.ZBODefSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ZDataFieldSearchSvc/index.html" , "Ice.BO.ZDataFieldSearchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ZDataSetSvc/index.html" , "Ice.BO.ZDataSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ZDataTableSvc/index.html" , "Ice.BO.ZDataTableSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ZKeySvc/index.html" , "Ice.BO.ZKeySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.ZSubDataSetSvc/index.html" , "Ice.BO.ZSubDataSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.BO.iceMaintSvc/index.html" , "Ice.BO.iceMaintSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.LIB.QuickShipSvc/index.html" , "Erp.LIB.QuickShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.AppExtensionRegistrySvc/index.html" , "Ice.LIB.AppExtensionRegistrySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.BOReaderSvc/index.html" , "Ice.LIB.BOReaderSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.BPMExtAssembliesSvc/index.html" , "Ice.LIB.BPMExtAssembliesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.BPMExtMethodsSvc/index.html" , "Ice.LIB.BPMExtMethodsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.BpEscConnectorSvc/index.html" , "Ice.LIB.BpEscConnectorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.CdcManageSvc/index.html" , "Ice.LIB.CdcManageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.CdcSubscriberSvc/index.html" , "Ice.LIB.CdcSubscriberSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.ClassAttributeSvc/index.html" , "Ice.LIB.ClassAttributeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.ClientCacheSvc/index.html" , "Ice.LIB.ClientCacheSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.ClientFunctionsSvc/index.html" , "Ice.LIB.ClientFunctionsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.DataFabricSvc/index.html" , "Ice.LIB.DataFabricSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.ESIndexSvc/index.html" , "Ice.LIB.ESIndexSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.EcfToolsSvc/index.html" , "Ice.LIB.EcfToolsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.EffectiveFieldsSvc/index.html" , "Ice.LIB.EffectiveFieldsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.EfxLibraryDesignerSvc/index.html" , "Ice.LIB.EfxLibraryDesignerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.FeatureFlagSvc/index.html" , "Ice.LIB.FeatureFlagSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.FieldHelpSvc/index.html" , "Ice.LIB.FieldHelpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.FileStoreSvc/index.html" , "Ice.LIB.FileStoreSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.FileTransferSvc/index.html" , "Ice.LIB.FileTransferSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.IdentityProviderConfigSvc/index.html" , "Ice.LIB.IdentityProviderConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.InAppNotificationsSvc/index.html" , "Ice.LIB.InAppNotificationsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.IntegrationPortalSvc/index.html" , "Ice.LIB.IntegrationPortalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.MessageHubConfigSvc/index.html" , "Ice.LIB.MessageHubConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.MetaFXSvc/index.html" , "Ice.LIB.MetaFXSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.RunTaskSvc/index.html" , "Ice.LIB.RunTaskSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.ServerPathSvc/index.html" , "Ice.LIB.ServerPathSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.SessionModSvc/index.html" , "Ice.LIB.SessionModSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.SetupInfoSvc/index.html" , "Ice.LIB.SetupInfoSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.SsrsReportAnalyzerSvc/index.html" , "Ice.LIB.SsrsReportAnalyzerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.SynergySvc/index.html" , "Ice.LIB.SynergySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.TenantInstanceSvc/index.html" , "Ice.LIB.TenantInstanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.TokenServiceSvc/index.html" , "Ice.LIB.TokenServiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.UserDefinedServiceManagerSvc/index.html" , "Ice.LIB.UserDefinedServiceManagerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.LIB.UxAppVersionSvc/index.html" , "Ice.LIB.UxAppVersionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AGCAEASubmitSvc/index.html" , "Erp.PROC.AGCAEASubmitSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AGTaxOutputSvc/index.html" , "Erp.PROC.AGTaxOutputSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APBillsOfExchangePostSvc/index.html" , "Erp.PROC.APBillsOfExchangePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APInvoicePostSvc/index.html" , "Erp.PROC.APInvoicePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APPIPaymentPostSvc/index.html" , "Erp.PROC.APPIPaymentPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APPIStatusChangePostSvc/index.html" , "Erp.PROC.APPIStatusChangePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APPIVoidingPostSvc/index.html" , "Erp.PROC.APPIVoidingPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APPIWriteOffPostSvc/index.html" , "Erp.PROC.APPIWriteOffPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.APPaymentPostSvc/index.html" , "Erp.PROC.APPaymentPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARBalanceSvc/index.html" , "Erp.PROC.ARBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARInvAdjPostSvc/index.html" , "Erp.PROC.ARInvAdjPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARInvoicePostSvc/index.html" , "Erp.PROC.ARInvoicePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARPIPaymentPostSvc/index.html" , "Erp.PROC.ARPIPaymentPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARPIStatusChangePostSvc/index.html" , "Erp.PROC.ARPIStatusChangePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARPIVoidingPostSvc/index.html" , "Erp.PROC.ARPIVoidingPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ARTaxConfirmSvc/index.html" , "Erp.PROC.ARTaxConfirmSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ActBdnRevRecSvc/index.html" , "Erp.PROC.ActBdnRevRecSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AllocationQueueSvc/index.html" , "Erp.PROC.AllocationQueueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ApplyRecurJrnlsSvc/index.html" , "Erp.PROC.ApplyRecurJrnlsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AssetDepreciationSvc/index.html" , "Erp.PROC.AssetDepreciationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AssetPostingProcSvc/index.html" , "Erp.PROC.AssetPostingProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AssetYearEndSvc/index.html" , "Erp.PROC.AssetYearEndSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AutoJobClosingSvc/index.html" , "Erp.PROC.AutoJobClosingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AutoJobCompletionSvc/index.html" , "Erp.PROC.AutoJobCompletionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AutoJobFirmSvc/index.html" , "Erp.PROC.AutoJobFirmSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AutoJobReleaseSvc/index.html" , "Erp.PROC.AutoJobReleaseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.AvaCustMassUpdateSvc/index.html" , "Erp.PROC.AvaCustMassUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BEDCSvc/index.html" , "Erp.PROC.BEDCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BackFlushLaborProcessSvc/index.html" , "Erp.PROC.BackFlushLaborProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankAdjPostSvc/index.html" , "Erp.PROC.BankAdjPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankBatchUnlockSvc/index.html" , "Erp.PROC.BankBatchUnlockSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankFileImportExpressSvc/index.html" , "Erp.PROC.BankFileImportExpressSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankFundPostSvc/index.html" , "Erp.PROC.BankFundPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankReconciliationPostSvc/index.html" , "Erp.PROC.BankReconciliationPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankStatementConversionSvc/index.html" , "Erp.PROC.BankStatementConversionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankStatementImportSvc/index.html" , "Erp.PROC.BankStatementImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankStatementUnlockSvc/index.html" , "Erp.PROC.BankStatementUnlockSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BankTransferNoticeProcSvc/index.html" , "Erp.PROC.BankTransferNoticeProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BudgetExportProcSvc/index.html" , "Erp.PROC.BudgetExportProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BudgetImportProcSvc/index.html" , "Erp.PROC.BudgetImportProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.BulkAddrValSvc/index.html" , "Erp.PROC.BulkAddrValSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CNDataExportSvc/index.html" , "Erp.PROC.CNDataExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CNFinRepConfigConversionSvc/index.html" , "Erp.PROC.CNFinRepConfigConversionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CNGTIDataConversionSvc/index.html" , "Erp.PROC.CNGTIDataConversionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CNGTIExportProcessSvc/index.html" , "Erp.PROC.CNGTIExportProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CNLegalNumHistoryUpdateSvc/index.html" , "Erp.PROC.CNLegalNumHistoryUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.COAExportProcSvc/index.html" , "Erp.PROC.COAExportProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.COAImportProcSvc/index.html" , "Erp.PROC.COAImportProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CVAP0030Svc/index.html" , "Erp.PROC.CVAP0030Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CVCR0007Svc/index.html" , "Erp.PROC.CVCR0007Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CVImageSvc/index.html" , "Erp.PROC.CVImageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CVJC0050Svc/index.html" , "Erp.PROC.CVJC0050Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CVJC0078Svc/index.html" , "Erp.PROC.CVJC0078Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CVXA0081Svc/index.html" , "Erp.PROC.CVXA0081Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CaptureCOSWIPSvc/index.html" , "Erp.PROC.CaptureCOSWIPSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CaptureRevenueCOSSvc/index.html" , "Erp.PROC.CaptureRevenueCOSSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CaptureWBSPhaseRevenueCOSSvc/index.html" , "Erp.PROC.CaptureWBSPhaseRevenueCOSSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CashRecPostSvc/index.html" , "Erp.PROC.CashRecPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CheckDigitConversionSvc/index.html" , "Erp.PROC.CheckDigitConversionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CloseAPLOCSvc/index.html" , "Erp.PROC.CloseAPLOCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CloseARLOCSvc/index.html" , "Erp.PROC.CloseARLOCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ClosePOMultiCompanySvc/index.html" , "Erp.PROC.ClosePOMultiCompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CollectionsPostSvc/index.html" , "Erp.PROC.CollectionsPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ConfiguratorSyncDirectSvc/index.html" , "Erp.PROC.ConfiguratorSyncDirectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ConfiguratorSyncSvc/index.html" , "Erp.PROC.ConfiguratorSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ConsPostSvc/index.html" , "Erp.PROC.ConsPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ConsYearEndSvc/index.html" , "Erp.PROC.ConsYearEndSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ConvertPcInValuesSvc/index.html" , "Erp.PROC.ConvertPcInValuesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CopyBudgetProcSvc/index.html" , "Erp.PROC.CopyBudgetProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CopyGLCToTaxEffRateSvc/index.html" , "Erp.PROC.CopyGLCToTaxEffRateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CostWBPostSvc/index.html" , "Erp.PROC.CostWBPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CostWBRollUpSvc/index.html" , "Erp.PROC.CostWBRollUpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CreateInitialExtSystemRecordsSvc/index.html" , "Erp.PROC.CreateInitialExtSystemRecordsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CreditCardSvc/index.html" , "Erp.PROC.CreditCardSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CurrencyReportProcessSvc/index.html" , "Erp.PROC.CurrencyReportProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CurrencyRevalueProcessSvc/index.html" , "Erp.PROC.CurrencyRevalueProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CustShpCCProcSvc/index.html" , "Erp.PROC.CustShpCCProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.CustomerCreditHoldSvc/index.html" , "Erp.PROC.CustomerCreditHoldSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DBPurgeSvc/index.html" , "Erp.PROC.DBPurgeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DEImportRatesSvc/index.html" , "Erp.PROC.DEImportRatesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DELookupDataExportSvc/index.html" , "Erp.PROC.DELookupDataExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DELookupDataImportSvc/index.html" , "Erp.PROC.DELookupDataImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DEZ4Z10ExportSvc/index.html" , "Erp.PROC.DEZ4Z10ExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DataCheckProcSvc/index.html" , "Erp.PROC.DataCheckProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DataFixProcSvc/index.html" , "Erp.PROC.DataFixProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DefExpRecogProcSvc/index.html" , "Erp.PROC.DefExpRecogProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DefRevAmortProcSvc/index.html" , "Erp.PROC.DefRevAmortProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DefRevRecogProcSvc/index.html" , "Erp.PROC.DefRevRecogProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DeleteAccountsProcSvc/index.html" , "Erp.PROC.DeleteAccountsProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DeleteWhenClosedOrderRelSvc/index.html" , "Erp.PROC.DeleteWhenClosedOrderRelSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DemandMassProcessSvc/index.html" , "Erp.PROC.DemandMassProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DetectRedundantBomSvc/index.html" , "Erp.PROC.DetectRedundantBomSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.DynSegValUpdSvc/index.html" , "Erp.PROC.DynSegValUpdSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCCustomerExtendedSvc/index.html" , "Erp.PROC.ECCCustomerExtendedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCCustomerMasterSvc/index.html" , "Erp.PROC.ECCCustomerMasterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCCustomerOrdersSvc/index.html" , "Erp.PROC.ECCCustomerOrdersSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCCustomerPartsSvc/index.html" , "Erp.PROC.ECCCustomerPartsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCSupplierExtendedSvc/index.html" , "Erp.PROC.ECCSupplierExtendedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCSupplierSyncSvc/index.html" , "Erp.PROC.ECCSupplierSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ECCUOMAndCustomerE10Svc/index.html" , "Erp.PROC.ECCUOMAndCustomerE10Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.EInvGetFromOperatorSvc/index.html" , "Erp.PROC.EInvGetFromOperatorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.EInvGetStatusSvc/index.html" , "Erp.PROC.EInvGetStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.EInvSendExternalServiceSvc/index.html" , "Erp.PROC.EInvSendExternalServiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.EInvStatusImportSvc/index.html" , "Erp.PROC.EInvStatusImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.EInvStatusUpdateSvc/index.html" , "Erp.PROC.EInvStatusUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.EInvoiceProcessSvc/index.html" , "Erp.PROC.EInvoiceProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.Export1099Svc/index.html" , "Erp.PROC.Export1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ExportMattecSvc/index.html" , "Erp.PROC.ExportMattecSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ExportRevisionSvc/index.html" , "Erp.PROC.ExportRevisionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ExtPRWriteFileSvc/index.html" , "Erp.PROC.ExtPRWriteFileSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FAssetMassChangeSvc/index.html" , "Erp.PROC.FAssetMassChangeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FillShopCapSvc/index.html" , "Erp.PROC.FillShopCapSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FinChargeCalcSvc/index.html" , "Erp.PROC.FinChargeCalcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FirmJobsSvc/index.html" , "Erp.PROC.FirmJobsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FixBankTranRptAmtsSvc/index.html" , "Erp.PROC.FixBankTranRptAmtsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FixBinsAllNewSvc/index.html" , "Erp.PROC.FixBinsAllNewSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FixBookDtlSvc/index.html" , "Erp.PROC.FixBookDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FixBookRelSvc/index.html" , "Erp.PROC.FixBookRelSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.FixResourcesHorizonSvc/index.html" , "Erp.PROC.FixResourcesHorizonSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GLBatchBalancesSvc/index.html" , "Erp.PROC.GLBatchBalancesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GLImportProcSvc/index.html" , "Erp.PROC.GLImportProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GLJrnAsynchSvc/index.html" , "Erp.PROC.GLJrnAsynchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GLRevalueSvc/index.html" , "Erp.PROC.GLRevalueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GLSumExportSvc/index.html" , "Erp.PROC.GLSumExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GLVerifyBalancesSvc/index.html" , "Erp.PROC.GLVerifyBalancesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GUIAPToTaxDeclareSvc/index.html" , "Erp.PROC.GUIAPToTaxDeclareSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GUIARToTaxDeclareSvc/index.html" , "Erp.PROC.GUIARToTaxDeclareSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GUIVATTaxSvc/index.html" , "Erp.PROC.GUIVATTaxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenActualCostAllocSvc/index.html" , "Erp.PROC.GenActualCostAllocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenPeriodicAvgCostingSvc/index.html" , "Erp.PROC.GenPeriodicAvgCostingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenProdActSvc/index.html" , "Erp.PROC.GenProdActSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenRebateTranSvc/index.html" , "Erp.PROC.GenRebateTranSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenSup1099Svc/index.html" , "Erp.PROC.GenSup1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenTaxBoxSumSvc/index.html" , "Erp.PROC.GenTaxBoxSumSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenW2FileSvc/index.html" , "Erp.PROC.GenW2FileSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenerateAccountsProcSvc/index.html" , "Erp.PROC.GenerateAccountsProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenerateAssembliesProcSvc/index.html" , "Erp.PROC.GenerateAssembliesProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenerateWBSPhaseAnalysisSvc/index.html" , "Erp.PROC.GenerateWBSPhaseAnalysisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenericImportSvc/index.html" , "Erp.PROC.GenericImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GenericSvc/index.html" , "Erp.PROC.GenericSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GetEmpExpSvc/index.html" , "Erp.PROC.GetEmpExpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.GetShipSvc/index.html" , "Erp.PROC.GetShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.INBusinessCatCreationSvc/index.html" , "Erp.PROC.INBusinessCatCreationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.INInitTaxRptCatAndTaxTextSvc/index.html" , "Erp.PROC.INInitTaxRptCatAndTaxTextSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.IQSSyncSvc/index.html" , "Erp.PROC.IQSSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ImageExportSvc/index.html" , "Erp.PROC.ImageExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ImportAPEInvoiceSvc/index.html" , "Erp.PROC.ImportAPEInvoiceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ImportEDISvc/index.html" , "Erp.PROC.ImportEDISvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ImportLaborSchedSvc/index.html" , "Erp.PROC.ImportLaborSchedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ImportRevisionSvc/index.html" , "Erp.PROC.ImportRevisionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.InitLastCCDateSvc/index.html" , "Erp.PROC.InitLastCCDateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.InitMultiCompanyGLSvc/index.html" , "Erp.PROC.InitMultiCompanyGLSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.InitPhysicalInvSvc/index.html" , "Erp.PROC.InitPhysicalInvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.IntrastatExportProcessSvc/index.html" , "Erp.PROC.IntrastatExportProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.IntrastatUDCodesCreationSvc/index.html" , "Erp.PROC.IntrastatUDCodesCreationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.InvDefRevRecogPostSvc/index.html" , "Erp.PROC.InvDefRevRecogPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.JPAPPerBillRegenSvc/index.html" , "Erp.PROC.JPAPPerBillRegenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.JobLoadRestoreSvc/index.html" , "Erp.PROC.JobLoadRestoreSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.JobRoHSSvc/index.html" , "Erp.PROC.JobRoHSSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.KBMaxCustomSyncSvc/index.html" , "Erp.PROC.KBMaxCustomSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.KBMaxPartSyncSvc/index.html" , "Erp.PROC.KBMaxPartSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.KBMaxQuoteSyncSvc/index.html" , "Erp.PROC.KBMaxQuoteSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.KanbanReceiptsProcSvc/index.html" , "Erp.PROC.KanbanReceiptsProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.LoadCostWBDetailsSvc/index.html" , "Erp.PROC.LoadCostWBDetailsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.LocationViewUpdateSvc/index.html" , "Erp.PROC.LocationViewUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.LockBoxSvc/index.html" , "Erp.PROC.LockBoxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.LogAPInvVoidPostSvc/index.html" , "Erp.PROC.LogAPInvVoidPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.LogAPInvoicePostSvc/index.html" , "Erp.PROC.LogAPInvoicePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MLPeggingSvc/index.html" , "Erp.PROC.MLPeggingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MRPRecalcNeededSvc/index.html" , "Erp.PROC.MRPRecalcNeededSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MRPSvc/index.html" , "Erp.PROC.MRPSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXCancellationGenSvc/index.html" , "Erp.PROC.MXCancellationGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXCartaPorteGenSvc/index.html" , "Erp.PROC.MXCartaPorteGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXGLJournalsSvc/index.html" , "Erp.PROC.MXGLJournalsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXListOfAccountsSvc/index.html" , "Erp.PROC.MXListOfAccountsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXPaymentMethodSATUpdateSvc/index.html" , "Erp.PROC.MXPaymentMethodSATUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXTrialBalanceSvc/index.html" , "Erp.PROC.MXTrialBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXUpdateAttachmentsPathsSvc/index.html" , "Erp.PROC.MXUpdateAttachmentsPathsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXWHTCertPayTypeUpdateSvc/index.html" , "Erp.PROC.MXWHTCertPayTypeUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MXWHTCertSendToPACSvc/index.html" , "Erp.PROC.MXWHTCertSendToPACSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MassTaxValidationSvc/index.html" , "Erp.PROC.MassTaxValidationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MassVoidCCAuthSvc/index.html" , "Erp.PROC.MassVoidCCAuthSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MfgLeadTimeCalcSvc/index.html" , "Erp.PROC.MfgLeadTimeCalcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MobileSvc/index.html" , "Erp.PROC.MobileSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MultiCompanyDirectSvc/index.html" , "Erp.PROC.MultiCompanyDirectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.MultiCompanySvc/index.html" , "Erp.PROC.MultiCompanySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.NACreditRecalcSvc/index.html" , "Erp.PROC.NACreditRecalcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.NLICPDigipoortSubmitSvc/index.html" , "Erp.PROC.NLICPDigipoortSubmitSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.NLVATDeclarationSubmitSvc/index.html" , "Erp.PROC.NLVATDeclarationSubmitSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.NatAcctMassUpdateSvc/index.html" , "Erp.PROC.NatAcctMassUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PBInvcGenProcSvc/index.html" , "Erp.PROC.PBInvcGenProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PCShrinkFieldPropertiesSvc/index.html" , "Erp.PROC.PCShrinkFieldPropertiesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PEElecPercCertGenSvc/index.html" , "Erp.PROC.PEElecPercCertGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PEElecRetenCertGenSvc/index.html" , "Erp.PROC.PEElecRetenCertGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PLMSvc/index.html" , "Erp.PROC.PLMSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.POGenSugSvc/index.html" , "Erp.PROC.POGenSugSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PRCheckPostSvc/index.html" , "Erp.PROC.PRCheckPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PWJobSvc/index.html" , "Erp.PROC.PWJobSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PartRoHSSvc/index.html" , "Erp.PROC.PartRoHSSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PerBillRegenSvc/index.html" , "Erp.PROC.PerBillRegenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PettyCashPostSvc/index.html" , "Erp.PROC.PettyCashPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PlantCostIDUpdateSvc/index.html" , "Erp.PROC.PlantCostIDUpdateSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PositivePaySvc/index.html" , "Erp.PROC.PositivePaySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PostActualCostAllocSvc/index.html" , "Erp.PROC.PostActualCostAllocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PostPeriodicAvgCostingSvc/index.html" , "Erp.PROC.PostPeriodicAvgCostingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PostTaxReportSvc/index.html" , "Erp.PROC.PostTaxReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PrdPlannerWBSvc/index.html" , "Erp.PROC.PrdPlannerWBSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PreventMntPlanProcessSvc/index.html" , "Erp.PROC.PreventMntPlanProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PriceLstImportExportProcSvc/index.html" , "Erp.PROC.PriceLstImportExportProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ProcessMilestonesSvc/index.html" , "Erp.PROC.ProcessMilestonesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ProcessNettingSvc/index.html" , "Erp.PROC.ProcessNettingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ProdYieldRecalcSvc/index.html" , "Erp.PROC.ProdYieldRecalcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ProjectAnalSvc/index.html" , "Erp.PROC.ProjectAnalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PurchaseSchedulesSvc/index.html" , "Erp.PROC.PurchaseSchedulesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.PurgeGLHistSvc/index.html" , "Erp.PROC.PurgeGLHistSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.QuoteExpirationSvc/index.html" , "Erp.PROC.QuoteExpirationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RJConfirmProcSvc/index.html" , "Erp.PROC.RJConfirmProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RebuildGLAcctDispSvc/index.html" , "Erp.PROC.RebuildGLAcctDispSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RecalculateCustCreditSvc/index.html" , "Erp.PROC.RecalculateCustCreditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RecalculatePartLowLevelSvc/index.html" , "Erp.PROC.RecalculatePartLowLevelSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RecurringAPInvGenSvc/index.html" , "Erp.PROC.RecurringAPInvGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RecurringInvGenSvc/index.html" , "Erp.PROC.RecurringInvGenSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RecycleMRPSvc/index.html" , "Erp.PROC.RecycleMRPSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RefreshOrderRelQtySvc/index.html" , "Erp.PROC.RefreshOrderRelQtySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RegenConfigProcSvc/index.html" , "Erp.PROC.RegenConfigProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RegenerateTaxBoxTranSvc/index.html" , "Erp.PROC.RegenerateTaxBoxTranSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RemoveOrphanPartWipJobOpSvc/index.html" , "Erp.PROC.RemoveOrphanPartWipJobOpSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RemoveOrphanRVLockSvc/index.html" , "Erp.PROC.RemoveOrphanRVLockSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RenewContractProcSvc/index.html" , "Erp.PROC.RenewContractProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RepairInvcDtlShipCostsSvc/index.html" , "Erp.PROC.RepairInvcDtlShipCostsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RepairJobHeadDupPersonSvc/index.html" , "Erp.PROC.RepairJobHeadDupPersonSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RepairJobOperHrsAndCostsSvc/index.html" , "Erp.PROC.RepairJobOperHrsAndCostsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RevAllocRunSvc/index.html" , "Erp.PROC.RevAllocRunSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RevenuePostSvc/index.html" , "Erp.PROC.RevenuePostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.RunGLAllocationsSvc/index.html" , "Erp.PROC.RunGLAllocationsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SGTaxSetupImportSvc/index.html" , "Erp.PROC.SGTaxSetupImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SalesForceSyncSvc/index.html" , "Erp.PROC.SalesForceSyncSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SchedSetOrderProcessSvc/index.html" , "Erp.PROC.SchedSetOrderProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SchedulingProcessSvc/index.html" , "Erp.PROC.SchedulingProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SetContainerDefaultsAndTaxesSvc/index.html" , "Erp.PROC.SetContainerDefaultsAndTaxesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SetCustEInvoiceDefProcSvc/index.html" , "Erp.PROC.SetCustEInvoiceDefProcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SetPOTotalAndTaxDefaultsSvc/index.html" , "Erp.PROC.SetPOTotalAndTaxDefaultsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.SetReceiptDefaultsAndTaxesSvc/index.html" , "Erp.PROC.SetReceiptDefaultsAndTaxesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.ShipConfirmSvc/index.html" , "Erp.PROC.ShipConfirmSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.TransferBalancesSvc/index.html" , "Erp.PROC.TransferBalancesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.TransferCustomerHistorySvc/index.html" , "Erp.PROC.TransferCustomerHistorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.TransferIntermSvc/index.html" , "Erp.PROC.TransferIntermSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.US1099ConvSvc/index.html" , "Erp.PROC.US1099ConvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.UpdatePcValueGrpRelToColsSvc/index.html" , "Erp.PROC.UpdatePcValueGrpRelToColsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.UploadTranGLCDataSvc/index.html" , "Erp.PROC.UploadTranGLCDataSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.UseTaxProcessSvc/index.html" , "Erp.PROC.UseTaxProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.VendPartRoHSSvc/index.html" , "Erp.PROC.VendPartRoHSSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.PROC.VerifyExistingConfigSvc/index.html" , "Erp.PROC.VerifyExistingConfigSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.CdcLogProcessorSvc/index.html" , "Ice.PROC.CdcLogProcessorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.CdcNotificationSenderSvc/index.html" , "Ice.PROC.CdcNotificationSenderSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.CnvProgsProcessSvc/index.html" , "Ice.PROC.CnvProgsProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.DataFabricProcessorSvc/index.html" , "Ice.PROC.DataFabricProcessorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.DynamicQueryExportSvc/index.html" , "Ice.PROC.DynamicQueryExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.FileDataExportSvc/index.html" , "Ice.PROC.FileDataExportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.FileManagerSvc/index.html" , "Ice.PROC.FileManagerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.HealthCheckProcessSvc/index.html" , "Ice.PROC.HealthCheckProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.IoTDeviceEventProcessorSvc/index.html" , "Ice.PROC.IoTDeviceEventProcessorSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.IoTDeviceEventRetrieverSvc/index.html" , "Ice.PROC.IoTDeviceEventRetrieverSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.LanguageImportSvc/index.html" , "Ice.PROC.LanguageImportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.SchedProcSetSvc/index.html" , "Ice.PROC.SchedProcSetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.ScheduledFunctionSvc/index.html" , "Ice.PROC.ScheduledFunctionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.PROC.SysCubeProcessSvc/index.html" , "Ice.PROC.SysCubeProcessSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AGVATPurchaseSvc/index.html" , "Erp.RPT.AGVATPurchaseSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AGVATSalesSvc/index.html" , "Erp.RPT.AGVATSalesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APAgedPayableReportSvc/index.html" , "Erp.RPT.APAgedPayableReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APBankFileImportReportSvc/index.html" , "Erp.RPT.APBankFileImportReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APDebitMemoFormSvc/index.html" , "Erp.RPT.APDebitMemoFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APExpDistbReportSvc/index.html" , "Erp.RPT.APExpDistbReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APInvBalanceReportSvc/index.html" , "Erp.RPT.APInvBalanceReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APInvEditSvc/index.html" , "Erp.RPT.APInvEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APLOCReportSvc/index.html" , "Erp.RPT.APLOCReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APPayEditListReportSvc/index.html" , "Erp.RPT.APPayEditListReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APPromNotesEditSvc/index.html" , "Erp.RPT.APPromNotesEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APPromissoryNotesReportSvc/index.html" , "Erp.RPT.APPromissoryNotesReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APRecNotInvReportSvc/index.html" , "Erp.RPT.APRecNotInvReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.APSelfInvoiceFormSvc/index.html" , "Erp.RPT.APSelfInvoiceFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARAdvBillDepReportSvc/index.html" , "Erp.RPT.ARAdvBillDepReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARAgedRecReportSvc/index.html" , "Erp.RPT.ARAgedRecReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARBankRemittanceSlipSvc/index.html" , "Erp.RPT.ARBankRemittanceSlipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARBillOfExchangeSvc/index.html" , "Erp.RPT.ARBillOfExchangeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARCashRcptEditSvc/index.html" , "Erp.RPT.ARCashRcptEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARDiscAnalysisSvc/index.html" , "Erp.RPT.ARDiscAnalysisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARE1DocReportSvc/index.html" , "Erp.RPT.ARE1DocReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARInvBalanceReportSvc/index.html" , "Erp.RPT.ARInvBalanceReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARInvEditSvc/index.html" , "Erp.RPT.ARInvEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARInvFormSvc/index.html" , "Erp.RPT.ARInvFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARLOCReportSvc/index.html" , "Erp.RPT.ARLOCReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARPayInstrumentReportSvc/index.html" , "Erp.RPT.ARPayInstrumentReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARPercCertReportSvc/index.html" , "Erp.RPT.ARPercCertReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARProcPaymSvc/index.html" , "Erp.RPT.ARProcPaymSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARPromNotesEditSvc/index.html" , "Erp.RPT.ARPromNotesEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARPromissoryNoteReportSvc/index.html" , "Erp.RPT.ARPromissoryNoteReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARRecBalanceSvc/index.html" , "Erp.RPT.ARRecBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARRemittanceSlipSvc/index.html" , "Erp.RPT.ARRemittanceSlipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ARShipNotInvReportSvc/index.html" , "Erp.RPT.ARShipNotInvReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AdvPayBalSvc/index.html" , "Erp.RPT.AdvPayBalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AllocEditSvc/index.html" , "Erp.RPT.AllocEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AnnualJournalRptSvc/index.html" , "Erp.RPT.AnnualJournalRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AssetAnnualScheduleSvc/index.html" , "Erp.RPT.AssetAnnualScheduleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AssetDepreciationReportSvc/index.html" , "Erp.RPT.AssetDepreciationReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AssetEditListSvc/index.html" , "Erp.RPT.AssetEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AssetLabelReportSvc/index.html" , "Erp.RPT.AssetLabelReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.AssetOverviewSvc/index.html" , "Erp.RPT.AssetOverviewSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BENonAdmExpenseReportSvc/index.html" , "Erp.RPT.BENonAdmExpenseReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BESalesReportSvc/index.html" , "Erp.RPT.BESalesReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BEVATTaxDeclReportSvc/index.html" , "Erp.RPT.BEVATTaxDeclReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BOLFormSvc/index.html" , "Erp.RPT.BOLFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BOMCostReportSvc/index.html" , "Erp.RPT.BOMCostReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BOMResAvSvc/index.html" , "Erp.RPT.BOMResAvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BOMSummarizedReportSvc/index.html" , "Erp.RPT.BOMSummarizedReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BTGenJobSvc/index.html" , "Erp.RPT.BTGenJobSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BTGenPCIDSvc/index.html" , "Erp.RPT.BTGenPCIDSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BTGenQASvc/index.html" , "Erp.RPT.BTGenQASvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BankAdjEditSvc/index.html" , "Erp.RPT.BankAdjEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BarGenInvSvc/index.html" , "Erp.RPT.BarGenInvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BarGenRcptSvc/index.html" , "Erp.RPT.BarGenRcptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.BomListingReportSvc/index.html" , "Erp.RPT.BomListingReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCAccuracyRptSvc/index.html" , "Erp.RPT.CCAccuracyRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCMissingABCSvc/index.html" , "Erp.RPT.CCMissingABCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCPCIDCountRptSvc/index.html" , "Erp.RPT.CCPCIDCountRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCPartStatusSvc/index.html" , "Erp.RPT.CCPartStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCPartsNotPostedSvc/index.html" , "Erp.RPT.CCPartsNotPostedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCPartsSelRptSvc/index.html" , "Erp.RPT.CCPartsSelRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CCScheduleRptSvc/index.html" , "Erp.RPT.CCScheduleRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CJ5ReportSvc/index.html" , "Erp.RPT.CJ5ReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNBalanceSheetReportSvc/index.html" , "Erp.RPT.CNBalanceSheetReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNBookVoucherFCReportSvc/index.html" , "Erp.RPT.CNBookVoucherFCReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNBookVoucherReportSvc/index.html" , "Erp.RPT.CNBookVoucherReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNCashBalancesReportSvc/index.html" , "Erp.RPT.CNCashBalancesReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNCashFlowReportSvc/index.html" , "Erp.RPT.CNCashFlowReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNGLedgerReportSvc/index.html" , "Erp.RPT.CNGLedgerReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNGTIStatusReportSvc/index.html" , "Erp.RPT.CNGTIStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNIncomeStmtReportSvc/index.html" , "Erp.RPT.CNIncomeStmtReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNJLedgerReportSvc/index.html" , "Erp.RPT.CNJLedgerReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNSLFCReportSvc/index.html" , "Erp.RPT.CNSLFCReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CNSLReportSvc/index.html" , "Erp.RPT.CNSLReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COAuxiliarIVASvc/index.html" , "Erp.RPT.COAuxiliarIVASvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COBalanceInvSvc/index.html" , "Erp.RPT.COBalanceInvSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COCertificatesSvc/index.html" , "Erp.RPT.COCertificatesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COGLAuxSvc/index.html" , "Erp.RPT.COGLAuxSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COIFRSInventorySvc/index.html" , "Erp.RPT.COIFRSInventorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COInvoicingReportSvc/index.html" , "Erp.RPT.COInvoicingReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COKardexSvc/index.html" , "Erp.RPT.COKardexSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COLocCashRecSvc/index.html" , "Erp.RPT.COLocCashRecSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COLocJrnRecSvc/index.html" , "Erp.RPT.COLocJrnRecSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CONetPresentValueSvc/index.html" , "Erp.RPT.CONetPresentValueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CORevelationReportSvc/index.html" , "Erp.RPT.CORevelationReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.COSupportDocumentSvc/index.html" , "Erp.RPT.COSupportDocumentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CVXA0041Svc/index.html" , "Erp.RPT.CVXA0041Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CalcABCSvc/index.html" , "Erp.RPT.CalcABCSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ChartOfAcctSvc/index.html" , "Erp.RPT.ChartOfAcctSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CheckRegisterSvc/index.html" , "Erp.RPT.CheckRegisterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CntVarReportSvc/index.html" , "Erp.RPT.CntVarReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CntVarSerialNReportSvc/index.html" , "Erp.RPT.CntVarSerialNReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CommissionReportSvc/index.html" , "Erp.RPT.CommissionReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ConsReportSvc/index.html" , "Erp.RPT.ConsReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ConsolidatedPickTicketSvc/index.html" , "Erp.RPT.ConsolidatedPickTicketSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ContLandedCostSvc/index.html" , "Erp.RPT.ContLandedCostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ContShipStatusSvc/index.html" , "Erp.RPT.ContShipStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CostWBInternalReportSvc/index.html" , "Erp.RPT.CostWBInternalReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CostWBUnapprovedReportSvc/index.html" , "Erp.RPT.CostWBUnapprovedReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CostWorkBenchGroupReportSvc/index.html" , "Erp.RPT.CostWorkBenchGroupReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CreditCardRptSvc/index.html" , "Erp.RPT.CreditCardRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CurrencyAcctReportSvc/index.html" , "Erp.RPT.CurrencyAcctReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CurrencyRevalueSvc/index.html" , "Erp.RPT.CurrencyRevalueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CustComplianceSvc/index.html" , "Erp.RPT.CustComplianceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CustomerStatementSvc/index.html" , "Erp.RPT.CustomerStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.CutListsSvc/index.html" , "Erp.RPT.CutListsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DEZ4Z10ReportSvc/index.html" , "Erp.RPT.DEZ4Z10ReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DMRProcRejectSvc/index.html" , "Erp.RPT.DMRProcRejectSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DMRStatusReportSvc/index.html" , "Erp.RPT.DMRStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DefExpRecogEditListSvc/index.html" , "Erp.RPT.DefExpRecogEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DefExpReconRptSvc/index.html" , "Erp.RPT.DefExpReconRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DefExpenseForecastSvc/index.html" , "Erp.RPT.DefExpenseForecastSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DefRevRecogEditListSvc/index.html" , "Erp.RPT.DefRevRecogEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DefRevReconSvc/index.html" , "Erp.RPT.DefRevReconSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DefRevenueSvc/index.html" , "Erp.RPT.DefRevenueSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DeleteAccountsRptSvc/index.html" , "Erp.RPT.DeleteAccountsRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DemandNetChangeReportSvc/index.html" , "Erp.RPT.DemandNetChangeReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DemandReviewReportSvc/index.html" , "Erp.RPT.DemandReviewReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DepositSlipsSvc/index.html" , "Erp.RPT.DepositSlipsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.DiscountAnalysisRptSvc/index.html" , "Erp.RPT.DiscountAnalysisRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EInvoiceReceiptFormSvc/index.html" , "Erp.RPT.EInvoiceReceiptFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EinvoiceStatusReportSvc/index.html" , "Erp.RPT.EinvoiceStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EmpBadgeSvc/index.html" , "Erp.RPT.EmpBadgeSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EmpCourseReportSvc/index.html" , "Erp.RPT.EmpCourseReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EmpEfficiencySvc/index.html" , "Erp.RPT.EmpEfficiencySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EquipListReportSvc/index.html" , "Erp.RPT.EquipListReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EstPrintSvc/index.html" , "Erp.RPT.EstPrintSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.EuropeanSalesReportSvc/index.html" , "Erp.RPT.EuropeanSalesReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ExcessStockReportSvc/index.html" , "Erp.RPT.ExcessStockReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ExpenseReportSvc/index.html" , "Erp.RPT.ExpenseReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ForecastDprtnRptSvc/index.html" , "Erp.RPT.ForecastDprtnRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLAccountSummarySvc/index.html" , "Erp.RPT.GLAccountSummarySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLDistributionReportSvc/index.html" , "Erp.RPT.GLDistributionReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLEntryEditListSvc/index.html" , "Erp.RPT.GLEntryEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLFinancialReportSvc/index.html" , "Erp.RPT.GLFinancialReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLInvReconciliationSvc/index.html" , "Erp.RPT.GLInvReconciliationSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLRefReportSvc/index.html" , "Erp.RPT.GLRefReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLRptEditSvc/index.html" , "Erp.RPT.GLRptEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GLTrialBalanceSvc/index.html" , "Erp.RPT.GLTrialBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GUIAPCheckListSvc/index.html" , "Erp.RPT.GUIAPCheckListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GUIARCheckListSvc/index.html" , "Erp.RPT.GUIARCheckListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GenSOSvc/index.html" , "Erp.RPT.GenSOSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GenShipSvc/index.html" , "Erp.RPT.GenShipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GeneralLedgerSvc/index.html" , "Erp.RPT.GeneralLedgerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GenerateAccountsRptSvc/index.html" , "Erp.RPT.GenerateAccountsRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GlBookReportSvc/index.html" , "Erp.RPT.GlBookReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.GlRecJrnlEditSvc/index.html" , "Erp.RPT.GlRecJrnlEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.INARE3DocSvc/index.html" , "Erp.RPT.INARE3DocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.INAdvBillReceiptReportSvc/index.html" , "Erp.RPT.INAdvBillReceiptReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.INRG1ReportSvc/index.html" , "Erp.RPT.INRG1ReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.INSalesRegisterReportSvc/index.html" , "Erp.RPT.INSalesRegisterReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ImportLogListingSvc/index.html" , "Erp.RPT.ImportLogListingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.InTransitStockSvc/index.html" , "Erp.RPT.InTransitStockSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.InaeReportSvc/index.html" , "Erp.RPT.InaeReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.InspPendReportSvc/index.html" , "Erp.RPT.InspPendReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.IntraStatGenericSvc/index.html" , "Erp.RPT.IntraStatGenericSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.IntraStatIrisSvc/index.html" , "Erp.RPT.IntraStatIrisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.IntraStatReportGenericSvc/index.html" , "Erp.RPT.IntraStatReportGenericSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.IntraStatReportIDEPSvc/index.html" , "Erp.RPT.IntraStatReportIDEPSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.IntraStatReportIrisSvc/index.html" , "Erp.RPT.IntraStatReportIrisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.InvWIPReconSvc/index.html" , "Erp.RPT.InvWIPReconSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.InventoryMovementSvc/index.html" , "Erp.RPT.InventoryMovementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.InventoryUsageSvc/index.html" , "Erp.RPT.InventoryUsageSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JPAPPerBillStmtRptSvc/index.html" , "Erp.RPT.JPAPPerBillStmtRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JPConsumptionTaxReportSvc/index.html" , "Erp.RPT.JPConsumptionTaxReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JobComplianceSvc/index.html" , "Erp.RPT.JobComplianceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JobMtlReqReportSvc/index.html" , "Erp.RPT.JobMtlReqReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JobPickListReportSvc/index.html" , "Erp.RPT.JobPickListReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JobProdDtlSvc/index.html" , "Erp.RPT.JobProdDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JobStatusReportSvc/index.html" , "Erp.RPT.JobStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JobTravSvc/index.html" , "Erp.RPT.JobTravSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.JournalListingSvc/index.html" , "Erp.RPT.JournalListingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.LaborEditSvc/index.html" , "Erp.RPT.LaborEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.LegalNumChangeLogReportSvc/index.html" , "Erp.RPT.LegalNumChangeLogReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.LegalNumCnfgReportSvc/index.html" , "Erp.RPT.LegalNumCnfgReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.LegalNumHistoryReportSvc/index.html" , "Erp.RPT.LegalNumHistoryReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.LogAPInvEditSvc/index.html" , "Erp.RPT.LogAPInvEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.LogInvSuspBalRptSvc/index.html" , "Erp.RPT.LogInvSuspBalRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MESMenuReportSvc/index.html" , "Erp.RPT.MESMenuReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MStockStatusReportSvc/index.html" , "Erp.RPT.MStockStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MXWHTaxCertRptSvc/index.html" , "Erp.RPT.MXWHTaxCertRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MYAnnualLMWSvc/index.html" , "Erp.RPT.MYAnnualLMWSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MYLMWFinishedGoodsSvc/index.html" , "Erp.RPT.MYLMWFinishedGoodsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MYLMWRawMaterialSvc/index.html" , "Erp.RPT.MYLMWRawMaterialSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MYSalesServiceDtlRptSvc/index.html" , "Erp.RPT.MYSalesServiceDtlRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MaintJobRptSvc/index.html" , "Erp.RPT.MaintJobRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MaintReqRptSvc/index.html" , "Erp.RPT.MaintReqRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MasterPackSlipSvc/index.html" , "Erp.RPT.MasterPackSlipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MasterProductionScheduleSvc/index.html" , "Erp.RPT.MasterProductionScheduleSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MaterialTranDetailSvc/index.html" , "Erp.RPT.MaterialTranDetailSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MethodsMasterSvc/index.html" , "Erp.RPT.MethodsMasterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MscPackSlipSvc/index.html" , "Erp.RPT.MscPackSlipSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MscShpLabelSvc/index.html" , "Erp.RPT.MscShpLabelSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MtlQueueRptSvc/index.html" , "Erp.RPT.MtlQueueRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.MtlTagsSvc/index.html" , "Erp.RPT.MtlTagsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NLICPRptReportSvc/index.html" , "Erp.RPT.NLICPRptReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NLVATDeclarationReportSvc/index.html" , "Erp.RPT.NLVATDeclarationReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NOAPPayListReportSvc/index.html" , "Erp.RPT.NOAPPayListReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NatAcctMassUpdRptSvc/index.html" , "Erp.RPT.NatAcctMassUpdRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NettingEditListSvc/index.html" , "Erp.RPT.NettingEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NettingTranReportSvc/index.html" , "Erp.RPT.NettingTranReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.NonConfAnalReportSvc/index.html" , "Erp.RPT.NonConfAnalReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ObsoleteStockReportSvc/index.html" , "Erp.RPT.ObsoleteStockReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.OpenPOReportSvc/index.html" , "Erp.RPT.OpenPOReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.OpenRMASvc/index.html" , "Erp.RPT.OpenRMASvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PBGInvcRptSvc/index.html" , "Erp.RPT.PBGInvcRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PCIDContentsSvc/index.html" , "Erp.RPT.PCIDContentsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PCashEditListSvc/index.html" , "Erp.RPT.PCashEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEAPInvBalanceReportSvc/index.html" , "Erp.RPT.PEAPInvBalanceReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEARInvBalanceReportSvc/index.html" , "Erp.RPT.PEARInvBalanceReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEBalanceSheetSvc/index.html" , "Erp.RPT.PEBalanceSheetSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PECashFlowStatementSvc/index.html" , "Erp.RPT.PECashFlowStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PECostsOfSalesStatementSvc/index.html" , "Erp.RPT.PECostsOfSalesStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEDtlsOfAccBal10Svc/index.html" , "Erp.RPT.PEDtlsOfAccBal10Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEDtlsOfAccTransSvc/index.html" , "Erp.RPT.PEDtlsOfAccTransSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEDtlsOfCashTransSvc/index.html" , "Erp.RPT.PEDtlsOfCashTransSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEFARCurrencyGainLossSvc/index.html" , "Erp.RPT.PEFARCurrencyGainLossSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEFARRevalDtlSvc/index.html" , "Erp.RPT.PEFARRevalDtlSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEFixedAssetsDetailSvc/index.html" , "Erp.RPT.PEFixedAssetsDetailSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEGLTrialBalanceSvc/index.html" , "Erp.RPT.PEGLTrialBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEGeneralLedgerSvc/index.html" , "Erp.RPT.PEGeneralLedgerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEIncomeFrom2CatSvc/index.html" , "Erp.RPT.PEIncomeFrom2CatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEIncomeFrom4CatSvc/index.html" , "Erp.RPT.PEIncomeFrom4CatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEJournalListingSvc/index.html" , "Erp.RPT.PEJournalListingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEKardexReportSvc/index.html" , "Erp.RPT.PEKardexReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEMonthCostElementsSvc/index.html" , "Erp.RPT.PEMonthCostElementsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEProdCostStatementSvc/index.html" , "Erp.RPT.PEProdCostStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEProfitLossStatementSvc/index.html" , "Erp.RPT.PEProfitLossStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEPurchRegisterSvc/index.html" , "Erp.RPT.PEPurchRegisterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PESalesRegisterSvc/index.html" , "Erp.RPT.PESalesRegisterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PEWithholdingsSvc/index.html" , "Erp.RPT.PEWithholdingsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.POFormSvc/index.html" , "Erp.RPT.POFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PRCheckRegisterSvc/index.html" , "Erp.RPT.PRCheckRegisterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PRDeductReportSvc/index.html" , "Erp.RPT.PRDeductReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PREmplEarningsReportSvc/index.html" , "Erp.RPT.PREmplEarningsReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PREmplMasterListingReportSvc/index.html" , "Erp.RPT.PREmplMasterListingReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PRQtrTaxReportSvc/index.html" , "Erp.RPT.PRQtrTaxReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PTranLogSvc/index.html" , "Erp.RPT.PTranLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PackingSlipPrintSvc/index.html" , "Erp.RPT.PackingSlipPrintSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PartComplianceSvc/index.html" , "Erp.RPT.PartComplianceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PartLotWhereUsedReportSvc/index.html" , "Erp.RPT.PartLotWhereUsedReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PartPriceHistorySvc/index.html" , "Erp.RPT.PartPriceHistorySvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PaymentProposalSvc/index.html" , "Erp.RPT.PaymentProposalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PayrollCheckPrintSvc/index.html" , "Erp.RPT.PayrollCheckPrintSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PerBillStmtRptSvc/index.html" , "Erp.RPT.PerBillStmtRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PkgControlIDGeneratorOptsSvc/index.html" , "Erp.RPT.PkgControlIDGeneratorOptsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PlantTransferRsrcTstRptSvc/index.html" , "Erp.RPT.PlantTransferRsrcTstRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PlasticPackagingTaxDetailRptSvc/index.html" , "Erp.RPT.PlasticPackagingTaxDetailRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PlasticPackagingTaxRptSvc/index.html" , "Erp.RPT.PlasticPackagingTaxRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.Prcs1099Svc/index.html" , "Erp.RPT.Prcs1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PrintPettyCashDayBookSvc/index.html" , "Erp.RPT.PrintPettyCashDayBookSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PrintPettyCashSvc/index.html" , "Erp.RPT.PrintPettyCashSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PrintRFQSvc/index.html" , "Erp.RPT.PrintRFQSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PrintTagsSvc/index.html" , "Erp.RPT.PrintTagsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PriorityDispatchSvc/index.html" , "Erp.RPT.PriorityDispatchSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ProFormaInvcSvc/index.html" , "Erp.RPT.ProFormaInvcSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ProcessPaymentSvc/index.html" , "Erp.RPT.ProcessPaymentSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ProdCfgListingSvc/index.html" , "Erp.RPT.ProdCfgListingSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ProjStatRptSvc/index.html" , "Erp.RPT.ProjStatRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PrvDobtCollAcctSvc/index.html" , "Erp.RPT.PrvDobtCollAcctSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PurContSchedRptSvc/index.html" , "Erp.RPT.PurContSchedRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PurchaseListReportSvc/index.html" , "Erp.RPT.PurchaseListReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PurchaseRegisterSvc/index.html" , "Erp.RPT.PurchaseRegisterSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.PurchaseRequisitionSvc/index.html" , "Erp.RPT.PurchaseRequisitionSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.QtyVariancesSvc/index.html" , "Erp.RPT.QtyVariancesSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.QuotFormSvc/index.html" , "Erp.RPT.QuotFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.QuoteWSFormSvc/index.html" , "Erp.RPT.QuoteWSFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RG23AReportSvc/index.html" , "Erp.RPT.RG23AReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RMAFormSvc/index.html" , "Erp.RPT.RMAFormSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RcvLabelSvc/index.html" , "Erp.RPT.RcvLabelSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RefDesBomSvc/index.html" , "Erp.RPT.RefDesBomSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ReminderLetterRptSvc/index.html" , "Erp.RPT.ReminderLetterRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RepSup1099Svc/index.html" , "Erp.RPT.RepSup1099Svc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ReplenishmentMoveSvc/index.html" , "Erp.RPT.ReplenishmentMoveSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ResGrpEffSvc/index.html" , "Erp.RPT.ResGrpEffSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RevRecWBSPhaseEditListSvc/index.html" , "Erp.RPT.RevRecWBSPhaseEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.RevRecognitionEditListSvc/index.html" , "Erp.RPT.RevRecognitionEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ReviewJrnReportSvc/index.html" , "Erp.RPT.ReviewJrnReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SCTicketSvc/index.html" , "Erp.RPT.SCTicketSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SOPickListReportSvc/index.html" , "Erp.RPT.SOPickListReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesAnalysisSvc/index.html" , "Erp.RPT.SalesAnalysisSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesGrossMarginSvc/index.html" , "Erp.RPT.SalesGrossMarginSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesOrderAckSvc/index.html" , "Erp.RPT.SalesOrderAckSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesOrderBacklogSvc/index.html" , "Erp.RPT.SalesOrderBacklogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesOrderOnHoldSvc/index.html" , "Erp.RPT.SalesOrderOnHoldSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesTaxEditSvc/index.html" , "Erp.RPT.SalesTaxEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesTaxReportSvc/index.html" , "Erp.RPT.SalesTaxReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesTaxStatementSvc/index.html" , "Erp.RPT.SalesTaxStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SalesTerEditSvc/index.html" , "Erp.RPT.SalesTerEditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SchedShipmentsSvc/index.html" , "Erp.RPT.SchedShipmentsSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ScheduleImpactSvc/index.html" , "Erp.RPT.ScheduleImpactSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ServiceCallStatusSvc/index.html" , "Erp.RPT.ServiceCallStatusSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ServiceContractStatSvc/index.html" , "Erp.RPT.ServiceContractStatSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ServiceTechDispatchReportSvc/index.html" , "Erp.RPT.ServiceTechDispatchReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SettlementVATSvc/index.html" , "Erp.RPT.SettlementVATSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.ShopLoadReportSvc/index.html" , "Erp.RPT.ShopLoadReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SlowMovingStockSvc/index.html" , "Erp.RPT.SlowMovingStockSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.StockAgingReportSvc/index.html" , "Erp.RPT.StockAgingReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.StockMoveReportSvc/index.html" , "Erp.RPT.StockMoveReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.StockStatusReportSvc/index.html" , "Erp.RPT.StockStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.StructuredTrialBalanceSvc/index.html" , "Erp.RPT.StructuredTrialBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SubCPackSvc/index.html" , "Erp.RPT.SubCPackSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SubShipLablSvc/index.html" , "Erp.RPT.SubShipLablSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SubcontractStatReportSvc/index.html" , "Erp.RPT.SubcontractStatReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SubmissionPropReportSvc/index.html" , "Erp.RPT.SubmissionPropReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SubstShipCustomerSvc/index.html" , "Erp.RPT.SubstShipCustomerSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SubstWhereUsedSvc/index.html" , "Erp.RPT.SubstWhereUsedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.SupplierStatementSvc/index.html" , "Erp.RPT.SupplierStatementSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocAPInvPostSvc/index.html" , "Erp.RPT.THLocAPInvPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocAPPayPostSvc/index.html" , "Erp.RPT.THLocAPPayPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocARInvPostSvc/index.html" , "Erp.RPT.THLocARInvPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocARTaxRecRepSvc/index.html" , "Erp.RPT.THLocARTaxRecRepSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocCashRPostSvc/index.html" , "Erp.RPT.THLocCashRPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocGLJrnPostSvc/index.html" , "Erp.RPT.THLocGLJrnPostSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.THLocMonthlyVATReportSvc/index.html" , "Erp.RPT.THLocMonthlyVATReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TOPackSvc/index.html" , "Erp.RPT.TOPackSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TOPickSvc/index.html" , "Erp.RPT.TOPickSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TWAPInvListSvc/index.html" , "Erp.RPT.TWAPInvListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TWARGUIRptSvc/index.html" , "Erp.RPT.TWARGUIRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TWARInvListSvc/index.html" , "Erp.RPT.TWARInvListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TWARZeroRatedSalesListRptSvc/index.html" , "Erp.RPT.TWARZeroRatedSalesListRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TWVoidBlankLegalNumRptSvc/index.html" , "Erp.RPT.TWVoidBlankLegalNumRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TaxBoxRptSvc/index.html" , "Erp.RPT.TaxBoxRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TaxReconciliationReportSvc/index.html" , "Erp.RPT.TaxReconciliationReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TimeBookingExceptionRptSvc/index.html" , "Erp.RPT.TimeBookingExceptionRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TimePhaseMatReqmtSvc/index.html" , "Erp.RPT.TimePhaseMatReqmtSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TimeReportSvc/index.html" , "Erp.RPT.TimeReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TrialBalanceSvc/index.html" , "Erp.RPT.TrialBalanceSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.TstRulesReportSvc/index.html" , "Erp.RPT.TstRulesReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.USTINValidationReportSvc/index.html" , "Erp.RPT.USTINValidationReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.USTINValidationResultRptSvc/index.html" , "Erp.RPT.USTINValidationResultRptSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.UVTagsReportSvc/index.html" , "Erp.RPT.UVTagsReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.UseTaxReportSvc/index.html" , "Erp.RPT.UseTaxReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VATTaxJournalSvc/index.html" , "Erp.RPT.VATTaxJournalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VATTaxJrnReportSvc/index.html" , "Erp.RPT.VATTaxJrnReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNDICashInBankSvc/index.html" , "Erp.RPT.VNDICashInBankSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNGLReportSvc/index.html" , "Erp.RPT.VNGLReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNInventoryCardSvc/index.html" , "Erp.RPT.VNInventoryCardSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNPurInvListSvc/index.html" , "Erp.RPT.VNPurInvListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNPurchaseDocSvc/index.html" , "Erp.RPT.VNPurchaseDocSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNSaleInvListSvc/index.html" , "Erp.RPT.VNSaleInvListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VNTGLFinancialReportSvc/index.html" , "Erp.RPT.VNTGLFinancialReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VendPriceReportSvc/index.html" , "Erp.RPT.VendPriceReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.VoidLegalNumReportSvc/index.html" , "Erp.RPT.VoidLegalNumReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.W2EditListSvc/index.html" , "Erp.RPT.W2EditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WHTPaymentReportSvc/index.html" , "Erp.RPT.WHTPaymentReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WHTPaymentSubmitReportSvc/index.html" , "Erp.RPT.WHTPaymentSubmitReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WIPReportSvc/index.html" , "Erp.RPT.WIPReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WarrantyStatusReportSvc/index.html" , "Erp.RPT.WarrantyStatusReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WhereUsedSvc/index.html" , "Erp.RPT.WhereUsedSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WithholdCertSvc/index.html" , "Erp.RPT.WithholdCertSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WithholdSchemaBookSvc/index.html" , "Erp.RPT.WithholdSchemaBookSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WorkerCompReportSvc/index.html" , "Erp.RPT.WorkerCompReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.WrntyAnalReportSvc/index.html" , "Erp.RPT.WrntyAnalReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.YTDLoadEditListSvc/index.html" , "Erp.RPT.YTDLoadEditListSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.bankreceditSvc/index.html" , "Erp.RPT.bankreceditSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.bankrecrecapSvc/index.html" , "Erp.RPT.bankrecrecapSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.servcontanalSvc/index.html" , "Erp.RPT.servcontanalSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Erp.RPT.w2formSvc/index.html" , "Erp.RPT.w2formSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.APITraceReportSvc/index.html" , "Ice.RPT.APITraceReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.BAQReportSvc/index.html" , "Ice.RPT.BAQReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.ChgLogReportSvc/index.html" , "Ice.RPT.ChgLogReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.DataDictFieldSvc/index.html" , "Ice.RPT.DataDictFieldSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.DynamicCriteriaSvc/index.html" , "Ice.RPT.DynamicCriteriaSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.FailedLogonAuditLogSvc/index.html" , "Ice.RPT.FailedLogonAuditLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.HealthCheckReportSvc/index.html" , "Ice.RPT.HealthCheckReportSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.SessionAuditLogSvc/index.html" , "Ice.RPT.SessionAuditLogSvc" ],
    ["https://centralusdtapp34.epicorsaas.com/SaaS840/api/swagger/v1/odata/Ice.RPT.UserGroupReportSvc/index.html" , "Ice.RPT.UserGroupReportSvc"],
]


obj = {
    "info",
    "servers",
    "paths",
    "components",
    "tags",
}

async def collectSchema(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url ,headers=creds) as resp:
            if(resp.status != 200):
                print("Error on Getting BAQ ")
                print( resp)
                raise Exception("bad Response")
            return await resp.json()
    
async def writeObjectToPythonFile(fileName, odataObj,methodsObj):    
    serviceName = odataObj["servers"][0]["url"]
    if(url in serviceName):
        serviceName = serviceName.replace(url,"")
    
    f = open("PythonEpicorRestAPI/" + fileName + ".py", "w",  encoding='utf-8')
    
    pythonText = ""
    pythonText += "import asyncio" + "\n"
    pythonText += "import aiohttp" + "\n"
    pythonText += "import configEpicorSchemas" + "\n"
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "\n"
    if("title" in odataObj["info"]):
        pythonText += "# Title: " + odataObj["info"]["title"] + "\n"
    if("description" in odataObj["info"]):
        pythonText += "# Description: " + odataObj["info"]["description"] + "\n"
    if("version" in odataObj["info"]):
        pythonText += "# Version: " + odataObj["info"]["version"] + "\n"
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "#########################################################################" + "\n"
    pythonText += "# OData methods:" + "\n"
    pythonText += "#########################################################################" + "\n"
    
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    
    #Handles OData Methods
    for key,value in odataObj["paths"].items():
        
        for method,methodValue in value.items():
            
            inputParams = []
            inputParamsOptional = []
            hasRequestBody = False
        
            modKey = str(key)
            for thing in thingsToReplace:
                if(thing in modKey):
                    modKey = modKey.replace(thing,"_")
                    
            if(modKey[len(modKey)-1] == "_"):
                modKey = modKey[0:len(modKey)-1]
            
            parameters = ""
            first = 0
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    # if(first > 0):
                        # parameters += ", "
                    if("required" in param.keys()):
                        if(str(param["required"]) == "True"):
                            parameters += param["name"] + ", "
                            inputParams.append(param["name"])
                        else:
                            parameters += param["name"] + " = None, "
                            inputParamsOptional.append(param["name"])
                    else:
                        name = param["name"]
                        if("$" in name):
                            name = name.replace("$","")
                        parameters += name + " = None, "
                    first += 1
            if("requestBody" in methodValue.keys()):
                # if(first > 0):
                    # parameters += 
                parameters += "requestBody, "
                hasRequestBody = True
            if(modKey == ""):
                modKey = "ServiceDocument"
            pythonText += "async def " + method + "" + modKey + "(" + parameters + "epicorHeaders = None):" + "\n"
            print("odata method async def " + method + "" + modKey + "(" + parameters + "):" + "\n")
            
            pythonText += "   \"\"\"  " + "\n"
            if("summary" in methodValue):
                pythonText += "   Summary: " + methodValue["summary"] + "\n"
            if("description" in methodValue):
                pythonText += "   Description: " + methodValue["description"] + "\n"
            if("operationId" in methodValue):
                pythonText += "   OperationID: " + methodValue["operationId"] + "\n"
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    name = param["name"]
                    if("$" in name):
                        name = name.replace("$","")
                    if("description" in param):
                        pythonText += "      :param " + name + ": Desc: " + param["description"]
                    else:
                        pythonText += "      :param " + name + ": Desc: none "
                    if("required" in param.keys()):
                        pythonText += "   Required: " + str(param["required"])
                    if("allowEmptyValue" in param.keys()):
                        pythonText += "   Allow empty value : " + str(param["allowEmptyValue"])
                    pythonText += "\n"
            pythonText += "      :param epicorHeaders: A string representing the epicor log in information to be used, "+ "\n"
            pythonText += "         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds" + "\n"
            if("requestBody" in methodValue.keys()):
                pythonText += "      :param requestBody: Desc: " + methodValue["requestBody"]["description"] + " "
                if("content" in methodValue["requestBody"]):
                        if("application/json" in methodValue["requestBody"]["content"]):
                            if("schema" in methodValue["requestBody"]["content"]["application/json"]):
                                if("$ref" in methodValue["requestBody"]["content"]["application/json"]["schema"]):
                                    pythonText += " => reference" + methodValue["requestBody"]["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    pythonText += " => application/json/schema"
                            else:
                                pythonText += " => application/json"
                        else:
                            pythonText += " => content"
                pythonText += "\n"                
            if("responses" in methodValue.keys()):
                pythonText += "   Returns: " + "\n"
                for response, responseValue in methodValue["responses"].items():
                    pythonText += "      " + response + " Desc: " + responseValue["description"]
                    if("content" in responseValue):
                        if("application/json" in responseValue["content"]):
                            if("schema" in responseValue["content"]["application/json"]):
                                if("$ref" in responseValue["content"]["application/json"]["schema"]):
                                    pythonText += " => reference" + responseValue["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    pythonText += " => application/json/schema"
                            else:
                                pythonText += " => application/json"
                        else:
                            pythonText += " => content"
                    pythonText += "\n"
            
            pythonText += "   \"\"\"  " + "\n"
            pythonText += "\n"
            
            # if(len(inputParams) > 0 or 
            if(len(inputParamsOptional) > 0 ):
                pythonText += "   firstParam = True" + "\n"  
                pythonText += "   params = \"\"" + "\n"           
                # for p in inputParams:
                #     pythonText += "   if(firstParam):" + "\n"  
                #     pythonText += "      params += \"?\"" + "\n"  
                #     pythonText += "      firstParam = False" + "\n"  
                #     pythonText += "   else:" + "\n"  
                #     pythonText += "      params += \"&\"" + "\n"  
                #     pythonText += "   params += \"" + p + "=\" + " + p + "\n"  
                for p in inputParamsOptional:
                    pythonText += "   if(" + p + " != None):" + "\n"  
                    pythonText += "      if(firstParam):" + "\n"  
                    pythonText += "         params += \"?\"" + "\n"  
                    pythonText += "         firstParam = False" + "\n"  
                    pythonText += "      else:" + "\n"  
                    pythonText += "         params += \"&\"" + "\n"  
                    pythonText += "      params += \"" + p + "=\" + " + p + "\n"  
            
            pythonText += "\n"
            
            pythonText += "   creds = configEpicorSchemas.epicorCreds" + "\n"
            pythonText += "   if(epicorHeaders != None):" + "\n"
            pythonText += "         creds = epicorHeaders" + "\n"  
            pythonText += "\n"
            
            pythonText += "   async with aiohttp.ClientSession() as session:" + "\n"
            
            keyName = key
            
            if("{" in keyName):
                keyName = keyName.replace("{", "\" + ")
            if("}" in keyName):
                keyName = keyName.replace("}", " + \"")
                
            
            pythonText += "       async with session." + method + "(configEpicorSchemas.epicorURL + \"" + serviceName + keyName + "\""
            # if(len(inputParams) > 0 or 
            if(len(inputParamsOptional) > 0 ):
                pythonText += " + params"
            if(hasRequestBody):
                pythonText += ", json=requestBody"
            pythonText +=  ",headers=creds) as resp:" + "\n"
            pythonText += "           return await resp.json()" + "\n"
            pythonText += "\n"
            
    
    
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "#########################################################################" + "\n"
    pythonText += "# Custom methods:" + "\n"
    pythonText += "#########################################################################" + "\n"
    
    
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    
    #Handles Custom Methods
    for key,value in methodsObj["paths"].items():
        
        for method,methodValue in value.items():
            
            if("deprecated" in methodValue.keys()):
                if(str(methodValue["deprecated"]) == "True"):
                    continue
                
            inputParams = []
            inputParamsOptional = []
            hasRequestBody = False
        
            modKey = str(key)
            for thing in thingsToReplace:
                if(thing in modKey):
                    modKey = modKey.replace(thing,"_")
                    
            if(modKey[len(modKey)-1] == "_"):
                modKey = modKey[0:len(modKey)-1]
            
            parameters = ""
            first = 0
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    # if(first > 0):
                        # parameters += ", "
                    if("required" in param.keys()):
                        if(str(param["required"]) == "True"):
                            parameters += param["name"] +", "
                            inputParams.append(param["name"])
                        else:
                            parameters += param["name"] + " = None, "
                            inputParamsOptional.append(param["name"])
                    else:
                        name = param["name"]
                        if("$" in name):
                            name = name.replace("$","")
                        parameters += name + " = None, "
                    first += 1
            if("requestBody" in methodValue.keys()):
                # if(first > 0):
                    # parameters += ", "
                parameters += "requestBody, "
                hasRequestBody = True
            if(modKey == ""):
                modKey = "ServiceDocument"
            pythonText += "async def " + method + "" + modKey + "(" + parameters + "epicorHeaders = None):" + "\n"
            print("custom method async def " + method + "" + modKey + "(" + parameters + "epicorHeaders = None):" + "\n")
            
            pythonText += "   \"\"\"  " + "\n"
            if("summary" in methodValue):
                pythonText += "   Summary: " + methodValue["summary"] + "\n"
            if("description" in methodValue):
                pythonText += "   Description: " + methodValue["description"] + "\n"
            if("operationId" in methodValue):
                pythonText += "   OperationID: " + methodValue["operationId"] + "\n"
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    name = param["name"]
                    if("$" in name):
                        name = name.replace("$","")
                    if("description" in param):
                        pythonText += "      :param " + name + ": Desc: " + param["description"]
                    if("required" in param.keys()):
                        pythonText += "   Required: " + str(param["required"])
                    if("allowEmptyValue" in param.keys()):
                        pythonText += "   Allow empty value : " + str(param["allowEmptyValue"])
                    pythonText += "\n"
            pythonText += "      :param epicorHeaders: A string representing the epicor log in information to be used, "+ "\n"
            pythonText += "         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds" + "\n"
            if("requestBody" in methodValue.keys()):
                pythonText += "      :param requestBody: Desc: " + methodValue["requestBody"]["description"] + " "
                if("content" in methodValue["requestBody"]):
                        if("application/json" in methodValue["requestBody"]["content"]):
                            if("schema" in methodValue["requestBody"]["content"]["application/json"]):
                                if("$ref" in methodValue["requestBody"]["content"]["application/json"]["schema"]):
                                    pythonText += " => reference" + methodValue["requestBody"]["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    pythonText += " => application/json/schema"
                            else:
                                pythonText += " => application/json"
                        else:
                            pythonText += " => content"
                pythonText += "\n"
                
            if("responses" in methodValue.keys()):
                pythonText += "   Returns: " + "\n"
                for response, responseValue in methodValue["responses"].items():
                    pythonText += "      " + response + " Desc: " + responseValue["description"]
                    if("content" in responseValue):
                        if("application/json" in responseValue["content"]):
                            if("schema" in responseValue["content"]["application/json"]):
                                if("$ref" in responseValue["content"]["application/json"]["schema"]):
                                    pythonText += " => reference" + responseValue["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    pythonText += " => application/json/schema"
                            else:
                                pythonText += " => application/json"
                        else:
                            pythonText += " => content"
                    pythonText += "\n"
                
            pythonText += "   \"\"\"  " + "\n"
            pythonText += "\n"
            
            if(len(inputParams) > 0 or len(inputParamsOptional) > 0 ):
                pythonText += "   firstParam = True" + "\n"  
                pythonText += "   params = \"\"" + "\n"           
                for p in inputParams:
                    pythonText += "   if(firstParam):" + "\n"  
                    pythonText += "      params += \"?\"" + "\n"  
                    pythonText += "      firstParam = False" + "\n"  
                    pythonText += "   else:" + "\n"  
                    pythonText += "      params += \"&\"" + "\n"  
                    pythonText += "   params += \"" + p + "=\" + " + p + "\n"  
                for p in inputParamsOptional:
                    pythonText += "   if(" + p + " != None):" + "\n"  
                    pythonText += "      if(firstParam):" + "\n"  
                    pythonText += "         params += \"?\"" + "\n"  
                    pythonText += "         firstParam = False" + "\n"  
                    pythonText += "      else:" + "\n"  
                    pythonText += "         params += \"&\"" + "\n"  
                    pythonText += "      params += \"" + p + "=\" + " + p + "\n"  
            
            pythonText += "\n"
            
            pythonText += "   creds = configEpicorSchemas.epicorCreds" + "\n"
            pythonText += "   if(epicorHeaders != None):" + "\n"
            pythonText += "         creds = epicorHeaders" + "\n"  
            pythonText += "\n"
        
            if("{" in keyName):
                keyName = keyName.replace("{", "\" + ")
            if("}" in keyName):
                keyName = keyName.replace("}", " + \"")
            
            pythonText += "   async with aiohttp.ClientSession() as session:" + "\n"
            pythonText += "       async with session." + method + "(configEpicorSchemas.epicorURL + \"" + serviceName + keyName + "\""
            if(len(inputParams) > 0 or len(inputParamsOptional) > 0 ):
                pythonText += " + params"
            if(hasRequestBody):
                pythonText += ", json=requestBody"
            pythonText +=  ",headers=creds) as resp:" + "\n"
            pythonText += "           return await resp.json()" + "\n"
            pythonText += "\n"
    
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "#########################################################################" + "\n"
    pythonText += "# OData Schemas:" + "\n"
    pythonText += "#########################################################################" + "\n"
    
    if("schemas" in odataObj["components"]):   
        for key,value in odataObj["components"]["schemas"].items():
            name = key
            if("." in name):
                name = name.replace(".","_")
                
            pythonText += "class " + name + ":" + "\n"
            print("odata schema class " + name + ":")
            
            pythonText += "   def __init__(self, obj):"  + "\n"
            
            if("properties" in value):
                for property, propertyValue in value["properties"].items():  
                    propName = property
                    if("." in propName):
                        propName = propName.replace(".","")
                    pythonText += "      self." + propName
                                    
                    if("type" in propertyValue):
                        if(propertyValue["type"] == "array"):
                            if("items" in propertyValue):
                                if("$ref" in propertyValue["items"]):
                                    # for ref in propertyValue["items"]:
                                    refName = propertyValue["items"]["$ref"]
                                    if("#/components/schemas/" in refName):
                                        refName = refName.replace("#/components/schemas/","")                                
                                    if("." in refName):
                                        refName = refName.replace(".","_")
                                        
                                    pythonText +=  ":list[" + refName  + "] = obj[\"" + propName + "\"]" + "\n"
                            
                        elif (propertyValue["type"] == "string"):
                            pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                        elif (propertyValue["type"] == "boolean"):
                            pythonText +=  ":bool = obj[\"" + propName + "\"]" + "\n"
                        elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                            pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                        else:
                            pythonText +=  ":" + propertyValue["type"] + " = obj[\"" + propName + "\"]" + "\n"
                    else:
                        pythonText +=  ":any" + "\n"
                        
                    if("description" in propertyValue):
                        pythonText +=  "      \"\"\"  " + str(propertyValue["description"]) + "  \"\"\"  " + "\n"
                        
            pythonText += "      pass" + "\n"
            pythonText += "\n"
        
    
    
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "\n"
    pythonText += "#########################################################################" + "\n"
    pythonText += "# Custom Schemas:" + "\n"
    pythonText += "#########################################################################" + "\n"
    
    if("schemas" in methodsObj["components"]): 
        for key,value in methodsObj["components"]["schemas"].items():
            name = key
            if("." in name):
                name = name.replace(".","_")
                
            pythonText += "class " + name + ":" + "\n"
            print("custom schema class " + name + ":")
            if("required" in value):
                pythonText += "   \"\"\" Required : " + "\n"
                for req in value["required"]:
                    pythonText += "   " + str(req) + "\n"
                pythonText += "   \"\"\"  "   + "\n"
            pythonText += "   def __init__(self, obj):"  + "\n"
            needsPass = True
            if("properties" in value):
                for property, propertyValue in value["properties"].items():  
                    propName = property
                    if("." in propName):
                        propName = propName.replace(".","")
                    if(propName != "parameters"):
                        if(propName == "import"):
                            pythonText += "      self." + propName + "_"
                        else:
                            pythonText += "      self." + propName
                        if("type" in propertyValue):
                            if(propertyValue["type"] == "array"):
                                if("items" in propertyValue):
                                    if("$ref" in propertyValue["items"]):
                                        refName = propertyValue["items"]["$ref"]
                                        if("#/components/schemas/" in refName):
                                            refName = refName.replace("#/components/schemas/","")                                
                                        if("." in refName):
                                            refName = refName.replace(".","_")
                                            
                                        pythonText +=  ":list[" + refName  + "] = obj[\"" + propName + "\"]" + "\n"
                                    elif("type" in propertyValue["items"]):
                                        if (propertyValue["items"]["type"] == "string"):
                                            pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                                        elif (propertyValue["items"]["type"] == "boolean"):
                                            pythonText +=  ":bool = obj[\"" + propName + "\"]" + "\n"
                                        elif (propertyValue["items"]["type"] == "integer" or propertyValue["items"]["type"] == "number"):
                                            pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                                        else:
                                            pythonText +=  ":" + propertyValue["items"]["type"] + "\n"
                            elif (propertyValue["type"] == "string"):
                                pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                            elif (propertyValue["type"] == "boolean"):
                                pythonText +=  ":bool = obj[\"" + propName + "\"]" + "\n"
                            elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                                pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                            elif (propertyValue["type"] == "object"):
                                if("properties" in propertyValue):
                                    for p, pValue in propertyValue["properties"].items():
                                        pythonText += "      self." + p
                                        if("$ref" in pValue):
                                            refName = pValue["$ref"]
                                            if("#/components/schemas/" in refName):
                                                refName = refName.replace("#/components/schemas/","")                                
                                            if("." in refName):
                                                refName = refName.replace(".","_")
                                                
                                            pythonText +=  ":list[" + refName  + "] = obj[\"" + p + "\"]" + "\n"
                                        elif("type" in pValue):
                                            if (propertyValue["type"] == "string"):
                                                pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                                            elif (propertyValue["type"] == "boolean"):
                                                pythonText +=  ":bool = obj[\"" + propName + "\"]" + "\n"
                                            elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                                                pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                                            elif (propertyValue["type"] == "array"):
                                                pythonText +=  ":list = obj[any]" + "\n"
                                            else:
                                                pythonText +=  ": UNKNOW TYPE(error 2269) = obj[\"" + p + "\"]" + "\n"
                                        else:
                                                pythonText += " UNKOWN SOMETHING "  + "\n"
                                else:
                                    pythonText += "      #schema had no properties on an object."  + "\n"
                            else:
                                pythonText +=  ":" + propertyValue["type"] + "\n"
                        elif("$ref" in propertyValue):
                            refName = propertyValue["$ref"]
                            if("#/components/schemas/" in refName):
                                refName = refName.replace("#/components/schemas/","")                                
                            if("." in refName):
                                refName = refName.replace(".","_")    
                            pythonText +=  ":list[" + refName  + "] = obj[\"" + propName + "\"]" + "\n"
                            
                            
                    
                                
                    elif(propName == "parameters"): 
                        needsPass = False
                        pythonText += "      pass" + "\n"
                        pythonText += "\n"
                        pythonText += "   def parameters(self, obj):"  + "\n"
                        
                        if("type" in propertyValue):
                            if(propertyValue["type"] == "array"):
                                if("items" in propertyValue):
                                    if("$ref" in propertyValue["items"]):
                                        refName = propertyValue["items"]["$ref"]
                                        if("#/components/schemas/" in refName):
                                            refName = refName.replace("#/components/schemas/","")                                
                                        if("." in refName):
                                            refName = refName.replace(".","_")
                                            
                                        pythonText +=  ":list[" + refName  + "] = obj[\"" + propName + "\"]" + "\n"
                                    elif("type" in propertyValue["items"]):
                                        if (propertyValue["items"]["type"] == "string"):
                                            pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                                        elif (propertyValue["items"]["type"] == "boolean"):
                                            pythonText +=  ":bool = obj[\"" + propName + "\"]" + "\n"
                                        elif (propertyValue["items"]["type"] == "integer" or propertyValue["items"]["type"] == "number"):
                                            pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                                        else:
                                            pythonText +=  ":" + propertyValue["items"]["type"] + "\n"
                            elif (propertyValue["type"] == "string"):
                                pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                            elif (propertyValue["type"] == "boolean"):
                                pythonText +=  ":bool = obj[\"" + propName + "\"]" + "\n"
                            elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                                pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                            elif (propertyValue["type"] == "object"):
                                for p, pValue in propertyValue["properties"].items():
                                    pythonText += "      self." + p
                                    if("$ref" in pValue):
                                        refName = pValue["$ref"]
                                        if("#/components/schemas/" in refName):
                                            refName = refName.replace("#/components/schemas/","")                                
                                        if("." in refName):
                                            refName = refName.replace(".","_")
                                            
                                        pythonText +=  ":list[" + refName  + "] = obj[\"" + p + "\"]" + "\n"
                                    elif("type" in pValue):
                                        if (pValue["type"] == "boolean"):
                                            pythonText +=  ":bool = obj[\"" + p + "\"]" + "\n"
                                        elif (pValue["type"] == "string"):
                                            pythonText +=  ":str = obj[\"" + propName + "\"]" + "\n"
                                        elif (pValue["type"] == "integer" or pValue["type"] == "number"):
                                            pythonText +=  ":int = obj[\"" + propName + "\"]" + "\n"
                                        elif (pValue["type"] == "array"):
                                            pythonText +=  ":list = obj[any]" + "\n"
                                        else:
                                            pythonText +=  ": UNKNOW TYPE(error 2338) = obj[\"" + p + "\"]" + "\n"
                                    else:
                                            pythonText += " UNKOWN SOMETHING(error 2340) "  + "\n"
                            else:
                                pythonText +=  ":" + propertyValue["type"] + "\n"
                        elif("$ref" in propertyValue):
                            refName = propertyValue["$ref"]
                            if("#/components/schemas/" in refName):
                                refName = refName.replace("#/components/schemas/","")                                
                            if("." in refName):
                                refName = refName.replace(".","_")    
                            pythonText +=  ":list[" + refName  + "] = obj[\"" + propName + "\"]" + "\n"
                        
                        pythonText += "      pass" + "\n"
                        pythonText += "\n"
                    else:
                        pythonText +=  ":error = " + "error" + "\n"
                        
                        
                    if("description" in propertyValue):
                        pythonText +=  "      \"\"\"  " + str(propertyValue["description"]) + "  \"\"\"  " + "\n"
                if(needsPass):
                    pythonText += "      pass" + "\n"
                pythonText += "\n"
            else:
                pythonText += "      pass" + "\n"
                pythonText += "\n"
        
    
    f.write(pythonText)
    f.close()

async def pyConfig():
    if not os.path.exists("PythonEpicorRestAPI/configEpicorSchemas.py"):
        f = open("PythonEpicorRestAPI/configEpicorSchemas.py", "w",  encoding='utf-8')
        configPy = "import base64" + "\n"
        configPy += "\n"
        configPy += "epicorURL = \"YOUR_EPICOR_API_URL_HERE\"" + "\n"
        configPy += "b64 = base64.b64encode(('USERNAME:PASSWORD').encode(\"ascii\")).decode(\"ascii\") " + "\n"
        configPy += "epicorCreds = {'Authorization':'Basic ' + b64}" + "\n"
        configPy += "\n"
        configPy += "def encodeToBase64(str):" + "\n"
        configPy += "    return base64.b64encode((str).encode(\"ascii\")).decode(\"ascii\")" + "\n"
        configPy += "\n"
        configPy += "def encodeToBase64(username, password):" + "\n"
        configPy += "    return base64.b64encode((username + \":\" + password).encode(\"ascii\")).decode(\"ascii\")" + "\n"
        configPy += "\n"
        configPy += "def setEpicorURL(str):" + "\n"
        configPy += "    global epicorURL" + "\n"
        configPy += "    epicorURL = str" + "\n"
        configPy += "\n"
        configPy += "def getEpicorURL():" + "\n"
        configPy += "    return epicorURL" + "\n"
        configPy += "\n"
        configPy += "def setEpicorCreds(creds):" + "\n"
        configPy += "    global epicorCreds" + "\n"
        configPy += "    epicorCreds = creds" + "\n"
        configPy += "\n"    
        configPy += "def setEpicorCreds(username, password):" + "\n"
        configPy += "    global epicorCreds" + "\n"
        configPy += "    epicorCreds = base64.b64encode((username + \":\" + password).encode(\"ascii\")).decode(\"ascii\")" + "\n"
        configPy += "\n"
        configPy += "\n"
        f.write(configPy)
        f.close()
    
async def pyMain():
    
    if not os.path.exists("PythonEpicorRestAPI"):
        os.mkdir("PythonEpicorRestAPI")
        
    pyConfig()
        
    if not os.path.exists("__init__.py"):
        f = open("__init__.py", "w")
        initPy = ""
        f.write(initPy)
        f.close()
    
    i = 1    

    for svc in list:
        print("##########")
        print("##########")
        print("##########")
        print(" Adding schema " + str(i) + "/" + str(len(list)) + "    ->    " + svc[1].replace(".","_"))
        svcURL = svc[0]
        if("/index.html" in svcURL):
            svcURL = svcURL.replace("/index.html","")
        odataObj = await collectSchema(svcURL + ".json")
        methodsObj = await collectSchema(svcURL.replace("odata","methods") + ".json")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("Service : " + svc[1])
        print("########################################################")
        print("########################################################")
        print("########################################################")
        await writeObjectToPythonFile(svc[1].replace(".","_"),odataObj,methodsObj)
        i+=1
        # if(i>20):
            # break

async def writeObjectToTypeScriptFile(fileName, odataObj,methodsObj):    
    serviceName = odataObj["servers"][0]["url"]
    if(url in serviceName):
        serviceName = serviceName.replace(url,"")
    
    f = open("TypeScriptEpicorRestAPI/" + fileName + ".tsx", "w",  encoding='utf-8')
    
    typescriptText = "import * as configEpicorSchemas from \"./configEpicorSchemas\""
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "\n"
    if("title" in odataObj["info"]):
        typescriptText += "// Title: " + odataObj["info"]["title"] + "\n"
    if("description" in odataObj["info"]):
        typescriptText += "// Description: " + odataObj["info"]["description"] + "\n"
    if("version" in odataObj["info"]):
        typescriptText += "// Version: " + odataObj["info"]["version"] + "\n"
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    typescriptText += "// OData methods:" + "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    
    #Handles OData Methods
    for key,value in odataObj["paths"].items():
        
        for method,methodValue in value.items():
            
            inputParams = []
            inputParamsOptional = []
            hasRequestBody = False
        
            modKey = str(key)
            for thing in thingsToReplace:
                if(thing in modKey):
                    modKey = modKey.replace(thing,"_")
                    
            if(modKey[len(modKey)-1] == "_"):
                modKey = modKey[0:len(modKey)-1]
            
            parameters = ""
            first = 0
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    # if(first > 0):
                        # parameters += ", "
                    if("required" in param.keys()):
                        if(str(param["required"]) == "True"):
                            parameters += param["name"] + ":string, "
                            inputParams.append(param["name"])
                        else:
                            parameters += param["name"] + "?:string, "
                            inputParamsOptional.append(param["name"])
                    else:
                        name = param["name"]
                        if("$" in name):
                            name = name.replace("$","")
                        parameters += name + "?:string, "
                    first += 1
            if("requestBody" in methodValue.keys()):
                parameters += "requestBody:any, "
                hasRequestBody = True
            if(modKey == ""):
                modKey = "ServiceDocument"
            
            typescriptText += "\n"
            typescriptText += "   /**  " + "\n"
            if("summary" in methodValue):
                typescriptText += "   Summary: " + methodValue["summary"] + "\n"
            if("description" in methodValue):
                typescriptText += "   Description: " + methodValue["description"] + "\n"
            if("operationId" in methodValue):
                typescriptText += "   OperationID: " + methodValue["operationId"] + "\n"
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    name = param["name"]
                    if("$" in name):
                        name = name.replace("$","")
                    if("description" in param):
                        typescriptText += "      @param " + name + " Desc: " + param["description"]
                    else:
                        typescriptText += "      @param " + name + " Desc: none "
                    if("required" in param.keys()):
                        typescriptText += "   Required: " + str(param["required"])
                    if("allowEmptyValue" in param.keys()):
                        typescriptText += "   Allow empty value : " + str(param["allowEmptyValue"])
                    typescriptText += "\n"
            typescriptText += "      :param epicorHeaders: A string representing the epicor log in information to be used, "+ "\n"
            typescriptText += "         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers" + "\n"
            if("requestBody" in methodValue.keys()):
                typescriptText += "      :param requestBody: Desc: " + methodValue["requestBody"]["description"] + " "
                if("content" in methodValue["requestBody"]):
                        if("application/json" in methodValue["requestBody"]["content"]):
                            if("schema" in methodValue["requestBody"]["content"]["application/json"]):
                                if("$ref" in methodValue["requestBody"]["content"]["application/json"]["schema"]):
                                    typescriptText += " => reference" + methodValue["requestBody"]["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    typescriptText += " => application/json/schema"
                            else:
                                typescriptText += " => application/json"
                        else:
                            typescriptText += " => content"
                typescriptText += "\n"
            returnType = "any"                
            if("responses" in methodValue.keys()):
                typescriptText += "   Returns: " + "\n"
                for response, responseValue in methodValue["responses"].items():
                    typescriptText += "      " + response + " Desc: " + responseValue["description"]
                    if("content" in responseValue):
                        if("application/json" in responseValue["content"]):
                            if("schema" in responseValue["content"]["application/json"]):
                                if("$ref" in responseValue["content"]["application/json"]["schema"]):
                                    if("description" in responseValue):
                                        if(responseValue["description"] == "OK"):
                                            returnType = str(responseValue["content"]["application/json"]["schema"]["$ref"]).replace("#/components/schemas/","")
                                            returnType = returnType.replace(".","_")
                                    typescriptText += " => reference" + responseValue["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    typescriptText += " => application/json/schema"
                            else:
                                if("description" in responseValue):
                                    if(responseValue["description"] == "OK"):
                                        returnType = "JSON"
                                typescriptText += " => application/json"
                        else:
                            typescriptText += " => content"
                    typescriptText += "\n"
            
            typescriptText += "   */  " + "\n"
            
            typescriptText += "export function " + method + "" + modKey + "(" + parameters + "epicorHeaders?:Headers){" + "\n"
            print("odata method export function " + method + "" + modKey + "(" + parameters + "epicorHeaders?:Headers){")
            
            # if(len(inputParams) > 0 or 
            if(len(inputParamsOptional) > 0 ):
                typescriptText += "   var firstParam = true" + "\n"  
                typescriptText += "   var params = \"\"" + "\n"           
                # for p in inputParams:
                #     pythonText += "   if(firstParam):" + "\n"  
                #     pythonText += "      params += \"?\"" + "\n"  
                #     pythonText += "      firstParam = False" + "\n"  
                #     pythonText += "   else:" + "\n"  
                #     pythonText += "      params += \"&\"" + "\n"  
                #     pythonText += "   params += \"" + p + "=\" + " + p + "\n"  
                for p in inputParamsOptional:
                    typescriptText += "   if(typeof " + p + "!== 'undefined'){" + "\n"  
                    typescriptText += "      if(firstParam){" + "\n"  
                    typescriptText += "         params += \"?\"" + "\n"  
                    typescriptText += "         firstParam = false" + "\n"  
                    typescriptText += "      }else{" + "\n"  
                    typescriptText += "         params += \"&\"" + "\n"  
                    typescriptText += "      }" + "\n"  
                    typescriptText += "      params += \"" + p + "=\" + " + p + "\n"  
                    typescriptText += "   }" + "\n"  
            
            typescriptText += "\n"
            
            typescriptText += "   var headers = configEpicorSchemas.epicorHeaders" + "\n"
            typescriptText += "   if(typeof epicorHeaders !== 'undefined'){" + "\n"
            typescriptText += "         headers = epicorHeaders" + "\n"  
            typescriptText += "   }" + "\n"  
            typescriptText += "\n"
            
            keyName = key
            
            if("{" in keyName):
                keyName = keyName.replace("{", "\" + ")
            if("}" in keyName):
                keyName = keyName.replace("}", " + \"")
            
            typescriptText += "   return (new Promise<" + returnType + ">((resolve, reject) => {" + "\n"
            typescriptText += "      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + \"" + serviceName + keyName + "\""
            if(len(inputParamsOptional) > 0 ):
                typescriptText += " + params"
            typescriptText += ", {" + "\n"
            typescriptText += "          method: '" + method + "'," + "\n"
            typescriptText += "          headers: headers," + "\n"
            if(hasRequestBody):
                typescriptText += "          body: JSON.stringify(requestBody)" + "\n"
            typescriptText += "      })" + "\n"
            typescriptText += "      fetch(request)" + "\n"
            typescriptText += "      .then((res) => res.json())" + "\n"
            typescriptText += "      .then((data) => {" + "\n"
            typescriptText += "         resolve(data as " + returnType + ")" + "\n"
            typescriptText += "          })" + "\n"
            typescriptText += "      .catch((error) => {" + "\n"
            typescriptText += "          reject(error)" + "\n"
            typescriptText += "      })" + "\n"
            typescriptText += "   }))" + "\n"
            typescriptText += "}" + "\n"
            
    
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    typescriptText += "// Custom methods:" + "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    
    
    # #########################################################################################################
    # #########################################################################################################
    # #########################################################################################################
    
    #Handles Custom Methods
    for key,value in methodsObj["paths"].items():
        
        for method,methodValue in value.items():
            
            if("deprecated" in methodValue.keys()):
                if(str(methodValue["deprecated"]) == "True"):
                    continue
                
            inputParams = []
            inputParamsOptional = []
            hasRequestBody = False
        
            modKey = str(key)
            for thing in thingsToReplace:
                if(thing in modKey):
                    modKey = modKey.replace(thing,"_")
                    
            if(modKey[len(modKey)-1] == "_"):
                modKey = modKey[0:len(modKey)-1]
            
            parameters = ""
            first = 0
            returnType = "any"    
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    # if(first > 0):
                        # parameters += ", "
                    if("required" in param.keys()):
                        if(str(param["required"]) == "True"):
                            parameters += param["name"] +":string, "
                            inputParams.append(param["name"])
                        else:
                            parameters += param["name"] + "?:string, "
                            inputParamsOptional.append(param["name"])
                    else:
                        name = param["name"]
                        if("$" in name):
                            name = name.replace("$","")
                        parameters += name + "?:string, "
                    first += 1
            if("requestBody" in methodValue.keys()):
                # if(first > 0):
                    # parameters += ", "
                parameters += "requestBody:any, "
                hasRequestBody = True
            if(modKey == ""):
                modKey = "ServiceDocument"
            
            typescriptText += "\n"
            typescriptText += "   /**  " + "\n"
            if("summary" in methodValue):
                typescriptText += "   Summary: " + methodValue["summary"] + "\n"
            if("description" in methodValue):
                typescriptText += "   Description: " + methodValue["description"] + "\n"
            if("operationId" in methodValue):
                typescriptText += "   OperationID: " + methodValue["operationId"] + "\n"
            if("parameters" in methodValue.keys()):
                for param in methodValue["parameters"]:
                    name = param["name"]
                    if("$" in name):
                        name = name.replace("$","")
                    if("description" in param):
                        typescriptText += "      @param " + name + " Desc: " + param["description"]
                    if("required" in param.keys()):
                        typescriptText += "   Required: " + str(param["required"])
                    if("allowEmptyValue" in param.keys()):
                        typescriptText += "   Allow empty value : " + str(param["allowEmptyValue"])
                    typescriptText += "\n"
            typescriptText += "      :param epicorHeaders: A string representing the epicor log in information to be used, "+ "\n"
            typescriptText += "         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds" + "\n"
            if("requestBody" in methodValue.keys()):
                typescriptText += "      :param requestBody: Desc: " + methodValue["requestBody"]["description"] + " "
                if("content" in methodValue["requestBody"]):
                        if("application/json" in methodValue["requestBody"]["content"]):
                            if("schema" in methodValue["requestBody"]["content"]["application/json"]):
                                if("$ref" in methodValue["requestBody"]["content"]["application/json"]["schema"]):
                                    if("description" in responseValue):
                                        if(responseValue["description"] == "OK"):
                                            returnType = str(responseValue["content"]["application/json"]["schema"]["$ref"]).replace("#/components/schemas/","")
                                            returnType = returnType.replace(".","_")
                                    typescriptText += " => reference" + methodValue["requestBody"]["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    typescriptText += " => application/json/schema"
                            else:
                                if("description" in responseValue):
                                    if(responseValue["description"] == "OK"):
                                        returnType = "JSON"
                                typescriptText += " => application/json"
                        else:
                            typescriptText += " => content"
                typescriptText += "\n"
                
            if("responses" in methodValue.keys()):
                typescriptText += "   Returns: " + "\n"
                for response, responseValue in methodValue["responses"].items():
                    typescriptText += "      " + response + " Desc: " + responseValue["description"]
                    if("content" in responseValue):
                        if("application/json" in responseValue["content"]):
                            if("schema" in responseValue["content"]["application/json"]):
                                if("$ref" in responseValue["content"]["application/json"]["schema"]):
                                    typescriptText += " => reference" + responseValue["content"]["application/json"]["schema"]["$ref"]
                                else:
                                    typescriptText += " => application/json/schema"
                            else:
                                typescriptText += " => application/json"
                        else:
                            typescriptText += " => content"
                    typescriptText += "\n"
                
            typescriptText += "   */  " + "\n"
            
            typescriptText += "export function " + method + "" + modKey + "(" + parameters + "epicorHeaders?:Headers){" + "\n"
            print("custom method export function " + method + "" + modKey + "(" + parameters + "epicorHeaders?:Headers){" )
            
            if(len(inputParams) > 0 or len(inputParamsOptional) > 0 ):
                typescriptText += "   var firstParam = true" + "\n"  
                typescriptText += "   var params = \"\"" + "\n"           
                for p in inputParams:
                    typescriptText += "   if(typeof " + p + "!== 'undefined'){" + "\n"  
                    typescriptText += "      if(firstParam){" + "\n"  
                    typescriptText += "         params += \"?\"" + "\n"  
                    typescriptText += "         firstParam = false" + "\n"  
                    typescriptText += "      }else{" + "\n"  
                    typescriptText += "         params += \"&\"" + "\n"  
                    typescriptText += "      }" + "\n"  
                    typescriptText += "      params += \"" + p + "=\" + " + p + "\n"  
                    typescriptText += "   }" + "\n"  
                for p in inputParamsOptional:
                    typescriptText += "   if(typeof " + p + "!== 'undefined'){" + "\n"  
                    typescriptText += "      if(firstParam){" + "\n"  
                    typescriptText += "         params += \"?\"" + "\n"  
                    typescriptText += "         firstParam = false" + "\n"  
                    typescriptText += "      }else{" + "\n"  
                    typescriptText += "         params += \"&\"" + "\n"  
                    typescriptText += "      }" + "\n"  
                    typescriptText += "      params += \"" + p + "=\" + " + p + "\n"  
                    typescriptText += "   }" + "\n"  
            
            typescriptText += "\n"
            
            typescriptText += "   var headers = configEpicorSchemas.epicorHeaders" + "\n"
            typescriptText += "   if(typeof epicorHeaders !== 'undefined'){" + "\n"
            typescriptText += "         headers = epicorHeaders" + "\n"  
            typescriptText += "   }" + "\n"  
            typescriptText += "\n"
            
            keyName = key
            
            if("{" in keyName):
                keyName = keyName.replace("{", "\" + ")
            if("}" in keyName):
                keyName = keyName.replace("}", " + \"")
            
            typescriptText += "   return (new Promise<" + returnType + ">((resolve, reject) => {" + "\n"
            typescriptText += "      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + \"" + serviceName + keyName + "\""
            if(len(inputParams) > 0 or len(inputParamsOptional) > 0 ):
                typescriptText += " + params"
            typescriptText += ", {" + "\n"
            typescriptText += "          method: '" + method + "'," + "\n"
            typescriptText += "          headers: headers," + "\n"
            if(hasRequestBody):
                typescriptText += "          body: JSON.stringify(requestBody)" + "\n"
            typescriptText += "      })" + "\n"
            typescriptText += "      fetch(request)" + "\n"
            typescriptText += "      .then((res) => res.json())" + "\n"
            typescriptText += "      .then((data) => {" + "\n"
            typescriptText += "         resolve(data as " + returnType + ")" + "\n"
            typescriptText += "          })" + "\n"
            typescriptText += "      .catch((error) => {" + "\n"
            typescriptText += "          reject(error)" + "\n"
            typescriptText += "      })" + "\n"
            typescriptText += "   }))" + "\n"
            typescriptText += "}" + "\n"
    
    # #########################################################################################################
    # #########################################################################################################
    # #########################################################################################################
    
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    typescriptText += "// OData Schemas:" + "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    
    if("schemas" in odataObj["components"]):   
        for key,value in odataObj["components"]["schemas"].items():
            name = key
            if("." in name):
                name = name.replace(".","_")
                
            typescriptText += "export interface " + name + "{" + "\n"
            print("odata schema export interface " + name + "{")
                        
            if("properties" in value):
                for property, propertyValue in value["properties"].items():  
                    propName = property
                    if("." in propName):
                        propName = propName.replace(".","")
                        
                    if("description" in propertyValue):
                        typescriptText +=  "      /**  " + str(propertyValue["description"]) + "  */  " + "\n"
                        
                    typescriptText += "   \"" + propName + "\""
                    
                    if("type" in propertyValue):
                        if(propertyValue["type"] == "array"):
                            if("items" in propertyValue):
                                if("$ref" in propertyValue["items"]):
                                    # for ref in propertyValue["items"]:
                                    refName = propertyValue["items"]["$ref"]
                                    if("#/components/schemas/" in refName):
                                        refName = refName.replace("#/components/schemas/","")                                
                                    if("." in refName):
                                        refName = refName.replace(".","_")
                                        
                                    typescriptText +=  ":" + refName  + "[]," + "\n"
                            
                        elif (propertyValue["type"] == "string"):
                            typescriptText +=  ":string," + "\n"
                        elif (propertyValue["type"] == "boolean"):
                            typescriptText +=  ":boolean," + "\n"
                        elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                            typescriptText +=  ":number," + "\n"
                        else:
                            typescriptText +=  ":" + propertyValue["type"] + "," + "\n"
                    else:
                        typescriptText +=  ":any" + "\n"
                        
                    
                        
            typescriptText += "}" + "\n"
            typescriptText += "\n"
        
    
    
    # #########################################################################################################
    # #########################################################################################################
    # #########################################################################################################
    
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    typescriptText += "// Custom Schemas:" + "\n"
    typescriptText += "//////////////////////////////////////////////////////////////////////////" + "\n"
    
    if("schemas" in methodsObj["components"]): 
        for key,value in methodsObj["components"]["schemas"].items():
            name = key
            if("." in name):
                name = name.replace(".","_")
                
            if("required" in value):
                typescriptText += "   /** Required : " + "\n"
                for req in value["required"]:
                    typescriptText += "      @param " + str(req) + "\n"
                typescriptText += "   */  "   + "\n"
                
            typescriptText += "export interface " + name + "{" + "\n"
            print("custom schema export interface " + name + ":")
            
            needsPass = True
            needsParams = False
            if("properties" in value):
                for property, propertyValue in value["properties"].items():  
                    propName = property
                                                
                    if("." in propName):
                        propName = propName.replace(".","")
                    if(propName != "parameters"):
                        
                        if("description" in propertyValue):
                            typescriptText +=  "      /**  " + str(propertyValue["description"]) + "  */  " + "\n"
                            
                        needsParams = True
                        if(propName == "import"):
                            typescriptText += "   " + propName + "_"
                        else:
                            typescriptText += "   " + propName
                        if("type" in propertyValue):
                            if(propertyValue["type"] == "array"):
                                if("items" in propertyValue):
                                    if("$ref" in propertyValue["items"]):
                                        refName = propertyValue["items"]["$ref"]
                                        if("#/components/schemas/" in refName):
                                            refName = refName.replace("#/components/schemas/","")                                
                                        if("." in refName):
                                            refName = refName.replace(".","_")
                                            
                                        typescriptText +=  ":" + refName  + "[]," + "\n"
                                    elif("type" in propertyValue["items"]):
                                        if (propertyValue["items"]["type"] == "string"):
                                            typescriptText +=  ":string," + "\n"
                                        elif (propertyValue["items"]["type"] == "boolean"):
                                            typescriptText +=  ":boolean," + "\n"
                                        elif (propertyValue["items"]["type"] == "integer" or propertyValue["items"]["type"] == "number"):
                                            typescriptText +=  ":number," + "\n"
                                        else:
                                            typescriptText +=  ":" + propertyValue["items"]["type"] + "\n"
                            elif (propertyValue["type"] == "string"):
                                typescriptText +=  ":string," + "\n"
                            elif (propertyValue["type"] == "boolean"):
                                typescriptText +=  ":boolean," + "\n"
                            elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                                typescriptText +=  ":number," + "\n"
                            elif (propertyValue["type"] == "object"):
                                if("properties" in propertyValue):
                                    for p, pValue in propertyValue["properties"].items():
                                        typescriptText += "   " + p
                                        if("$ref" in pValue):
                                            refName = pValue["$ref"]
                                            if("#/components/schemas/" in refName):
                                                refName = refName.replace("#/components/schemas/","")                                
                                            if("." in refName):
                                                refName = refName.replace(".","_")
                                                
                                            typescriptText +=  ":" + refName  + "[]," + "\n"
                                        elif("type" in pValue):
                                            if (propertyValue["type"] == "string"):
                                                typescriptText +=  ":string," + "\n"
                                            elif (propertyValue["type"] == "boolean"):
                                                typescriptText +=  ":boolean," + "\n"
                                            elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                                                typescriptText +=  ":number," + "\n"
                                            elif (propertyValue["type"] == "array"):
                                                typescriptText +=  ":any[]" + "\n"
                                            else:
                                                typescriptText +=  ": UNKNOW TYPE(error 2269)," + "\n"
                                        else:
                                                typescriptText += " UNKOWN SOMETHING "  + "\n"
                                else:
                                    typescriptText += ":any,      //schema had no properties on an object."  + "\n"
                            else:
                                typescriptText +=  ":" + propertyValue["type"] + "," + "\n"
                        elif("$ref" in propertyValue):
                            refName = propertyValue["$ref"]
                            if("#/components/schemas/" in refName):
                                refName = refName.replace("#/components/schemas/","")                                
                            if("." in refName):
                                refName = refName.replace(".","_")    
                            typescriptText +=  ":" + refName  + "[]," + "\n"
                            
                            
                    
                                
                    elif(propName == "parameters"): 
                        needsPass = False
                        # if(needsParams):
                            # typescriptText += "}" + "\n"
                            # typescriptText += "\n"                                
                            # typescriptText += "export interface " + name + "_parameters{"  + "\n"
                        # else:
                            # typescriptText += "export interface " + name + "{"  + "\n"
                            
                        typescriptText += "parameters : {"  + "\n"
                        
                        if("description" in propertyValue):
                            typescriptText +=  "      /**  " + str(propertyValue["description"]) + "  */  " + "\n"
                        
                        if("type" in propertyValue):
                            if(propertyValue["type"] == "array"):
                                if("items" in propertyValue):
                                    if("$ref" in propertyValue["items"]):
                                        refName = propertyValue["items"]["$ref"]
                                        if("#/components/schemas/" in refName):
                                            refName = refName.replace("#/components/schemas/","")                                
                                        if("." in refName):
                                            refName = refName.replace(".","_")
                                            
                                        typescriptText +=  ":" + refName  + "[]," + "\n"
                                    elif("type" in propertyValue["items"]):
                                        if (propertyValue["items"]["type"] == "string"):
                                            typescriptText +=  ":string," + "\n"
                                        elif (propertyValue["items"]["type"] == "boolean"):
                                            typescriptText +=  ":boolean," + "\n"
                                        elif (propertyValue["items"]["type"] == "integer" or propertyValue["items"]["type"] == "number"):
                                            typescriptText +=  ":number," + "\n"
                                        else:
                                            typescriptText +=  ":" + propertyValue["items"]["type"] + "\n"
                            elif (propertyValue["type"] == "string"):
                                typescriptText +=  ":string," + "\n"
                            elif (propertyValue["type"] == "boolean"):
                                typescriptText +=  ":boolean," + "\n"
                            elif (propertyValue["type"] == "integer" or propertyValue["type"] == "number"):
                                typescriptText +=  ":number," + "\n"
                            elif (propertyValue["type"] == "object"):
                                for p, pValue in propertyValue["properties"].items():
                                    typescriptText += "   " + p
                                    if("$ref" in pValue):
                                        refName = pValue["$ref"]
                                        if("#/components/schemas/" in refName):
                                            refName = refName.replace("#/components/schemas/","")                                
                                        if("." in refName):
                                            refName = refName.replace(".","_")
                                            
                                        typescriptText +=  ":" + refName  + "[]," + "\n"
                                    elif("type" in pValue):
                                        if (pValue["type"] == "boolean"):
                                            typescriptText +=  ":boolean," + "\n"
                                        elif (pValue["type"] == "string"):
                                            typescriptText +=  ":string," + "\n"
                                        elif (pValue["type"] == "integer" or pValue["type"] == "number"):
                                            typescriptText +=  ":number," + "\n"
                                        elif (pValue["type"] == "array"):
                                            typescriptText +=  ":any[]," + "\n"
                                        else:
                                            typescriptText +=  ": UNKNOW TYPE(error 2338)," + "\n"
                                    else:
                                            typescriptText += " UNKOWN SOMETHING(error 2340) "  + "\n"
                            else:
                                typescriptText +=  ":" + propertyValue["type"] + "," + "\n"
                        elif("$ref" in propertyValue):
                            refName = propertyValue["$ref"]
                            if("#/components/schemas/" in refName):
                                refName = refName.replace("#/components/schemas/","")                                
                            if("." in refName):
                                refName = refName.replace(".","_")    
                            typescriptText +=  ":" + refName  + "[]," + "\n"
                        
                        typescriptText += "}" + "\n"
                        # typescriptText += "\n"
                    else:
                        typescriptText +=  ":error = " + "error" + "\n"
                        
                    
                # if(needsPass):
            
            typescriptText += "}" + "\n"
            typescriptText += "\n"
        
    
    f.write(typescriptText)
    f.close()
    
async def typescriptConfig():
    if not os.path.exists("TypeScriptEpicorRestAPI/configEpicorSchemas.tsx"):
        f = open("TypeScriptEpicorRestAPI/configEpicorSchemas.tsx", "w",  encoding='utf-8')
        configTS = ""
        configTS += "\n"
        configTS += "export var epicorURL = \"YOUR_EPICOR_API_URL_HERE\"" + "\n"
        configTS += "/** Used to encode a string to base64 encoding */" + "\n"
        configTS += "export const encode = (str: string):string => Buffer.from(str, 'binary').toString('base64');"  + "\n"
        configTS += "export var epicorHeaders: Headers = new Headers({'Content-Type': 'application/json','Accept': 'application/json'})" + "\n"
        configTS += "\n"
        configTS += "export function encodeToBase64(username:string, password:string){" + "\n"
        configTS += "    return encode(username + \":\" + password)" + "\n"
        configTS += "}" + "\n"
        configTS += "\n"
        configTS += "export function setEpicorURL(str:string){" + "\n"
        configTS += "    epicorURL = str" + "\n"
        configTS += "}" + "\n"
        configTS += "\n"
        configTS += "export function getEpicorURL(){" + "\n"
        configTS += "    return epicorURL" + "\n"
        configTS += "}" + "\n"
        configTS += "\n"
        configTS += "export function setEpicorHeader(header:Headers){" + "\n"
        configTS += "    epicorHeaders = header" + "\n"
        configTS += "}" + "\n"
        configTS += "\n"    
        configTS += "export function setEpicorHeaderAuthoriziation(username:string, password:string){" + "\n"
        configTS += "    epicorHeaders.set('Authorization', \"Basic \" + encode(username + ':' + password))" + "\n"
        configTS += "}" + "\n"
        configTS += "export interface EpicorJsonObject{" + "\n"
        configTS += "   \"odata.metadata\" : string" + "\n"
        configTS += "   value : any" + "\n"
        configTS += "}" + "\n"
        configTS += "\n"
        configTS += "\n"
        
        f.write(configTS)
        f.close()

async def tsMain():
    
    if not os.path.exists("TypeScriptEpicorRestAPI"):
        os.mkdir("TypeScriptEpicorRestAPI")
        
    await typescriptConfig()
    
    i = 1    

    for svc in list:
        print("##########")
        print("##########")
        print("##########")
        print(" Adding schema " + str(i) + "/" + str(len(list)) + "    ->    " + svc[1].replace(".","_"))
        svcURL = svc[0]
        if("/index.html" in svcURL):
            svcURL = svcURL.replace("/index.html","")
        odataObj = await collectSchema(svcURL + ".json")
        methodsObj = await collectSchema(svcURL.replace("odata","methods") + ".json")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("Service : " + svc[1])
        print("########################################################")
        print("########################################################")
        print("########################################################")
        await writeObjectToTypeScriptFile(svc[1].replace(".","_"),odataObj,methodsObj)
        i+=1
        # if(i>20):
            # break
    
async def main():
    print()
    
    #await pyMain()
    
    await tsMain()
    
    
    
    
    
    
start = datetime.datetime.now()
print("StartTime : ", start)

asyncio.run(main())

end = datetime.datetime.now()
timediff = end-start

print("timetake = ",(timediff))

