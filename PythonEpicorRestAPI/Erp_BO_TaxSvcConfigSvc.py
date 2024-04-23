import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxSvcConfigSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcConfigs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxSvcConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcConfigs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs",headers=creds) as resp:
           return await resp.json()

async def post_TaxSvcConfigs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcConfigs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxSvcConfigs_Company(Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxSvcConfig item
   Description: Calls GetByID to retrieve the TaxSvcConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcConfig
      :param Company: Desc: Company   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxSvcConfigs_Company(Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxSvcConfig for the service
   Description: Calls UpdateExt to update TaxSvcConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcConfig
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs(" + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxSvcConfigs_Company(Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxSvcConfig item
   Description: Call UpdateExt to delete TaxSvcConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcConfig
      :param Company: Desc: Company   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs(" + Company + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxSvcConfig, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxSvcConfig=" + whereClauseTaxSvcConfig
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxSvcConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxSvcConfig
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcConfigListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxSvcConfigRow] = obj["value"]
      pass

class Erp_Tablesets_TaxSvcConfigListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.URL:str = obj["URL"]
      """  The location of the AvaTax service when the address will not change between the client and web service.  """  
      self.ViaURL:str = obj["ViaURL"]
      """  The intermediary server, for example a firewall, for the AvaTax service.  """  
      self.TextCase:str = obj["TextCase"]
      """  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  """  
      self.Account:str = obj["Account"]
      """  The unique account number provided by Avalara for verification against the service. May also contain a username.  """  
      self.Key:str = obj["Key"]
      """  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  """  
      self.TaxConnectEnabled:bool = obj["TaxConnectEnabled"]
      """  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  """  
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      """   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  """  
      self.TaxCalcEnabled:bool = obj["TaxCalcEnabled"]
      """  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  """  
      self.TaxIdPrefix:str = obj["TaxIdPrefix"]
      """  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  """  
      self.RequestTimeOut:int = obj["RequestTimeOut"]
      """  Request timeout value for tax connect requests, in seconds.  """  
      self.DefaultTaxCatID:str = obj["DefaultTaxCatID"]
      """  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  """  
      self.LastDocId:int = obj["LastDocId"]
      """  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcConfigRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.URL:str = obj["URL"]
      """  The location of the AvaTax service when the address will not change between the client and web service.  """  
      self.ViaURL:str = obj["ViaURL"]
      """  The intermediary server, for example a firewall, for the AvaTax service.  """  
      self.TextCase:str = obj["TextCase"]
      """  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  """  
      self.Account:str = obj["Account"]
      """  The unique account number provided by Avalara for verification against the service. May also contain a username.  """  
      self.Key:str = obj["Key"]
      """  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  """  
      self.TaxConnectEnabled:bool = obj["TaxConnectEnabled"]
      """  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  """  
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      """   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  """  
      self.TaxCalcEnabled:bool = obj["TaxCalcEnabled"]
      """  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  """  
      self.TaxIdPrefix:str = obj["TaxIdPrefix"]
      """  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  """  
      self.RequestTimeOut:int = obj["RequestTimeOut"]
      """  Request timeout value for tax connect requests, in seconds.  """  
      self.DefaultTaxCatID:str = obj["DefaultTaxCatID"]
      """  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  """  
      self.LastDocId:int = obj["LastDocId"]
      """  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ValidateISOCode:bool = obj["ValidateISOCode"]
      """  ValidateISOCode  """  
      self.CertCaptureEnabled:bool = obj["CertCaptureEnabled"]
      """  Indicates whether the system can perform CertCapture transactions. If CertCaptureEnabled is true, CertCapture features will be available. Otherwise, they won't.  """  
      self.APTaxDisplayAccount:str = obj["APTaxDisplayAccount"]
      self.APTaxAcctDesc:str = obj["APTaxAcctDesc"]
      self.ARTaxDisplayAccount:str = obj["ARTaxDisplayAccount"]
      self.ARTaxAcctDesc:str = obj["ARTaxAcctDesc"]
      self.ETCOffline:bool = obj["ETCOffline"]
      """  External field to be used to indicate that the Tax Connect service is off line. This filed can be set by the BL when a communication failure with tax connect occurs, or can be set manually in the UI when the user indicates that tax connect is offline. If set to true then the BL will not attempt any communication with the tax service. This is used to save unnecessary processing delays trying to communicate with the tax service when it is known that the service is unavailable.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCatDescription:str = obj["TaxCatDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxSvcConfigListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.URL:str = obj["URL"]
      """  The location of the AvaTax service when the address will not change between the client and web service.  """  
      self.ViaURL:str = obj["ViaURL"]
      """  The intermediary server, for example a firewall, for the AvaTax service.  """  
      self.TextCase:str = obj["TextCase"]
      """  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  """  
      self.Account:str = obj["Account"]
      """  The unique account number provided by Avalara for verification against the service. May also contain a username.  """  
      self.Key:str = obj["Key"]
      """  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  """  
      self.TaxConnectEnabled:bool = obj["TaxConnectEnabled"]
      """  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  """  
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      """   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  """  
      self.TaxCalcEnabled:bool = obj["TaxCalcEnabled"]
      """  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  """  
      self.TaxIdPrefix:str = obj["TaxIdPrefix"]
      """  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  """  
      self.RequestTimeOut:int = obj["RequestTimeOut"]
      """  Request timeout value for tax connect requests, in seconds.  """  
      self.DefaultTaxCatID:str = obj["DefaultTaxCatID"]
      """  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  """  
      self.LastDocId:int = obj["LastDocId"]
      """  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcConfigListTableset:
   def __init__(self, obj):
      self.TaxSvcConfigList:list[Erp_Tablesets_TaxSvcConfigListRow] = obj["TaxSvcConfigList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxSvcConfigRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.URL:str = obj["URL"]
      """  The location of the AvaTax service when the address will not change between the client and web service.  """  
      self.ViaURL:str = obj["ViaURL"]
      """  The intermediary server, for example a firewall, for the AvaTax service.  """  
      self.TextCase:str = obj["TextCase"]
      """  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  """  
      self.Account:str = obj["Account"]
      """  The unique account number provided by Avalara for verification against the service. May also contain a username.  """  
      self.Key:str = obj["Key"]
      """  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  """  
      self.TaxConnectEnabled:bool = obj["TaxConnectEnabled"]
      """  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  """  
      self.AddrValEnabled:bool = obj["AddrValEnabled"]
      """   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  """  
      self.TaxCalcEnabled:bool = obj["TaxCalcEnabled"]
      """  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  """  
      self.TaxIdPrefix:str = obj["TaxIdPrefix"]
      """  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  """  
      self.RequestTimeOut:int = obj["RequestTimeOut"]
      """  Request timeout value for tax connect requests, in seconds.  """  
      self.DefaultTaxCatID:str = obj["DefaultTaxCatID"]
      """  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  """  
      self.LastDocId:int = obj["LastDocId"]
      """  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  """  
      self.DebugMode:bool = obj["DebugMode"]
      """  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ValidateISOCode:bool = obj["ValidateISOCode"]
      """  ValidateISOCode  """  
      self.CertCaptureEnabled:bool = obj["CertCaptureEnabled"]
      """  Indicates whether the system can perform CertCapture transactions. If CertCaptureEnabled is true, CertCapture features will be available. Otherwise, they won't.  """  
      self.APTaxDisplayAccount:str = obj["APTaxDisplayAccount"]
      self.APTaxAcctDesc:str = obj["APTaxAcctDesc"]
      self.ARTaxDisplayAccount:str = obj["ARTaxDisplayAccount"]
      self.ARTaxAcctDesc:str = obj["ARTaxAcctDesc"]
      self.ETCOffline:bool = obj["ETCOffline"]
      """  External field to be used to indicate that the Tax Connect service is off line. This filed can be set by the BL when a communication failure with tax connect occurs, or can be set manually in the UI when the user indicates that tax connect is offline. If set to true then the BL will not attempt any communication with the tax service. This is used to save unnecessary processing delays trying to communicate with the tax service when it is known that the service is unavailable.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.TaxCatDescription:str = obj["TaxCatDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxSvcConfigTableset:
   def __init__(self, obj):
      self.TaxSvcConfig:list[Erp_Tablesets_TaxSvcConfigRow] = obj["TaxSvcConfig"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTaxSvcConfigTableset:
   def __init__(self, obj):
      self.TaxSvcConfig:list[Erp_Tablesets_TaxSvcConfigRow] = obj["TaxSvcConfig"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxSvcConfigListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxSvcConfig_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["ds"]
      pass

class GetNewTaxSvcConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxSvcConfig
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxSvcConfig:str = obj["whereClauseTaxSvcConfig"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxSvcConfigTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxSvcConfigTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxSvcConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

