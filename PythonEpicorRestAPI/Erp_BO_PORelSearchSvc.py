import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PORelSearchSvc
# Description: PO Release Search
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PORelSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PORelSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PORelSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches",headers=creds) as resp:
           return await resp.json()

async def post_PORelSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PORelSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PORelRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PORelSearches_Company_PONum_POLine_PORelNum(Company, PONum, POLine, PORelNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PORelSearch item
   Description: Calls GetByID to retrieve the PORelSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PORelSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PORelRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PORelSearches_Company_PONum_POLine_PORelNum(Company, PONum, POLine, PORelNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PORelSearch for the service
   Description: Calls UpdateExt to update PORelSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PORelSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PORelRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PORelSearches_Company_PONum_POLine_PORelNum(Company, PONum, POLine, PORelNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PORelSearch item
   Description: Call UpdateExt to delete PORelSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PORelSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param POLine: Desc: POLine   Required: True
      :param PORelNum: Desc: PORelNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/PORelSearches(" + Company + "," + PONum + "," + POLine + "," + PORelNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PORelListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePORel, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePORel=" + whereClausePORel
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(poNum, poLine, poRelNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
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
   params += "poNum=" + poNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "poLine=" + poLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "poRelNum=" + poRelNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListWithPOLinePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListWithPOLinePartNum
   Description: This method receives whereClause in format "POLinePartNum >= 'VALUE' order by POLinePartNum" which is generated in Kinetic search engine.
Then modify this where to use in ContainerPORelSearch
   OperationID: GetListWithPOLinePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListWithPOLinePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListWithPOLinePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForContainer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForContainer
   Description: Get List of PO Releases available for Container.
   OperationID: GetListForContainer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForContainer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForContainer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ContainerPORelSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ContainerPORelSearch
   Description: Purpose:
Parameters:
<param name="WhereClausePoRel">PO Release search clause</param><returns>PO Rel List Data Set</returns><param name="pageSize">Page size</param><param name="absolutePage">Absolute page</param><param name="morePages">More Pages</param>
Notes:
   OperationID: ContainerPORelSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ContainerPORelSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ContainerPORelSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCloseReleaseAt(epicorHeaders = None):
   """  
   Summary: Invoke method GetCloseReleaseAt
   Description: This method returns the 'Close Release At' company setting
   OperationID: GetCloseReleaseAt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCloseReleaseAt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRowsExcludeGlobal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsExcludeGlobal
   Description: Filter Releases from other Companies. Call normal GetRows method.
   OperationID: GetRowsExcludeGlobal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsExcludeGlobal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsExcludeGlobal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPORel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPORel
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPORel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPORel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPORel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PORelSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PORelListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PORelRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PORelRow] = obj["value"]
      pass

class Erp_Tablesets_PORelListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  """  
      self.ExpOverride:bool = obj["ExpOverride"]
      """  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this PORel record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this PORel record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web", "client", or "rejected"  """  
      self.ReqChgDate:str = obj["ReqChgDate"]
      """   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  """  
      self.ReqChgQty:int = obj["ReqChgQty"]
      """   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  """  
      self.LockRel:str = obj["LockRel"]
      """  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Line created for this PO Release for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPlant:str = obj["GlbPlant"]
      """  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbWarehouse:str = obj["GlbWarehouse"]
      """  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbCreateJobMtl:bool = obj["GlbCreateJobMtl"]
      """  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  """  
      self.ShippedDate:str = obj["ShippedDate"]
      """  Shipped Date  """  
      self.ContainerID:int = obj["ContainerID"]
      """  ID field to the ContainerHeader table.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.PreviousDueDate:str = obj["PreviousDueDate"]
      """  This field holds the previous value of Due Date.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderRelNum:int = obj["BTOOrderRelNum"]
      """  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order POs.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  """  
      self.SMIRcvdQty:int = obj["SMIRcvdQty"]
      """  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Release flag  """  
      self.Mapping:bool = obj["Mapping"]
      """  Mapping  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  """  
      self.WBSPhaseID:str = obj["WBSPhaseID"]
      """  Project Phase ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LockQty:bool = obj["LockQty"]
      """  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  """  
      self.LockDate:bool = obj["LockDate"]
      """  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  """  
      self.ExpDesc:str = obj["ExpDesc"]
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.IUM:str = obj["IUM"]
      self.Inspection:bool = obj["Inspection"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.PUM:str = obj["PUM"]
      """  Replicate PUM on detail  """  
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.UseGlbFields:bool = obj["UseGlbFields"]
      """  Indicates if Glb fields should be used in place of the non-global equivalent  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.GlbPlantName:str = obj["GlbPlantName"]
      self.GlbWhseName:str = obj["GlbWhseName"]
      self.Lock:bool = obj["Lock"]
      """  This field will be used in the UI to Lock and unLock a release.  """  
      self.VendorID:str = obj["VendorID"]
      """  Related Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Related Vendor Name  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.PurPoint:str = obj["PurPoint"]
      """  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.EnableGLAcct:bool = obj["EnableGLAcct"]
      """  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  """  
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical indicating if the container has been shipped.  """  
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Release related to a Contract Purchase Order?  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.POType:str = obj["POType"]
      """  Identifies the type of PO  """  
      self.MangCustID:str = obj["MangCustID"]
      """  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  """  
      self.MangCustName:str = obj["MangCustName"]
      """  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.PONumShipName:str = obj["PONumShipName"]
      """  defaults from the company file.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      """  defaults from the company file.  """  
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      """  Ship to contact name.  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.SoldToNumName:str = obj["SoldToNumName"]
      """  The full name of the customer.  """  
      self.SoldToNumBTName:str = obj["SoldToNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.SoldToNumCustID:str = obj["SoldToNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  """  
      self.ExpOverride:bool = obj["ExpOverride"]
      """  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this PORel record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this PORel record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web", "client", or "rejected"  """  
      self.ReqChgDate:str = obj["ReqChgDate"]
      """   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  """  
      self.ReqChgQty:int = obj["ReqChgQty"]
      """   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  """  
      self.LockRel:str = obj["LockRel"]
      """  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Line created for this PO Release for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPlant:str = obj["GlbPlant"]
      """  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbWarehouse:str = obj["GlbWarehouse"]
      """  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbCreateJobMtl:bool = obj["GlbCreateJobMtl"]
      """  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  """  
      self.ShippedDate:str = obj["ShippedDate"]
      """  Shipped Date  """  
      self.ContainerID:int = obj["ContainerID"]
      """  ID field to the ContainerHeader table.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.PreviousDueDate:str = obj["PreviousDueDate"]
      """  This field holds the previous value of Due Date.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderRelNum:int = obj["BTOOrderRelNum"]
      """  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order POs.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  """  
      self.SMIRcvdQty:int = obj["SMIRcvdQty"]
      """  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Release flag  """  
      self.Mapping:bool = obj["Mapping"]
      """  Mapping  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  """  
      self.WBSPhaseID:str = obj["WBSPhaseID"]
      """  Project Phase ID  """  
      self.IsMultiRel:bool = obj["IsMultiRel"]
      """  IsMultiRel  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SMIRemQty:int = obj["SMIRemQty"]
      """  Field to track the SMIRcvdQty that has not yet been moved to stock  """  
      self.LockQty:bool = obj["LockQty"]
      """  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  """  
      self.LockDate:bool = obj["LockDate"]
      """  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  """  
      self.DueDateChanged:bool = obj["DueDateChanged"]
      """  Indicates Due Date has been changed.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.Status:str = obj["Status"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  """  
      self.InvoicedQty:int = obj["InvoicedQty"]
      """  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  """  
      self.LockNeedByDate:bool = obj["LockNeedByDate"]
      """  Set to 'true' if 'NeedByDate' was derived from a valid demand.  """  
      self.InspectionQty:int = obj["InspectionQty"]
      """  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.DeliverTo:str = obj["DeliverTo"]
      """  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.ReqChgPromiseDate:str = obj["ReqChgPromiseDate"]
      """  When the Promise Date is changed, this is the previous PromiseDt  """  
      self.OTSEMailAddress:str = obj["OTSEMailAddress"]
      """  One Time ShipTo email address.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  Indicates if this release is  "FIRM".  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.EDIShipReferenceType:str = obj["EDIShipReferenceType"]
      """  Name of the ship reference that is going to be stored.  """  
      self.EDIShipReferenceData:str = obj["EDIShipReferenceData"]
      """  Data that is going to be stored as ship reference.  """  
      self.EDIEstimatedDockDate:str = obj["EDIEstimatedDockDate"]
      """  Estimated time when the shipment will arrive.  """  
      self.EDIShipQty:int = obj["EDIShipQty"]
      """  Quantity sent by the supplier.  """  
      self.EDIShipQtyUOM:str = obj["EDIShipQtyUOM"]
      """  Unit of Measure of the EDIShipQty.  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Release related to a Contract Purchase Order?  """  
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.EnableBTOOrderNum:bool = obj["EnableBTOOrderNum"]
      """  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  """  
      self.EnableGLAcct:bool = obj["EnableGLAcct"]
      """  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.ExpDesc:str = obj["ExpDesc"]
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.GlbPlantName:str = obj["GlbPlantName"]
      self.GlbWhseName:str = obj["GlbWhseName"]
      self.Inspection:bool = obj["Inspection"]
      self.IUM:str = obj["IUM"]
      self.Lock:bool = obj["Lock"]
      """  This field will be used in the UI to Lock and unLock a release.  """  
      self.MangCustID:str = obj["MangCustID"]
      """  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  """  
      self.MangCustName:str = obj["MangCustName"]
      """  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.POType:str = obj["POType"]
      """  Identifies the type of PO  """  
      self.PUM:str = obj["PUM"]
      """  Replicate PUM on detail  """  
      self.PurPoint:str = obj["PurPoint"]
      """  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.StatusDescription:str = obj["StatusDescription"]
      """  Description text of the Status field  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  """  
      self.UseGlbFields:bool = obj["UseGlbFields"]
      """  Indicates if Glb fields should be used in place of the non-global equivalent  """  
      self.VendorID:str = obj["VendorID"]
      """  Related Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Related Vendor Name  """  
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical indicating if the container has been shipped.  """  
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      """  The formatted ship to address  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.JobMtlSeq:int = obj["JobMtlSeq"]
      self.JobOprSeq:int = obj["JobOprSeq"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.ContainerHeaderPromiseDate:str = obj["ContainerHeaderPromiseDate"]
      self.ContainerHeaderDueDate:str = obj["ContainerHeaderDueDate"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PlantName:str = obj["PlantName"]
      self.POLineRevisionNum:str = obj["POLineRevisionNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.SoldToNumCustID:str = obj["SoldToNumCustID"]
      self.SoldToNumBTName:str = obj["SoldToNumBTName"]
      self.SoldToNumName:str = obj["SoldToNumName"]
      self.SoldToNumInactive:bool = obj["SoldToNumInactive"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WBSPhaseDescription:str = obj["WBSPhaseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ContainerPORelSearch_input:
   """ Required : 
   WhereClausePoRel
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.WhereClausePoRel:str = obj["WhereClausePoRel"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class ContainerPORelSearch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PORelListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PORelListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  """  
      self.ExpOverride:bool = obj["ExpOverride"]
      """  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this PORel record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this PORel record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web", "client", or "rejected"  """  
      self.ReqChgDate:str = obj["ReqChgDate"]
      """   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  """  
      self.ReqChgQty:int = obj["ReqChgQty"]
      """   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  """  
      self.LockRel:str = obj["LockRel"]
      """  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Line created for this PO Release for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPlant:str = obj["GlbPlant"]
      """  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbWarehouse:str = obj["GlbWarehouse"]
      """  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbCreateJobMtl:bool = obj["GlbCreateJobMtl"]
      """  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  """  
      self.ShippedDate:str = obj["ShippedDate"]
      """  Shipped Date  """  
      self.ContainerID:int = obj["ContainerID"]
      """  ID field to the ContainerHeader table.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.PreviousDueDate:str = obj["PreviousDueDate"]
      """  This field holds the previous value of Due Date.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderRelNum:int = obj["BTOOrderRelNum"]
      """  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order POs.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  """  
      self.SMIRcvdQty:int = obj["SMIRcvdQty"]
      """  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Release flag  """  
      self.Mapping:bool = obj["Mapping"]
      """  Mapping  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  """  
      self.WBSPhaseID:str = obj["WBSPhaseID"]
      """  Project Phase ID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LockQty:bool = obj["LockQty"]
      """  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  """  
      self.LockDate:bool = obj["LockDate"]
      """  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  """  
      self.ExpDesc:str = obj["ExpDesc"]
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.IUM:str = obj["IUM"]
      self.Inspection:bool = obj["Inspection"]
      self.DelPoSug:bool = obj["DelPoSug"]
      self.PUM:str = obj["PUM"]
      """  Replicate PUM on detail  """  
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.UseGlbFields:bool = obj["UseGlbFields"]
      """  Indicates if Glb fields should be used in place of the non-global equivalent  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.GlbPlantName:str = obj["GlbPlantName"]
      self.GlbWhseName:str = obj["GlbWhseName"]
      self.Lock:bool = obj["Lock"]
      """  This field will be used in the UI to Lock and unLock a release.  """  
      self.VendorID:str = obj["VendorID"]
      """  Related Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Related Vendor Name  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.PurPoint:str = obj["PurPoint"]
      """  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.EnableGLAcct:bool = obj["EnableGLAcct"]
      """  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  """  
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical indicating if the container has been shipped.  """  
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Release related to a Contract Purchase Order?  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.POType:str = obj["POType"]
      """  Identifies the type of PO  """  
      self.MangCustID:str = obj["MangCustID"]
      """  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  """  
      self.MangCustName:str = obj["MangCustName"]
      """  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      """  Ship to contact name. Prints on Purchase order form. Defaults from the CustCnt or VendCnt.  """  
      self.PONumShipName:str = obj["PONumShipName"]
      """  defaults from the company file.  """  
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      """  Full description of Project Management Code.  """  
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records. If no job reference then uses the Part.PartDescription if its a valid PartNum.  """  
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      """  defaults from the company file.  """  
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      """  Ship to contact name.  """  
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      """  The full name of the customer.  """  
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.SoldToNumName:str = obj["SoldToNumName"]
      """  The full name of the customer.  """  
      self.SoldToNumBTName:str = obj["SoldToNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.SoldToNumCustID:str = obj["SoldToNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelListTableset:
   def __init__(self, obj):
      self.PORelList:list[Erp_Tablesets_PORelListRow] = obj["PORelList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PORelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  Indicates if this release is open.  This is normally closed via the receiving program. But can be changed indirectly  by the user during order entry when they "Void" the release..  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.
When an PORel record is 'voided',  PORel.OpenRelease is set to "no".  If no other open PORel records exist for the related PODetail then the PoDetail.OpenLine is set to "No". If no other open PoDetail records exist then set the PoHeader.OperOrder = No.
This can also be set when the related PoDetail or PoHeader is voided.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.DueDate:str = obj["DueDate"]
      """  Specifies the date by which you need to receive a release of a part. This date is taken from the Purchase Order Line Due Date, if it’s null, PORel.DueDate will take the value from POHeader.DueDate. If you're adding releases from: - BTO or Drop Shipments, PORel.DueDate will take the value from OrderRel.NeedByDate  - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.XRelQty:int = obj["XRelQty"]
      """  Order quantity for this release in our unit of measure.  """  
      self.PurchasingFactor:int = obj["PurchasingFactor"]
      """   This value is used to convert quantity when there is a difference in the vendors unit of measure and how it is stocked in inventory or used in manufacturing. Example is purchased in pounds, stocked in sheets. When this field is not zero Purchase Order Entry calculates the Vendor order qty (RelQty) whenever the Order Qty in our U/M (XRelQty) is changed or Vice-Versa.
Formula: XRelQty * Factor = RelQty  """  
      self.RelQty:int = obj["RelQty"]
      """  Order quantity for this release in vendors unit of measure.  """  
      self.JobNum:str = obj["JobNum"]
      """  This is populated for Purchase Direct items only and contains the job number for the purchased direct item.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This is populated for Purchase Direct items only and contains the assembly number for the purchased direct item.  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Qualifies the JobSeq field as to be a "M" - Material (JobMtl) record or "S" - Subcontract (JobOper) reference.
FYI: This field can indirectly sets the TranType field via the write trigger. It can itself be set from the TranType. System keeps them compatible. JobSeqType/TranType values are; M = PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN. This possibly could have been deleted. However we decided to keep it for backward compatablity reasons.  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse that the item on this release is being purchased for.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Total quantity received to stock to date. In Purchasing unit of measure. This is a field maintained by the receipt process.  """  
      self.ExpOverride:bool = obj["ExpOverride"]
      """  Indicates if the user overrode the default  expense accounts for this release. This field prevents the program from resetting the account #'s when the user changes other fields that trigger new default accounts to be set. If "Yes" then the defaults will not be used.  """  
      self.ReqNum:int = obj["ReqNum"]
      """  Requisition which generated this PORel record.  """  
      self.ReqLine:int = obj["ReqLine"]
      """  Requisition line which generated this PORel record.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.PromiseDt:str = obj["PromiseDt"]
      """  Specifies the date on which the supplier has promised to ship this release.This date is taken from POHeader.PromiseDate. If you're adding releases from: - BTO or Drop Shipments, PORel.PromiseDt will take the value from OrderRel.NeedByDate. - Job Material , PORel.DueDate will take the value from JobMtl.ReqDate. - Subcontract Operations, PORel.DueDate wil take the value from JobOper.DueDate  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Confirmed:bool = obj["Confirmed"]
      """  Indicated Supplier Confirmed the PO.  Will default from the PO header.  Also used when the supplier or  """  
      self.ConfirmVia:str = obj["ConfirmVia"]
      """  Can be "web", "client", or "rejected"  """  
      self.ReqChgDate:str = obj["ReqChgDate"]
      """   When the Due Date is changed, this is the previous DueDate.
(originally was "Requested pending date change")  """  
      self.ReqChgQty:int = obj["ReqChgQty"]
      """   When the RelQty is changed, this is the previous RelQty.
(was "Requested change quantity")  """  
      self.LockRel:str = obj["LockRel"]
      """  OBSOLETE FIELD-A PO release with a locked status will not generate a change suggestion.  SEV, 11/21/02: New convention to indicate who is blocking new suggestions: the presence of "B" indicates the Buyer, and "V" indicates the Vendor.  "BV" means both Buyer and Vendor want no changes in Date or Qty on this release.  """  
      self.RefDisplayAccount:str = obj["RefDisplayAccount"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!, REPLACED BY ADDING INDIVIDUAL COMPONENT FIELDS) A character string made up of Division, GLDept and Chart fields concatenated using the user defined configuration options found in XaSyst file.  This should be formatted exactly how the user expects to see their account numbers (including separators).  This field is generated via the maintenance program.  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType. Not displayed.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.RefCodeDesc:str = obj["RefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number created for this PO for the Inter-Company Trading.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line created for this PO Line for the Inter-Company Trading.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Line created for this PO Release for the Inter-Company Trading.  """  
      self.Linked:bool = obj["Linked"]
      """  Linked to sales order release.  """  
      self.ExtCompany:str = obj["ExtCompany"]
      """  External Trading Company Identifier.  """  
      self.ShippedQty:int = obj["ShippedQty"]
      """  Total quantity shipped but not received (In-Transit).  In Purchasing unit of measure.  This is a summary maintained by the receipt process.  This number is 0 every time the company receives every thing the other company ships.  """  
      self.TranType:str = obj["TranType"]
      """   Indicates what the item is being purchased for.  Items can be purchased for Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"),  Stock ("PUR-STK") or Other ("PUR-UKN").
FYI: This field indirectly sets the JobSeqType field via the write trigger. It can itself be set from the JobSeqType. System keeps them compatible. JobSeqType/TranType values are; M =PUR-MTL,  S = PUR-SUB, " " = PUR-STK or PUR-UKN.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPlant:str = obj["GlbPlant"]
      """  Global Site identifier.  Relates to the External Site record that is created to correlate the Consolidated Purchasing company to a Site in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbWarehouse:str = obj["GlbWarehouse"]
      """  Global Warehouse identifier.  Relates to the External Warehouse record that is created to correlate the Consolidated Purchasing company to a Warehouse in a local Company.  Used in Consolidated Purchasing.  """  
      self.GlbCreateJobMtl:bool = obj["GlbCreateJobMtl"]
      """  When this PORel is received in the local company, if this flag is set create JobMtl.  Used in Consolidated Purchasing.  """  
      self.ShippedDate:str = obj["ShippedDate"]
      """  Shipped Date  """  
      self.ContainerID:int = obj["ContainerID"]
      """  ID field to the ContainerHeader table.  """  
      self.PurchasingFactorDirection:str = obj["PurchasingFactorDirection"]
      """  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  """  
      self.PreviousDueDate:str = obj["PreviousDueDate"]
      """  This field holds the previous value of Due Date.  """  
      self.BaseQty:int = obj["BaseQty"]
      """  Quantity in the Parts Base UOM.  Set by the system by doing a UOM conversion of the PORel.XRelQty to the PORel.BaseUOM .  """  
      self.BaseUOM:str = obj["BaseUOM"]
      """   Unit of Measure of the PORel.BaseRequiredQty.
If valid part, then it is the Parts Primary Inventory UOM otherwise it is the same as PODetail.IUM  """  
      self.BTOOrderNum:int = obj["BTOOrderNum"]
      """  Order Num related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderLine:int = obj["BTOOrderLine"]
      """  The line number of the sales order related to this purchase order. Used only for Buy To Order POs.  """  
      self.BTOOrderRelNum:int = obj["BTOOrderRelNum"]
      """  The release number of the sales order line related to this purchase order. Used only for Buy To Order POs.  """  
      self.DropShip:bool = obj["DropShip"]
      """  The value of this field comes from the sales order release. Used only for Buy To Order POs.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The ShipTo Num from the sales order release. Used only for Buy To Order POs.  """  
      self.SoldToNum:int = obj["SoldToNum"]
      """  The SoldTo ID from the sales order release. Used only for Buy To Order POs.  """  
      self.SMIRcvdQty:int = obj["SMIRcvdQty"]
      """  This is only updated for SMI type POs.  It will indicate how many items have been received into a SMI bin.  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  Contains the key value for the shipping contact.  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  """  
      self.MangCustNum:int = obj["MangCustNum"]
      """  This is the customer number associated with the managed customer defined in the whsebin for CMI type PO transactions.  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  Indicates that the One Time ShipTO information defined for this release should be used. OTS fields are only used for Drop Shipments.  """  
      self.OTSName:str = obj["OTSName"]
      """  One Time Shipto Name of the ShipTo.  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  One Time Shipto first line of the ShipTo address.  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  One Time Shipto  second line of the ShipTo address.  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  One Time Shipto  third line of the ShipTo address.  """  
      self.OTSCity:str = obj["OTSCity"]
      """  City portion of the One Time Shipto  address.  """  
      self.OTSState:str = obj["OTSState"]
      """  The state or province portion of the One Time Shipto  address.  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  The zip or postal code portion of the One Time ShipTo  address.  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  The State Tax Identification Number of the One Time Shipto.  """  
      self.OTSContact:str = obj["OTSContact"]
      """  One Time Ship To Contact Name  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  Fax number for the One Time ShipTo.  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  Phone number for the One Time ShipTo  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  One Time Shipping Country Number  """  
      self.ComplianceMsg:str = obj["ComplianceMsg"]
      """  Displays the cause why the item is not compliant.  """  
      self.PORelOpen:bool = obj["PORelOpen"]
      """  Open Purchase Release flag  """  
      self.Mapping:bool = obj["Mapping"]
      """  Mapping  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The Project WBS Phase Id associated with this release. This field can only have data if PORel.ProjectID is not blank.  """  
      self.WBSPhaseID:str = obj["WBSPhaseID"]
      """  Project Phase ID  """  
      self.IsMultiRel:bool = obj["IsMultiRel"]
      """  IsMultiRel  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SMIRemQty:int = obj["SMIRemQty"]
      """  Field to track the SMIRcvdQty that has not yet been moved to stock  """  
      self.LockQty:bool = obj["LockQty"]
      """  When the field is checked, no Increase, Reduce or Cancel suggestions will be created for the PO Release  """  
      self.LockDate:bool = obj["LockDate"]
      """  When the field is checked, no Expedite or Postpone suggestions will be created for the PO Release  """  
      self.DueDateChanged:bool = obj["DueDateChanged"]
      """  Indicates Due Date has been changed.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  """  
      self.Status:str = obj["Status"]
      """  Indicates the current status of the release. This field is maintained by the System automatically. The possible values are: Open (O), Arrived (A), Inspection (I), Received (R), Consumed (U), Drop Shipped (D), Closed (C), Voided (V).  """  
      self.ArrivedQty:int = obj["ArrivedQty"]
      """  Total quantity arrived to our site to date. In Purchasing unit of measure. This is a field maintained by the Receipt Process.  """  
      self.InvoicedQty:int = obj["InvoicedQty"]
      """  Total quantity invoiced to date. In Purchasing unit of measure. This is a field maintained by the AP Invoicing Process.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  Date the PO Release is required for, this can be either from the Sales Order, Material Job, Subcontract Operation, Due Date set within Generate POSuggestions or the Purchase Order Header Date.  """  
      self.LockNeedByDate:bool = obj["LockNeedByDate"]
      """  Set to 'true' if 'NeedByDate' was derived from a valid demand.  """  
      self.InspectionQty:int = obj["InspectionQty"]
      """  Total to date quantity that has been placed into inspection.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.DeliverTo:str = obj["DeliverTo"]
      """  PO Line types of 'Other' have no specified warehouse / bin and what this field provides is a means of designating 'where / whom' this delivery is intended for.  """  
      self.Taxable:bool = obj["Taxable"]
      """  Taxable  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if this item is exempt from PO tax for this line item.  If field is non-blank it is considered exempt.  This code is totally user definable and no validation is required.  This field is intended to be used for analysis purposes.  When the value is changed from blank to non-blank or vice versa tax calculation logic kicks in to calculate the PO tax info.  """  
      self.NoTaxRecalc:bool = obj["NoTaxRecalc"]
      """  This flag determines whether any manual taxes were created for a line miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.ReqChgPromiseDate:str = obj["ReqChgPromiseDate"]
      """  When the Promise Date is changed, this is the previous PromiseDt  """  
      self.OTSEMailAddress:str = obj["OTSEMailAddress"]
      """  One Time ShipTo email address.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.NumberOfPiecesUOM:str = obj["NumberOfPiecesUOM"]
      """  Unit of measure for the NumberOfPieces.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  Indicates if this release is  "FIRM".  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.EDIShipReferenceType:str = obj["EDIShipReferenceType"]
      """  Name of the ship reference that is going to be stored.  """  
      self.EDIShipReferenceData:str = obj["EDIShipReferenceData"]
      """  Data that is going to be stored as ship reference.  """  
      self.EDIEstimatedDockDate:str = obj["EDIEstimatedDockDate"]
      """  Estimated time when the shipment will arrive.  """  
      self.EDIShipQty:int = obj["EDIShipQty"]
      """  Quantity sent by the supplier.  """  
      self.EDIShipQtyUOM:str = obj["EDIShipQtyUOM"]
      """  Unit of Measure of the EDIShipQty.  """  
      self.ConsolidatedPO:bool = obj["ConsolidatedPO"]
      self.ContractOrder:bool = obj["ContractOrder"]
      """  Is this Release related to a Contract Purchase Order?  """  
      self.DelPoSug:bool = obj["DelPoSug"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocTotalDedTax:int = obj["DocTotalDedTax"]
      """  Total deductable tax amount for this PO Line in document currency.  """  
      self.DocTotalSATax:int = obj["DocTotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in document currency.  """  
      self.DocTotalTax:int = obj["DocTotalTax"]
      """  Total Tax amount for this PO Line in document currency.  """  
      self.EnableBTOOrderNum:bool = obj["EnableBTOOrderNum"]
      """  flag to determine whether the BTOOrderNum field can be enabled.  If a drop shipment has been Received/Shipped for this line, we cannot allow them to change the BTOOrderNum.  """  
      self.EnableGLAcct:bool = obj["EnableGLAcct"]
      """  Indicates whether the GL account field should be enabled. Based on GLSyst.PostInvtyWipCos and the line type  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      self.ExpDesc:str = obj["ExpDesc"]
      self.FromPOSugChg:bool = obj["FromPOSugChg"]
      self.GlbPlantName:str = obj["GlbPlantName"]
      self.GlbWhseName:str = obj["GlbWhseName"]
      self.Inspection:bool = obj["Inspection"]
      self.IUM:str = obj["IUM"]
      self.Lock:bool = obj["Lock"]
      """  This field will be used in the UI to Lock and unLock a release.  """  
      self.MangCustID:str = obj["MangCustID"]
      """  For CMI type POs, this is the associated customer that we will verify against the WhseBin.CustNum  """  
      self.MangCustName:str = obj["MangCustName"]
      """  For CMI type POs, this is the associated customer Name that we will verify against the WhseBin.CustNum  """  
      self.NotCompliant:bool = obj["NotCompliant"]
      """  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  THIS FIELD COMES DIRECTLY FROM THE POHEADER TABLE.  Indicates if an order is flagged as being HELD , this  is primarily used as a visual indicator in receipt entry. It does not prevent receipts from being entered for this order.  """  
      self.POHeaderApprove:bool = obj["POHeaderApprove"]
      self.POType:str = obj["POType"]
      """  Identifies the type of PO  """  
      self.PUM:str = obj["PUM"]
      """  Replicate PUM on detail  """  
      self.PurPoint:str = obj["PurPoint"]
      """  THIS FIELD IS EXTRACTED DIRECTLY FROM THE POHEADER TABLE. Ties the PO header back to the VendPP master file. This can be blank indicating No purchase point.  """  
      self.RefCodeStatus:str = obj["RefCodeStatus"]
      self.Rpt1TotalDedTax:int = obj["Rpt1TotalDedTax"]
      """  Total deductable tax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalSATax:int = obj["Rpt1TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt1 currency.  """  
      self.Rpt1TotalTax:int = obj["Rpt1TotalTax"]
      """  Total Tax amount for this PO Line in Rpt1 currency,  """  
      self.Rpt2TotalDedTax:int = obj["Rpt2TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalSATax:int = obj["Rpt2TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt2 currency.  """  
      self.Rpt2TotalTax:int = obj["Rpt2TotalTax"]
      """  Total Tax amount for this PO Line in Rpt2 currency,  """  
      self.Rpt3TotalDedTax:int = obj["Rpt3TotalDedTax"]
      """  Total Deductable tax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalSATax:int = obj["Rpt3TotalSATax"]
      """  Total Self AssessedTax amount for this PO Line in Rpt3 currency.  """  
      self.Rpt3TotalTax:int = obj["Rpt3TotalTax"]
      """  Total Tax amount for this PO Line in Rpt3 currency,  """  
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.StatusDescription:str = obj["StatusDescription"]
      """  Description text of the Status field  """  
      self.TotalDedTax:int = obj["TotalDedTax"]
      """  Total deductable tax amount for this PO Line in base currency.  """  
      self.TotalSATax:int = obj["TotalSATax"]
      """  Total Order Self Assessed Taxes for this PO Line in base currency.  """  
      self.TotalTax:int = obj["TotalTax"]
      """  Total Tax amount for this PO Line in base currency,  """  
      self.TranTypeDesc:str = obj["TranTypeDesc"]
      """   Transaction Type Description i.e. Job Material ("PUR-MTL"), Job Subcontract ("PUR-SUB"), 
Stock ("PUR-STK") and Other ("PUR-UKN").  """  
      self.UseGlbFields:bool = obj["UseGlbFields"]
      """  Indicates if Glb fields should be used in place of the non-global equivalent  """  
      self.VendorID:str = obj["VendorID"]
      """  Related Supplier ID  """  
      self.VendorName:str = obj["VendorName"]
      """  Related Vendor Name  """  
      self.ContainerShipped:bool = obj["ContainerShipped"]
      """  Logical indicating if the container has been shipped.  """  
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      """  The formatted ship to address  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level. This feature requires the Advanced Unit of Measure license.  """  
      self.EnableDynAttrButton:bool = obj["EnableDynAttrButton"]
      """  Internal flag used for the row rules to control whether the inventory attributes should be enabled or not.  """  
      self.AttributeQtyMismatch:bool = obj["AttributeQtyMismatch"]
      """  True if there is a remaining qty difference between the attribute quantity and the receipt line quantity.  """  
      self.JobMtlSeq:int = obj["JobMtlSeq"]
      self.JobOprSeq:int = obj["JobOprSeq"]
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.ContainerHeaderPromiseDate:str = obj["ContainerHeaderPromiseDate"]
      self.ContainerHeaderDueDate:str = obj["ContainerHeaderDueDate"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.PlantName:str = obj["PlantName"]
      self.POLineRevisionNum:str = obj["POLineRevisionNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.PONumShipName:str = obj["PONumShipName"]
      self.PONumShipToConName:str = obj["PONumShipToConName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.ReqLineLineDesc:str = obj["ReqLineLineDesc"]
      self.ReqNumShipName:str = obj["ReqNumShipName"]
      self.ReqNumShipToConName:str = obj["ReqNumShipToConName"]
      self.ShipToCustNumInactive:bool = obj["ShipToCustNumInactive"]
      self.ShipToCustNumBTName:str = obj["ShipToCustNumBTName"]
      self.ShipToCustNumCustID:str = obj["ShipToCustNumCustID"]
      self.ShipToCustNumName:str = obj["ShipToCustNumName"]
      self.ShipToNumInactive:bool = obj["ShipToNumInactive"]
      self.SoldToNumCustID:str = obj["SoldToNumCustID"]
      self.SoldToNumBTName:str = obj["SoldToNumBTName"]
      self.SoldToNumName:str = obj["SoldToNumName"]
      self.SoldToNumInactive:bool = obj["SoldToNumInactive"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.WBSPhaseDescription:str = obj["WBSPhaseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PORelSearchTableset:
   def __init__(self, obj):
      self.PORel:list[Erp_Tablesets_PORelRow] = obj["PORel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPORelSearchTableset:
   def __init__(self, obj):
      self.PORel:list[Erp_Tablesets_PORelRow] = obj["PORel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   poNum
   poLine
   poRelNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      self.poRelNum:int = obj["poRelNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PORelSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PORelSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PORelSearchTableset] = obj["returnObj"]
      pass

class GetCloseReleaseAt_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  CloseReleaseAt  """  
      pass

class GetListForContainer_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  PO Release search clause  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      pass

class GetListForContainer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PORelListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetListWithPOLinePartNum_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListWithPOLinePartNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PORelListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_PORelListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPORel_input:
   """ Required : 
   ds
   poNum
   poLine
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PORelSearchTableset] = obj["ds"]
      self.poNum:int = obj["poNum"]
      self.poLine:int = obj["poLine"]
      pass

class GetNewPORel_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PORelSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsExcludeGlobal_input:
   """ Required : 
   whereClausePoRel
   excludeGlobal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePoRel:str = obj["whereClausePoRel"]
      """  PO Release search clause  """  
      self.excludeGlobal:bool = obj["excludeGlobal"]
      """  excludeGlobal  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page  """  
      pass

class GetRowsExcludeGlobal_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PORelSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePORel
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePORel:str = obj["whereClausePORel"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PORelSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPORelSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPORelSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PORelSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PORelSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

