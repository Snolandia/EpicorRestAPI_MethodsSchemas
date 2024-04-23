import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AssetClosePeriodSvc
# Description: This updates the FiscalPer table if used in Asset Register to close
fiscal periods used in asset activities.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AssetClosePeriods(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AssetClosePeriods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetClosePeriods
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods",headers=creds) as resp:
           return await resp.json()

async def post_AssetClosePeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetClosePeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AssetClosePeriods_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AssetClosePeriod item
   Description: Calls GetByID to retrieve the AssetClosePeriod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetClosePeriod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AssetClosePeriods_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AssetClosePeriod for the service
   Description: Calls UpdateExt to update AssetClosePeriod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetClosePeriod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FiscalPerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AssetClosePeriods_Company_FiscalCalendarID_FiscalYear_FiscalYearSuffix_FiscalPeriod(Company, FiscalCalendarID, FiscalYear, FiscalYearSuffix, FiscalPeriod, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AssetClosePeriod item
   Description: Call UpdateExt to delete AssetClosePeriod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetClosePeriod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalCalendarID: Desc: FiscalCalendarID   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/AssetClosePeriods(" + Company + "," + FiscalCalendarID + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FiscalPerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFiscalPer, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFiscalPer=" + whereClauseFiscalPer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(fiscalCalendarID, fiscalYear, fiscalYearSuffix, fiscalPeriod, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
   Required: True
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
   params += "fiscalCalendarID=" + fiscalCalendarID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYear=" + fiscalYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYearSuffix=" + fiscalYearSuffix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalPeriod=" + fiscalPeriod

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckYearEndStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckYearEndStatus
   Description: Returns a logical value to indicate if the Year End Process should be enabled.
   OperationID: CheckYearEndStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckYearEndStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckYearEndStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFAClosedPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFAClosedPeriod
   Description: Run when the FiscalPer.FAClosedPeriod field changes.
   OperationID: OnChangeFAClosedPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFAClosedPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFAClosedPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFiscalYear
   Description: Verifies if given Fiscal Year exists
   OperationID: OnChangeFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFiscalYearSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFiscalYearSuffix
   Description: Verifies if given Fiscal Year Suffix exists
   OperationID: OnChangeFiscalYearSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFiscalPer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFiscalPer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFiscalPer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFiscalPer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFiscalPer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetClosePeriodSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FiscalPerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FiscalPerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FiscalPerRow] = obj["value"]
      pass

class Erp_Tablesets_FiscalPerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.FAClosedPeriod:bool = obj["FAClosedPeriod"]
      """  Indicates if the Fixed Asset period is open or closed.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.DepHoliday:bool = obj["DepHoliday"]
      """  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JPYear:int = obj["JPYear"]
      """  JPYear  """  
      self.EnableEndDate:bool = obj["EnableEndDate"]
      """  Indicates if EndDate can be modified by the user.  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate can be changed by the user.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.FiscalYrDescription:str = obj["FiscalYrDescription"]
      """  Fiscal year description.  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.NoOfDays:str = obj["NoOfDays"]
      """  Number of days (EndDate - StartDate)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalPerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.FAClosedPeriod:bool = obj["FAClosedPeriod"]
      """  Indicates if the Fixed Asset period is open or closed.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.DepHoliday:bool = obj["DepHoliday"]
      """  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JPYear:int = obj["JPYear"]
      """  JPYear  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate can be changed by the user.  """  
      self.EnableEndDate:bool = obj["EnableEndDate"]
      """  Indicates if EndDate can be modified by the user.  """  
      self.NoOfDays:str = obj["NoOfDays"]
      """  Number of days (EndDate - StartDate)  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.AssetRegCurrYear:int = obj["AssetRegCurrYear"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrYearSuffix:str = obj["AssetRegCurrYearSuffix"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrPeriod:int = obj["AssetRegCurrPeriod"]
      """  Used in Close Asset Period / Year process  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckYearEndStatus_input:
   """ Required : 
   ipCalendarID
   ipYear
   ipYearSuffix
   """  
   def __init__(self, obj):
      self.ipCalendarID:str = obj["ipCalendarID"]
      """  The input fiscal calendar ID  """  
      self.ipYear:int = obj["ipYear"]
      """  The input fiscal year  """  
      self.ipYearSuffix:str = obj["ipYearSuffix"]
      """  The input fiscal year suffix  """  
      pass

class CheckYearEndStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opAllowed:bool = obj["opAllowed"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AssetClosePeriodTableset:
   def __init__(self, obj):
      self.FiscalPer:list[Erp_Tablesets_FiscalPerRow] = obj["FiscalPer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FiscalPerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.FAClosedPeriod:bool = obj["FAClosedPeriod"]
      """  Indicates if the Fixed Asset period is open or closed.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.DepHoliday:bool = obj["DepHoliday"]
      """  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JPYear:int = obj["JPYear"]
      """  JPYear  """  
      self.EnableEndDate:bool = obj["EnableEndDate"]
      """  Indicates if EndDate can be modified by the user.  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate can be changed by the user.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      """  Calendar description.  """  
      self.FiscalYrDescription:str = obj["FiscalYrDescription"]
      """  Fiscal year description.  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.NoOfDays:str = obj["NoOfDays"]
      """  Number of days (EndDate - StartDate)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FiscalPerListTableset:
   def __init__(self, obj):
      self.FiscalPerList:list[Erp_Tablesets_FiscalPerListRow] = obj["FiscalPerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FiscalPerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The id of the fiscal calendar this record is related to.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  The fiscal year suffix.  Allows for additional breakdown/definition of fiscal years, for example, by quarters.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period number in the fiscal year.  """  
      self.StartDate:str = obj["StartDate"]
      """  The start date of the fiscal period.  """  
      self.EndDate:str = obj["EndDate"]
      """  End date of the fiscal period  """  
      self.FAClosedPeriod:bool = obj["FAClosedPeriod"]
      """  Indicates if the Fixed Asset period is open or closed.  """  
      self.AdditionalDeductions:int = obj["AdditionalDeductions"]
      """  Additional Deductions to be claimed. User should calculate this value manually  """  
      self.LossesCredit:int = obj["LossesCredit"]
      """  Income Tax losses to be claimed. User should calculate this value manually  """  
      self.InvestmentCredit:int = obj["InvestmentCredit"]
      """  Investments Credit to be claimed. User should calculate this value manually  """  
      self.InventoriesCredit:int = obj["InventoriesCredit"]
      """  Inventories Credit to be claimed. User should calculate this value manually.  """  
      self.UpdateRate:int = obj["UpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.DepHoliday:bool = obj["DepHoliday"]
      """  Flag to indicate if the fiscal period is a holiday period.  This flag will be used in the asset depreciation calculation process to skip calculation of preiod depreciation charge if it's a holiday.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JPYear:int = obj["JPYear"]
      """  JPYear  """  
      self.EnableStartDate:bool = obj["EnableStartDate"]
      """  Indicates if StartDate can be changed by the user.  """  
      self.EnableEndDate:bool = obj["EnableEndDate"]
      """  Indicates if EndDate can be modified by the user.  """  
      self.NoOfDays:str = obj["NoOfDays"]
      """  Number of days (EndDate - StartDate)  """  
      self.ITUpdateRate:int = obj["ITUpdateRate"]
      """  This is the rate used to calculate the actual value for Additional Deductions; Losses, Investment and Inventories Credit. User should calculate this value manually.  """  
      self.AssetRegCurrYear:int = obj["AssetRegCurrYear"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrYearSuffix:str = obj["AssetRegCurrYearSuffix"]
      """  Used in Close Asset Period / Year process  """  
      self.AssetRegCurrPeriod:int = obj["AssetRegCurrPeriod"]
      """  Used in Close Asset Period / Year process  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAssetClosePeriodTableset:
   def __init__(self, obj):
      self.FiscalPer:list[Erp_Tablesets_FiscalPerRow] = obj["FiscalPer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FiscalPerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFiscalPer_input:
   """ Required : 
   ds
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["ds"]
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetNewFiscalPer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFiscalPer
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFiscalPer:str = obj["whereClauseFiscalPer"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["returnObj"]
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

class OnChangeFAClosedPeriod_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:bool = obj["ipProposedValue"]
      """  Value that the user has entered  """  
      self.ds:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["ds"]
      pass

class OnChangeFAClosedPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFiscalYearSuffix_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class OnChangeFiscalYearSuffix_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnChangeFiscalYear_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      self.fiscalYear:int = obj["fiscalYear"]
      pass

class OnChangeFiscalYear_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetClosePeriodTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetClosePeriodTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetClosePeriodTableset] = obj["ds"]
      pass

      """  output parameters  """  

