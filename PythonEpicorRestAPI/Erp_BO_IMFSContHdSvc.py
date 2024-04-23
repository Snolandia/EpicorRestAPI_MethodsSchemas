import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMFSContHdSvc
# Description: Bi-Directional integration point for FSContHd, FSContDt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AckFSContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AckFSContHd
   Description: Acknowledges that passed in IntQueIDs have been received and processed and can be removed from the IntQueOut and IM tables.
   OperationID: AckFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AckFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AckFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CountFSContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CountFSContHd
   Description: Returns the count of existing IntQueOut records along with the count of updated FSContHd in the database that IntQueOut records have not yet been created for
   OperationID: CountFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CountFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CountFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllFSContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllFSContHd
   Description: Generates IntQueOut and IMFSContHd rows since the last time this was called and then returns these along with any existing
   OperationID: GetAllFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFSContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFSContHd
   Description: Generates IntQueOut and IMFSContHd rows since the last time this was called and then returns these along with any existing
   OperationID: GetFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteFSContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteFSContHd
   Description: Delete contract and contract related tables
   OperationID: DeleteFSContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteFSContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteFSContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddFsContHd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddFsContHd
   Description: Add customer and customer related tables
   OperationID: AddFsContHd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddFsContHd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddFsContHd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMFSContHdSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AckFSContHd_input:
   """ Required : 
   ts
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.ts:list[Erp_Tablesets_IMFSContHdTableset] = obj["ts"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class AckFSContHd_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class AddFsContHd_input:
   """ Required : 
   IMFSContHdTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   saveAddOnError
   imIntegrationKey
   """  
   def __init__(self, obj):
      self.IMFSContHdTableset:list[Erp_Tablesets_IMFSContHdTableset] = obj["IMFSContHdTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.saveAddOnError:bool = obj["saveAddOnError"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

class AddFsContHd_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

      """  output parameters  """  

class CountFSContHd_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class CountFSContHd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.totalCount:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteFSContHd_input:
   """ Required : 
   IMFSContHdTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   """  
   def __init__(self, obj):
      self.IMFSContHdTableset:list[Erp_Tablesets_IMFSContHdTableset] = obj["IMFSContHdTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      pass

class DeleteFSContHd_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMFSContDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the detail contract line item. These will be printed on the Sales Acknowledgements and service contracts  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSContHdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the Customer number that the Service Contract is for.  This must be valid in the Customer table.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  Same as OrderDate when SLSORD.  TODAY when CNTENT  """  
      self.ContractCode:str = obj["ContractCode"]
      """  A unique code that identifies the Contract  """  
      self.ContractComment:str = obj["ContractComment"]
      """  Contains comments about the overall Contract. These will be printed on the Service Contract.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Indicates which customer ship to is to be used  for the Service Contract. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  """  
      self.ActiveDate:str = obj["ActiveDate"]
      """   The date of the earliest FscontSp.activateDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed. This will always be the earliest activate date on this contract.  """  
      self.ExpireDate:str = obj["ExpireDate"]
      """   The date of the Latest FscontSp.ExpirationDate for this contract.
Not user maintainable.  It is written when the fscontsp record is created or changed.  this will always be the Latest activate date on this contract.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.Modifier:str = obj["Modifier"]
      """  Whether the duration is for Days, Months, years.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Renewable:bool = obj["Renewable"]
      """  Indicates if the service contract using is valid for renewal.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the service contract has to be synchronized with Epicor FSA application.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier of related IntQueIn/IntQueOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      """  Unique identifier of row in actual table  """  
      self.FSAServiceAgreementNum:int = obj["FSAServiceAgreementNum"]
      """  Used to indicate which FSA Service Agreement a Contract Renewal is related to.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSContHdTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMFSContDt:list[Erp_Tablesets_IMFSContDtRow] = obj["IMFSContDt"]
      self.IMFSContHd:list[Erp_Tablesets_IMFSContHdRow] = obj["IMFSContHd"]
      self.IMFSContSN:list[Erp_Tablesets_IMFSContSNRow] = obj["IMFSContSN"]
      self.IMFSRenewal:list[Erp_Tablesets_IMFSRenewalRow] = obj["IMFSRenewal"]
      self.IMFSRenewalDt:list[Erp_Tablesets_IMFSRenewalDtRow] = obj["IMFSRenewalDt"]
      self.IMFSRenewalSN:list[Erp_Tablesets_IMFSRenewalSNRow] = obj["IMFSRenewalSN"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMFSContSNRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the Part that is assigned to this Field Service contract line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key of related IntQueInOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSRenewalDtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.RenewalLine:int = obj["RenewalLine"]
      """  This field along with Company and ContractNum make up the unique key to the table.  """  
      self.ContractLine:int = obj["ContractLine"]
      """  This field along with Company and ContractNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the FSContDtl record for the Contract and the adding 1 to it.  The user can override this number if they wish.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. The Part.Description can be used as a default.  """  
      self.IUM:str = obj["IUM"]
      """  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if its a valid Part.  """  
      self.ContractQty:int = obj["ContractQty"]
      """  Total Contract Quantity for the line item.  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the FSContDt records for a specific customer.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Contains the Order Number that ties this detail record back to an OrderHed record.  """  
      self.Inactive:bool = obj["Inactive"]
      """  A value of Yes indicates the line is not part of the service contract agreement and it will not be included in the contract amounts.  """  
      self.BillStartDate:str = obj["BillStartDate"]
      """  This is the first date the contract line is considered for billing purposes.  """  
      self.BillEndDate:str = obj["BillEndDate"]
      """  This is the last date the contract line is considered for billing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates this line has been invoiced.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key of related IntQueInOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSRenewalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  When creating a new Service Contract the user is prompted for an Contract number. If the field is left blank, the next available Number is assigned by the system. The system generates a number by finding the order # of the last record on file and then a 1 to it.  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.Material:bool = obj["Material"]
      """  Coverage  for material  """  
      self.Labor:bool = obj["Labor"]
      """  Coverage for Labor  """  
      self.Misc:bool = obj["Misc"]
      """  Coverage for Misc charges. This includes the miscellaneous expenses like travel, etc.  """  
      self.OnSite:bool = obj["OnSite"]
      """  This contract covers on site visits  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  The invoice for this Service contract  has been created. The Order line that this contract is linked to has shipped.  """  
      self.Duration:int = obj["Duration"]
      """  Duration of Contract  """  
      self.RenewalComment:str = obj["RenewalComment"]
      """  Used to establish invoice comments about the overall Renewal.  """  
      self.RenewEffDate:str = obj["RenewEffDate"]
      """  Date when the renewal begins.  """  
      self.RenewedUntil:str = obj["RenewedUntil"]
      """  Date the renewal ends.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  It is the same as the contract type but applied to renewals  """  
      self.Modifier:str = obj["Modifier"]
      """  The unit of measure of time that the renewal contract lasts.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key of related IntQueInOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMFSRenewalSNRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Number of the Contract  """  
      self.RenewalNbr:int = obj["RenewalNbr"]
      """  Contract renewal number. If the value is zero then the contract is not for a renewal.  """  
      self.RenewalLine:int = obj["RenewalLine"]
      """  This field along with Company and ContractNum make up the unique key to the table.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part. Not directly maintainable. Mirror image of FSContDt.PartNum. Having this field, allows a SerialNo record to find the contracts that it is related to.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number of the Part that is assigned to this Field Service contract line.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Key of related IntQueInOut record  """  
      self.IntSysRowID:str = obj["IntSysRowID"]
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMIntegrationKeyRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      """  The master file which the integration is related to.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMIntegrationKeyTableset:
   def __init__(self, obj):
      self.IMIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyRow] = obj["IMIntegrationKey"]
      self.IMNaturalKeys:list[Erp_Tablesets_IMNaturalKeysRow] = obj["IMNaturalKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMNaturalKeysRow:
   def __init__(self, obj):
      self.KeyValue:str = obj["KeyValue"]
      self.KeyColumn:str = obj["KeyColumn"]
      self.Sequence:int = obj["Sequence"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllFSContHd_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetAllFSContHd_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMFSContHdTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetFSContHd_input:
   """ Required : 
   company
   extSystemID
   transferMethod
   extCompanyID
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.pageSize:int = obj["pageSize"]
      """  Optional. If this is not zero it will return this number of IntQueInOut records with the related data.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Optional. If this is greater than one it will skip to this page when returning data.  """  
      pass

class GetFSContHd_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IMFSContHdTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

