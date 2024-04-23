import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BESalesIntracomSvc
# Description: Begium Intracom Sales List BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BESalesIntracoms(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BESalesIntracoms items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BESalesIntracoms
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BESalesIntracomRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/BESalesIntracoms",headers=creds) as resp:
           return await resp.json()

async def post_BESalesIntracoms(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BESalesIntracoms
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BESalesIntracomRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BESalesIntracomRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/BESalesIntracoms", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BESalesIntracoms_Company_ECSalesReportID(Company, ECSalesReportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BESalesIntracom item
   Description: Calls GetByID to retrieve the BESalesIntracom item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BESalesIntracom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BESalesIntracomRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/BESalesIntracoms(" + Company + "," + ECSalesReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BESalesIntracoms_Company_ECSalesReportID(Company, ECSalesReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BESalesIntracom for the service
   Description: Calls UpdateExt to update BESalesIntracom. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BESalesIntracom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BESalesIntracomRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/BESalesIntracoms(" + Company + "," + ECSalesReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BESalesIntracoms_Company_ECSalesReportID(Company, ECSalesReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BESalesIntracom item
   Description: Call UpdateExt to delete BESalesIntracom item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BESalesIntracom
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ECSalesReportID: Desc: ECSalesReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/BESalesIntracoms(" + Company + "," + ECSalesReportID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BESalesIntracomListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBESalesIntracom, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseBESalesIntracom=" + whereClauseBESalesIntracom
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(ecSalesReportID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ecSalesReportID=" + ecSalesReportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDateOfPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDateOfPeriod
   OperationID: GetDateOfPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDateOfPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateOfPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenExportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenExportFile
   Description: Export BE Sales List.
   OperationID: GenExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBESalesIntracom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBESalesIntracom
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBESalesIntracom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBESalesIntracom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBESalesIntracom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BESalesIntracomSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BESalesIntracomListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BESalesIntracomListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BESalesIntracomRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BESalesIntracomRow] = obj["value"]
      pass

class Erp_Tablesets_BESalesIntracomListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InsideEUOnly:bool = obj["InsideEUOnly"]
      """  Sales outside the EU should not be included if any of the tax liabilities has the "Inside EU" flag checked  """  
      self.BEReportType:str = obj["BEReportType"]
      """  Report Type (CSF Belgium)  """  
      self.BERptLanguage:str = obj["BERptLanguage"]
      """  Report Language (CSF Belgium)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BESalesIntracomRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.RoundAmounts:bool = obj["RoundAmounts"]
      """  Round Amounts option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.TaxList:str = obj["TaxList"]
      self.VATTReportList:str = obj["VATTReportList"]
      self.Description:str = obj["Description"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.ManualXML:bool = obj["ManualXML"]
      """  Field to identify manual changes on XML info.  """  
      self.Module:str = obj["Module"]
      """  Report Module parameter, options: AR or AR/AP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InsideEUOnly:bool = obj["InsideEUOnly"]
      """  Sales outside the EU should not be included if any of the tax liabilities has the "Inside EU" flag checked  """  
      self.BEReportType:str = obj["BEReportType"]
      """  Report Type (CSF Belgium)  """  
      self.BERptLanguage:str = obj["BERptLanguage"]
      """  Report Language (CSF Belgium)  """  
      self.BEDspLimitAmount:int = obj["BEDspLimitAmount"]
      """  Display Limit Amount (CSF Belgium)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.EndFiscalPeriod:int = obj["EndFiscalPeriod"]
      """  End Fiscal Period  """  
      self.StartFiscalPeriod:int = obj["StartFiscalPeriod"]
      """  Start Fiscal Period  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   ecSalesReportID
   """  
   def __init__(self, obj):
      self.ecSalesReportID:str = obj["ecSalesReportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BESalesIntracomListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.Description:str = obj["Description"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InsideEUOnly:bool = obj["InsideEUOnly"]
      """  Sales outside the EU should not be included if any of the tax liabilities has the "Inside EU" flag checked  """  
      self.BEReportType:str = obj["BEReportType"]
      """  Report Type (CSF Belgium)  """  
      self.BERptLanguage:str = obj["BERptLanguage"]
      """  Report Language (CSF Belgium)  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BESalesIntracomListTableset:
   def __init__(self, obj):
      self.BESalesIntracomList:list[Erp_Tablesets_BESalesIntracomListRow] = obj["BESalesIntracomList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BESalesIntracomRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ECSalesReportID:str = obj["ECSalesReportID"]
      """  European Sales List ID  """  
      self.EndDate:str = obj["EndDate"]
      """  Report End Date  """  
      self.RangeOption:str = obj["RangeOption"]
      """  Range Option  """  
      self.RoundAmounts:bool = obj["RoundAmounts"]
      """  Round Amounts option  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date Report  """  
      self.TaxList:str = obj["TaxList"]
      self.VATTReportList:str = obj["VATTReportList"]
      self.Description:str = obj["Description"]
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Unique identifier of the EFT. Related to EFTHead.EFTHeadUID.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  This will be the default filename for the output file created by the electronic interface  """  
      self.ManualXML:bool = obj["ManualXML"]
      """  Field to identify manual changes on XML info.  """  
      self.Module:str = obj["Module"]
      """  Report Module parameter, options: AR or AR/AP  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InsideEUOnly:bool = obj["InsideEUOnly"]
      """  Sales outside the EU should not be included if any of the tax liabilities has the "Inside EU" flag checked  """  
      self.BEReportType:str = obj["BEReportType"]
      """  Report Type (CSF Belgium)  """  
      self.BERptLanguage:str = obj["BERptLanguage"]
      """  Report Language (CSF Belgium)  """  
      self.BEDspLimitAmount:int = obj["BEDspLimitAmount"]
      """  Display Limit Amount (CSF Belgium)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.EndFiscalPeriod:int = obj["EndFiscalPeriod"]
      """  End Fiscal Period  """  
      self.StartFiscalPeriod:int = obj["StartFiscalPeriod"]
      """  Start Fiscal Period  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BESalesIntracomTableset:
   def __init__(self, obj):
      self.BESalesIntracom:list[Erp_Tablesets_BESalesIntracomRow] = obj["BESalesIntracom"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtBESalesIntracomTableset:
   def __init__(self, obj):
      self.BESalesIntracom:list[Erp_Tablesets_BESalesIntracomRow] = obj["BESalesIntracom"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenExportFile_input:
   """ Required : 
   ipSalesReportID
   ipFileFile
   """  
   def __init__(self, obj):
      self.ipSalesReportID:str = obj["ipSalesReportID"]
      """  BE Sales Report ID  """  
      self.ipFileFile:str = obj["ipFileFile"]
      """  File Name  """  
      pass

class GenExportFile_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   ecSalesReportID
   """  
   def __init__(self, obj):
      self.ecSalesReportID:str = obj["ecSalesReportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BESalesIntracomTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BESalesIntracomTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BESalesIntracomTableset] = obj["returnObj"]
      pass

class GetDateOfPeriod_input:
   """ Required : 
   ipYear
   ipYearSuffix
   ipPeriod
   ipStartOrEnd
   """  
   def __init__(self, obj):
      self.ipYear:int = obj["ipYear"]
      self.ipYearSuffix:str = obj["ipYearSuffix"]
      self.ipPeriod:int = obj["ipPeriod"]
      self.ipStartOrEnd:str = obj["ipStartOrEnd"]
      pass

class GetDateOfPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opDate:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_BESalesIntracomListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBESalesIntracom_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BESalesIntracomTableset] = obj["ds"]
      pass

class GetNewBESalesIntracom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BESalesIntracomTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBESalesIntracom
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBESalesIntracom:str = obj["whereClauseBESalesIntracom"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BESalesIntracomTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtBESalesIntracomTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBESalesIntracomTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BESalesIntracomTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BESalesIntracomTableset] = obj["ds"]
      pass

      """  output parameters  """  

