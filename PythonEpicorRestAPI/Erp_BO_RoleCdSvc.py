import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RoleCdSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RoleCds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RoleCds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RoleCds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RoleCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds",headers=creds) as resp:
           return await resp.json()

async def post_RoleCds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RoleCds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RoleCdRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RoleCdRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RoleCds_Company_RoleCode(Company, RoleCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RoleCd item
   Description: Calls GetByID to retrieve the RoleCd item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RoleCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCode: Desc: RoleCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RoleCdRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RoleCds_Company_RoleCode(Company, RoleCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RoleCd for the service
   Description: Calls UpdateExt to update RoleCd. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RoleCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCode: Desc: RoleCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RoleCdRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RoleCds_Company_RoleCode(Company, RoleCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RoleCd item
   Description: Call UpdateExt to delete RoleCd item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RoleCd
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCode: Desc: RoleCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_RoleCds_Company_RoleCode_PrjRoleRts(Company, RoleCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PrjRoleRts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PrjRoleRts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCode: Desc: RoleCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PrjRoleRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")/PrjRoleRts",headers=creds) as resp:
           return await resp.json()

async def get_RoleCds_Company_RoleCode_PrjRoleRts_Company_RoleCd_Seq(Company, RoleCode, RoleCd, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PrjRoleRt item
   Description: Calls GetByID to retrieve the PrjRoleRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PrjRoleRt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCode: Desc: RoleCode   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/RoleCds(" + Company + "," + RoleCode + ")/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PrjRoleRts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PrjRoleRts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PrjRoleRts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PrjRoleRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts",headers=creds) as resp:
           return await resp.json()

async def post_PrjRoleRts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PrjRoleRts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PrjRoleRts_Company_RoleCd_Seq(Company, RoleCd, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PrjRoleRt item
   Description: Calls GetByID to retrieve the PrjRoleRt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PrjRoleRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PrjRoleRts_Company_RoleCd_Seq(Company, RoleCd, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PrjRoleRt for the service
   Description: Calls UpdateExt to update PrjRoleRt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PrjRoleRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PrjRoleRtRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PrjRoleRts_Company_RoleCd_Seq(Company, RoleCd, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PrjRoleRt item
   Description: Call UpdateExt to delete PrjRoleRt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PrjRoleRt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RoleCd: Desc: RoleCd   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/PrjRoleRts(" + Company + "," + RoleCd + "," + Seq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RoleCdListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRoleCd, whereClausePrjRoleRt, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRoleCd=" + whereClauseRoleCd
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePrjRoleRt=" + whereClausePrjRoleRt
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(roleCode, epicorHeaders = None):
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
   params += "roleCode=" + roleCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSupervisorRole(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSupervisorRole
   Description: Method to call when changing supervisor role.
   OperationID: ChangeSupervisorRole
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSupervisorRole_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupervisorRole_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckCapabilityBefUpd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckCapabilityBefUpd
   OperationID: CheckCapabilityBefUpd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckCapabilityBefUpd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCapabilityBefUpd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOKDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOKDelete
   Description: Method used to validate if the Role Code is currently in use by operations,
employees or projects
   OperationID: ValidateOKDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOKDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOKDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRoleCd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRoleCd
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPrjRoleRt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPrjRoleRt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPrjRoleRt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPrjRoleRt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPrjRoleRt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RoleCdSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PrjRoleRtRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PrjRoleRtRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RoleCdListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RoleCdRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RoleCdRow] = obj["value"]
      pass

class Erp_Tablesets_PrjRoleRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Role Code  """  
      self.RateEffDte:str = obj["RateEffDte"]
      """  The effective date of the project role code rate.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.Rate:int = obj["Rate"]
      """  The charge rate for role code expressed in the designated currency code.  """  
      self.RateEndDte:str = obj["RateEndDte"]
      """  The end date of the project role code rate.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence field used to keep the primary key unique  """  
      self.GlobalPrjRoleRt:bool = obj["GlobalPrjRoleRt"]
      """  Marks this PrjRoleRt as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoleCdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Unique identifier of this role assigned by the user.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      """  A description of the role.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this role is available in certain drop-down selection lists.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Determines whether or not this role is a commisionable role.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.UseResGrp:bool = obj["UseResGrp"]
      """  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  """  
      self.TimeApprover:bool = obj["TimeApprover"]
      """  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  """  
      self.ExpenseApprover:bool = obj["ExpenseApprover"]
      """  Determines if this Role includes the ability to be chosen as a Expense Approver.  """  
      self.EmployeeRole:bool = obj["EmployeeRole"]
      """  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  """  
      self.ApprovalSupervisorLevel:int = obj["ApprovalSupervisorLevel"]
      """  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  """  
      self.SupervisorRole:bool = obj["SupervisorRole"]
      """  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  """  
      self.ProjectMgrRole:bool = obj["ProjectMgrRole"]
      """  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  """  
      self.GlobalRoleCd:bool = obj["GlobalRoleCd"]
      """  Marks this RoleCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseResGrpDisable:bool = obj["UseResGrpDisable"]
      """  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  """  
      self.TEAppRequired:bool = obj["TEAppRequired"]
      """  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  """  
      self.TEApprovalRole:bool = obj["TEApprovalRole"]
      """  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      """  Long description of the Resource Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoleCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Unique identifier of this role assigned by the user.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      """  A description of the role.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this role is available in certain drop-down selection lists.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Determines whether or not this role is a commisionable role.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.UseResGrp:bool = obj["UseResGrp"]
      """  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  """  
      self.TimeApprover:bool = obj["TimeApprover"]
      """  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  """  
      self.ExpenseApprover:bool = obj["ExpenseApprover"]
      """  Determines if this Role includes the ability to be chosen as a Expense Approver.  """  
      self.EmployeeRole:bool = obj["EmployeeRole"]
      """  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  """  
      self.ApprovalSupervisorLevel:int = obj["ApprovalSupervisorLevel"]
      """  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  """  
      self.SupervisorRole:bool = obj["SupervisorRole"]
      """  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  """  
      self.ProjectMgrRole:bool = obj["ProjectMgrRole"]
      """  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  """  
      self.GlobalRoleCd:bool = obj["GlobalRoleCd"]
      """  Marks this RoleCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseResGrpDisable:bool = obj["UseResGrpDisable"]
      """  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  """  
      self.TEAppRequired:bool = obj["TEAppRequired"]
      """  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  """  
      self.TEApprovalRole:bool = obj["TEApprovalRole"]
      """  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeSupervisorRole_input:
   """ Required : 
   ProposedSupervisorRole
   ds
   """  
   def __init__(self, obj):
      self.ProposedSupervisorRole:bool = obj["ProposedSupervisorRole"]
      """  The proposed supervisor role value  """  
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

class ChangeSupervisorRole_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckCapabilityBefUpd_input:
   """ Required : 
   iCapabilityID
   iDescription
   iResourceGrpID
   """  
   def __init__(self, obj):
      self.iCapabilityID:str = obj["iCapabilityID"]
      self.iDescription:str = obj["iDescription"]
      self.iResourceGrpID:str = obj["iResourceGrpID"]
      pass

class CheckCapabilityBefUpd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oResourceGrp:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   roleCode
   """  
   def __init__(self, obj):
      self.roleCode:str = obj["roleCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PrjRoleRtRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Role Code  """  
      self.RateEffDte:str = obj["RateEffDte"]
      """  The effective date of the project role code rate.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.Rate:int = obj["Rate"]
      """  The charge rate for role code expressed in the designated currency code.  """  
      self.RateEndDte:str = obj["RateEndDte"]
      """  The end date of the project role code rate.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence field used to keep the primary key unique  """  
      self.GlobalPrjRoleRt:bool = obj["GlobalPrjRoleRt"]
      """  Marks this PrjRoleRt as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoleCdListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Unique identifier of this role assigned by the user.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      """  A description of the role.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this role is available in certain drop-down selection lists.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Determines whether or not this role is a commisionable role.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.UseResGrp:bool = obj["UseResGrp"]
      """  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  """  
      self.TimeApprover:bool = obj["TimeApprover"]
      """  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  """  
      self.ExpenseApprover:bool = obj["ExpenseApprover"]
      """  Determines if this Role includes the ability to be chosen as a Expense Approver.  """  
      self.EmployeeRole:bool = obj["EmployeeRole"]
      """  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  """  
      self.ApprovalSupervisorLevel:int = obj["ApprovalSupervisorLevel"]
      """  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  """  
      self.SupervisorRole:bool = obj["SupervisorRole"]
      """  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  """  
      self.ProjectMgrRole:bool = obj["ProjectMgrRole"]
      """  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  """  
      self.GlobalRoleCd:bool = obj["GlobalRoleCd"]
      """  Marks this RoleCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseResGrpDisable:bool = obj["UseResGrpDisable"]
      """  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  """  
      self.TEAppRequired:bool = obj["TEAppRequired"]
      """  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  """  
      self.TEApprovalRole:bool = obj["TEApprovalRole"]
      """  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      """  Long description of the Resource Group.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoleCdListTableset:
   def __init__(self, obj):
      self.RoleCdList:list[Erp_Tablesets_RoleCdListRow] = obj["RoleCdList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RoleCdRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Unique identifier of this role assigned by the user.  """  
      self.RoleDescription:str = obj["RoleDescription"]
      """  A description of the role.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Determines whether or not this role is available in certain drop-down selection lists.  """  
      self.Commissionable:bool = obj["Commissionable"]
      """  Determines whether or not this role is a commisionable role.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code uniquely identifies a Resource Group.  Cannot be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.UseResGrp:bool = obj["UseResGrp"]
      """  Indicates whether this Role Code can be used fro applications that require a resource group ID and billing rates (such as project billing)  """  
      self.TimeApprover:bool = obj["TimeApprover"]
      """  Determines if this Role includes the ability to be chosen as a Timesheet Approver.  """  
      self.ExpenseApprover:bool = obj["ExpenseApprover"]
      """  Determines if this Role includes the ability to be chosen as a Expense Approver.  """  
      self.EmployeeRole:bool = obj["EmployeeRole"]
      """  Indicates if this role code is an employee role.  Is used in Task creation for time and expense approvals.  If task has a role code assigned to it where EmployeeRole is true, a task will automatically be created for the employee the time or expense is for.  """  
      self.ApprovalSupervisorLevel:int = obj["ApprovalSupervisorLevel"]
      """  Used for time and expense approval tasks.  The number of levels of supervisors above the employee where the approval responsibility lies.  Zero indicates the employee's supervisor does not approve.  One indicates the employee's supervisor (EmpBasic.SupervisorID) does approve. Two indicates that you need to find the employee's supervisor's supervisor, and so on.  """  
      self.SupervisorRole:bool = obj["SupervisorRole"]
      """  Indicates this role is for supervisors.  Used in conjunction with ApprovalSupervisorLevel to determine the supervisor an approval task is created for.  """  
      self.ProjectMgrRole:bool = obj["ProjectMgrRole"]
      """  Indicates this role is for project managers.  When the Project Manager check box is selected and used in a Workforce Group, then the time/expense approvals process will create an an approval task for the Project Manger.  """  
      self.GlobalRoleCd:bool = obj["GlobalRoleCd"]
      """  Marks this RoleCd as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UseResGrpDisable:bool = obj["UseResGrpDisable"]
      """  Purpose of this column is using  it in RowRule to disable or enable UseResGrp checkbox.  """  
      self.TEAppRequired:bool = obj["TEAppRequired"]
      """  Indicates if time or expense approvals are required.  Rowrules will use this for making some fields enabled or disabled.  """  
      self.TEApprovalRole:bool = obj["TEApprovalRole"]
      """  Combines the ExpenseApprover and TimeApprover fields to display as just one field on the Role Code Maintenance UI.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RoleCdTableset:
   def __init__(self, obj):
      self.RoleCd:list[Erp_Tablesets_RoleCdRow] = obj["RoleCd"]
      self.PrjRoleRt:list[Erp_Tablesets_PrjRoleRtRow] = obj["PrjRoleRt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRoleCdTableset:
   def __init__(self, obj):
      self.RoleCd:list[Erp_Tablesets_RoleCdRow] = obj["RoleCd"]
      self.PrjRoleRt:list[Erp_Tablesets_PrjRoleRtRow] = obj["PrjRoleRt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   roleCode
   """  
   def __init__(self, obj):
      self.roleCode:str = obj["roleCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RoleCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RoleCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RoleCdTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RoleCdListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPrjRoleRt_input:
   """ Required : 
   ds
   roleCd
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      self.roleCd:str = obj["roleCd"]
      pass

class GetNewPrjRoleRt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRoleCd_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

class GetNewRoleCd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRoleCd
   whereClausePrjRoleRt
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRoleCd:str = obj["whereClauseRoleCd"]
      self.whereClausePrjRoleRt:str = obj["whereClausePrjRoleRt"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RoleCdTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtRoleCdTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRoleCdTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RoleCdTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOKDelete_input:
   """ Required : 
   ipRoleCode
   """  
   def __init__(self, obj):
      self.ipRoleCode:str = obj["ipRoleCode"]
      """  The role code value  """  
      pass

class ValidateOKDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opOKDelete:bool = obj["opOKDelete"]
      pass

      """  output parameters  """  

