import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartRevSearchSvc
# Description: PartRev search
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartRevSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartRevSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartRevSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches",headers=creds) as resp:
           return await resp.json()

async def post_PartRevSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartRevSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartRevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartRevSearches_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartRevSearch item
   Description: Calls GetByID to retrieve the PartRevSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartRevSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartRevSearches_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, PartNum, RevisionNum, AltMethod, ProcessMfgID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartRevSearch for the service
   Description: Calls UpdateExt to update PartRevSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartRevSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartRevSearches_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, PartNum, RevisionNum, AltMethod, ProcessMfgID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartRevSearch item
   Description: Call UpdateExt to delete PartRevSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartRevSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/PartRevSearches(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartRev, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartRev=" + whereClausePartRev
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, revisionNum, altMethod, processMfgID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revisionNum=" + revisionNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "altMethod=" + altMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processMfgID=" + processMfgID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_PartRevionsExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartRevionsExists
   Description: Determine id a part revision exists
   OperationID: PartRevionsExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartRevionsExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartRevionsExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindRevsionRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindRevsionRecord
   Description: Find first part revision based on criteria.
   OperationID: FindRevsionRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindRevsionRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindRevsionRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAltMethodByPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAltMethodByPlant
   Description: Get appropriate Part Revision (Alt Method) according to parameters.
If there are several methods with the same date and plant then get primary Atl Method
   OperationID: GetAltMethodByPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAltMethodByPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAltMethodByPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartRevListByConfigID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartRevListByConfigID
   OperationID: GetPartRevListByConfigID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartRevListByConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartRevListByConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFirstPartRevByDateDescending(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFirstPartRevByDateDescending
   OperationID: GetFirstPartRevByDateDescending
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFirstPartRevByDateDescending_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFirstPartRevByDateDescending_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartRev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartRevSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartRevListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartRevRow] = obj["value"]
      pass

class Erp_Tablesets_PartRevListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.ProdCode:str = obj["ProdCode"]
      self.NonStock:bool = obj["NonStock"]
      self.Class:str = obj["Class"]
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      """  The description of the inspection plan  """  
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      """  Describes the Part.  """  
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      """  Full description of the rough cut parameter set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      """  SIValuesGroupSeq  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      """  SIValuesHeadNum  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.DefaultConfigPart:bool = obj["DefaultConfigPart"]
      """  DefaultConfigPart  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  Number of COPart required in the Revision  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  Material Cost Factor  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  Labor Cost Factor  """  
      self.CoPartsPerOp:int = obj["CoPartsPerOp"]
      """  Number of COParts per Operation  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      """  Customs BOM  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: General, Site, Master.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ProcessMfgLastGroupID:str = obj["ProcessMfgLastGroupID"]
      """  The last Group to modify this Revision for Recipe Authoring.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      """  This field will be set to true if two or more ECOCoParts records exist for the revision.  """  
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part Number of the Parent Part  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  Revision number  of Parent Part.  """  
      self.ProdCode:str = obj["ProdCode"]
      self.RevStatusAsOfDate:int = obj["RevStatusAsOfDate"]
      """   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.Class:str = obj["Class"]
      self.NonStock:bool = obj["NonStock"]
      self.IsRootNode:bool = obj["IsRootNode"]
      """  Indicates that the PartRev is the root node in the tree  """  
      self.EngineeringApproved:bool = obj["EngineeringApproved"]
      """  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      self.PartDescriptionTypeCode:str = obj["PartDescriptionTypeCode"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PlantName:str = obj["PlantName"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartRevListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.ProdCode:str = obj["ProdCode"]
      self.NonStock:bool = obj["NonStock"]
      self.Class:str = obj["Class"]
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      """  The description of the inspection plan  """  
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      """  Describes the Part.  """  
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      """  Full description of the rough cut parameter set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevListTableset:
   def __init__(self, obj):
      self.PartRevList:list[Erp_Tablesets_PartRevListRow] = obj["PartRevList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      """  SIValuesGroupSeq  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      """  SIValuesHeadNum  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.DefaultConfigPart:bool = obj["DefaultConfigPart"]
      """  DefaultConfigPart  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  Number of COPart required in the Revision  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  Material Cost Factor  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  Labor Cost Factor  """  
      self.CoPartsPerOp:int = obj["CoPartsPerOp"]
      """  Number of COParts per Operation  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      """  Customs BOM  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: General, Site, Master.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ProcessMfgLastGroupID:str = obj["ProcessMfgLastGroupID"]
      """  The last Group to modify this Revision for Recipe Authoring.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      """  This field will be set to true if two or more ECOCoParts records exist for the revision.  """  
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part Number of the Parent Part  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  Revision number  of Parent Part.  """  
      self.ProdCode:str = obj["ProdCode"]
      self.RevStatusAsOfDate:int = obj["RevStatusAsOfDate"]
      """   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.Class:str = obj["Class"]
      self.NonStock:bool = obj["NonStock"]
      self.IsRootNode:bool = obj["IsRootNode"]
      """  Indicates that the PartRev is the root node in the tree  """  
      self.EngineeringApproved:bool = obj["EngineeringApproved"]
      """  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      self.PartDescriptionTypeCode:str = obj["PartDescriptionTypeCode"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PlantName:str = obj["PlantName"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevSearchTableset:
   def __init__(self, obj):
      self.PartRev:list[Erp_Tablesets_PartRevRow] = obj["PartRev"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartRevSearchTableset:
   def __init__(self, obj):
      self.PartRev:list[Erp_Tablesets_PartRevRow] = obj["PartRev"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindRevsionRecord_input:
   """ Required : 
   partnum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.partnum:str = obj["partnum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class FindRevsionRecord_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartRevSearchTableset] = obj["returnObj"]
      pass

class GetAltMethodByPlant_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipAsOfDate
   ipPlant
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The as of date for the revisions, what would this look as of this date  """  
      self.ipPlant:str = obj["ipPlant"]
      """  The Plant to return data for.  """  
      pass

class GetAltMethodByPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outAltMethod:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartRevSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartRevSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartRevSearchTableset] = obj["returnObj"]
      pass

class GetFirstPartRevByDateDescending_input:
   """ Required : 
   cPartNum
   """  
   def __init__(self, obj):
      self.cPartNum:str = obj["cPartNum"]
      pass

class GetFirstPartRevByDateDescending_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartRevListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PartRevListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartRev_input:
   """ Required : 
   ds
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartRevSearchTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class GetNewPartRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartRevSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartRevListByConfigID_input:
   """ Required : 
   WhereClause
   PartWhereClause
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      self.PartWhereClause:str = obj["PartWhereClause"]
      self.PageSize:int = obj["PageSize"]
      self.AbsolutePage:int = obj["AbsolutePage"]
      pass

class GetPartRevListByConfigID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartRevListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartRev
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartRev:str = obj["whereClausePartRev"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartRevSearchTableset] = obj["returnObj"]
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

class PartRevionsExists_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      pass

class PartRevionsExists_output:
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
      self.ds:list[Erp_Tablesets_UpdExtPartRevSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartRevSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartRevSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartRevSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

