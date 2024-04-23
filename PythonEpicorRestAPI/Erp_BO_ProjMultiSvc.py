import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ProjMultiSvc
# Description: Service to have the visibility of all project cost/revenue details
in a single view (dashboard) and based on that information run the
revenue recognition for one or more selected projects at the same time.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ProjMultis(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProjMultis items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProjMultis
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjMultiRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis",headers=creds) as resp:
           return await resp.json()

async def post_ProjMultis(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProjMultis
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProjMultiRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProjMultiRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProjMultis_Company_ProjectID(Company, ProjectID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProjMulti item
   Description: Calls GetByID to retrieve the ProjMulti item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjMulti
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProjMultiRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProjMultis_Company_ProjectID(Company, ProjectID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProjMulti for the service
   Description: Calls UpdateExt to update ProjMulti. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProjMulti
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProjMultiRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProjMultis_Company_ProjectID(Company, ProjectID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProjMulti item
   Description: Call UpdateExt to delete ProjMulti item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProjMulti
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProjMultis_Company_ProjectID_ProjectCsts(Company, ProjectID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ProjectCsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ProjectCsts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjectCstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")/ProjectCsts",headers=creds) as resp:
           return await resp.json()

async def get_ProjMultis_Company_ProjectID_ProjectCsts_Company_ProjectID(Company, ProjectID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProjectCst item
   Description: Calls GetByID to retrieve the ProjectCst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjectCst1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjMultis(" + Company + "," + ProjectID + ")/ProjectCsts(" + Company + "," + ProjectID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProjectCsts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProjectCsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProjectCsts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjectCstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts",headers=creds) as resp:
           return await resp.json()

async def post_ProjectCsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProjectCsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProjectCsts_Company_ProjectID(Company, ProjectID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProjectCst item
   Description: Calls GetByID to retrieve the ProjectCst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProjectCst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts(" + Company + "," + ProjectID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProjectCsts_Company_ProjectID(Company, ProjectID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProjectCst for the service
   Description: Calls UpdateExt to update ProjectCst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProjectCst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ProjectCstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts(" + Company + "," + ProjectID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProjectCsts_Company_ProjectID(Company, ProjectID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProjectCst item
   Description: Call UpdateExt to delete ProjectCst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProjectCst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ProjectID: Desc: ProjectID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/ProjectCsts(" + Company + "," + ProjectID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ProjMultiListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseProjMulti, whereClauseProjectCst, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseProjMulti=" + whereClauseProjMulti
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseProjectCst=" + whereClauseProjectCst
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(projectID, epicorHeaders = None):
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
   params += "projectID=" + projectID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsByFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsByFilter
   Description: It checks files of input filter ProjFilter if some of them are not empty
then creates where-clause against it and generates a total where-clause
against Project table
   OperationID: GetRowsByFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsByFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsByFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshAll
   Description: Refresh UI with ProjectIDs
   OperationID: RefreshAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProjMulti(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProjMulti
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProjMulti
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProjMulti_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProjMulti_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProjectCst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProjectCst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewProjectCst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProjectCst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProjectCst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProjMultiSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProjMultiListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjMultiRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProjMultiRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ProjectCstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ProjectCstRow] = obj["value"]
      pass

class Erp_Tablesets_ProjMultiListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Description:str = obj["Description"]
      """  Full description of Project Management Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date of the project  """  
      self.ConCustNum:int = obj["ConCustNum"]
      """  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  """  
      self.ConProjMgr:str = obj["ConProjMgr"]
      """  Employee ID of the person who has responsibility for the project  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LastAction:str = obj["LastAction"]
      """  Last action performed on Project as relates to revenue recognition.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  Date when the LastAction happened to the Project.  """  
      self.Approved:bool = obj["Approved"]
      self.Selected:bool = obj["Selected"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjMultiRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Description:str = obj["Description"]
      """  Full description of Project Management Code.  """  
      self.ActiveProject:bool = obj["ActiveProject"]
      """  Indicates if this Project is active.  Can be changed directly by the user during entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for project comments.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.UserMap:str = obj["UserMap"]
      """  Will contain the coma separated list of the fields that the user has added to the project from within Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Holds the default project warehouse code.  """  
      self.BinNum:str = obj["BinNum"]
      """  Holds the default project bin code.  """  
      self.PrimaryJob:str = obj["PrimaryJob"]
      """  This holds the top level job to which all of the jobs created for a WBS Phase will be associated  """  
      self.PrimaryMtl:int = obj["PrimaryMtl"]
      """  This is the material placeholder in the primary project job to which all WBS Phase jobs will be linked.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  The sales category code used in the Revenue recognition process.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  The Product Group code used in the Revenue Recognition process.  """  
      self.CloseAccrual:bool = obj["CloseAccrual"]
      """  RESERVED FOR FUTURE USE: Logical field. When set to true it indicates that the journals created to recognise the revenue for the project have been reversed.  """  
      self.PrimaryAsmSeq:int = obj["PrimaryAsmSeq"]
      """  Assembly Seq from JobAsmbl record.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date of the project  """  
      self.ConCustNum:int = obj["ConCustNum"]
      """  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  """  
      self.ConStartDate:str = obj["ConStartDate"]
      """  Contract start date  """  
      self.ConEndDate:str = obj["ConEndDate"]
      """  Date the contract is due to be complete  """  
      self.ConProjectedEnd:str = obj["ConProjectedEnd"]
      """  Projected Contract End Date. Defaults to the Contract End Date but can be used to report on the projected end date.  """  
      self.ConReference:str = obj["ConReference"]
      """   Contract Reference number for project.
At the Epicor 9.05 release this field is reference only, at the Epicor 9.1 release when the whole contract system is enhanced then this field will reference an actual contract and a search will be provided.  """  
      self.ConProjMgr:str = obj["ConProjMgr"]
      """  Employee ID of the person who has responsibility for the project  """  
      self.ConTotValue:int = obj["ConTotValue"]
      """  Total contract value for the project.  """  
      self.ConTotInv:int = obj["ConTotInv"]
      """  Value of the posted invoices to date (system field)  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Foreign key to the QMarkUp  """  
      self.PBLbMarkUp:int = obj["PBLbMarkUp"]
      """  Override of Labor Markup Percent  """  
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      """  Override of Material Markup Percent  """  
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      """  Override of Subcontract Markup Percentage  """  
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      """  Override of Other Direct Cost Markup %  """  
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      """  Retention percentage. How this is used is dependent on RetentionProc field.  """  
      self.PBRetentionProc:str = obj["PBRetentionProc"]
      """   How the retention percentage will be used.
The options are ?M? = Maximum of Contract Value
?P? = Percent of Invoice Value.  """  
      self.PBFeeProject:int = obj["PBFeeProject"]
      """  Project Fee  """  
      self.PBFeeApply:str = obj["PBFeeApply"]
      """  Apply Fee with list of the options: F =  First Invoice Only, A = All Invoices  """  
      self.PBFeeType:str = obj["PBFeeType"]
      """  Fee Type with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      """  Apply Fees on list with the options: N = Net Cost, G = Gross Cost.  """  
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      """  Fee Invoice Text in Free format to allow the user to enter text that will be displayed on the invoice  """  
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice  """  
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      """  Labor Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      """  Labor Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice  """  
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      """  Material Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      """  Material Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice.  """  
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      """  Subcontract Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      """  Subcontract Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice.  """  
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      """  Miscellaneous Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      """  Miscellaneous Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ConBTCustNum:int = obj["ConBTCustNum"]
      """  Contract Customer Bill To number, foreign key to Customer  """  
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      """  If invoices are allowed to be generated even if the element is over the predefined ceiling.  """  
      self.ConRevMethod:str = obj["ConRevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  """  
      self.ConListCode:str = obj["ConListCode"]
      """  Price list is used to establish the price for any materials when the invoicing method is set to T & M or Cost Plus. Can be empty.  """  
      self.ConHrsInvc:str = obj["ConHrsInvc"]
      """  Hours for Invoicing allows the user to decide which hours are to be used by the invoicing process, it has system list with the options: L =  Labor, B = Burden  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type Code  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  """  
      self.EndDate:str = obj["EndDate"]
      """  This is the projected end date of the project but is not required and is only used if entered in the creation of the project job and for any user reporting requirements.  """  
      self.PBPrjRtSrc:str = obj["PBPrjRtSrc"]
      """  Defaults from JCSyst.DfltPrjRtSrc. Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  """  
      self.DocConTotInv:int = obj["DocConTotInv"]
      """  Value of the posted invoices to date (system field) in the Project currency  """  
      self.CreatePrjJob:bool = obj["CreatePrjJob"]
      """  If set to true a new primary job will be created automatically for the project.  """  
      self.Rpt1ConTotInv:int = obj["Rpt1ConTotInv"]
      """  Value of the posted invoices to date (system field) in the Reporting currency  """  
      self.Revision:int = obj["Revision"]
      """  Project revision number  """  
      self.Rpt2ConTotInv:int = obj["Rpt2ConTotInv"]
      """  Value of the posted invoices to date (system field) in the Reporting currency  """  
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      """   This is the percentage of the costs for material, labor and burden that will be invoiced.
This is also used by the invoice entry process when invoicing regular shipments to determine the actual value of the invoice and how much will be relieved from the Progress Payments to date.  """  
      self.Rpt3ConTotInv:int = obj["Rpt3ConTotInv"]
      """  Value of the posted invoices to date (system field) in the Reporting currency  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """   This will allow regular shipments to be invoiced normally.
Setting the field to true will cause the Customer Shipment process to place any packing slips for any sales order associated with the project to be placed on hold to prevent them being selected for invoicing. 
When the user changes this flag to true it will trigger business logic that will release the shipments for invoicing.  """  
      self.DocConTotValue:int = obj["DocConTotValue"]
      """  Total contract value for the project. in the Project currency  """  
      self.PPActive:bool = obj["PPActive"]
      """   This will default to true which will then trigger the Invoice Preparation process to produce a Progress Payment Invoice.
Setting this to false will cause the project to be ignored by the Invoice Preparation process.  """  
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      """  Total contract value for the project. in the Reporting currency  """  
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      """  Total contract value for the project. in the Reporting currency  """  
      self.TotLiqToDate:int = obj["TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments.  """  
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      """  Total contract value for the project. in the Reporting currency  """  
      self.PPCeilingTotal:int = obj["PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then  """  
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Project currency  """  
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  """  
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  """  
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  """  
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Project currency  """  
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  """  
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  """  
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  """  
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Project currency  """  
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Reporting currency  """  
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Reporting currency  """  
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Reporting currency  """  
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Project currency  """  
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  """  
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  """  
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  """  
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      """  Allows individual ceilings to be applied to suppliers  """  
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      """  Allows individual ceilings to be applied to employee  """  
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      """  Allows individual ceilings to be applied to role  """  
      self.PBDocInvoicedMtl:int = obj["PBDocInvoicedMtl"]
      """  Material Cost invoiced by date.  """  
      self.PBDocInvoicedLbr:int = obj["PBDocInvoicedLbr"]
      """  Labor cost invoiced by date.  """  
      self.PBDocInvoicedSub:int = obj["PBDocInvoicedSub"]
      """  Subcontract cost invoiced by date.  """  
      self.PBDocInvoicedMtlBur:int = obj["PBDocInvoicedMtlBur"]
      """  Material Burden Material cost invoiced by date.  """  
      self.PBDocInvoicedMisc:int = obj["PBDocInvoicedMisc"]
      """  Other direct Costs invoiced by date.  """  
      self.PBDocInvoicedBur:int = obj["PBDocInvoicedBur"]
      """  Burden Costs invoiced by date.  """  
      self.PBDocInvoicedFees:int = obj["PBDocInvoicedFees"]
      """  Fees charged by date  """  
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      """  Next Temporary Invoice number used in the Invoice preparation table before invoice is generated  """  
      self.DocTotLiqToDate:int = obj["DocTotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Project currency  """  
      self.Rpt1TotLiqToDate:int = obj["Rpt1TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  """  
      self.Rpt2TotLiqToDate:int = obj["Rpt2TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  """  
      self.Rpt3TotLiqToDate:int = obj["Rpt3TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  """  
      self.DocPPCeilingTotal:int = obj["DocPPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Project currency  """  
      self.Rpt1PPCeilingTotal:int = obj["Rpt1PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  """  
      self.Rpt2PPCeilingTotal:int = obj["Rpt2PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  """  
      self.Rpt3PPCeilingTotal:int = obj["Rpt3PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  """  
      self.PBOrderNum:int = obj["PBOrderNum"]
      """  Progress Billing - Order Number  """  
      self.PPOrderNum:int = obj["PPOrderNum"]
      """  Progress Payment - Order Number  """  
      self.PBOrderLine:int = obj["PBOrderLine"]
      """  Progress Billing - Order Line  """  
      self.PPOrderLine:int = obj["PPOrderLine"]
      """  Progress Payment - Order Line  """  
      self.DocPBFeeProject:int = obj["DocPBFeeProject"]
      """  Project Fee in the Project currency  """  
      self.Rpt1PBFeeProject:int = obj["Rpt1PBFeeProject"]
      """  Project Fee in the Reporting currency  """  
      self.Rpt2PBFeeProject:int = obj["Rpt2PBFeeProject"]
      """  Project Fee in the Reporting currency  """  
      self.Rpt3PBFeeProject:int = obj["Rpt3PBFeeProject"]
      """  Project Fee in the Reporting currency  """  
      self.PBClose:bool = obj["PBClose"]
      """  Set to true when the close billing has been executed. For Fixed Fee this is set only after all PBillSch are closed. For other types this is set when Close Project is executed.  """  
      self.PBTrueUp:bool = obj["PBTrueUp"]
      """  This field is set to true after the Project True Up has been executed.  """  
      self.TimeApprovalsMethod:str = obj["TimeApprovalsMethod"]
      """  Defines the Approvals Method for Time related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for Time transactions related to this Project.  """  
      self.ExpenseApprovalsMethod:str = obj["ExpenseApprovalsMethod"]
      """  Defines the Approvals Method for Expenses related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for Expense transactions related to this Project.  """  
      self.PBNumInvoices:int = obj["PBNumInvoices"]
      """  Number of Invoices generated for the Project  """  
      self.PBTrueUpYearList:str = obj["PBTrueUpYearList"]
      """  List of fiscal years for which True Up was called  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier  """  
      self.ConConNum:int = obj["ConConNum"]
      """  Customer Contract Number  """  
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  material lines. If blank the standard InvcDtl.TaxCatID defaulting will be used.  """  
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  labor lines.  """  
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  fee lines.  """  
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  ODC lines. If blank use the tax category from the PurMisc misc charge code record  """  
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID Subcontract lines.  """  
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Tax Category to default for PB Invoice InvcDtl.TaxCatID  Burden lines.  """  
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      """  Calculate taxes on the amount net of the retention (for future use)  """  
      self.LastAnalDate:str = obj["LastAnalDate"]
      """  Date of last project analysis run.  """  
      self.RegenReqd:bool = obj["RegenReqd"]
      """  Indicates if full Re-gen is required for the project. When this is set, the next generate of project analysis will be full re-gen.  """  
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling.  """  
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Project currency  """  
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.PBCeilingFees:int = obj["PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling.  """  
      self.DocPBCeilingFees:int = obj["DocPBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Project currency  """  
      self.Rpt1PBCeilingFees:int = obj["Rpt1PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt2PBCeilingFees:int = obj["Rpt2PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt3PBCeilingFees:int = obj["Rpt3PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.ChkEmpPrjRole:bool = obj["ChkEmpPrjRole"]
      """  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  """  
      self.PPLiquidPct:int = obj["PPLiquidPct"]
      """  Progress Payment Liquidation Percentage, used in Get Shipment.  """  
      self.PPAllOrderLines:bool = obj["PPAllOrderLines"]
      """  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  """  
      self.PPAllPrjJobs:bool = obj["PPAllPrjJobs"]
      """  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  """  
      self.AvoidPriceList:bool = obj["AvoidPriceList"]
      """  AvoidPriceList  """  
      self.PbsTaxCatID:str = obj["PbsTaxCatID"]
      """  PbsTaxCatID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.RecognizeRevenueAtPhaseLevel:bool = obj["RecognizeRevenueAtPhaseLevel"]
      """  Activate Revenue Recognition at WBS Phase level  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Indicates the date when the project is closed, if the project is reopen, the field will be cleared.  """  
      self.LastAction:str = obj["LastAction"]
      """  Last action performed on Project as relates to revenue recognition.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  Date when the LastAction happened to the Project.  """  
      self.Approved:bool = obj["Approved"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConCustNumName:str = obj["ConCustNumName"]
      self.ConCustNumCustID:str = obj["ConCustNumCustID"]
      self.ConCustNumBTName:str = obj["ConCustNumBTName"]
      self.ConProjMgrLastName:str = obj["ConProjMgrLastName"]
      self.ConProjMgrName:str = obj["ConProjMgrName"]
      self.ConProjMgrFirstName:str = obj["ConProjMgrFirstName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.CustNum_c:int = obj["CustNum_c"]
      self.ShipToNum_c:str = obj["ShipToNum_c"]
      self.LienRequired_c:bool = obj["LienRequired_c"]
      self.DNBComplete_c:bool = obj["DNBComplete_c"]
      self.DNBCompletedBy_c:str = obj["DNBCompletedBy_c"]
      self.PermitRequired_c:bool = obj["PermitRequired_c"]
      self.RightToLien_c:bool = obj["RightToLien_c"]
      self.RightToLienWithInDays_c:int = obj["RightToLienWithInDays_c"]
      self.ReviewedBy_c:str = obj["ReviewedBy_c"]
      self.TermsCode_c:str = obj["TermsCode_c"]
      self.AdditionalTerms_c:str = obj["AdditionalTerms_c"]
      self.PlannedShipDate_c:str = obj["PlannedShipDate_c"]
      self.SchedSubmittalDate_c:str = obj["SchedSubmittalDate_c"]
      self.FreightAmt_c:int = obj["FreightAmt_c"]
      self.NextMilestoneDate_c:str = obj["NextMilestoneDate_c"]
      self.NextMilestoneDesc_c:str = obj["NextMilestoneDesc_c"]
      self.EstProfit_c:int = obj["EstProfit_c"]
      self.EstMargin_c:int = obj["EstMargin_c"]
      self.CommissionApproval_c:str = obj["CommissionApproval_c"]
      self.CommissionApprovedBy_c:str = obj["CommissionApprovedBy_c"]
      self.CommissionApprovalDate_c:str = obj["CommissionApprovalDate_c"]
      pass

class Erp_Tablesets_ProjectCstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.EstBurdenCost:int = obj["EstBurdenCost"]
      """  Estimated burden cost.  """  
      self.EstBurdenHours:int = obj["EstBurdenHours"]
      """  Estimated burden hours.  """  
      self.EstLaborCost:int = obj["EstLaborCost"]
      """  Estimated labor cost.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated labor hours.  """  
      self.EstSubcontractCost:int = obj["EstSubcontractCost"]
      """  Estimated subcontract cost.  """  
      self.EstMtlCost:int = obj["EstMtlCost"]
      """  Estimated material cost.  """  
      self.EstMtlBurdenCost:int = obj["EstMtlBurdenCost"]
      """  Estimated material burden cost.  """  
      self.RollBudgetstoProject:bool = obj["RollBudgetstoProject"]
      """  To control if the project phase budget values are to be rolled up to the project  """  
      self.RollManEstToCpte:bool = obj["RollManEstToCpte"]
      """  to control if the project phase manual estimate to complete values are to be rolled up to the project  """  
      self.TotEstLbrHrs:int = obj["TotEstLbrHrs"]
      """  Total Costd labour hours for the Project  """  
      self.TotEstBurdenHrs:int = obj["TotEstBurdenHrs"]
      """  Total estimated burden hours for the project  """  
      self.TotEstLbrCost:int = obj["TotEstLbrCost"]
      """  Total estimated labour cost for the project. This is production and setup combined.  """  
      self.TotEstMtlCost:int = obj["TotEstMtlCost"]
      """  Total estimated material costs for the project  """  
      self.TotEstSubContCost:int = obj["TotEstSubContCost"]
      """  Total estimated subcontract costs for the project  """  
      self.TotActLbrHrs:int = obj["TotActLbrHrs"]
      """  Total actual labour hours for the project  """  
      self.TotActBurHrs:int = obj["TotActBurHrs"]
      """  Total actual burden hours for the project.  """  
      self.TotActLbrCost:int = obj["TotActLbrCost"]
      """  Total actual labour cost for the project. This is production and setup combined.  """  
      self.TotActBurCost:int = obj["TotActBurCost"]
      """  Total actual burden cost for the project. This is production and setup combined.  """  
      self.TotActSubContCost:int = obj["TotActSubContCost"]
      """  Total actual subcontract costs for the project  """  
      self.TotActMtlCost:int = obj["TotActMtlCost"]
      """  Total actual material costs for the project  """  
      self.TotActMtlBurCost:int = obj["TotActMtlBurCost"]
      """  Total actual material burden costs for the project  """  
      self.ManEstCtcLbrHrs:int = obj["ManEstCtcLbrHrs"]
      """  Manually entered estimate to complete for the labour hours for the project.  """  
      self.ManEstCtcBurHrs:int = obj["ManEstCtcBurHrs"]
      """  Manually entered estimate to complete for the burden hours for the project.  """  
      self.ManEstCtcLbrCost:int = obj["ManEstCtcLbrCost"]
      """  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project.  """  
      self.ManEstCtcBurCost:int = obj["ManEstCtcBurCost"]
      """  Manually entered estimate to complete for the burden cost for the project.  """  
      self.ManEstCtcSubConCost:int = obj["ManEstCtcSubConCost"]
      """  Manually entered estimate to complete for the Subcontract cost for the project.  """  
      self.ManEstCtcMtlCost:int = obj["ManEstCtcMtlCost"]
      """  Manually entered estimate to complete for the material cost for the project.  """  
      self.ManEstCtcMtlBurCost:int = obj["ManEstCtcMtlBurCost"]
      """  Manually entered estimate to complete for the material burden cost for the project.  """  
      self.TotCtcLbrHours:int = obj["TotCtcLbrHours"]
      """  Total calculated cost to complete labour hours for the project.  """  
      self.TotCtcBurHours:int = obj["TotCtcBurHours"]
      """  Total calculated cost to complete burden hours for the project.  """  
      self.TotCtcBurCost:int = obj["TotCtcBurCost"]
      """  Total calculated cost to complete burden cost for the project. This will be both production and setup.  """  
      self.TotCtcLbrCost:int = obj["TotCtcLbrCost"]
      """  Total calculated cost to complete labour cost for the project. This will be both production and setup.  """  
      self.TotCtcSubConCost:int = obj["TotCtcSubConCost"]
      """  Total calculated cost to complete subcontract cost for the project.  """  
      self.TotCtcMtlCost:int = obj["TotCtcMtlCost"]
      """  Total calculated cost to complete material cost for the project.  """  
      self.TotCtcMtlBurCost:int = obj["TotCtcMtlBurCost"]
      """  Total calculated cost to complete material burden cost for the project.  """  
      self.TotQuotLbrHrs:int = obj["TotQuotLbrHrs"]
      """  Total quoted labour hours for the project  """  
      self.TotQuotBurHrs:int = obj["TotQuotBurHrs"]
      """  Total quoted burden hours for the project  """  
      self.TotQuotLbrCost:int = obj["TotQuotLbrCost"]
      """  Total quoted labour cost for the project. This will be both production and setup.  """  
      self.TotQuotSubContCost:int = obj["TotQuotSubContCost"]
      """  Total quoted subcontract cost for the project.  """  
      self.TotQuotMtlCost:int = obj["TotQuotMtlCost"]
      """  Total quoted material cost for the project.  """  
      self.TotQuotMtlBurCost:int = obj["TotQuotMtlBurCost"]
      """  Total quoted material burden cost for the project.  """  
      self.TotEstBurCost:int = obj["TotEstBurCost"]
      """  Total estimated burden costs for the project  """  
      self.TotQuotBurCost:int = obj["TotQuotBurCost"]
      """  Total quoted burden cost for the project. This will be both production and setup.  """  
      self.RevenueRecAutoToDate:int = obj["RevenueRecAutoToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  """  
      self.MaterialRecAutoCstTodate:int = obj["MaterialRecAutoCstTodate"]
      """  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.LaborRecAutoCstTodate:int = obj["LaborRecAutoCstTodate"]
      """  The labor costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.BurdenRecAutoCstTodate:int = obj["BurdenRecAutoCstTodate"]
      """  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.MtlBurdenRecAutoCstTodate:int = obj["MtlBurdenRecAutoCstTodate"]
      """  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  """  
      self.BudTotLbrHours:int = obj["BudTotLbrHours"]
      """  Total budget labour hours for the Project  """  
      self.BudTotBurHrs:int = obj["BudTotBurHrs"]
      """  Total budget burden hours for the Project  """  
      self.BudTotLbrCost:int = obj["BudTotLbrCost"]
      """  Total budget labour cost for the Project. This is production and setup combined.  """  
      self.BudTotBurCost:int = obj["BudTotBurCost"]
      """  Total budget burden cost for the Project. This is production and setup combined.  """  
      self.BudTotSubCost:int = obj["BudTotSubCost"]
      """  Total budget subcontract costs for the Project  """  
      self.BudTotMtlCost:int = obj["BudTotMtlCost"]
      """  Total budget material costs for the Project  """  
      self.BudTotMtlBurCost:int = obj["BudTotMtlBurCost"]
      """  Total budget material burden costs for the Project phase.  """  
      self.TotEstMtlBurCost:int = obj["TotEstMtlBurCost"]
      """  Total estimated material burden costs for the Project phase  """  
      self.SubConRecAutoCstTodate:int = obj["SubConRecAutoCstTodate"]
      """  The subcontract costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  """  
      self.RevenueRecManToDate:int = obj["RevenueRecManToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  """  
      self.MaterialRecManCstTodate:int = obj["MaterialRecManCstTodate"]
      """  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.LaborRecManCstTodate:int = obj["LaborRecManCstTodate"]
      """  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.BurdenRecManCstTodate:int = obj["BurdenRecManCstTodate"]
      """  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  """  
      self.SubConRecManCstTodate:int = obj["SubConRecManCstTodate"]
      """  The subcontract costs posted to cost of sales to date. This is cost that has been manually recognised using this process  """  
      self.MtlBurdenRecManCstTodate:int = obj["MtlBurdenRecManCstTodate"]
      """  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.MaterialCostOfSales:int = obj["MaterialCostOfSales"]
      """  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  """  
      self.LaborCostOfSales:int = obj["LaborCostOfSales"]
      """  The labor costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  """  
      self.BurdenCostOfSales:int = obj["BurdenCostOfSales"]
      """  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  """  
      self.SubConCostOfSales:int = obj["SubConCostOfSales"]
      """  The subcontract costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActSubContractCost  """  
      self.MtlBurdenCostOfSales:int = obj["MtlBurdenCostOfSales"]
      """  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  """  
      self.TotQuotODCCost:int = obj["TotQuotODCCost"]
      """  Other Direct Cost Quoted  """  
      self.TotEstODCCost:int = obj["TotEstODCCost"]
      """  Other Direct Cost Estimated  """  
      self.TotActODCCost:int = obj["TotActODCCost"]
      """  ODC Actual  """  
      self.ManEstCTCODCCost:int = obj["ManEstCTCODCCost"]
      """  Other direct cost manual CTC  """  
      self.TotCTCODCCost:int = obj["TotCTCODCCost"]
      """  Other direct Cost total CTC  """  
      self.BudTotODCCost:int = obj["BudTotODCCost"]
      """  Other direct Cost Budget Total  """  
      self.ODCRecAutoCstToDate:int = obj["ODCRecAutoCstToDate"]
      """  Other Direct cost Recognition to Date  """  
      self.ODCRecManCstTodate:int = obj["ODCRecManCstTodate"]
      """  Other Direct Cost Manual Recognition to Date  """  
      self.EstODCCost:int = obj["EstODCCost"]
      """  Estimated other direct cost  """  
      self.BdnRecSeqPosted:int = obj["BdnRecSeqPosted"]
      """  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  """  
      self.BdnRecSeqLastAdded:int = obj["BdnRecSeqLastAdded"]
      """  Number of Recalculation of burden amounts created by Revenue Recognition process  """  
      self.BdnRevenueAutoToday:int = obj["BdnRevenueAutoToday"]
      """  Sum of all Actual Burden Charges posted by today  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  AsOfDate  """  
      self.BuildAnalysis:bool = obj["BuildAnalysis"]
      """  BuildAnalysis  """  
      self.LbrPur:int = obj["LbrPur"]
      """  LbrPur  """  
      self.BurPur:int = obj["BurPur"]
      """  BurPur  """  
      self.MtlPur:int = obj["MtlPur"]
      """  MtlPur  """  
      self.SubPur:int = obj["SubPur"]
      """  SubPur  """  
      self.MtlBurPur:int = obj["MtlBurPur"]
      """  MtlBurPur  """  
      self.ODCPur:int = obj["ODCPur"]
      """  ODCPur  """  
      self.LaborLbrCstToDate:int = obj["LaborLbrCstToDate"]
      """  LaborLbrCstToDate  """  
      self.BurdenLbrCstToDate:int = obj["BurdenLbrCstToDate"]
      """  BurdenLbrCstToDate  """  
      self.ActMtlNonJobCost:int = obj["ActMtlNonJobCost"]
      """  ActMtlNonJobCost  """  
      self.RecManPosted:int = obj["RecManPosted"]
      """  RecManPosted  """  
      self.LbrManPosted:int = obj["LbrManPosted"]
      """  LbrManPosted  """  
      self.BurManPosted:int = obj["BurManPosted"]
      """  BurManPosted  """  
      self.MtlManPosted:int = obj["MtlManPosted"]
      """  MtlManPosted  """  
      self.SubCManPosted:int = obj["SubCManPosted"]
      """  SubCManPosted  """  
      self.MtlBurManPosted:int = obj["MtlBurManPosted"]
      """  MtlBurManPosted  """  
      self.ODCManPosted:int = obj["ODCManPosted"]
      """  ODCManPosted  """  
      self.Reverse:str = obj["Reverse"]
      """  Reverse  """  
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      """  NextTmpInvcNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PercentageOfCompletion:int = obj["PercentageOfCompletion"]
      """  Percentage of Completion  """  
      self.ToBeRecognizedLbrCost:int = obj["ToBeRecognizedLbrCost"]
      """  Labor Cost To Be Recognized  """  
      self.ToBeRecognizedBurCost:int = obj["ToBeRecognizedBurCost"]
      """  Burden Cost To Be Recognized  """  
      self.ToBeRecognizedMtlCost:int = obj["ToBeRecognizedMtlCost"]
      """  Material Cost To Be Recognized  """  
      self.ToBeRecognizedSubCost:int = obj["ToBeRecognizedSubCost"]
      """  Subcontract Cost To Be Recognized  """  
      self.ToBeRecognizedMtlBurCost:int = obj["ToBeRecognizedMtlBurCost"]
      """  Material Burden Cost To Be Recognized  """  
      self.ToBeRecognizedODCCost:int = obj["ToBeRecognizedODCCost"]
      """  ODC Cost To Be Recognized  """  
      self.ToBeRecognizedRevenue:int = obj["ToBeRecognizedRevenue"]
      """  Revenue To Be Recognized  """  
      self.BillingToDate:int = obj["BillingToDate"]
      """  BillingToDate  """  
      self.RecogToDtBilling:int = obj["RecogToDtBilling"]
      """  RecogToDtBilling  """  
      self.TotProjRev:int = obj["TotProjRev"]
      """  TotProjRev  """  
      self.RecogToDtLbk:int = obj["RecogToDtLbk"]
      """  RecogToDtLbk  """  
      self.RecogToDtManual:int = obj["RecogToDtManual"]
      """  RecogToDtManual  """  
      self.RetentionDt:int = obj["RetentionDt"]
      """  RetentionDt  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocBudTotBurCost:int = obj["DocBudTotBurCost"]
      self.DocBudTotLbrCost:int = obj["DocBudTotLbrCost"]
      self.DocBudTotMtlBurCost:int = obj["DocBudTotMtlBurCost"]
      self.DocBudTotMtlCost:int = obj["DocBudTotMtlCost"]
      self.DocBudTotODCCost:int = obj["DocBudTotODCCost"]
      self.DocBudTotSubCost:int = obj["DocBudTotSubCost"]
      self.DocEstBurdenCost:int = obj["DocEstBurdenCost"]
      self.DocEstLaborCost:int = obj["DocEstLaborCost"]
      self.DocEstMtlBurdenCost:int = obj["DocEstMtlBurdenCost"]
      self.DocEstMtlCost:int = obj["DocEstMtlCost"]
      self.DocEstODCCost:int = obj["DocEstODCCost"]
      self.DocEstSubcontractCost:int = obj["DocEstSubcontractCost"]
      self.DocEstTotalCost:int = obj["DocEstTotalCost"]
      self.DocGTActualCost:int = obj["DocGTActualCost"]
      self.DocGTBudgetCost:int = obj["DocGTBudgetCost"]
      self.DocGTCalculatedCost:int = obj["DocGTCalculatedCost"]
      self.DocGTEstimatedCost:int = obj["DocGTEstimatedCost"]
      self.DocGTManualCost:int = obj["DocGTManualCost"]
      self.DocGTQuotedCost:int = obj["DocGTQuotedCost"]
      self.DocProjectedTotalBurCost:int = obj["DocProjectedTotalBurCost"]
      self.DocProjectedTotalCost:int = obj["DocProjectedTotalCost"]
      self.DocProjectedTotalLbrCost:int = obj["DocProjectedTotalLbrCost"]
      self.DocProjectedTotalMtlBurCost:int = obj["DocProjectedTotalMtlBurCost"]
      self.DocProjectedTotalMtlCost:int = obj["DocProjectedTotalMtlCost"]
      self.DocProjectedTotalODCCost:int = obj["DocProjectedTotalODCCost"]
      self.DocProjectedTotalSubContCost:int = obj["DocProjectedTotalSubContCost"]
      self.DocTotActMtlBurCost:int = obj["DocTotActMtlBurCost"]
      self.DocTotActMtlCost:int = obj["DocTotActMtlCost"]
      self.DocTotActODCCost:int = obj["DocTotActODCCost"]
      self.DocTotActSubContCost:int = obj["DocTotActSubContCost"]
      self.DocTotCtcBurCost:int = obj["DocTotCtcBurCost"]
      self.DocTotCtcLbrCost:int = obj["DocTotCtcLbrCost"]
      self.DocTotCtcMtlBurCost:int = obj["DocTotCtcMtlBurCost"]
      self.DocTotCtcMtlCost:int = obj["DocTotCtcMtlCost"]
      self.DocTotCTCODCCost:int = obj["DocTotCTCODCCost"]
      self.DocTotCtcSubConCost:int = obj["DocTotCtcSubConCost"]
      self.DocTotEstBurCost:int = obj["DocTotEstBurCost"]
      self.DocTotEstLbrCost:int = obj["DocTotEstLbrCost"]
      self.DocTotEstMtlBurCost:int = obj["DocTotEstMtlBurCost"]
      self.DocTotEstMtlCost:int = obj["DocTotEstMtlCost"]
      self.DocTotEstODCCost:int = obj["DocTotEstODCCost"]
      self.DocTotEstSubContCost:int = obj["DocTotEstSubContCost"]
      self.DocTotQuotBurCost:int = obj["DocTotQuotBurCost"]
      self.DocTotQuotLbrCost:int = obj["DocTotQuotLbrCost"]
      self.DocTotQuotMtlBurCost:int = obj["DocTotQuotMtlBurCost"]
      self.DocTotQuotMtlCost:int = obj["DocTotQuotMtlCost"]
      self.DocTotQuotODCCost:int = obj["DocTotQuotODCCost"]
      self.DocTotQuotSubContCost:int = obj["DocTotQuotSubContCost"]
      self.EstTotalCost:int = obj["EstTotalCost"]
      """  This is a calculated field: the sum of the other Project.Est*Cost fields.  It is not stored in the database.  """  
      self.GTActualCost:int = obj["GTActualCost"]
      self.GTBudgetCost:int = obj["GTBudgetCost"]
      self.GTCalculatedCost:int = obj["GTCalculatedCost"]
      self.GTEstimatedCost:int = obj["GTEstimatedCost"]
      self.GTManualCost:int = obj["GTManualCost"]
      self.GTQuotedCost:int = obj["GTQuotedCost"]
      self.ProjectedTotalBurCost:int = obj["ProjectedTotalBurCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalCost:int = obj["ProjectedTotalCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalLbrCost:int = obj["ProjectedTotalLbrCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalMtlBurCost:int = obj["ProjectedTotalMtlBurCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalMtlCost:int = obj["ProjectedTotalMtlCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalODCCost:int = obj["ProjectedTotalODCCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalSubContCost:int = obj["ProjectedTotalSubContCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ReconToDtBilling:int = obj["ReconToDtBilling"]
      """  Recognized to Date Billing  """  
      self.Rpt1BudTotBurCost:int = obj["Rpt1BudTotBurCost"]
      self.Rpt1BudTotLbrCost:int = obj["Rpt1BudTotLbrCost"]
      self.Rpt1BudTotMtlBurCost:int = obj["Rpt1BudTotMtlBurCost"]
      self.Rpt1BudTotMtlCost:int = obj["Rpt1BudTotMtlCost"]
      self.Rpt1BudTotODCCost:int = obj["Rpt1BudTotODCCost"]
      self.Rpt1BudTotSubCost:int = obj["Rpt1BudTotSubCost"]
      self.Rpt1EstBurdenCost:int = obj["Rpt1EstBurdenCost"]
      self.Rpt1EstLaborCost:int = obj["Rpt1EstLaborCost"]
      self.Rpt1EstMtlBurdenCost:int = obj["Rpt1EstMtlBurdenCost"]
      self.Rpt1EstMtlCost:int = obj["Rpt1EstMtlCost"]
      self.Rpt1EstODCCost:int = obj["Rpt1EstODCCost"]
      self.Rpt1EstSubcontractCost:int = obj["Rpt1EstSubcontractCost"]
      self.Rpt1EstTotalCost:int = obj["Rpt1EstTotalCost"]
      self.Rpt1GTActualCost:int = obj["Rpt1GTActualCost"]
      self.Rpt1GTBudgetCost:int = obj["Rpt1GTBudgetCost"]
      self.Rpt1GTCalculatedCost:int = obj["Rpt1GTCalculatedCost"]
      self.Rpt1GTEstimatedCost:int = obj["Rpt1GTEstimatedCost"]
      self.Rpt1GTManualCost:int = obj["Rpt1GTManualCost"]
      self.Rpt1GTQuotedCost:int = obj["Rpt1GTQuotedCost"]
      self.Rpt1ManEstCtcBurCost:int = obj["Rpt1ManEstCtcBurCost"]
      self.Rpt1ManEstCtcLbrCost:int = obj["Rpt1ManEstCtcLbrCost"]
      self.Rpt1ManEstCtcMtlBurCost:int = obj["Rpt1ManEstCtcMtlBurCost"]
      self.Rpt1ManEstCtcMtlCost:int = obj["Rpt1ManEstCtcMtlCost"]
      self.Rpt1ManEstCTCODCCost:int = obj["Rpt1ManEstCTCODCCost"]
      self.Rpt1ManEstCtcSubConCost:int = obj["Rpt1ManEstCtcSubConCost"]
      self.Rpt1ProjectedTotalBurCost:int = obj["Rpt1ProjectedTotalBurCost"]
      self.Rpt1ProjectedTotalCost:int = obj["Rpt1ProjectedTotalCost"]
      self.Rpt1ProjectedTotalLbrCost:int = obj["Rpt1ProjectedTotalLbrCost"]
      self.Rpt1ProjectedTotalMtlBurCost:int = obj["Rpt1ProjectedTotalMtlBurCost"]
      self.Rpt1ProjectedTotalMtlCost:int = obj["Rpt1ProjectedTotalMtlCost"]
      self.Rpt1ProjectedTotalODCCost:int = obj["Rpt1ProjectedTotalODCCost"]
      self.Rpt1ProjectedTotalSubContCost:int = obj["Rpt1ProjectedTotalSubContCost"]
      self.Rpt1TotActBurCost:int = obj["Rpt1TotActBurCost"]
      self.Rpt1TotActLbrCost:int = obj["Rpt1TotActLbrCost"]
      self.Rpt1TotActMtlBurCost:int = obj["Rpt1TotActMtlBurCost"]
      self.Rpt1TotActMtlCost:int = obj["Rpt1TotActMtlCost"]
      self.Rpt1TotActODCCost:int = obj["Rpt1TotActODCCost"]
      self.Rpt1TotActSubContCost:int = obj["Rpt1TotActSubContCost"]
      self.Rpt1TotCtcBurCost:int = obj["Rpt1TotCtcBurCost"]
      self.Rpt1TotCtcLbrCost:int = obj["Rpt1TotCtcLbrCost"]
      self.Rpt1TotCtcMtlBurCost:int = obj["Rpt1TotCtcMtlBurCost"]
      self.Rpt1TotCtcMtlCost:int = obj["Rpt1TotCtcMtlCost"]
      self.Rpt1TotCTCODCCost:int = obj["Rpt1TotCTCODCCost"]
      self.Rpt1TotCtcSubConCost:int = obj["Rpt1TotCtcSubConCost"]
      self.Rpt1TotEstBurCost:int = obj["Rpt1TotEstBurCost"]
      self.Rpt1TotEstLbrCost:int = obj["Rpt1TotEstLbrCost"]
      self.Rpt1TotEstMtlBurCost:int = obj["Rpt1TotEstMtlBurCost"]
      self.Rpt1TotEstMtlCost:int = obj["Rpt1TotEstMtlCost"]
      self.Rpt1TotEstODCCost:int = obj["Rpt1TotEstODCCost"]
      self.Rpt1TotEstSubContCost:int = obj["Rpt1TotEstSubContCost"]
      self.Rpt1TotQuotBurCost:int = obj["Rpt1TotQuotBurCost"]
      self.Rpt1TotQuotLbrCost:int = obj["Rpt1TotQuotLbrCost"]
      self.Rpt1TotQuotMtlBurCost:int = obj["Rpt1TotQuotMtlBurCost"]
      self.Rpt1TotQuotMtlCost:int = obj["Rpt1TotQuotMtlCost"]
      self.Rpt1TotQuotODCCost:int = obj["Rpt1TotQuotODCCost"]
      self.Rpt1TotQuotSubContCost:int = obj["Rpt1TotQuotSubContCost"]
      self.Rpt2BudTotBurCost:int = obj["Rpt2BudTotBurCost"]
      self.Rpt2BudTotLbrCost:int = obj["Rpt2BudTotLbrCost"]
      self.Rpt2BudTotMtlBurCost:int = obj["Rpt2BudTotMtlBurCost"]
      self.Rpt2BudTotMtlCost:int = obj["Rpt2BudTotMtlCost"]
      self.Rpt2BudTotODCCost:int = obj["Rpt2BudTotODCCost"]
      self.Rpt2BudTotSubCost:int = obj["Rpt2BudTotSubCost"]
      self.Rpt2EstBurdenCost:int = obj["Rpt2EstBurdenCost"]
      self.Rpt2EstLaborCost:int = obj["Rpt2EstLaborCost"]
      self.Rpt2EstMtlBurdenCost:int = obj["Rpt2EstMtlBurdenCost"]
      self.Rpt2EstMtlCost:int = obj["Rpt2EstMtlCost"]
      self.Rpt2EstODCCost:int = obj["Rpt2EstODCCost"]
      self.Rpt2EstSubcontractCost:int = obj["Rpt2EstSubcontractCost"]
      self.Rpt2EstTotalCost:int = obj["Rpt2EstTotalCost"]
      self.Rpt2GTActualCost:int = obj["Rpt2GTActualCost"]
      self.Rpt2GTBudgetCost:int = obj["Rpt2GTBudgetCost"]
      self.Rpt2GTCalculatedCost:int = obj["Rpt2GTCalculatedCost"]
      self.Rpt2GTEstimatedCost:int = obj["Rpt2GTEstimatedCost"]
      self.Rpt2GTManualCost:int = obj["Rpt2GTManualCost"]
      self.Rpt2GTQuotedCost:int = obj["Rpt2GTQuotedCost"]
      self.Rpt2ManEstCtcBurCost:int = obj["Rpt2ManEstCtcBurCost"]
      self.Rpt2ManEstCtcLbrCost:int = obj["Rpt2ManEstCtcLbrCost"]
      self.Rpt2ManEstCtcMtlBurCost:int = obj["Rpt2ManEstCtcMtlBurCost"]
      self.Rpt2ManEstCtcMtlCost:int = obj["Rpt2ManEstCtcMtlCost"]
      self.Rpt2ManEstCTCODCCost:int = obj["Rpt2ManEstCTCODCCost"]
      self.Rpt2ManEstCtcSubConCost:int = obj["Rpt2ManEstCtcSubConCost"]
      self.Rpt2ProjectedTotalBurCost:int = obj["Rpt2ProjectedTotalBurCost"]
      self.Rpt2ProjectedTotalCost:int = obj["Rpt2ProjectedTotalCost"]
      self.Rpt2ProjectedTotalLbrCost:int = obj["Rpt2ProjectedTotalLbrCost"]
      self.Rpt2ProjectedTotalMtlBurCost:int = obj["Rpt2ProjectedTotalMtlBurCost"]
      self.Rpt2ProjectedTotalMtlCost:int = obj["Rpt2ProjectedTotalMtlCost"]
      self.Rpt2ProjectedTotalODCCost:int = obj["Rpt2ProjectedTotalODCCost"]
      self.Rpt2ProjectedTotalSubContCost:int = obj["Rpt2ProjectedTotalSubContCost"]
      self.Rpt2TotActBurCost:int = obj["Rpt2TotActBurCost"]
      self.Rpt2TotActLbrCost:int = obj["Rpt2TotActLbrCost"]
      self.Rpt2TotActMtlBurCost:int = obj["Rpt2TotActMtlBurCost"]
      self.Rpt2TotActMtlCost:int = obj["Rpt2TotActMtlCost"]
      self.Rpt2TotActODCCost:int = obj["Rpt2TotActODCCost"]
      self.Rpt2TotActSubContCost:int = obj["Rpt2TotActSubContCost"]
      self.Rpt2TotCtcBurCost:int = obj["Rpt2TotCtcBurCost"]
      self.Rpt2TotCtcLbrCost:int = obj["Rpt2TotCtcLbrCost"]
      self.Rpt2TotCtcMtlBurCost:int = obj["Rpt2TotCtcMtlBurCost"]
      self.Rpt2TotCtcMtlCost:int = obj["Rpt2TotCtcMtlCost"]
      self.Rpt2TotCTCODCCost:int = obj["Rpt2TotCTCODCCost"]
      self.Rpt2TotCtcSubConCost:int = obj["Rpt2TotCtcSubConCost"]
      self.Rpt2TotEstBurCost:int = obj["Rpt2TotEstBurCost"]
      self.Rpt2TotEstLbrCost:int = obj["Rpt2TotEstLbrCost"]
      self.Rpt2TotEstMtlBurCost:int = obj["Rpt2TotEstMtlBurCost"]
      self.Rpt2TotEstMtlCost:int = obj["Rpt2TotEstMtlCost"]
      self.Rpt2TotEstODCCost:int = obj["Rpt2TotEstODCCost"]
      self.Rpt2TotEstSubContCost:int = obj["Rpt2TotEstSubContCost"]
      self.Rpt2TotQuotBurCost:int = obj["Rpt2TotQuotBurCost"]
      self.Rpt2TotQuotLbrCost:int = obj["Rpt2TotQuotLbrCost"]
      self.Rpt2TotQuotMtlBurCost:int = obj["Rpt2TotQuotMtlBurCost"]
      self.Rpt2TotQuotMtlCost:int = obj["Rpt2TotQuotMtlCost"]
      self.Rpt2TotQuotODCCost:int = obj["Rpt2TotQuotODCCost"]
      self.Rpt2TotQuotSubContCost:int = obj["Rpt2TotQuotSubContCost"]
      self.Rpt3BudTotBurCost:int = obj["Rpt3BudTotBurCost"]
      self.Rpt3BudTotLbrCost:int = obj["Rpt3BudTotLbrCost"]
      self.Rpt3BudTotMtlBurCost:int = obj["Rpt3BudTotMtlBurCost"]
      self.Rpt3BudTotMtlCost:int = obj["Rpt3BudTotMtlCost"]
      self.Rpt3BudTotODCCost:int = obj["Rpt3BudTotODCCost"]
      self.Rpt3BudTotSubCost:int = obj["Rpt3BudTotSubCost"]
      self.Rpt3EstBurdenCost:int = obj["Rpt3EstBurdenCost"]
      self.Rpt3EstLaborCost:int = obj["Rpt3EstLaborCost"]
      self.Rpt3EstMtlBurdenCost:int = obj["Rpt3EstMtlBurdenCost"]
      self.Rpt3EstMtlCost:int = obj["Rpt3EstMtlCost"]
      self.Rpt3EstODCCost:int = obj["Rpt3EstODCCost"]
      self.Rpt3EstSubcontractCost:int = obj["Rpt3EstSubcontractCost"]
      self.Rpt3EstTotalCost:int = obj["Rpt3EstTotalCost"]
      self.Rpt3GTActualCost:int = obj["Rpt3GTActualCost"]
      self.Rpt3GTBudgetCost:int = obj["Rpt3GTBudgetCost"]
      self.Rpt3GTCalculatedCost:int = obj["Rpt3GTCalculatedCost"]
      self.Rpt3GTEstimatedCost:int = obj["Rpt3GTEstimatedCost"]
      self.Rpt3GTManualCost:int = obj["Rpt3GTManualCost"]
      self.Rpt3GTQuotedCost:int = obj["Rpt3GTQuotedCost"]
      self.Rpt3ManEstCtcBurCost:int = obj["Rpt3ManEstCtcBurCost"]
      self.Rpt3ManEstCtcLbrCost:int = obj["Rpt3ManEstCtcLbrCost"]
      self.Rpt3ManEstCtcMtlBurCost:int = obj["Rpt3ManEstCtcMtlBurCost"]
      self.Rpt3ManEstCtcMtlCost:int = obj["Rpt3ManEstCtcMtlCost"]
      self.Rpt3ManEstCTCODCCost:int = obj["Rpt3ManEstCTCODCCost"]
      self.Rpt3ManEstCtcSubConCost:int = obj["Rpt3ManEstCtcSubConCost"]
      self.Rpt3ProjectedTotalBurCost:int = obj["Rpt3ProjectedTotalBurCost"]
      self.Rpt3ProjectedTotalCost:int = obj["Rpt3ProjectedTotalCost"]
      self.Rpt3ProjectedTotalLbrCost:int = obj["Rpt3ProjectedTotalLbrCost"]
      self.Rpt3ProjectedTotalMtlBurCost:int = obj["Rpt3ProjectedTotalMtlBurCost"]
      self.Rpt3ProjectedTotalMtlCost:int = obj["Rpt3ProjectedTotalMtlCost"]
      self.Rpt3ProjectedTotalODCCost:int = obj["Rpt3ProjectedTotalODCCost"]
      self.Rpt3ProjectedTotalSubContCost:int = obj["Rpt3ProjectedTotalSubContCost"]
      self.Rpt3TotActBurCost:int = obj["Rpt3TotActBurCost"]
      self.Rpt3TotActLbrCost:int = obj["Rpt3TotActLbrCost"]
      self.Rpt3TotActMtlBurCost:int = obj["Rpt3TotActMtlBurCost"]
      self.Rpt3TotActMtlCost:int = obj["Rpt3TotActMtlCost"]
      self.Rpt3TotActODCCost:int = obj["Rpt3TotActODCCost"]
      self.Rpt3TotActSubContCost:int = obj["Rpt3TotActSubContCost"]
      self.Rpt3TotCtcBurCost:int = obj["Rpt3TotCtcBurCost"]
      self.Rpt3TotCtcLbrCost:int = obj["Rpt3TotCtcLbrCost"]
      self.Rpt3TotCtcMtlBurCost:int = obj["Rpt3TotCtcMtlBurCost"]
      self.Rpt3TotCtcMtlCost:int = obj["Rpt3TotCtcMtlCost"]
      self.Rpt3TotCTCODCCost:int = obj["Rpt3TotCTCODCCost"]
      self.Rpt3TotCtcSubConCost:int = obj["Rpt3TotCtcSubConCost"]
      self.Rpt3TotEstBurCost:int = obj["Rpt3TotEstBurCost"]
      self.Rpt3TotEstLbrCost:int = obj["Rpt3TotEstLbrCost"]
      self.Rpt3TotEstMtlBurCost:int = obj["Rpt3TotEstMtlBurCost"]
      self.Rpt3TotEstMtlCost:int = obj["Rpt3TotEstMtlCost"]
      self.Rpt3TotEstODCCost:int = obj["Rpt3TotEstODCCost"]
      self.Rpt3TotEstSubContCost:int = obj["Rpt3TotEstSubContCost"]
      self.Rpt3TotQuotBurCost:int = obj["Rpt3TotQuotBurCost"]
      self.Rpt3TotQuotLbrCost:int = obj["Rpt3TotQuotLbrCost"]
      self.Rpt3TotQuotMtlBurCost:int = obj["Rpt3TotQuotMtlBurCost"]
      self.Rpt3TotQuotMtlCost:int = obj["Rpt3TotQuotMtlCost"]
      self.Rpt3TotQuotODCCost:int = obj["Rpt3TotQuotODCCost"]
      self.Rpt3TotQuotSubContCost:int = obj["Rpt3TotQuotSubContCost"]
      self.DocManEstCtcBurCost:int = obj["DocManEstCtcBurCost"]
      self.DocManEstCtcLbrCost:int = obj["DocManEstCtcLbrCost"]
      self.DocManEstCtcMtlBurCost:int = obj["DocManEstCtcMtlBurCost"]
      self.DocManEstCtcMtlCost:int = obj["DocManEstCtcMtlCost"]
      self.DocManEstCTCODCCost:int = obj["DocManEstCTCODCCost"]
      self.DocManEstCtcSubConCost:int = obj["DocManEstCtcSubConCost"]
      self.DocTotActBurCost:int = obj["DocTotActBurCost"]
      self.DocTotActLbrCost:int = obj["DocTotActLbrCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   projectID
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_ProjFilterRow:
   def __init__(self, obj):
      self.ContractAmtFrom:int = obj["ContractAmtFrom"]
      self.ContractAmtTo:int = obj["ContractAmtTo"]
      self.CustomerName:str = obj["CustomerName"]
      self.Description:str = obj["Description"]
      self.ProjectIDFrom:str = obj["ProjectIDFrom"]
      self.ProjectIDTo:str = obj["ProjectIDTo"]
      self.ProjectManagerID:str = obj["ProjectManagerID"]
      self.Selected:bool = obj["Selected"]
      self.StartDateFrom:str = obj["StartDateFrom"]
      self.StartDateTo:str = obj["StartDateTo"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjFilterTableset:
   def __init__(self, obj):
      self.ProjFilter:list[Erp_Tablesets_ProjFilterRow] = obj["ProjFilter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjMultiListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Description:str = obj["Description"]
      """  Full description of Project Management Code.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date of the project  """  
      self.ConCustNum:int = obj["ConCustNum"]
      """  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  """  
      self.ConProjMgr:str = obj["ConProjMgr"]
      """  Employee ID of the person who has responsibility for the project  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.LastAction:str = obj["LastAction"]
      """  Last action performed on Project as relates to revenue recognition.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  Date when the LastAction happened to the Project.  """  
      self.Approved:bool = obj["Approved"]
      self.Selected:bool = obj["Selected"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProjMultiListTableset:
   def __init__(self, obj):
      self.ProjMultiList:list[Erp_Tablesets_ProjMultiListRow] = obj["ProjMultiList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjMultiRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.Description:str = obj["Description"]
      """  Full description of Project Management Code.  """  
      self.ActiveProject:bool = obj["ActiveProject"]
      """  Indicates if this Project is active.  Can be changed directly by the user during entry.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for project comments.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.UserMap:str = obj["UserMap"]
      """  Will contain the coma separated list of the fields that the user has added to the project from within Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Holds the default project warehouse code.  """  
      self.BinNum:str = obj["BinNum"]
      """  Holds the default project bin code.  """  
      self.PrimaryJob:str = obj["PrimaryJob"]
      """  This holds the top level job to which all of the jobs created for a WBS Phase will be associated  """  
      self.PrimaryMtl:int = obj["PrimaryMtl"]
      """  This is the material placeholder in the primary project job to which all WBS Phase jobs will be linked.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  The sales category code used in the Revenue recognition process.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  The Product Group code used in the Revenue Recognition process.  """  
      self.CloseAccrual:bool = obj["CloseAccrual"]
      """  RESERVED FOR FUTURE USE: Logical field. When set to true it indicates that the journals created to recognise the revenue for the project have been reversed.  """  
      self.PrimaryAsmSeq:int = obj["PrimaryAsmSeq"]
      """  Assembly Seq from JobAsmbl record.  """  
      self.StartDate:str = obj["StartDate"]
      """  Start Date of the project  """  
      self.ConCustNum:int = obj["ConCustNum"]
      """  A  unique integer assigned by the system to new customers by Contract customer number. This field can be blank.  """  
      self.ConStartDate:str = obj["ConStartDate"]
      """  Contract start date  """  
      self.ConEndDate:str = obj["ConEndDate"]
      """  Date the contract is due to be complete  """  
      self.ConProjectedEnd:str = obj["ConProjectedEnd"]
      """  Projected Contract End Date. Defaults to the Contract End Date but can be used to report on the projected end date.  """  
      self.ConReference:str = obj["ConReference"]
      """   Contract Reference number for project.
At the Epicor 9.05 release this field is reference only, at the Epicor 9.1 release when the whole contract system is enhanced then this field will reference an actual contract and a search will be provided.  """  
      self.ConProjMgr:str = obj["ConProjMgr"]
      """  Employee ID of the person who has responsibility for the project  """  
      self.ConTotValue:int = obj["ConTotValue"]
      """  Total contract value for the project.  """  
      self.ConTotInv:int = obj["ConTotInv"]
      """  Value of the posted invoices to date (system field)  """  
      self.ConInvMeth:str = obj["ConInvMeth"]
      """   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
?CP? = Cost Plus
The default is Customer Shipment.  """  
      self.MarkUpID:str = obj["MarkUpID"]
      """  Foreign key to the QMarkUp  """  
      self.PBLbMarkUp:int = obj["PBLbMarkUp"]
      """  Override of Labor Markup Percent  """  
      self.PBMtlMarkUp:int = obj["PBMtlMarkUp"]
      """  Override of Material Markup Percent  """  
      self.PBSubMarkUp:int = obj["PBSubMarkUp"]
      """  Override of Subcontract Markup Percentage  """  
      self.PBMiscMarkUp:int = obj["PBMiscMarkUp"]
      """  Override of Other Direct Cost Markup %  """  
      self.PBRetentionPcnt:int = obj["PBRetentionPcnt"]
      """  Retention percentage. How this is used is dependent on RetentionProc field.  """  
      self.PBRetentionProc:str = obj["PBRetentionProc"]
      """   How the retention percentage will be used.
The options are ?M? = Maximum of Contract Value
?P? = Percent of Invoice Value.  """  
      self.PBFeeProject:int = obj["PBFeeProject"]
      """  Project Fee  """  
      self.PBFeeApply:str = obj["PBFeeApply"]
      """  Apply Fee with list of the options: F =  First Invoice Only, A = All Invoices  """  
      self.PBFeeType:str = obj["PBFeeType"]
      """  Fee Type with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeApplyOn:str = obj["PBFeeApplyOn"]
      """  Apply Fees on list with the options: N = Net Cost, G = Gross Cost.  """  
      self.PBFeeInvoiceText:str = obj["PBFeeInvoiceText"]
      """  Fee Invoice Text in Free format to allow the user to enter text that will be displayed on the invoice  """  
      self.PBFeeLbrCharge:int = obj["PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice  """  
      self.PBFeeLbrType:str = obj["PBFeeLbrType"]
      """  Labor Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeLbrApply:str = obj["PBFeeLbrApply"]
      """  Labor Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMtlCharge:int = obj["PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice  """  
      self.PBFeeMtlType:str = obj["PBFeeMtlType"]
      """  Material Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeMtlApply:str = obj["PBFeeMtlApply"]
      """  Material Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeSubCharge:int = obj["PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice.  """  
      self.PBFeeSubType:str = obj["PBFeeSubType"]
      """  Subcontract Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeSubApply:str = obj["PBFeeSubApply"]
      """  Subcontract Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.PBFeeMiscCharge:int = obj["PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice.  """  
      self.PBFeeMiscType:str = obj["PBFeeMiscType"]
      """  Miscellaneous Fee Type of with list of the options: P = Percentage, F = Fixed Amount  """  
      self.PBFeeMiscApply:str = obj["PBFeeMiscApply"]
      """  Miscellaneous Fee Apply on  with list of options F = First Invoice Only, A = All Invoices.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.ConBTCustNum:int = obj["ConBTCustNum"]
      """  Contract Customer Bill To number, foreign key to Customer  """  
      self.ConOverCeiling:bool = obj["ConOverCeiling"]
      """  If invoices are allowed to be generated even if the element is over the predefined ceiling.  """  
      self.ConRevMethod:str = obj["ConRevMethod"]
      """  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  """  
      self.ConListCode:str = obj["ConListCode"]
      """  Price list is used to establish the price for any materials when the invoicing method is set to T & M or Cost Plus. Can be empty.  """  
      self.ConHrsInvc:str = obj["ConHrsInvc"]
      """  Hours for Invoicing allows the user to decide which hours are to be used by the invoicing process, it has system list with the options: L =  Labor, B = Burden  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type Code  """  
      self.LockRate:bool = obj["LockRate"]
      """  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange rate that will be used for this role code entry.  Defaults from CurrRate.CurrentRate  """  
      self.EndDate:str = obj["EndDate"]
      """  This is the projected end date of the project but is not required and is only used if entered in the creation of the project job and for any user reporting requirements.  """  
      self.PBPrjRtSrc:str = obj["PBPrjRtSrc"]
      """  Defaults from JCSyst.DfltPrjRtSrc. Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  """  
      self.DocConTotInv:int = obj["DocConTotInv"]
      """  Value of the posted invoices to date (system field) in the Project currency  """  
      self.CreatePrjJob:bool = obj["CreatePrjJob"]
      """  If set to true a new primary job will be created automatically for the project.  """  
      self.Rpt1ConTotInv:int = obj["Rpt1ConTotInv"]
      """  Value of the posted invoices to date (system field) in the Reporting currency  """  
      self.Revision:int = obj["Revision"]
      """  Project revision number  """  
      self.Rpt2ConTotInv:int = obj["Rpt2ConTotInv"]
      """  Value of the posted invoices to date (system field) in the Reporting currency  """  
      self.PPAllowPcnt:int = obj["PPAllowPcnt"]
      """   This is the percentage of the costs for material, labor and burden that will be invoiced.
This is also used by the invoice entry process when invoicing regular shipments to determine the actual value of the invoice and how much will be relieved from the Progress Payments to date.  """  
      self.Rpt3ConTotInv:int = obj["Rpt3ConTotInv"]
      """  Value of the posted invoices to date (system field) in the Reporting currency  """  
      self.HoldPrdInv:bool = obj["HoldPrdInv"]
      """   This will allow regular shipments to be invoiced normally.
Setting the field to true will cause the Customer Shipment process to place any packing slips for any sales order associated with the project to be placed on hold to prevent them being selected for invoicing. 
When the user changes this flag to true it will trigger business logic that will release the shipments for invoicing.  """  
      self.DocConTotValue:int = obj["DocConTotValue"]
      """  Total contract value for the project. in the Project currency  """  
      self.PPActive:bool = obj["PPActive"]
      """   This will default to true which will then trigger the Invoice Preparation process to produce a Progress Payment Invoice.
Setting this to false will cause the project to be ignored by the Invoice Preparation process.  """  
      self.Rpt1ConTotValue:int = obj["Rpt1ConTotValue"]
      """  Total contract value for the project. in the Reporting currency  """  
      self.Rpt2ConTotValue:int = obj["Rpt2ConTotValue"]
      """  Total contract value for the project. in the Reporting currency  """  
      self.TotLiqToDate:int = obj["TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments.  """  
      self.Rpt3ConTotValue:int = obj["Rpt3ConTotValue"]
      """  Total contract value for the project. in the Reporting currency  """  
      self.PPCeilingTotal:int = obj["PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then  """  
      self.DocPBFeeLbrCharge:int = obj["DocPBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Project currency  """  
      self.Rpt1PBFeeLbrCharge:int = obj["Rpt1PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  """  
      self.Rpt2PBFeeLbrCharge:int = obj["Rpt2PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  """  
      self.Rpt3PBFeeLbrCharge:int = obj["Rpt3PBFeeLbrCharge"]
      """  Fee that is to be charged against any labor charges on an invoice in the Reporting currency  """  
      self.DocPBFeeMiscCharge:int = obj["DocPBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Project currency  """  
      self.Rpt1PBFeeMiscCharge:int = obj["Rpt1PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  """  
      self.Rpt2PBFeeMiscCharge:int = obj["Rpt2PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  """  
      self.Rpt3PBFeeMiscCharge:int = obj["Rpt3PBFeeMiscCharge"]
      """  Fee that is to be charged against any miscellaneous charges on an invoice. in the Reporting currency  """  
      self.DocPBFeeMtlCharge:int = obj["DocPBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Project currency  """  
      self.Rpt1PBFeeMtlCharge:int = obj["Rpt1PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Reporting currency  """  
      self.Rpt2PBFeeMtlCharge:int = obj["Rpt2PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Reporting currency  """  
      self.Rpt3PBFeeMtlCharge:int = obj["Rpt3PBFeeMtlCharge"]
      """  Fee that is to be charged against any material charges on an invoice in the Reporting currency  """  
      self.DocPBFeeSubCharge:int = obj["DocPBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Project currency  """  
      self.Rpt1PBFeeSubCharge:int = obj["Rpt1PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  """  
      self.Rpt2PBFeeSubCharge:int = obj["Rpt2PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  """  
      self.Rpt3PBFeeSubCharge:int = obj["Rpt3PBFeeSubCharge"]
      """  Fee that is to be charged against any Subcontract charges on an invoice. in the Reporting currency  """  
      self.PBIndCeilingSup:bool = obj["PBIndCeilingSup"]
      """  Allows individual ceilings to be applied to suppliers  """  
      self.PBIndCeilingEmp:bool = obj["PBIndCeilingEmp"]
      """  Allows individual ceilings to be applied to employee  """  
      self.PBIndCeilingPRole:bool = obj["PBIndCeilingPRole"]
      """  Allows individual ceilings to be applied to role  """  
      self.PBDocInvoicedMtl:int = obj["PBDocInvoicedMtl"]
      """  Material Cost invoiced by date.  """  
      self.PBDocInvoicedLbr:int = obj["PBDocInvoicedLbr"]
      """  Labor cost invoiced by date.  """  
      self.PBDocInvoicedSub:int = obj["PBDocInvoicedSub"]
      """  Subcontract cost invoiced by date.  """  
      self.PBDocInvoicedMtlBur:int = obj["PBDocInvoicedMtlBur"]
      """  Material Burden Material cost invoiced by date.  """  
      self.PBDocInvoicedMisc:int = obj["PBDocInvoicedMisc"]
      """  Other direct Costs invoiced by date.  """  
      self.PBDocInvoicedBur:int = obj["PBDocInvoicedBur"]
      """  Burden Costs invoiced by date.  """  
      self.PBDocInvoicedFees:int = obj["PBDocInvoicedFees"]
      """  Fees charged by date  """  
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      """  Next Temporary Invoice number used in the Invoice preparation table before invoice is generated  """  
      self.DocTotLiqToDate:int = obj["DocTotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Project currency  """  
      self.Rpt1TotLiqToDate:int = obj["Rpt1TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  """  
      self.Rpt2TotLiqToDate:int = obj["Rpt2TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  """  
      self.Rpt3TotLiqToDate:int = obj["Rpt3TotLiqToDate"]
      """  This is a system maintained field that reflects the value of liquidations that have taken place as part of customer shipments. in the Reporting currency  """  
      self.DocPPCeilingTotal:int = obj["DocPPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Project currency  """  
      self.Rpt1PPCeilingTotal:int = obj["Rpt1PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  """  
      self.Rpt2PPCeilingTotal:int = obj["Rpt2PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  """  
      self.Rpt3PPCeilingTotal:int = obj["Rpt3PPCeilingTotal"]
      """  If a value is entered in this field then this will be the ceiling for the overall project. Once this is reached then in the Reporting currency  """  
      self.PBOrderNum:int = obj["PBOrderNum"]
      """  Progress Billing - Order Number  """  
      self.PPOrderNum:int = obj["PPOrderNum"]
      """  Progress Payment - Order Number  """  
      self.PBOrderLine:int = obj["PBOrderLine"]
      """  Progress Billing - Order Line  """  
      self.PPOrderLine:int = obj["PPOrderLine"]
      """  Progress Payment - Order Line  """  
      self.DocPBFeeProject:int = obj["DocPBFeeProject"]
      """  Project Fee in the Project currency  """  
      self.Rpt1PBFeeProject:int = obj["Rpt1PBFeeProject"]
      """  Project Fee in the Reporting currency  """  
      self.Rpt2PBFeeProject:int = obj["Rpt2PBFeeProject"]
      """  Project Fee in the Reporting currency  """  
      self.Rpt3PBFeeProject:int = obj["Rpt3PBFeeProject"]
      """  Project Fee in the Reporting currency  """  
      self.PBClose:bool = obj["PBClose"]
      """  Set to true when the close billing has been executed. For Fixed Fee this is set only after all PBillSch are closed. For other types this is set when Close Project is executed.  """  
      self.PBTrueUp:bool = obj["PBTrueUp"]
      """  This field is set to true after the Project True Up has been executed.  """  
      self.TimeApprovalsMethod:str = obj["TimeApprovalsMethod"]
      """  Defines the Approvals Method for Time related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  """  
      self.TimeWFGroupID:str = obj["TimeWFGroupID"]
      """  Unique identifier of the workflow group for Time transactions related to this Project.  """  
      self.ExpenseApprovalsMethod:str = obj["ExpenseApprovalsMethod"]
      """  Defines the Approvals Method for Expenses related to the Project.  Valid values are E (Employee), P (Project) and A (Automatic).  If the application is configured not to require Time and Expense approvals, this value is set to Automatic.  A value set at the WBS Phase will override this value at the Project.  """  
      self.ExpenseWFGroupID:str = obj["ExpenseWFGroupID"]
      """  Unique identifier of the workflow group for Expense transactions related to this Project.  """  
      self.PBNumInvoices:int = obj["PBNumInvoices"]
      """  Number of Invoices generated for the Project  """  
      self.PBTrueUpYearList:str = obj["PBTrueUpYearList"]
      """  List of fiscal years for which True Up was called  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier  """  
      self.ConConNum:int = obj["ConConNum"]
      """  Customer Contract Number  """  
      self.MtlTaxCatID:str = obj["MtlTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  material lines. If blank the standard InvcDtl.TaxCatID defaulting will be used.  """  
      self.LbrTaxCatID:str = obj["LbrTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  labor lines.  """  
      self.FeeTaxCatID:str = obj["FeeTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  fee lines.  """  
      self.ODCTaxCatID:str = obj["ODCTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID  ODC lines. If blank use the tax category from the PurMisc misc charge code record  """  
      self.SubTaxCatID:str = obj["SubTaxCatID"]
      """  Tax Category to default for PB Invoice InvcDtl.TaxCatID Subcontract lines.  """  
      self.BdnTaxCatID:str = obj["BdnTaxCatID"]
      """  Descriptive code assigned by user which uniquely identifies a Tax Category to default for PB Invoice InvcDtl.TaxCatID  Burden lines.  """  
      self.TaxOnNetOfRet:bool = obj["TaxOnNetOfRet"]
      """  Calculate taxes on the amount net of the retention (for future use)  """  
      self.LastAnalDate:str = obj["LastAnalDate"]
      """  Date of last project analysis run.  """  
      self.RegenReqd:bool = obj["RegenReqd"]
      """  Indicates if full Re-gen is required for the project. When this is set, the next generate of project analysis will be full re-gen.  """  
      self.PBCeilingTotal:int = obj["PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling.  """  
      self.DocPBCeilingTotal:int = obj["DocPBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Project currency  """  
      self.Rpt1PBCeilingTotal:int = obj["Rpt1PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt2PBCeilingTotal:int = obj["Rpt2PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt3PBCeilingTotal:int = obj["Rpt3PBCeilingTotal"]
      """  Maximum value for overall Project that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.PBCeilingFees:int = obj["PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling.  """  
      self.DocPBCeilingFees:int = obj["DocPBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Project currency  """  
      self.Rpt1PBCeilingFees:int = obj["Rpt1PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt2PBCeilingFees:int = obj["Rpt2PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.Rpt3PBCeilingFees:int = obj["Rpt3PBCeilingFees"]
      """  Maximum value for Fees that can be charged. Zero means no ceiling. in the Reporting currency  """  
      self.ChkEmpPrjRole:bool = obj["ChkEmpPrjRole"]
      """  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  """  
      self.PPLiquidPct:int = obj["PPLiquidPct"]
      """  Progress Payment Liquidation Percentage, used in Get Shipment.  """  
      self.PPAllOrderLines:bool = obj["PPAllOrderLines"]
      """  Progress Invoice All Order Lines.  If this is set to trye, then the progress invoice preparation process will include the jobs as defined by the parameter PPAllPrjJobs.  """  
      self.PPAllPrjJobs:bool = obj["PPAllPrjJobs"]
      """  If this is false then the Progress Payment Invoice process will ONLY process jobs that have a demand link to the sales order defined on this sheet. If the field is true then all jobs linked to the project (WBS or Production) will be processed by the Invoice Preparation process.  """  
      self.AvoidPriceList:bool = obj["AvoidPriceList"]
      """  AvoidPriceList  """  
      self.PbsTaxCatID:str = obj["PbsTaxCatID"]
      """  PbsTaxCatID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.RecognizeRevenueAtPhaseLevel:bool = obj["RecognizeRevenueAtPhaseLevel"]
      """  Activate Revenue Recognition at WBS Phase level  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Indicates the date when the project is closed, if the project is reopen, the field will be cleared.  """  
      self.LastAction:str = obj["LastAction"]
      """  Last action performed on Project as relates to revenue recognition.  """  
      self.ActionDate:str = obj["ActionDate"]
      """  Date when the LastAction happened to the Project.  """  
      self.Approved:bool = obj["Approved"]
      self.Selected:bool = obj["Selected"]
      self.BitFlag:int = obj["BitFlag"]
      self.ConCustNumName:str = obj["ConCustNumName"]
      self.ConCustNumCustID:str = obj["ConCustNumCustID"]
      self.ConCustNumBTName:str = obj["ConCustNumBTName"]
      self.ConProjMgrLastName:str = obj["ConProjMgrLastName"]
      self.ConProjMgrName:str = obj["ConProjMgrName"]
      self.ConProjMgrFirstName:str = obj["ConProjMgrFirstName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.CustNum_c:int = obj["CustNum_c"]
      self.ShipToNum_c:str = obj["ShipToNum_c"]
      self.LienRequired_c:bool = obj["LienRequired_c"]
      self.DNBComplete_c:bool = obj["DNBComplete_c"]
      self.DNBCompletedBy_c:str = obj["DNBCompletedBy_c"]
      self.PermitRequired_c:bool = obj["PermitRequired_c"]
      self.RightToLien_c:bool = obj["RightToLien_c"]
      self.RightToLienWithInDays_c:int = obj["RightToLienWithInDays_c"]
      self.ReviewedBy_c:str = obj["ReviewedBy_c"]
      self.TermsCode_c:str = obj["TermsCode_c"]
      self.AdditionalTerms_c:str = obj["AdditionalTerms_c"]
      self.PlannedShipDate_c:str = obj["PlannedShipDate_c"]
      self.SchedSubmittalDate_c:str = obj["SchedSubmittalDate_c"]
      self.FreightAmt_c:int = obj["FreightAmt_c"]
      self.NextMilestoneDate_c:str = obj["NextMilestoneDate_c"]
      self.NextMilestoneDesc_c:str = obj["NextMilestoneDesc_c"]
      self.EstProfit_c:int = obj["EstProfit_c"]
      self.EstMargin_c:int = obj["EstMargin_c"]
      self.CommissionApproval_c:str = obj["CommissionApproval_c"]
      self.CommissionApprovedBy_c:str = obj["CommissionApprovedBy_c"]
      self.CommissionApprovalDate_c:str = obj["CommissionApprovalDate_c"]
      pass

class Erp_Tablesets_ProjMultiTableset:
   def __init__(self, obj):
      self.ProjMulti:list[Erp_Tablesets_ProjMultiRow] = obj["ProjMulti"]
      self.ProjectCst:list[Erp_Tablesets_ProjectCstRow] = obj["ProjectCst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ProjectCstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.EstBurdenCost:int = obj["EstBurdenCost"]
      """  Estimated burden cost.  """  
      self.EstBurdenHours:int = obj["EstBurdenHours"]
      """  Estimated burden hours.  """  
      self.EstLaborCost:int = obj["EstLaborCost"]
      """  Estimated labor cost.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated labor hours.  """  
      self.EstSubcontractCost:int = obj["EstSubcontractCost"]
      """  Estimated subcontract cost.  """  
      self.EstMtlCost:int = obj["EstMtlCost"]
      """  Estimated material cost.  """  
      self.EstMtlBurdenCost:int = obj["EstMtlBurdenCost"]
      """  Estimated material burden cost.  """  
      self.RollBudgetstoProject:bool = obj["RollBudgetstoProject"]
      """  To control if the project phase budget values are to be rolled up to the project  """  
      self.RollManEstToCpte:bool = obj["RollManEstToCpte"]
      """  to control if the project phase manual estimate to complete values are to be rolled up to the project  """  
      self.TotEstLbrHrs:int = obj["TotEstLbrHrs"]
      """  Total Costd labour hours for the Project  """  
      self.TotEstBurdenHrs:int = obj["TotEstBurdenHrs"]
      """  Total estimated burden hours for the project  """  
      self.TotEstLbrCost:int = obj["TotEstLbrCost"]
      """  Total estimated labour cost for the project. This is production and setup combined.  """  
      self.TotEstMtlCost:int = obj["TotEstMtlCost"]
      """  Total estimated material costs for the project  """  
      self.TotEstSubContCost:int = obj["TotEstSubContCost"]
      """  Total estimated subcontract costs for the project  """  
      self.TotActLbrHrs:int = obj["TotActLbrHrs"]
      """  Total actual labour hours for the project  """  
      self.TotActBurHrs:int = obj["TotActBurHrs"]
      """  Total actual burden hours for the project.  """  
      self.TotActLbrCost:int = obj["TotActLbrCost"]
      """  Total actual labour cost for the project. This is production and setup combined.  """  
      self.TotActBurCost:int = obj["TotActBurCost"]
      """  Total actual burden cost for the project. This is production and setup combined.  """  
      self.TotActSubContCost:int = obj["TotActSubContCost"]
      """  Total actual subcontract costs for the project  """  
      self.TotActMtlCost:int = obj["TotActMtlCost"]
      """  Total actual material costs for the project  """  
      self.TotActMtlBurCost:int = obj["TotActMtlBurCost"]
      """  Total actual material burden costs for the project  """  
      self.ManEstCtcLbrHrs:int = obj["ManEstCtcLbrHrs"]
      """  Manually entered estimate to complete for the labour hours for the project.  """  
      self.ManEstCtcBurHrs:int = obj["ManEstCtcBurHrs"]
      """  Manually entered estimate to complete for the burden hours for the project.  """  
      self.ManEstCtcLbrCost:int = obj["ManEstCtcLbrCost"]
      """  Manually entered estimate to complete for the labour cost. This will be both production and setup for the project.  """  
      self.ManEstCtcBurCost:int = obj["ManEstCtcBurCost"]
      """  Manually entered estimate to complete for the burden cost for the project.  """  
      self.ManEstCtcSubConCost:int = obj["ManEstCtcSubConCost"]
      """  Manually entered estimate to complete for the Subcontract cost for the project.  """  
      self.ManEstCtcMtlCost:int = obj["ManEstCtcMtlCost"]
      """  Manually entered estimate to complete for the material cost for the project.  """  
      self.ManEstCtcMtlBurCost:int = obj["ManEstCtcMtlBurCost"]
      """  Manually entered estimate to complete for the material burden cost for the project.  """  
      self.TotCtcLbrHours:int = obj["TotCtcLbrHours"]
      """  Total calculated cost to complete labour hours for the project.  """  
      self.TotCtcBurHours:int = obj["TotCtcBurHours"]
      """  Total calculated cost to complete burden hours for the project.  """  
      self.TotCtcBurCost:int = obj["TotCtcBurCost"]
      """  Total calculated cost to complete burden cost for the project. This will be both production and setup.  """  
      self.TotCtcLbrCost:int = obj["TotCtcLbrCost"]
      """  Total calculated cost to complete labour cost for the project. This will be both production and setup.  """  
      self.TotCtcSubConCost:int = obj["TotCtcSubConCost"]
      """  Total calculated cost to complete subcontract cost for the project.  """  
      self.TotCtcMtlCost:int = obj["TotCtcMtlCost"]
      """  Total calculated cost to complete material cost for the project.  """  
      self.TotCtcMtlBurCost:int = obj["TotCtcMtlBurCost"]
      """  Total calculated cost to complete material burden cost for the project.  """  
      self.TotQuotLbrHrs:int = obj["TotQuotLbrHrs"]
      """  Total quoted labour hours for the project  """  
      self.TotQuotBurHrs:int = obj["TotQuotBurHrs"]
      """  Total quoted burden hours for the project  """  
      self.TotQuotLbrCost:int = obj["TotQuotLbrCost"]
      """  Total quoted labour cost for the project. This will be both production and setup.  """  
      self.TotQuotSubContCost:int = obj["TotQuotSubContCost"]
      """  Total quoted subcontract cost for the project.  """  
      self.TotQuotMtlCost:int = obj["TotQuotMtlCost"]
      """  Total quoted material cost for the project.  """  
      self.TotQuotMtlBurCost:int = obj["TotQuotMtlBurCost"]
      """  Total quoted material burden cost for the project.  """  
      self.TotEstBurCost:int = obj["TotEstBurCost"]
      """  Total estimated burden costs for the project  """  
      self.TotQuotBurCost:int = obj["TotQuotBurCost"]
      """  Total quoted burden cost for the project. This will be both production and setup.  """  
      self.RevenueRecAutoToDate:int = obj["RevenueRecAutoToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been invoiced against the sales order either as an advanced billing or a shipment. This is the sum of ProjectAnalysis records with a Linecode of Revenue with a linesource of Invoice with value from ProjectAnalysis.ActMatCost.  """  
      self.MaterialRecAutoCstTodate:int = obj["MaterialRecAutoCstTodate"]
      """  The material costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.LaborRecAutoCstTodate:int = obj["LaborRecAutoCstTodate"]
      """  The labor costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.BurdenRecAutoCstTodate:int = obj["BurdenRecAutoCstTodate"]
      """  The burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order.  """  
      self.MtlBurdenRecAutoCstTodate:int = obj["MtlBurdenRecAutoCstTodate"]
      """  The material burden costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  """  
      self.BudTotLbrHours:int = obj["BudTotLbrHours"]
      """  Total budget labour hours for the Project  """  
      self.BudTotBurHrs:int = obj["BudTotBurHrs"]
      """  Total budget burden hours for the Project  """  
      self.BudTotLbrCost:int = obj["BudTotLbrCost"]
      """  Total budget labour cost for the Project. This is production and setup combined.  """  
      self.BudTotBurCost:int = obj["BudTotBurCost"]
      """  Total budget burden cost for the Project. This is production and setup combined.  """  
      self.BudTotSubCost:int = obj["BudTotSubCost"]
      """  Total budget subcontract costs for the Project  """  
      self.BudTotMtlCost:int = obj["BudTotMtlCost"]
      """  Total budget material costs for the Project  """  
      self.BudTotMtlBurCost:int = obj["BudTotMtlBurCost"]
      """  Total budget material burden costs for the Project phase.  """  
      self.TotEstMtlBurCost:int = obj["TotEstMtlBurCost"]
      """  Total estimated material burden costs for the Project phase  """  
      self.SubConRecAutoCstTodate:int = obj["SubConRecAutoCstTodate"]
      """  The subcontract costs posted to cost of sales to date. These costs are defined by the Capture Cost Activity for the project top job that is linked to the sales order  """  
      self.RevenueRecManToDate:int = obj["RevenueRecManToDate"]
      """  The revenue that has been recognised to date for the project. This is revenue that has been manually recognised using this process.  """  
      self.MaterialRecManCstTodate:int = obj["MaterialRecManCstTodate"]
      """  The material costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.LaborRecManCstTodate:int = obj["LaborRecManCstTodate"]
      """  The labor costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.BurdenRecManCstTodate:int = obj["BurdenRecManCstTodate"]
      """  The burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process  """  
      self.SubConRecManCstTodate:int = obj["SubConRecManCstTodate"]
      """  The subcontract costs posted to cost of sales to date. This is cost that has been manually recognised using this process  """  
      self.MtlBurdenRecManCstTodate:int = obj["MtlBurdenRecManCstTodate"]
      """  The material burden costs posted to cost of sales to date. This is cost that has been manually recognised using this process.  """  
      self.MaterialCostOfSales:int = obj["MaterialCostOfSales"]
      """  The material costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of Material with a linesource of COS with value from ProjectAnalysis.ActMatCost.  """  
      self.LaborCostOfSales:int = obj["LaborCostOfSales"]
      """  The labor costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActLaborCost.  """  
      self.BurdenCostOfSales:int = obj["BurdenCostOfSales"]
      """  The burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of labor with a linesource of COS with value from ProjectAnalysis.ActBurdenCost  """  
      self.SubConCostOfSales:int = obj["SubConCostOfSales"]
      """  The subcontract costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActSubContractCost  """  
      self.MtlBurdenCostOfSales:int = obj["MtlBurdenCostOfSales"]
      """  The material burden costs that have been posted to Cost of Sales. This is the sum of ProjectAnalysis records with a Linecode of material with a linesource of COS with value from ProjectAnalysis.ActMatBurdenCost  """  
      self.TotQuotODCCost:int = obj["TotQuotODCCost"]
      """  Other Direct Cost Quoted  """  
      self.TotEstODCCost:int = obj["TotEstODCCost"]
      """  Other Direct Cost Estimated  """  
      self.TotActODCCost:int = obj["TotActODCCost"]
      """  ODC Actual  """  
      self.ManEstCTCODCCost:int = obj["ManEstCTCODCCost"]
      """  Other direct cost manual CTC  """  
      self.TotCTCODCCost:int = obj["TotCTCODCCost"]
      """  Other direct Cost total CTC  """  
      self.BudTotODCCost:int = obj["BudTotODCCost"]
      """  Other direct Cost Budget Total  """  
      self.ODCRecAutoCstToDate:int = obj["ODCRecAutoCstToDate"]
      """  Other Direct cost Recognition to Date  """  
      self.ODCRecManCstTodate:int = obj["ODCRecManCstTodate"]
      """  Other Direct Cost Manual Recognition to Date  """  
      self.EstODCCost:int = obj["EstODCCost"]
      """  Estimated other direct cost  """  
      self.BdnRecSeqPosted:int = obj["BdnRecSeqPosted"]
      """  Number of Recalculation of burden amounts posted to GL by Revenue Recognition process  """  
      self.BdnRecSeqLastAdded:int = obj["BdnRecSeqLastAdded"]
      """  Number of Recalculation of burden amounts created by Revenue Recognition process  """  
      self.BdnRevenueAutoToday:int = obj["BdnRevenueAutoToday"]
      """  Sum of all Actual Burden Charges posted by today  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  AsOfDate  """  
      self.BuildAnalysis:bool = obj["BuildAnalysis"]
      """  BuildAnalysis  """  
      self.LbrPur:int = obj["LbrPur"]
      """  LbrPur  """  
      self.BurPur:int = obj["BurPur"]
      """  BurPur  """  
      self.MtlPur:int = obj["MtlPur"]
      """  MtlPur  """  
      self.SubPur:int = obj["SubPur"]
      """  SubPur  """  
      self.MtlBurPur:int = obj["MtlBurPur"]
      """  MtlBurPur  """  
      self.ODCPur:int = obj["ODCPur"]
      """  ODCPur  """  
      self.LaborLbrCstToDate:int = obj["LaborLbrCstToDate"]
      """  LaborLbrCstToDate  """  
      self.BurdenLbrCstToDate:int = obj["BurdenLbrCstToDate"]
      """  BurdenLbrCstToDate  """  
      self.ActMtlNonJobCost:int = obj["ActMtlNonJobCost"]
      """  ActMtlNonJobCost  """  
      self.RecManPosted:int = obj["RecManPosted"]
      """  RecManPosted  """  
      self.LbrManPosted:int = obj["LbrManPosted"]
      """  LbrManPosted  """  
      self.BurManPosted:int = obj["BurManPosted"]
      """  BurManPosted  """  
      self.MtlManPosted:int = obj["MtlManPosted"]
      """  MtlManPosted  """  
      self.SubCManPosted:int = obj["SubCManPosted"]
      """  SubCManPosted  """  
      self.MtlBurManPosted:int = obj["MtlBurManPosted"]
      """  MtlBurManPosted  """  
      self.ODCManPosted:int = obj["ODCManPosted"]
      """  ODCManPosted  """  
      self.Reverse:str = obj["Reverse"]
      """  Reverse  """  
      self.NextTmpInvcNum:int = obj["NextTmpInvcNum"]
      """  NextTmpInvcNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PercentageOfCompletion:int = obj["PercentageOfCompletion"]
      """  Percentage of Completion  """  
      self.ToBeRecognizedLbrCost:int = obj["ToBeRecognizedLbrCost"]
      """  Labor Cost To Be Recognized  """  
      self.ToBeRecognizedBurCost:int = obj["ToBeRecognizedBurCost"]
      """  Burden Cost To Be Recognized  """  
      self.ToBeRecognizedMtlCost:int = obj["ToBeRecognizedMtlCost"]
      """  Material Cost To Be Recognized  """  
      self.ToBeRecognizedSubCost:int = obj["ToBeRecognizedSubCost"]
      """  Subcontract Cost To Be Recognized  """  
      self.ToBeRecognizedMtlBurCost:int = obj["ToBeRecognizedMtlBurCost"]
      """  Material Burden Cost To Be Recognized  """  
      self.ToBeRecognizedODCCost:int = obj["ToBeRecognizedODCCost"]
      """  ODC Cost To Be Recognized  """  
      self.ToBeRecognizedRevenue:int = obj["ToBeRecognizedRevenue"]
      """  Revenue To Be Recognized  """  
      self.BillingToDate:int = obj["BillingToDate"]
      """  BillingToDate  """  
      self.RecogToDtBilling:int = obj["RecogToDtBilling"]
      """  RecogToDtBilling  """  
      self.TotProjRev:int = obj["TotProjRev"]
      """  TotProjRev  """  
      self.RecogToDtLbk:int = obj["RecogToDtLbk"]
      """  RecogToDtLbk  """  
      self.RecogToDtManual:int = obj["RecogToDtManual"]
      """  RecogToDtManual  """  
      self.RetentionDt:int = obj["RetentionDt"]
      """  RetentionDt  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocBudTotBurCost:int = obj["DocBudTotBurCost"]
      self.DocBudTotLbrCost:int = obj["DocBudTotLbrCost"]
      self.DocBudTotMtlBurCost:int = obj["DocBudTotMtlBurCost"]
      self.DocBudTotMtlCost:int = obj["DocBudTotMtlCost"]
      self.DocBudTotODCCost:int = obj["DocBudTotODCCost"]
      self.DocBudTotSubCost:int = obj["DocBudTotSubCost"]
      self.DocEstBurdenCost:int = obj["DocEstBurdenCost"]
      self.DocEstLaborCost:int = obj["DocEstLaborCost"]
      self.DocEstMtlBurdenCost:int = obj["DocEstMtlBurdenCost"]
      self.DocEstMtlCost:int = obj["DocEstMtlCost"]
      self.DocEstODCCost:int = obj["DocEstODCCost"]
      self.DocEstSubcontractCost:int = obj["DocEstSubcontractCost"]
      self.DocEstTotalCost:int = obj["DocEstTotalCost"]
      self.DocGTActualCost:int = obj["DocGTActualCost"]
      self.DocGTBudgetCost:int = obj["DocGTBudgetCost"]
      self.DocGTCalculatedCost:int = obj["DocGTCalculatedCost"]
      self.DocGTEstimatedCost:int = obj["DocGTEstimatedCost"]
      self.DocGTManualCost:int = obj["DocGTManualCost"]
      self.DocGTQuotedCost:int = obj["DocGTQuotedCost"]
      self.DocProjectedTotalBurCost:int = obj["DocProjectedTotalBurCost"]
      self.DocProjectedTotalCost:int = obj["DocProjectedTotalCost"]
      self.DocProjectedTotalLbrCost:int = obj["DocProjectedTotalLbrCost"]
      self.DocProjectedTotalMtlBurCost:int = obj["DocProjectedTotalMtlBurCost"]
      self.DocProjectedTotalMtlCost:int = obj["DocProjectedTotalMtlCost"]
      self.DocProjectedTotalODCCost:int = obj["DocProjectedTotalODCCost"]
      self.DocProjectedTotalSubContCost:int = obj["DocProjectedTotalSubContCost"]
      self.DocTotActMtlBurCost:int = obj["DocTotActMtlBurCost"]
      self.DocTotActMtlCost:int = obj["DocTotActMtlCost"]
      self.DocTotActODCCost:int = obj["DocTotActODCCost"]
      self.DocTotActSubContCost:int = obj["DocTotActSubContCost"]
      self.DocTotCtcBurCost:int = obj["DocTotCtcBurCost"]
      self.DocTotCtcLbrCost:int = obj["DocTotCtcLbrCost"]
      self.DocTotCtcMtlBurCost:int = obj["DocTotCtcMtlBurCost"]
      self.DocTotCtcMtlCost:int = obj["DocTotCtcMtlCost"]
      self.DocTotCTCODCCost:int = obj["DocTotCTCODCCost"]
      self.DocTotCtcSubConCost:int = obj["DocTotCtcSubConCost"]
      self.DocTotEstBurCost:int = obj["DocTotEstBurCost"]
      self.DocTotEstLbrCost:int = obj["DocTotEstLbrCost"]
      self.DocTotEstMtlBurCost:int = obj["DocTotEstMtlBurCost"]
      self.DocTotEstMtlCost:int = obj["DocTotEstMtlCost"]
      self.DocTotEstODCCost:int = obj["DocTotEstODCCost"]
      self.DocTotEstSubContCost:int = obj["DocTotEstSubContCost"]
      self.DocTotQuotBurCost:int = obj["DocTotQuotBurCost"]
      self.DocTotQuotLbrCost:int = obj["DocTotQuotLbrCost"]
      self.DocTotQuotMtlBurCost:int = obj["DocTotQuotMtlBurCost"]
      self.DocTotQuotMtlCost:int = obj["DocTotQuotMtlCost"]
      self.DocTotQuotODCCost:int = obj["DocTotQuotODCCost"]
      self.DocTotQuotSubContCost:int = obj["DocTotQuotSubContCost"]
      self.EstTotalCost:int = obj["EstTotalCost"]
      """  This is a calculated field: the sum of the other Project.Est*Cost fields.  It is not stored in the database.  """  
      self.GTActualCost:int = obj["GTActualCost"]
      self.GTBudgetCost:int = obj["GTBudgetCost"]
      self.GTCalculatedCost:int = obj["GTCalculatedCost"]
      self.GTEstimatedCost:int = obj["GTEstimatedCost"]
      self.GTManualCost:int = obj["GTManualCost"]
      self.GTQuotedCost:int = obj["GTQuotedCost"]
      self.ProjectedTotalBurCost:int = obj["ProjectedTotalBurCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalCost:int = obj["ProjectedTotalCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalLbrCost:int = obj["ProjectedTotalLbrCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalMtlBurCost:int = obj["ProjectedTotalMtlBurCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalMtlCost:int = obj["ProjectedTotalMtlCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalODCCost:int = obj["ProjectedTotalODCCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ProjectedTotalSubContCost:int = obj["ProjectedTotalSubContCost"]
      """  This is a calculated field: the sum of the other Project.ProjectedTotal*Cost fields.  It is not stored in the database.  """  
      self.ReconToDtBilling:int = obj["ReconToDtBilling"]
      """  Recognized to Date Billing  """  
      self.Rpt1BudTotBurCost:int = obj["Rpt1BudTotBurCost"]
      self.Rpt1BudTotLbrCost:int = obj["Rpt1BudTotLbrCost"]
      self.Rpt1BudTotMtlBurCost:int = obj["Rpt1BudTotMtlBurCost"]
      self.Rpt1BudTotMtlCost:int = obj["Rpt1BudTotMtlCost"]
      self.Rpt1BudTotODCCost:int = obj["Rpt1BudTotODCCost"]
      self.Rpt1BudTotSubCost:int = obj["Rpt1BudTotSubCost"]
      self.Rpt1EstBurdenCost:int = obj["Rpt1EstBurdenCost"]
      self.Rpt1EstLaborCost:int = obj["Rpt1EstLaborCost"]
      self.Rpt1EstMtlBurdenCost:int = obj["Rpt1EstMtlBurdenCost"]
      self.Rpt1EstMtlCost:int = obj["Rpt1EstMtlCost"]
      self.Rpt1EstODCCost:int = obj["Rpt1EstODCCost"]
      self.Rpt1EstSubcontractCost:int = obj["Rpt1EstSubcontractCost"]
      self.Rpt1EstTotalCost:int = obj["Rpt1EstTotalCost"]
      self.Rpt1GTActualCost:int = obj["Rpt1GTActualCost"]
      self.Rpt1GTBudgetCost:int = obj["Rpt1GTBudgetCost"]
      self.Rpt1GTCalculatedCost:int = obj["Rpt1GTCalculatedCost"]
      self.Rpt1GTEstimatedCost:int = obj["Rpt1GTEstimatedCost"]
      self.Rpt1GTManualCost:int = obj["Rpt1GTManualCost"]
      self.Rpt1GTQuotedCost:int = obj["Rpt1GTQuotedCost"]
      self.Rpt1ManEstCtcBurCost:int = obj["Rpt1ManEstCtcBurCost"]
      self.Rpt1ManEstCtcLbrCost:int = obj["Rpt1ManEstCtcLbrCost"]
      self.Rpt1ManEstCtcMtlBurCost:int = obj["Rpt1ManEstCtcMtlBurCost"]
      self.Rpt1ManEstCtcMtlCost:int = obj["Rpt1ManEstCtcMtlCost"]
      self.Rpt1ManEstCTCODCCost:int = obj["Rpt1ManEstCTCODCCost"]
      self.Rpt1ManEstCtcSubConCost:int = obj["Rpt1ManEstCtcSubConCost"]
      self.Rpt1ProjectedTotalBurCost:int = obj["Rpt1ProjectedTotalBurCost"]
      self.Rpt1ProjectedTotalCost:int = obj["Rpt1ProjectedTotalCost"]
      self.Rpt1ProjectedTotalLbrCost:int = obj["Rpt1ProjectedTotalLbrCost"]
      self.Rpt1ProjectedTotalMtlBurCost:int = obj["Rpt1ProjectedTotalMtlBurCost"]
      self.Rpt1ProjectedTotalMtlCost:int = obj["Rpt1ProjectedTotalMtlCost"]
      self.Rpt1ProjectedTotalODCCost:int = obj["Rpt1ProjectedTotalODCCost"]
      self.Rpt1ProjectedTotalSubContCost:int = obj["Rpt1ProjectedTotalSubContCost"]
      self.Rpt1TotActBurCost:int = obj["Rpt1TotActBurCost"]
      self.Rpt1TotActLbrCost:int = obj["Rpt1TotActLbrCost"]
      self.Rpt1TotActMtlBurCost:int = obj["Rpt1TotActMtlBurCost"]
      self.Rpt1TotActMtlCost:int = obj["Rpt1TotActMtlCost"]
      self.Rpt1TotActODCCost:int = obj["Rpt1TotActODCCost"]
      self.Rpt1TotActSubContCost:int = obj["Rpt1TotActSubContCost"]
      self.Rpt1TotCtcBurCost:int = obj["Rpt1TotCtcBurCost"]
      self.Rpt1TotCtcLbrCost:int = obj["Rpt1TotCtcLbrCost"]
      self.Rpt1TotCtcMtlBurCost:int = obj["Rpt1TotCtcMtlBurCost"]
      self.Rpt1TotCtcMtlCost:int = obj["Rpt1TotCtcMtlCost"]
      self.Rpt1TotCTCODCCost:int = obj["Rpt1TotCTCODCCost"]
      self.Rpt1TotCtcSubConCost:int = obj["Rpt1TotCtcSubConCost"]
      self.Rpt1TotEstBurCost:int = obj["Rpt1TotEstBurCost"]
      self.Rpt1TotEstLbrCost:int = obj["Rpt1TotEstLbrCost"]
      self.Rpt1TotEstMtlBurCost:int = obj["Rpt1TotEstMtlBurCost"]
      self.Rpt1TotEstMtlCost:int = obj["Rpt1TotEstMtlCost"]
      self.Rpt1TotEstODCCost:int = obj["Rpt1TotEstODCCost"]
      self.Rpt1TotEstSubContCost:int = obj["Rpt1TotEstSubContCost"]
      self.Rpt1TotQuotBurCost:int = obj["Rpt1TotQuotBurCost"]
      self.Rpt1TotQuotLbrCost:int = obj["Rpt1TotQuotLbrCost"]
      self.Rpt1TotQuotMtlBurCost:int = obj["Rpt1TotQuotMtlBurCost"]
      self.Rpt1TotQuotMtlCost:int = obj["Rpt1TotQuotMtlCost"]
      self.Rpt1TotQuotODCCost:int = obj["Rpt1TotQuotODCCost"]
      self.Rpt1TotQuotSubContCost:int = obj["Rpt1TotQuotSubContCost"]
      self.Rpt2BudTotBurCost:int = obj["Rpt2BudTotBurCost"]
      self.Rpt2BudTotLbrCost:int = obj["Rpt2BudTotLbrCost"]
      self.Rpt2BudTotMtlBurCost:int = obj["Rpt2BudTotMtlBurCost"]
      self.Rpt2BudTotMtlCost:int = obj["Rpt2BudTotMtlCost"]
      self.Rpt2BudTotODCCost:int = obj["Rpt2BudTotODCCost"]
      self.Rpt2BudTotSubCost:int = obj["Rpt2BudTotSubCost"]
      self.Rpt2EstBurdenCost:int = obj["Rpt2EstBurdenCost"]
      self.Rpt2EstLaborCost:int = obj["Rpt2EstLaborCost"]
      self.Rpt2EstMtlBurdenCost:int = obj["Rpt2EstMtlBurdenCost"]
      self.Rpt2EstMtlCost:int = obj["Rpt2EstMtlCost"]
      self.Rpt2EstODCCost:int = obj["Rpt2EstODCCost"]
      self.Rpt2EstSubcontractCost:int = obj["Rpt2EstSubcontractCost"]
      self.Rpt2EstTotalCost:int = obj["Rpt2EstTotalCost"]
      self.Rpt2GTActualCost:int = obj["Rpt2GTActualCost"]
      self.Rpt2GTBudgetCost:int = obj["Rpt2GTBudgetCost"]
      self.Rpt2GTCalculatedCost:int = obj["Rpt2GTCalculatedCost"]
      self.Rpt2GTEstimatedCost:int = obj["Rpt2GTEstimatedCost"]
      self.Rpt2GTManualCost:int = obj["Rpt2GTManualCost"]
      self.Rpt2GTQuotedCost:int = obj["Rpt2GTQuotedCost"]
      self.Rpt2ManEstCtcBurCost:int = obj["Rpt2ManEstCtcBurCost"]
      self.Rpt2ManEstCtcLbrCost:int = obj["Rpt2ManEstCtcLbrCost"]
      self.Rpt2ManEstCtcMtlBurCost:int = obj["Rpt2ManEstCtcMtlBurCost"]
      self.Rpt2ManEstCtcMtlCost:int = obj["Rpt2ManEstCtcMtlCost"]
      self.Rpt2ManEstCTCODCCost:int = obj["Rpt2ManEstCTCODCCost"]
      self.Rpt2ManEstCtcSubConCost:int = obj["Rpt2ManEstCtcSubConCost"]
      self.Rpt2ProjectedTotalBurCost:int = obj["Rpt2ProjectedTotalBurCost"]
      self.Rpt2ProjectedTotalCost:int = obj["Rpt2ProjectedTotalCost"]
      self.Rpt2ProjectedTotalLbrCost:int = obj["Rpt2ProjectedTotalLbrCost"]
      self.Rpt2ProjectedTotalMtlBurCost:int = obj["Rpt2ProjectedTotalMtlBurCost"]
      self.Rpt2ProjectedTotalMtlCost:int = obj["Rpt2ProjectedTotalMtlCost"]
      self.Rpt2ProjectedTotalODCCost:int = obj["Rpt2ProjectedTotalODCCost"]
      self.Rpt2ProjectedTotalSubContCost:int = obj["Rpt2ProjectedTotalSubContCost"]
      self.Rpt2TotActBurCost:int = obj["Rpt2TotActBurCost"]
      self.Rpt2TotActLbrCost:int = obj["Rpt2TotActLbrCost"]
      self.Rpt2TotActMtlBurCost:int = obj["Rpt2TotActMtlBurCost"]
      self.Rpt2TotActMtlCost:int = obj["Rpt2TotActMtlCost"]
      self.Rpt2TotActODCCost:int = obj["Rpt2TotActODCCost"]
      self.Rpt2TotActSubContCost:int = obj["Rpt2TotActSubContCost"]
      self.Rpt2TotCtcBurCost:int = obj["Rpt2TotCtcBurCost"]
      self.Rpt2TotCtcLbrCost:int = obj["Rpt2TotCtcLbrCost"]
      self.Rpt2TotCtcMtlBurCost:int = obj["Rpt2TotCtcMtlBurCost"]
      self.Rpt2TotCtcMtlCost:int = obj["Rpt2TotCtcMtlCost"]
      self.Rpt2TotCTCODCCost:int = obj["Rpt2TotCTCODCCost"]
      self.Rpt2TotCtcSubConCost:int = obj["Rpt2TotCtcSubConCost"]
      self.Rpt2TotEstBurCost:int = obj["Rpt2TotEstBurCost"]
      self.Rpt2TotEstLbrCost:int = obj["Rpt2TotEstLbrCost"]
      self.Rpt2TotEstMtlBurCost:int = obj["Rpt2TotEstMtlBurCost"]
      self.Rpt2TotEstMtlCost:int = obj["Rpt2TotEstMtlCost"]
      self.Rpt2TotEstODCCost:int = obj["Rpt2TotEstODCCost"]
      self.Rpt2TotEstSubContCost:int = obj["Rpt2TotEstSubContCost"]
      self.Rpt2TotQuotBurCost:int = obj["Rpt2TotQuotBurCost"]
      self.Rpt2TotQuotLbrCost:int = obj["Rpt2TotQuotLbrCost"]
      self.Rpt2TotQuotMtlBurCost:int = obj["Rpt2TotQuotMtlBurCost"]
      self.Rpt2TotQuotMtlCost:int = obj["Rpt2TotQuotMtlCost"]
      self.Rpt2TotQuotODCCost:int = obj["Rpt2TotQuotODCCost"]
      self.Rpt2TotQuotSubContCost:int = obj["Rpt2TotQuotSubContCost"]
      self.Rpt3BudTotBurCost:int = obj["Rpt3BudTotBurCost"]
      self.Rpt3BudTotLbrCost:int = obj["Rpt3BudTotLbrCost"]
      self.Rpt3BudTotMtlBurCost:int = obj["Rpt3BudTotMtlBurCost"]
      self.Rpt3BudTotMtlCost:int = obj["Rpt3BudTotMtlCost"]
      self.Rpt3BudTotODCCost:int = obj["Rpt3BudTotODCCost"]
      self.Rpt3BudTotSubCost:int = obj["Rpt3BudTotSubCost"]
      self.Rpt3EstBurdenCost:int = obj["Rpt3EstBurdenCost"]
      self.Rpt3EstLaborCost:int = obj["Rpt3EstLaborCost"]
      self.Rpt3EstMtlBurdenCost:int = obj["Rpt3EstMtlBurdenCost"]
      self.Rpt3EstMtlCost:int = obj["Rpt3EstMtlCost"]
      self.Rpt3EstODCCost:int = obj["Rpt3EstODCCost"]
      self.Rpt3EstSubcontractCost:int = obj["Rpt3EstSubcontractCost"]
      self.Rpt3EstTotalCost:int = obj["Rpt3EstTotalCost"]
      self.Rpt3GTActualCost:int = obj["Rpt3GTActualCost"]
      self.Rpt3GTBudgetCost:int = obj["Rpt3GTBudgetCost"]
      self.Rpt3GTCalculatedCost:int = obj["Rpt3GTCalculatedCost"]
      self.Rpt3GTEstimatedCost:int = obj["Rpt3GTEstimatedCost"]
      self.Rpt3GTManualCost:int = obj["Rpt3GTManualCost"]
      self.Rpt3GTQuotedCost:int = obj["Rpt3GTQuotedCost"]
      self.Rpt3ManEstCtcBurCost:int = obj["Rpt3ManEstCtcBurCost"]
      self.Rpt3ManEstCtcLbrCost:int = obj["Rpt3ManEstCtcLbrCost"]
      self.Rpt3ManEstCtcMtlBurCost:int = obj["Rpt3ManEstCtcMtlBurCost"]
      self.Rpt3ManEstCtcMtlCost:int = obj["Rpt3ManEstCtcMtlCost"]
      self.Rpt3ManEstCTCODCCost:int = obj["Rpt3ManEstCTCODCCost"]
      self.Rpt3ManEstCtcSubConCost:int = obj["Rpt3ManEstCtcSubConCost"]
      self.Rpt3ProjectedTotalBurCost:int = obj["Rpt3ProjectedTotalBurCost"]
      self.Rpt3ProjectedTotalCost:int = obj["Rpt3ProjectedTotalCost"]
      self.Rpt3ProjectedTotalLbrCost:int = obj["Rpt3ProjectedTotalLbrCost"]
      self.Rpt3ProjectedTotalMtlBurCost:int = obj["Rpt3ProjectedTotalMtlBurCost"]
      self.Rpt3ProjectedTotalMtlCost:int = obj["Rpt3ProjectedTotalMtlCost"]
      self.Rpt3ProjectedTotalODCCost:int = obj["Rpt3ProjectedTotalODCCost"]
      self.Rpt3ProjectedTotalSubContCost:int = obj["Rpt3ProjectedTotalSubContCost"]
      self.Rpt3TotActBurCost:int = obj["Rpt3TotActBurCost"]
      self.Rpt3TotActLbrCost:int = obj["Rpt3TotActLbrCost"]
      self.Rpt3TotActMtlBurCost:int = obj["Rpt3TotActMtlBurCost"]
      self.Rpt3TotActMtlCost:int = obj["Rpt3TotActMtlCost"]
      self.Rpt3TotActODCCost:int = obj["Rpt3TotActODCCost"]
      self.Rpt3TotActSubContCost:int = obj["Rpt3TotActSubContCost"]
      self.Rpt3TotCtcBurCost:int = obj["Rpt3TotCtcBurCost"]
      self.Rpt3TotCtcLbrCost:int = obj["Rpt3TotCtcLbrCost"]
      self.Rpt3TotCtcMtlBurCost:int = obj["Rpt3TotCtcMtlBurCost"]
      self.Rpt3TotCtcMtlCost:int = obj["Rpt3TotCtcMtlCost"]
      self.Rpt3TotCTCODCCost:int = obj["Rpt3TotCTCODCCost"]
      self.Rpt3TotCtcSubConCost:int = obj["Rpt3TotCtcSubConCost"]
      self.Rpt3TotEstBurCost:int = obj["Rpt3TotEstBurCost"]
      self.Rpt3TotEstLbrCost:int = obj["Rpt3TotEstLbrCost"]
      self.Rpt3TotEstMtlBurCost:int = obj["Rpt3TotEstMtlBurCost"]
      self.Rpt3TotEstMtlCost:int = obj["Rpt3TotEstMtlCost"]
      self.Rpt3TotEstODCCost:int = obj["Rpt3TotEstODCCost"]
      self.Rpt3TotEstSubContCost:int = obj["Rpt3TotEstSubContCost"]
      self.Rpt3TotQuotBurCost:int = obj["Rpt3TotQuotBurCost"]
      self.Rpt3TotQuotLbrCost:int = obj["Rpt3TotQuotLbrCost"]
      self.Rpt3TotQuotMtlBurCost:int = obj["Rpt3TotQuotMtlBurCost"]
      self.Rpt3TotQuotMtlCost:int = obj["Rpt3TotQuotMtlCost"]
      self.Rpt3TotQuotODCCost:int = obj["Rpt3TotQuotODCCost"]
      self.Rpt3TotQuotSubContCost:int = obj["Rpt3TotQuotSubContCost"]
      self.DocManEstCtcBurCost:int = obj["DocManEstCtcBurCost"]
      self.DocManEstCtcLbrCost:int = obj["DocManEstCtcLbrCost"]
      self.DocManEstCtcMtlBurCost:int = obj["DocManEstCtcMtlBurCost"]
      self.DocManEstCtcMtlCost:int = obj["DocManEstCtcMtlCost"]
      self.DocManEstCTCODCCost:int = obj["DocManEstCTCODCCost"]
      self.DocManEstCtcSubConCost:int = obj["DocManEstCtcSubConCost"]
      self.DocTotActBurCost:int = obj["DocTotActBurCost"]
      self.DocTotActLbrCost:int = obj["DocTotActLbrCost"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtProjMultiTableset:
   def __init__(self, obj):
      self.ProjMulti:list[Erp_Tablesets_ProjMultiRow] = obj["ProjMulti"]
      self.ProjectCst:list[Erp_Tablesets_ProjectCstRow] = obj["ProjectCst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   projectID
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjMultiTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProjMultiTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProjMultiTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProjMultiListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewProjMulti_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProjMultiTableset] = obj["ds"]
      pass

class GetNewProjMulti_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProjMultiTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewProjectCst_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProjMultiTableset] = obj["ds"]
      pass

class GetNewProjectCst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProjMultiTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsByFilter_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProjFilterTableset] = obj["ds"]
      pass

class GetRowsByFilter_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjMultiTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProjFilterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseProjMulti
   whereClauseProjectCst
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseProjMulti:str = obj["whereClauseProjMulti"]
      self.whereClauseProjectCst:str = obj["whereClauseProjectCst"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjMultiTableset] = obj["returnObj"]
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

class RefreshAll_input:
   """ Required : 
   projectIDs
   """  
   def __init__(self, obj):
      self.projectIDs:str = obj["projectIDs"]
      pass

class RefreshAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProjMultiTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProjMultiTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProjMultiTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProjMultiTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProjMultiTableset] = obj["ds"]
      pass

      """  output parameters  """  

