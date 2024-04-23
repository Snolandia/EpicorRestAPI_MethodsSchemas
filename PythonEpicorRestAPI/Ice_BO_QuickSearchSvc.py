import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.QuickSearchSvc
# Description: Provide a way to define and run a user-defined search
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearches(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickSearches
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches",headers=creds) as resp:
           return await resp.json()

async def post_QuickSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickSearches_Company_GlbCompany_QuickSearchID(Company, GlbCompany, QuickSearchID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickSearch item
   Description: Calls GetByID to retrieve the QuickSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickSearches_Company_GlbCompany_QuickSearchID(Company, GlbCompany, QuickSearchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickSearch for the service
   Description: Calls UpdateExt to update QuickSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuickSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickSearches_Company_GlbCompany_QuickSearchID(Company, GlbCompany, QuickSearchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickSearch item
   Description: Call UpdateExt to delete QuickSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearches_Company_GlbCompany_QuickSearchID_QuickSearchCriterias(Company, GlbCompany, QuickSearchID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuickSearchCriterias items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickSearchCriterias1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")/QuickSearchCriterias",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearches_Company_GlbCompany_QuickSearchID_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company, GlbCompany, QuickSearchID, Seq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickSearchCriteria item
   Description: Calls GetByID to retrieve the QuickSearchCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchCriteria1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearches(" + Company + "," + GlbCompany + "," + QuickSearchID + ")/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearchCriterias(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickSearchCriterias items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickSearchCriterias
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias",headers=creds) as resp:
           return await resp.json()

async def post_QuickSearchCriterias(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickSearchCriterias
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company, GlbCompany, QuickSearchID, Seq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickSearchCriteria item
   Description: Calls GetByID to retrieve the QuickSearchCriteria item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchCriteria
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company, GlbCompany, QuickSearchID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickSearchCriteria for the service
   Description: Calls UpdateExt to update QuickSearchCriteria. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickSearchCriteria
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuickSearchCriteriaRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq(Company, GlbCompany, QuickSearchID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickSearchCriteria item
   Description: Call UpdateExt to delete QuickSearchCriteria item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickSearchCriteria
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq_QuickSearchValueLists(Company, GlbCompany, QuickSearchID, Seq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get QuickSearchValueLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuickSearchValueLists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchValueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")/QuickSearchValueLists",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearchCriterias_Company_GlbCompany_QuickSearchID_Seq_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company, GlbCompany, QuickSearchID, Seq, ValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickSearchValueList item
   Description: Calls GetByID to retrieve the QuickSearchValueList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchValueList1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param ValueSeq: Desc: ValueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchCriterias(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + ")/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_QuickSearchValueLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickSearchValueLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickSearchValueLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchValueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists",headers=creds) as resp:
           return await resp.json()

async def post_QuickSearchValueLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickSearchValueLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company, GlbCompany, QuickSearchID, Seq, ValueSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickSearchValueList item
   Description: Calls GetByID to retrieve the QuickSearchValueList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickSearchValueList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param ValueSeq: Desc: ValueSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company, GlbCompany, QuickSearchID, Seq, ValueSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickSearchValueList for the service
   Description: Calls UpdateExt to update QuickSearchValueList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickSearchValueList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param ValueSeq: Desc: ValueSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.QuickSearchValueListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickSearchValueLists_Company_GlbCompany_QuickSearchID_Seq_ValueSeq(Company, GlbCompany, QuickSearchID, Seq, ValueSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickSearchValueList item
   Description: Call UpdateExt to delete QuickSearchValueList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickSearchValueList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GlbCompany: Desc: GlbCompany   Required: True   Allow empty value : True
      :param QuickSearchID: Desc: QuickSearchID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param ValueSeq: Desc: ValueSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/QuickSearchValueLists(" + Company + "," + GlbCompany + "," + QuickSearchID + "," + Seq + "," + ValueSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuickSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuickSearch, whereClauseQuickSearchCriteria, whereClauseQuickSearchValueList, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseQuickSearch=" + whereClauseQuickSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuickSearchCriteria=" + whereClauseQuickSearchCriteria
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseQuickSearchValueList=" + whereClauseQuickSearchValueList
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(glbCompany, quickSearchID, epicorHeaders = None):
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
   params += "quickSearchID=" + quickSearchID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetBAQConstants(epicorHeaders = None):
   """  
   Summary: Invoke method GetBAQConstants
   Description: Returns BAQ constant names in an untyped dataset
   OperationID: GetBAQConstants
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBAQConstants_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_BAQExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BAQExists
   Description: This method returns a list of quick searches for this user
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BAQsExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BAQsExist
   Description: This method returns a dataset of quick searches indicating if a BAQ exists
for each Quick Search
   OperationID: BAQsExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BAQsExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BAQsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyQuickSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyQuickSearch
   Description: This method copies a quick search
   OperationID: CopyQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBaseDefault(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBaseDefault
   Description: This method returns a quick search dataset with the given like field and call from name.
   OperationID: GetBaseDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBaseDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextDefault(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextDefault
   Description: This method returns a quick search dataset with the given like field and call from name.
   OperationID: GetContextDefault
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextDefault_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextDefault_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUserQuickSearches(epicorHeaders = None):
   """  
   Summary: Invoke method GetUserQuickSearches
   Description: This method returns a list of quick searches for this user
   OperationID: GetUserQuickSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUserQuickSearches_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetVersion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVersion
   Description: This method returns the version code of a quick searches
   OperationID: GetVersion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVersion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVersion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLikeFieldSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLikeFieldSearches
   Description: This method returns a list of quick searches for a like field
A like field has a format of table.field
   OperationID: GetLikeFieldSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLikeFieldSearches_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLikeFieldSearches_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListForBAQ(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListForBAQ
   Description: This method returns a list of quick searches that use a given BAQ
   OperationID: GetListForBAQ
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListForBAQ_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForBAQ_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunQuickSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunQuickSearch
   Description: This method runs a quick search based on a QuickSearchDataSet.
   OperationID: RunQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunQuickSearchPaged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunQuickSearchPaged
   Description: This method runs a quick search based on a QuickSearchDataSet.
   OperationID: RunQuickSearchPaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunQuickSearchPaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunQuickSearchPaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickSearchCriteria(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickSearchCriteria
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickSearchCriteria
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickSearchCriteria_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickSearchCriteria_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickSearchValueList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickSearchValueList
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickSearchValueList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickSearchValueList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickSearchValueList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.QuickSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchCriteriaRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuickSearchCriteriaRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuickSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuickSearchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuickSearchValueListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_QuickSearchValueListRow] = obj["value"]
      pass

class Ice_Tablesets_QuickSearchCriteriaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Record  """  
      self.Seq:int = obj["Seq"]
      self.DataTableID:str = obj["DataTableID"]
      """  The DataTableID this column bolongs to. If blank then this column is a calculated column.  """  
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.CriteriaType:str = obj["CriteriaType"]
      """   Indicating the type of this criteria: valid values are:
"prompt" - prompt for user input
"constant" - either a literal constant or a field from Conatants table, similar to BAQ  """  
      self.IsReturnCol:bool = obj["IsReturnCol"]
      """  Indicates that this column is the returned column that the original text field asks.  """  
      self.CriteriaValue:str = obj["CriteriaValue"]
      self.FilterOnNull:bool = obj["FilterOnNull"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CriteriaField:str = obj["CriteriaField"]
      self.CriteriaLikeFieldName:str = obj["CriteriaLikeFieldName"]
      self.CriteriaLikeTableID:str = obj["CriteriaLikeTableID"]
      self.FieldFormat:str = obj["FieldFormat"]
      """  The display format for this criteria column  """  
      self.LikeField:str = obj["LikeField"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.ForValidation:bool = obj["ForValidation"]
      """  true if this quick search is for validating during data entry  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.HotKey:str = obj["HotKey"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.IsPredictive:bool = obj["IsPredictive"]
      """  IsPredictive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.ForValidation:bool = obj["ForValidation"]
      """  true if this quick search is for validating during data entry  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.HotKey:str = obj["HotKey"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.IsPredictive:bool = obj["IsPredictive"]
      """  IsPredictive  """  
      self.SourceSystemCode:str = obj["SourceSystemCode"]
      """  SourceSystemCode  """  
      self.SourceTableID:str = obj["SourceTableID"]
      """  SourceTableID  """  
      self.SourceFieldName:str = obj["SourceFieldName"]
      """  SourceFieldName  """  
      self.SearchOnFieldSystemCode:str = obj["SearchOnFieldSystemCode"]
      """  SearchOnFieldSystemCode  """  
      self.SearchOnFieldTableID:str = obj["SearchOnFieldTableID"]
      """  SearchOnFieldTableID  """  
      self.SearchOnFieldName:str = obj["SearchOnFieldName"]
      """  SearchOnFieldName  """  
      self.SuppressBaseSearch:bool = obj["SuppressBaseSearch"]
      """  SuppressBaseSearch  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchValueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Record  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.ValueSeq:int = obj["ValueSeq"]
      """  Value Sequence  """  
      self.DisplayMember:str = obj["DisplayMember"]
      """  Display Field  """  
      self.ValueMember:str = obj["ValueMember"]
      """  Value Field  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BAQExists_input:
   """ Required : 
   glbCompany
   quickSearchId
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  The identifier of the global company.  """  
      self.quickSearchId:str = obj["quickSearchId"]
      """  The identifier of the quick search.  """  
      pass

class BAQExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.baqExists:bool = obj["baqExists"]
      pass

      """  output parameters  """  

class BAQsExist_input:
   """ Required : 
   glbCompany
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  The ID of the global company  """  
      self.ds:list[Ice_Tablesets_QuickSearchBAQsExistTableset] = obj["ds"]
      pass

class BAQsExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchBAQsExistTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CopyQuickSearch_input:
   """ Required : 
   sourceQuickSearchId
   targetQuickSearchId
   targetQuickSearchDescription
   """  
   def __init__(self, obj):
      self.sourceQuickSearchId:str = obj["sourceQuickSearchId"]
      """  The ID of source quick search  """  
      self.targetQuickSearchId:str = obj["targetQuickSearchId"]
      """  The ID of target quick search  """  
      self.targetQuickSearchDescription:str = obj["targetQuickSearchDescription"]
      """  The description for the new quick search.  """  
      pass

class CopyQuickSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.succeeded:bool = obj["succeeded"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   glbCompany
   quickSearchID
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.quickSearchID:str = obj["quickSearchID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetBAQConstants_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetBaseDefault_input:
   """ Required : 
   likeTableAndField
   callFrom
   """  
   def __init__(self, obj):
      self.likeTableAndField:str = obj["likeTableAndField"]
      """  The Like Field  """  
      self.callFrom:str = obj["callFrom"]
      """  The name of the call from  """  
      pass

class GetBaseDefault_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.baseSearchId:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   glbCompany
   quickSearchID
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      self.quickSearchID:str = obj["quickSearchID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QuickSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_QuickSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_QuickSearchTableset] = obj["returnObj"]
      pass

class GetContextDefault_input:
   """ Required : 
   likeTableAndField
   callFrom
   """  
   def __init__(self, obj):
      self.likeTableAndField:str = obj["likeTableAndField"]
      """  The Like Field  """  
      self.callFrom:str = obj["callFrom"]
      """  The name of the call from  """  
      pass

class GetContextDefault_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.contextSearchId:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLikeFieldSearches_input:
   """ Required : 
   likeTableAndField
   """  
   def __init__(self, obj):
      self.likeTableAndField:str = obj["likeTableAndField"]
      """  The name of the like field  """  
      pass

class GetLikeFieldSearches_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QuickSearchListTableset] = obj["returnObj"]
      pass

class GetListForBAQ_input:
   """ Required : 
   baqId
   """  
   def __init__(self, obj):
      self.baqId:str = obj["baqId"]
      """  The BAQ ID  """  
      pass

class GetListForBAQ_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QuickSearchListTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_QuickSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewQuickSearchCriteria_input:
   """ Required : 
   ds
   glbCompany
   quickSearchID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      self.quickSearchID:str = obj["quickSearchID"]
      pass

class GetNewQuickSearchCriteria_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuickSearchValueList_input:
   """ Required : 
   ds
   glbCompany
   quickSearchID
   seq
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      self.quickSearchID:str = obj["quickSearchID"]
      self.seq:int = obj["seq"]
      pass

class GetNewQuickSearchValueList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewQuickSearch_input:
   """ Required : 
   ds
   glbCompany
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      self.glbCompany:str = obj["glbCompany"]
      pass

class GetNewQuickSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQuickSearch
   whereClauseQuickSearchCriteria
   whereClauseQuickSearchValueList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuickSearch:str = obj["whereClauseQuickSearch"]
      self.whereClauseQuickSearchCriteria:str = obj["whereClauseQuickSearchCriteria"]
      self.whereClauseQuickSearchValueList:str = obj["whereClauseQuickSearchValueList"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QuickSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetUserQuickSearches_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_QuickSearchListTableset] = obj["returnObj"]
      pass

class GetVersion_input:
   """ Required : 
   glbCompany
   quickSearchId
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  The ID of the global company  """  
      self.quickSearchId:str = obj["quickSearchId"]
      """  The ID of the quick search  """  
      pass

class GetVersion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.version:str = obj["parameters"]
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

class Ice_Tablesets_QuickSearchBAQsExistRow:
   def __init__(self, obj):
      self.QuickSearchID:str = obj["QuickSearchID"]
      self.BAQExist:bool = obj["BAQExist"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchBAQsExistTableset:
   def __init__(self, obj):
      self.QuickSearchBAQsExist:list[Ice_Tablesets_QuickSearchBAQsExistRow] = obj["QuickSearchBAQsExist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QuickSearchCriteriaRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Record  """  
      self.Seq:int = obj["Seq"]
      self.DataTableID:str = obj["DataTableID"]
      """  The DataTableID this column bolongs to. If blank then this column is a calculated column.  """  
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.CriteriaType:str = obj["CriteriaType"]
      """   Indicating the type of this criteria: valid values are:
"prompt" - prompt for user input
"constant" - either a literal constant or a field from Conatants table, similar to BAQ  """  
      self.IsReturnCol:bool = obj["IsReturnCol"]
      """  Indicates that this column is the returned column that the original text field asks.  """  
      self.CriteriaValue:str = obj["CriteriaValue"]
      self.FilterOnNull:bool = obj["FilterOnNull"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CriteriaField:str = obj["CriteriaField"]
      self.CriteriaLikeFieldName:str = obj["CriteriaLikeFieldName"]
      self.CriteriaLikeTableID:str = obj["CriteriaLikeTableID"]
      self.FieldFormat:str = obj["FieldFormat"]
      """  The display format for this criteria column  """  
      self.LikeField:str = obj["LikeField"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.ForValidation:bool = obj["ForValidation"]
      """  true if this quick search is for validating during data entry  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.HotKey:str = obj["HotKey"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.IsPredictive:bool = obj["IsPredictive"]
      """  IsPredictive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchListTableset:
   def __init__(self, obj):
      self.QuickSearchList:list[Ice_Tablesets_QuickSearchListRow] = obj["QuickSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QuickSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier. If blank then this quick search is for all companies.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UserID:str = obj["UserID"]
      """  The userid of the user who created the export. If IsShared is false then this search is only available to this user.  """  
      self.ExportID:str = obj["ExportID"]
      """  The unique export identifier.  """  
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      """  TableID to use with LikeField  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.GlobalSearch:bool = obj["GlobalSearch"]
      """  true if this search is available to all fields that have the same like table/field.  """  
      self.ForValidation:bool = obj["ForValidation"]
      """  true if this quick search is for validating during data entry  """  
      self.IsShared:bool = obj["IsShared"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Used for indicating this quick search is provided by system, not by an end user.  """  
      self.ReturnFieldTableID:str = obj["ReturnFieldTableID"]
      """  TableID to of the returned column  """  
      self.ReturnFieldName:str = obj["ReturnFieldName"]
      """  Field name of the returned column  """  
      self.CallFrom:str = obj["CallFrom"]
      self.ContextDefault:bool = obj["ContextDefault"]
      self.BaseDefault:bool = obj["BaseDefault"]
      self.Version:str = obj["Version"]
      self.HotKey:str = obj["HotKey"]
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.IsPredictive:bool = obj["IsPredictive"]
      """  IsPredictive  """  
      self.SourceSystemCode:str = obj["SourceSystemCode"]
      """  SourceSystemCode  """  
      self.SourceTableID:str = obj["SourceTableID"]
      """  SourceTableID  """  
      self.SourceFieldName:str = obj["SourceFieldName"]
      """  SourceFieldName  """  
      self.SearchOnFieldSystemCode:str = obj["SearchOnFieldSystemCode"]
      """  SearchOnFieldSystemCode  """  
      self.SearchOnFieldTableID:str = obj["SearchOnFieldTableID"]
      """  SearchOnFieldTableID  """  
      self.SearchOnFieldName:str = obj["SearchOnFieldName"]
      """  SearchOnFieldName  """  
      self.SuppressBaseSearch:bool = obj["SuppressBaseSearch"]
      """  SuppressBaseSearch  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReturnDataType:str = obj["ReturnDataType"]
      """  The data type of the return column  """  
      self.ReturnField:str = obj["ReturnField"]
      """  The combined return field name in the format of <table>.<field>  """  
      self.LikeField:str = obj["LikeField"]
      """  The combined like field name in the format of <table>.<field>  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_QuickSearchTableset:
   def __init__(self, obj):
      self.QuickSearch:list[Ice_Tablesets_QuickSearchRow] = obj["QuickSearch"]
      self.QuickSearchCriteria:list[Ice_Tablesets_QuickSearchCriteriaRow] = obj["QuickSearchCriteria"]
      self.QuickSearchValueList:list[Ice_Tablesets_QuickSearchValueListRow] = obj["QuickSearchValueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_QuickSearchValueListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.QuickSearchID:str = obj["QuickSearchID"]
      """  The unique identifier for this quick search  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Record  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.ValueSeq:int = obj["ValueSeq"]
      """  Value Sequence  """  
      self.DisplayMember:str = obj["DisplayMember"]
      """  Display Field  """  
      self.ValueMember:str = obj["ValueMember"]
      """  Value Field  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtQuickSearchTableset:
   def __init__(self, obj):
      self.QuickSearch:list[Ice_Tablesets_QuickSearchRow] = obj["QuickSearch"]
      self.QuickSearchCriteria:list[Ice_Tablesets_QuickSearchCriteriaRow] = obj["QuickSearchCriteria"]
      self.QuickSearchValueList:list[Ice_Tablesets_QuickSearchValueListRow] = obj["QuickSearchValueList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class RunQuickSearchPaged_input:
   """ Required : 
   ds
   pageSize
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      self.pageSize:int = obj["pageSize"]
      """  The size of page  """  
      pass

class RunQuickSearchPaged_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class RunQuickSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      pass

class RunQuickSearch_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Returns the result dataset  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtQuickSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtQuickSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_QuickSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

