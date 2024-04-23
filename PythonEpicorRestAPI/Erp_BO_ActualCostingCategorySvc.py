import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ActualCostingCategorySvc
# Description: Actual Costing Category
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingCategories(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ActualCostingCategories items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ActualCostingCategories
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostingCategoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories",headers=creds) as resp:
           return await resp.json()

async def post_ActualCostingCategories(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ActualCostingCategories
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ActualCostingCategoryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ActualCostingCategoryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingCategories_Company_Plant_ActualCostingCategoryID(Company, Plant, ActualCostingCategoryID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ActualCostingCategory item
   Description: Calls GetByID to retrieve the ActualCostingCategory item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ActualCostingCategory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ActualCostingCategoryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories(" + Company + "," + Plant + "," + ActualCostingCategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ActualCostingCategories_Company_Plant_ActualCostingCategoryID(Company, Plant, ActualCostingCategoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ActualCostingCategory for the service
   Description: Calls UpdateExt to update ActualCostingCategory. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ActualCostingCategory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ActualCostingCategoryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories(" + Company + "," + Plant + "," + ActualCostingCategoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ActualCostingCategories_Company_Plant_ActualCostingCategoryID(Company, Plant, ActualCostingCategoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ActualCostingCategory item
   Description: Call UpdateExt to delete ActualCostingCategory item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ActualCostingCategory
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories(" + Company + "," + Plant + "," + ActualCostingCategoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingCategories_Company_Plant_ActualCostingCategoryID_ActualCostingGLAccountGroups(Company, Plant, ActualCostingCategoryID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ActualCostingGLAccountGroups items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ActualCostingGLAccountGroups1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostingGLAccountGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories(" + Company + "," + Plant + "," + ActualCostingCategoryID + ")/ActualCostingGLAccountGroups",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingCategories_Company_Plant_ActualCostingCategoryID_ActualCostingGLAccountGroups_Company_Plant_ActualCostingCategoryID_GroupNum(Company, Plant, ActualCostingCategoryID, GroupNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ActualCostingGLAccountGroup item
   Description: Calls GetByID to retrieve the ActualCostingGLAccountGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ActualCostingGLAccountGroup1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingCategories(" + Company + "," + Plant + "," + ActualCostingCategoryID + ")/ActualCostingGLAccountGroups(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingGLAccountGroups(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ActualCostingGLAccountGroups items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ActualCostingGLAccountGroups
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostingGLAccountGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups",headers=creds) as resp:
           return await resp.json()

async def post_ActualCostingGLAccountGroups(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ActualCostingGLAccountGroups
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountGroupRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountGroupRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingGLAccountGroups_Company_Plant_ActualCostingCategoryID_GroupNum(Company, Plant, ActualCostingCategoryID, GroupNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ActualCostingGLAccountGroup item
   Description: Calls GetByID to retrieve the ActualCostingGLAccountGroup item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ActualCostingGLAccountGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountGroupRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ActualCostingGLAccountGroups_Company_Plant_ActualCostingCategoryID_GroupNum(Company, Plant, ActualCostingCategoryID, GroupNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ActualCostingGLAccountGroup for the service
   Description: Calls UpdateExt to update ActualCostingGLAccountGroup. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ActualCostingGLAccountGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountGroupRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ActualCostingGLAccountGroups_Company_Plant_ActualCostingCategoryID_GroupNum(Company, Plant, ActualCostingCategoryID, GroupNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ActualCostingGLAccountGroup item
   Description: Call UpdateExt to delete ActualCostingGLAccountGroup item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ActualCostingGLAccountGroup
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingGLAccountGroups_Company_Plant_ActualCostingCategoryID_GroupNum_ActualCostingGLAccountLists(Company, Plant, ActualCostingCategoryID, GroupNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ActualCostingGLAccountLists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ActualCostingGLAccountLists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostingGLAccountListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + ")/ActualCostingGLAccountLists",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingGLAccountGroups_Company_Plant_ActualCostingCategoryID_GroupNum_ActualCostingGLAccountLists_Company_Plant_ActualCostingCategoryID_GroupNum_LineNum(Company, Plant, ActualCostingCategoryID, GroupNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ActualCostingGLAccountList item
   Description: Calls GetByID to retrieve the ActualCostingGLAccountList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ActualCostingGLAccountList1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountGroups(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + ")/ActualCostingGLAccountLists(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingGLAccountLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ActualCostingGLAccountLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ActualCostingGLAccountLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostingGLAccountListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountLists",headers=creds) as resp:
           return await resp.json()

async def post_ActualCostingGLAccountLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ActualCostingGLAccountLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ActualCostingGLAccountLists_Company_Plant_ActualCostingCategoryID_GroupNum_LineNum(Company, Plant, ActualCostingCategoryID, GroupNum, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ActualCostingGLAccountList item
   Description: Calls GetByID to retrieve the ActualCostingGLAccountList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ActualCostingGLAccountList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountLists(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ActualCostingGLAccountLists_Company_Plant_ActualCostingCategoryID_GroupNum_LineNum(Company, Plant, ActualCostingCategoryID, GroupNum, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ActualCostingGLAccountList for the service
   Description: Calls UpdateExt to update ActualCostingGLAccountList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ActualCostingGLAccountList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ActualCostingGLAccountListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountLists(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ActualCostingGLAccountLists_Company_Plant_ActualCostingCategoryID_GroupNum_LineNum(Company, Plant, ActualCostingCategoryID, GroupNum, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ActualCostingGLAccountList item
   Description: Call UpdateExt to delete ActualCostingGLAccountList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ActualCostingGLAccountList
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ActualCostingCategoryID: Desc: ActualCostingCategoryID   Required: True   Allow empty value : True
      :param GroupNum: Desc: GroupNum   Required: True
      :param LineNum: Desc: LineNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/ActualCostingGLAccountLists(" + Company + "," + Plant + "," + ActualCostingCategoryID + "," + GroupNum + "," + LineNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ActualCostingCategoryListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseActualCostingCategory, whereClauseActualCostingGLAccountGroup, whereClauseActualCostingGLAccountList, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseActualCostingCategory=" + whereClauseActualCostingCategory
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseActualCostingGLAccountGroup=" + whereClauseActualCostingGLAccountGroup
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseActualCostingGLAccountList=" + whereClauseActualCostingGLAccountList
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, actualCostingCategoryID, epicorHeaders = None):
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "actualCostingCategoryID=" + actualCostingCategoryID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFormula
   Description: This method validates the Formula.
   OperationID: OnChangeFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewActualCostingCategory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewActualCostingCategory
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewActualCostingCategory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewActualCostingCategory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewActualCostingCategory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewActualCostingGLAccountGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewActualCostingGLAccountGroup
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewActualCostingGLAccountGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewActualCostingGLAccountGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewActualCostingGLAccountGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewActualCostingGLAccountList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewActualCostingGLAccountList
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewActualCostingGLAccountList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewActualCostingGLAccountList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewActualCostingGLAccountList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ActualCostingCategorySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ActualCostingCategoryListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ActualCostingCategoryListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ActualCostingCategoryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ActualCostingCategoryRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ActualCostingGLAccountGroupRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ActualCostingGLAccountGroupRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ActualCostingGLAccountListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ActualCostingGLAccountListRow] = obj["value"]
      pass

class Erp_Tablesets_ActualCostingCategoryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is Active  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostingCategoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is Active  """  
      self.MinAllocationBaseAmt:int = obj["MinAllocationBaseAmt"]
      """  MinAllocationBaseAmt  """  
      self.MinAllocationAmt:int = obj["MinAllocationAmt"]
      """  MinAllocationAmt  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllocationBase:str = obj["AllocationBase"]
      """  Allocation Base  """  
      self.BurdenCostBase:str = obj["BurdenCostBase"]
      """  Burden Cost Base  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostingGLAccountGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.GroupNum:int = obj["GroupNum"]
      """  Group Number  """  
      self.Section:str = obj["Section"]
      """  Section  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SuppressNegative:bool = obj["SuppressNegative"]
      """  Suppress Negative  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostingGLAccountListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.GroupNum:int = obj["GroupNum"]
      """  Group Number  """  
      self.LineNum:int = obj["LineNum"]
      """  Line Number  """  
      self.IsOffset:bool = obj["IsOffset"]
      """  Is Offset  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AccountGroupSection:str = obj["AccountGroupSection"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   actualCostingCategoryID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ActualCostingCategoryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is Active  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostingCategoryListTableset:
   def __init__(self, obj):
      self.ActualCostingCategoryList:list[Erp_Tablesets_ActualCostingCategoryListRow] = obj["ActualCostingCategoryList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ActualCostingCategoryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.BookID:str = obj["BookID"]
      """  Book ID  """  
      self.IsActive:bool = obj["IsActive"]
      """  Is Active  """  
      self.MinAllocationBaseAmt:int = obj["MinAllocationBaseAmt"]
      """  MinAllocationBaseAmt  """  
      self.MinAllocationAmt:int = obj["MinAllocationAmt"]
      """  MinAllocationAmt  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllocationBase:str = obj["AllocationBase"]
      """  Allocation Base  """  
      self.BurdenCostBase:str = obj["BurdenCostBase"]
      """  Burden Cost Base  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostingCategoryTableset:
   def __init__(self, obj):
      self.ActualCostingCategory:list[Erp_Tablesets_ActualCostingCategoryRow] = obj["ActualCostingCategory"]
      self.ActualCostingGLAccountGroup:list[Erp_Tablesets_ActualCostingGLAccountGroupRow] = obj["ActualCostingGLAccountGroup"]
      self.ActualCostingGLAccountList:list[Erp_Tablesets_ActualCostingGLAccountListRow] = obj["ActualCostingGLAccountList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ActualCostingGLAccountGroupRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.GroupNum:int = obj["GroupNum"]
      """  Group Number  """  
      self.Section:str = obj["Section"]
      """  Section  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SuppressNegative:bool = obj["SuppressNegative"]
      """  Suppress Negative  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ActualCostingGLAccountListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Plant:str = obj["Plant"]
      """  Site  """  
      self.ActualCostingCategoryID:str = obj["ActualCostingCategoryID"]
      """  Actual Costing Category ID  """  
      self.GroupNum:int = obj["GroupNum"]
      """  Group Number  """  
      self.LineNum:int = obj["LineNum"]
      """  Line Number  """  
      self.IsOffset:bool = obj["IsOffset"]
      """  Is Offset  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AccountGroupSection:str = obj["AccountGroupSection"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtActualCostingCategoryTableset:
   def __init__(self, obj):
      self.ActualCostingCategory:list[Erp_Tablesets_ActualCostingCategoryRow] = obj["ActualCostingCategory"]
      self.ActualCostingGLAccountGroup:list[Erp_Tablesets_ActualCostingGLAccountGroupRow] = obj["ActualCostingGLAccountGroup"]
      self.ActualCostingGLAccountList:list[Erp_Tablesets_ActualCostingGLAccountListRow] = obj["ActualCostingGLAccountList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   actualCostingCategoryID
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ActualCostingCategoryListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewActualCostingCategory_input:
   """ Required : 
   ds
   plant
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      pass

class GetNewActualCostingCategory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewActualCostingGLAccountGroup_input:
   """ Required : 
   ds
   plant
   actualCostingCategoryID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      pass

class GetNewActualCostingGLAccountGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewActualCostingGLAccountList_input:
   """ Required : 
   ds
   plant
   actualCostingCategoryID
   groupNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.actualCostingCategoryID:str = obj["actualCostingCategoryID"]
      self.groupNum:int = obj["groupNum"]
      pass

class GetNewActualCostingGLAccountList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseActualCostingCategory
   whereClauseActualCostingGLAccountGroup
   whereClauseActualCostingGLAccountList
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseActualCostingCategory:str = obj["whereClauseActualCostingCategory"]
      self.whereClauseActualCostingGLAccountGroup:str = obj["whereClauseActualCostingGLAccountGroup"]
      self.whereClauseActualCostingGLAccountList:str = obj["whereClauseActualCostingGLAccountList"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["returnObj"]
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

class OnChangeFormula_input:
   """ Required : 
   formula
   """  
   def __init__(self, obj):
      self.formula:str = obj["formula"]
      """  The new proposed formula  """  
      pass

class OnChangeFormula_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtActualCostingCategoryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtActualCostingCategoryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ActualCostingCategoryTableset] = obj["ds"]
      pass

      """  output parameters  """  

