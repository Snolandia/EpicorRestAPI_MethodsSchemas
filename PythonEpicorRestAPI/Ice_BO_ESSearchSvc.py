import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ESSearchSvc
# Description: Provide a way to define and run field specified Enterprise Searches.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ESSearches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ESSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ESSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ESSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches",headers=creds) as resp:
           return await resp.json()

async def post_ESSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ESSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ESSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ESSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ESSearches_Company_GlbCompany_SearchID(Company, GlbCompany, SearchID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ESSearch item
   Description: Calls GetByID to retrieve the ESSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ESSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ESSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches(" + Company + "," + GlbCompany + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ESSearches_Company_GlbCompany_SearchID(Company, GlbCompany, SearchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ESSearch for the service
   Description: Calls UpdateExt to update ESSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ESSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ESSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches(" + Company + "," + GlbCompany + "," + SearchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ESSearches_Company_GlbCompany_SearchID(Company, GlbCompany, SearchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ESSearch item
   Description: Call UpdateExt to delete ESSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ESSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches(" + Company + "," + GlbCompany + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ESSearches_Company_GlbCompany_SearchID_ESSearchFields(Company, GlbCompany, SearchID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ESSearchFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ESSearchFields1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ESSearchFieldsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches(" + Company + "," + GlbCompany + "," + SearchID + ")/ESSearchFields",headers=creds) as resp:
           return await resp.json()

async def get_ESSearches_Company_GlbCompany_SearchID_ESSearchFields_Company_GlbCompany_SearchID_Seq(Company, GlbCompany, SearchID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ESSearchField item
   Description: Calls GetByID to retrieve the ESSearchField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ESSearchField1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ESSearchFieldsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearches(" + Company + "," + GlbCompany + "," + SearchID + ")/ESSearchFields(" + Company + "," + GlbCompany + "," + SearchID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ESSearchFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ESSearchFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ESSearchFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ESSearchFieldsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearchFields",headers=creds) as resp:
           return await resp.json()

async def post_ESSearchFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ESSearchFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ESSearchFieldsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ESSearchFieldsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearchFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ESSearchFields_Company_GlbCompany_SearchID_Seq(Company, GlbCompany, SearchID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ESSearchField item
   Description: Calls GetByID to retrieve the ESSearchField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ESSearchField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ESSearchFieldsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearchFields(" + Company + "," + GlbCompany + "," + SearchID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ESSearchFields_Company_GlbCompany_SearchID_Seq(Company, GlbCompany, SearchID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ESSearchField for the service
   Description: Calls UpdateExt to update ESSearchField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ESSearchField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ESSearchFieldsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearchFields(" + Company + "," + GlbCompany + "," + SearchID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ESSearchFields_Company_GlbCompany_SearchID_Seq(Company, GlbCompany, SearchID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ESSearchField item
   Description: Call UpdateExt to delete ESSearchField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ESSearchField
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/ESSearchFields(" + Company + "," + GlbCompany + "," + SearchID + "," + Seq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ESSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseESSearch, whereClauseESSearchFields, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseESSearch=" + whereClauseESSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseESSearchFields=" + whereClauseESSearchFields
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, searchID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "glbCompany=" + glbCompany
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "searchID=" + searchID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_BAQExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BAQExists
   Description: This method returns true if the BAQ exists and is approved.
   OperationID: BAQExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewESSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewESSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewESSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewESSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewESSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewESSearchFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewESSearchFields
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewESSearchFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewESSearchFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewESSearchFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ESSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ESSearchFieldsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ESSearchFieldsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ESSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ESSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ESSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ESSearchRow] = obj["value"]
      pass

class Ice_Tablesets_ESSearchFieldsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.SearchID:str = obj["SearchID"]
      """  Search ID  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Seq:int = obj["Seq"]
      """  The order to show columns in  """  
      self.DataTableId:str = obj["DataTableId"]
      """  Identifies the data table  """  
      self.FieldName:str = obj["FieldName"]
      """  The column to show  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.SearchID:str = obj["SearchID"]
      """  Search ID  """  
      self.BAQID:str = obj["BAQID"]
      """  BAQ ID  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SortColumn:str = obj["SortColumn"]
      """  The column to sort resluts by  """  
      self.SortDescending:bool = obj["SortDescending"]
      """  Sort resuts in Descending order  """  
      self.PageSize:int = obj["PageSize"]
      """  The number of results to return  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.SearchID:str = obj["SearchID"]
      """  Search ID  """  
      self.BAQID:str = obj["BAQID"]
      """  BAQ ID  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SortColumn:str = obj["SortColumn"]
      """  The column to sort resluts by  """  
      self.SortDescending:bool = obj["SortDescending"]
      """  Sort resuts in Descending order  """  
      self.PageSize:int = obj["PageSize"]
      """  The number of results to return  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BAQExists_input:
   """ Required : 
   globalCompanyId
   searchId
   """  
   def __init__(self, obj):
      self.globalCompanyId:str = obj["globalCompanyId"]
      """  The identifier of the global company.  """  
      self.searchId:str = obj["searchId"]
      """  The identifier of the Enterprise Search.  """  
      pass

class BAQExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.queryExists:bool = obj["queryExists"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   glbCompany
   searchID
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.searchID:str = obj["searchID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   glbCompany
   searchID
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.searchID:str = obj["searchID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ESSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ESSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ESSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewESSearchFields_input:
   """ Required : 
   ds
   glbCompany
   searchID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ESSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      self.searchID:str = obj["searchID"]
      pass

class GetNewESSearchFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ESSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewESSearch_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ESSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewESSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ESSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseESSearch
   whereClauseESSearchFields
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseESSearch:str = obj["whereClauseESSearch"]
      self.whereClauseESSearchFields:str = obj["whereClauseESSearchFields"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ESSearchTableset] = obj["returnObj"]
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

class Ice_Tablesets_ESSearchFieldsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.SearchID:str = obj["SearchID"]
      """  Search ID  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Seq:int = obj["Seq"]
      """  The order to show columns in  """  
      self.DataTableId:str = obj["DataTableId"]
      """  Identifies the data table  """  
      self.FieldName:str = obj["FieldName"]
      """  The column to show  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.SearchID:str = obj["SearchID"]
      """  Search ID  """  
      self.BAQID:str = obj["BAQID"]
      """  BAQ ID  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SortColumn:str = obj["SortColumn"]
      """  The column to sort resluts by  """  
      self.SortDescending:bool = obj["SortDescending"]
      """  Sort resuts in Descending order  """  
      self.PageSize:int = obj["PageSize"]
      """  The number of results to return  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESSearchListTableset:
   def __init__(self, obj):
      self.ESSearchList:list[Ice_Tablesets_ESSearchListRow] = obj["ESSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ESSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.SearchID:str = obj["SearchID"]
      """  Search ID  """  
      self.BAQID:str = obj["BAQID"]
      """  BAQ ID  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SortColumn:str = obj["SortColumn"]
      """  The column to sort resluts by  """  
      self.SortDescending:bool = obj["SortDescending"]
      """  Sort resuts in Descending order  """  
      self.PageSize:int = obj["PageSize"]
      """  The number of results to return  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ESSearchTableset:
   def __init__(self, obj):
      self.ESSearch:list[Ice_Tablesets_ESSearchRow] = obj["ESSearch"]
      self.ESSearchFields:list[Ice_Tablesets_ESSearchFieldsRow] = obj["ESSearchFields"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtESSearchTableset:
   def __init__(self, obj):
      self.ESSearch:list[Ice_Tablesets_ESSearchRow] = obj["ESSearch"]
      self.ESSearchFields:list[Ice_Tablesets_ESSearchFieldsRow] = obj["ESSearchFields"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtESSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtESSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ESSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ESSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

