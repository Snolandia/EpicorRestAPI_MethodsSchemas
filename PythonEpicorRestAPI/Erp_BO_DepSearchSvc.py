import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DepSearchSvc
# Description: This object returns deposit inoices and payments for the particulat sales order.
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DepSearchSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DepSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetDeposits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeposits
   Description: This method returns deposit inoices and payments for the particulat sales order.
   OperationID: GetDeposits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeposits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeposits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DepSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_AllocDepositTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.PrePayType:int = obj["PrePayType"]
      """  "0 - Prepaid Invoiced Deposit   1 - Cash Deposit 2 - Reverse Cash Deposit"  """  
      self.DepInvoiceNum:int = obj["DepInvoiceNum"]
      """  Deposit Invoice Number  """  
      self.DepGroupID:str = obj["DepGroupID"]
      """  Group ID of deposit payment  """  
      self.DepHeadNum:int = obj["DepHeadNum"]
      """  Identification of Deposit Payment  """  
      self.DepApplyDate:str = obj["DepApplyDate"]
      """  Apply Date of Deposit Invoice  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Sales Order Number  """  
      self.PrePayStatus:int = obj["PrePayStatus"]
      """  "0 - Unrecognized               1 - Partial Recognized 2 - Full Recognized"  """  
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      """  Allocated Amount  """  
      self.AllocAmt:int = obj["AllocAmt"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.DocAllocBal:int = obj["DocAllocBal"]
      """  Allocated Balance  """  
      self.AllocBal:int = obj["AllocBal"]
      self.Rpt1AllocBal:int = obj["Rpt1AllocBal"]
      self.Rpt2AllocBal:int = obj["Rpt2AllocBal"]
      self.Rpt3AllocBal:int = obj["Rpt3AllocBal"]
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Total Tax Amount of Deposit  """  
      self.TaxAmt:int = obj["TaxAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.DocAllocTaxBal:int = obj["DocAllocTaxBal"]
      """  Remaining Tax Amount of Deposit  """  
      self.AllocTaxBal:int = obj["AllocTaxBal"]
      self.Rpt1AllocTaxBal:int = obj["Rpt1AllocTaxBal"]
      self.Rpt2AllocTaxBal:int = obj["Rpt2AllocTaxBal"]
      self.Rpt3AllocTaxBal:int = obj["Rpt3AllocTaxBal"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Shipment Invoice Number for which this Deposit is allocated  """  
      self.DepCheckRef:str = obj["DepCheckRef"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  Currency switch used to determine what currency to display amounts in.  """  
      self.DocOriginalAmt:int = obj["DocOriginalAmt"]
      """  Original Amt  """  
      self.OriginalAmt:int = obj["OriginalAmt"]
      self.Rpt1OriginalAmt:int = obj["Rpt1OriginalAmt"]
      self.Rpt2OriginalAmt:int = obj["Rpt2OriginalAmt"]
      self.Rpt3OriginalAmt:int = obj["Rpt3OriginalAmt"]
      self.DocOriginalTaxAmt:int = obj["DocOriginalTaxAmt"]
      """  Original Tax Amt  """  
      self.OriginalTaxAmt:int = obj["OriginalTaxAmt"]
      self.Rpt1OriginalTaxAmt:int = obj["Rpt1OriginalTaxAmt"]
      self.Rpt2OriginalTaxAmt:int = obj["Rpt2OriginalTaxAmt"]
      self.Rpt3OriginalTaxAmt:int = obj["Rpt3OriginalTaxAmt"]
      self.CustNum:int = obj["CustNum"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.Reference:str = obj["Reference"]
      self.IsDepCM:bool = obj["IsDepCM"]
      """  IsDepCM to distinguish between Deposit Billing Invoices and Deposit Billing Credit Memos  """  
      self.DepInvoiceDate:str = obj["DepInvoiceDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DepSearchTableset:
   def __init__(self, obj):
      self.DepSearchTot:list[Erp_Tablesets_DepSearchTotRow] = obj["DepSearchTot"]
      self.AllocDepositTrk:list[Erp_Tablesets_AllocDepositTrkRow] = obj["AllocDepositTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DepSearchTotRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.AllocAmt:int = obj["AllocAmt"]
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.AllocBal:int = obj["AllocBal"]
      self.DocAllocBal:int = obj["DocAllocBal"]
      self.Rpt1AllocBal:int = obj["Rpt1AllocBal"]
      self.Rpt2AllocBal:int = obj["Rpt2AllocBal"]
      self.Rpt3AllocBal:int = obj["Rpt3AllocBal"]
      self.TaxAmt:int = obj["TaxAmt"]
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      self.AllocTaxBal:int = obj["AllocTaxBal"]
      self.DocAllocTaxBal:int = obj["DocAllocTaxBal"]
      self.Rpt1AllocTaxBal:int = obj["Rpt1AllocTaxBal"]
      self.Rpt2AllocTaxBal:int = obj["Rpt2AllocTaxBal"]
      self.Rpt3AllocTaxBal:int = obj["Rpt3AllocTaxBal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetDeposits_input:
   """ Required : 
   ipOrderNum
   ds
   """  
   def __init__(self, obj):
      self.ipOrderNum:int = obj["ipOrderNum"]
      """  Sales Order Number  """  
      self.ds:list[Erp_Tablesets_DepSearchTableset] = obj["ds"]
      pass

class GetDeposits_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DepSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

