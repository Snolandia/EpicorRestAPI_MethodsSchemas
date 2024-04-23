import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ProdActivitySvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ProdActivities(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ProdActivities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ProdActivities
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PActivityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities",headers=creds) as resp:
           return await resp.json()

async def post_ProdActivities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ProdActivities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PActivityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PActivityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ProdActivities_Company_ActID(Company, ActID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ProdActivity item
   Description: Calls GetByID to retrieve the ProdActivity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ProdActivity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PActivityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities(" + Company + "," + ActID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ProdActivities_Company_ActID(Company, ActID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ProdActivity for the service
   Description: Calls UpdateExt to update ProdActivity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ProdActivity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PActivityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities(" + Company + "," + ActID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ProdActivities_Company_ActID(Company, ActID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ProdActivity item
   Description: Call UpdateExt to delete ProdActivity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ProdActivity
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities(" + Company + "," + ActID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ProdActivities_Company_ActID_PActDtls(Company, ActID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PActDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PActDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PActDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities(" + Company + "," + ActID + ")/PActDtls",headers=creds) as resp:
           return await resp.json()

async def get_ProdActivities_Company_ActID_PActDtls_Company_ActID_DtailID(Company, ActID, DtailID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PActDtl item
   Description: Calls GetByID to retrieve the PActDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PActDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param DtailID: Desc: DtailID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PActDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/ProdActivities(" + Company + "," + ActID + ")/PActDtls(" + Company + "," + ActID + "," + DtailID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PActDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PActDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PActDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PActDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/PActDtls",headers=creds) as resp:
           return await resp.json()

async def post_PActDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PActDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PActDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PActDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/PActDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PActDtls_Company_ActID_DtailID(Company, ActID, DtailID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PActDtl item
   Description: Calls GetByID to retrieve the PActDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PActDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param DtailID: Desc: DtailID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PActDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/PActDtls(" + Company + "," + ActID + "," + DtailID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PActDtls_Company_ActID_DtailID(Company, ActID, DtailID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PActDtl for the service
   Description: Calls UpdateExt to update PActDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PActDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param DtailID: Desc: DtailID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PActDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/PActDtls(" + Company + "," + ActID + "," + DtailID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PActDtls_Company_ActID_DtailID(Company, ActID, DtailID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PActDtl item
   Description: Call UpdateExt to delete PActDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PActDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActID: Desc: ActID   Required: True
      :param DtailID: Desc: DtailID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/PActDtls(" + Company + "," + ActID + "," + DtailID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PActivityListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePActivity, whereClausePActDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePActivity=" + whereClausePActivity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePActDtl=" + whereClausePActDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(actID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "actID=" + actID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlanID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlanID
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPlanID">plan ID</param><param name="ds">dataset parameter</param>
   OperationID: ChangePlanID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlanID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlanID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Clear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Clear
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">dataset parameter</param>
   OperationID: Clear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Clear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Clear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Refresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Refresh
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">dataset parameter</param>
   OperationID: Refresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Refresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Refresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshPActDtlFormattedTimes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshPActDtlFormattedTimes
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">dataset parameter</param>
   OperationID: RefreshPActDtlFormattedTimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshPActDtlFormattedTimes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshPActDtlFormattedTimes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshPActDtlEndTimeFormatted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshPActDtlEndTimeFormatted
   Description: Purpose: Set EndTime from given EndTimeFormatted
<param name="ds">dataset parameter</param>
   OperationID: RefreshPActDtlEndTimeFormatted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshPActDtlEndTimeFormatted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshPActDtlEndTimeFormatted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPActivity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPActDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPActDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPActDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPActDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPActDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ProdActivitySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PActDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PActDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PActivityListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PActivityListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PActivityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PActivityRow] = obj["value"]
      pass

class Erp_Tablesets_PActDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ActID:int = obj["ActID"]
      """  When creating a new activity the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the activity # of the last record on file and then a 1 to it.  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail.  """  
      self.PAPeriod:int = obj["PAPeriod"]
      """  could be Day/Period/Shift  """  
      self.EstCrewSize:int = obj["EstCrewSize"]
      """  Estimated level of staffing for this time period.  """  
      self.EstProdQty:int = obj["EstProdQty"]
      """  Estimated number of pieces produced for this period.  """  
      self.EstScrapQty:int = obj["EstScrapQty"]
      """  Estimated number of pieces scrapped for this period.  """  
      self.EstNonConfQty:int = obj["EstNonConfQty"]
      """  Estimated Non Conformance Quantity  """  
      self.EstReworkQty:int = obj["EstReworkQty"]
      """  Estimated number of pieces identified as rework for this period  """  
      self.ActCrewSize:int = obj["ActCrewSize"]
      """  Actual level of staffing for this time period.  """  
      self.ActProdQty:int = obj["ActProdQty"]
      """  Actual number of pieces produced for this period.  """  
      self.ActScrapQty:int = obj["ActScrapQty"]
      """  Actual number of pieces scrapped for this period.  """  
      self.ActNonConfQty:int = obj["ActNonConfQty"]
      """  Actual number of pieces non-conformance for this period.  """  
      self.ActReworkQty:int = obj["ActReworkQty"]
      """  Actual number of pieces identified as rework for this period.  """  
      self.EndTime:int = obj["EndTime"]
      """  End Time.  Stored as seconds from midnight  """  
      self.ActComment:str = obj["ActComment"]
      """  Production Activity Comment text.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartTime:int = obj["StartTime"]
      self.EndTimeDT:str = obj["EndTimeDT"]
      self.StartTimeFormatted:str = obj["StartTimeFormatted"]
      """  Stores the StartTime field value in "HH:MM" format.  """  
      self.EndTimeFormatted:str = obj["EndTimeFormatted"]
      """  Stores the EndTime field value in "HH:MM" format.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PActivityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PAPlanID:str = obj["PAPlanID"]
      """  Plan Identifier  """  
      self.Description:str = obj["Description"]
      """  Defaults from PAPlan  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Approved:bool = obj["Approved"]
      """  Checkbox to indicate this is closed and no longer open for transactions.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  User ID of the person who checked the approved box.  Cannot be edited  """  
      self.AppDate:str = obj["AppDate"]
      """  System date of approval.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated Labor Hours  """  
      self.EstBurdenHrs:int = obj["EstBurdenHrs"]
      """  Estimated Burden Hours  """  
      self.EstIndirectHrs:int = obj["EstIndirectHrs"]
      """  Estimated Indirect Hours  """  
      self.EstReworkHrs:int = obj["EstReworkHrs"]
      """  Estimated Rework Hours  """  
      self.ActLaborHrs:int = obj["ActLaborHrs"]
      """  Actual Labor Hours  """  
      self.ActBurdenHrs:int = obj["ActBurdenHrs"]
      """  Actual Burden Hours  """  
      self.ActIndirectHrs:int = obj["ActIndirectHrs"]
      """  Actual Indirect Hours  """  
      self.ActReworkHrs:int = obj["ActReworkHrs"]
      """  Actual Rework Hours  """  
      self.ActID:int = obj["ActID"]
      """  When creating a new activity the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the activity # of the last record on file and then a 1 to it.  """  
      self.ActComments:str = obj["ActComments"]
      """  Activity Comments  """  
      self.ActivityDate:str = obj["ActivityDate"]
      """  Date for this the activity is being recorded.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResGrpDesc:str = obj["ResGrpDesc"]
      self.ResDesc:str = obj["ResDesc"]
      self.DisablDtlET:bool = obj["DisablDtlET"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PActivityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PAPlanID:str = obj["PAPlanID"]
      """  Plan Identifier  """  
      self.Description:str = obj["Description"]
      """  Defaults from PAPlan  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Approved:bool = obj["Approved"]
      """  Checkbox to indicate this is closed and no longer open for transactions.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  User ID of the person who checked the approved box.  Cannot be edited  """  
      self.AppDate:str = obj["AppDate"]
      """  System date of approval.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated Labor Hours  """  
      self.EstBurdenHrs:int = obj["EstBurdenHrs"]
      """  Estimated Burden Hours  """  
      self.EstIndirectHrs:int = obj["EstIndirectHrs"]
      """  Estimated Indirect Hours  """  
      self.EstReworkHrs:int = obj["EstReworkHrs"]
      """  Estimated Rework Hours  """  
      self.ActLaborHrs:int = obj["ActLaborHrs"]
      """  Actual Labor Hours  """  
      self.ActBurdenHrs:int = obj["ActBurdenHrs"]
      """  Actual Burden Hours  """  
      self.ActIndirectHrs:int = obj["ActIndirectHrs"]
      """  Actual Indirect Hours  """  
      self.ActReworkHrs:int = obj["ActReworkHrs"]
      """  Actual Rework Hours  """  
      self.ActID:int = obj["ActID"]
      """  When creating a new activity the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the activity # of the last record on file and then a 1 to it.  """  
      self.ActComments:str = obj["ActComments"]
      """  Activity Comments  """  
      self.ActivityDate:str = obj["ActivityDate"]
      """  Date for this the activity is being recorded.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResGrpDesc:str = obj["ResGrpDesc"]
      self.ResDesc:str = obj["ResDesc"]
      self.DisablDtlET:bool = obj["DisablDtlET"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangePlanID_input:
   """ Required : 
   ipPlanID
   ds
   """  
   def __init__(self, obj):
      self.ipPlanID:str = obj["ipPlanID"]
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class ChangePlanID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Clear_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class Clear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   actID
   """  
   def __init__(self, obj):
      self.actID:int = obj["actID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PActDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ActID:int = obj["ActID"]
      """  When creating a new activity the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the activity # of the last record on file and then a 1 to it.  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail.  """  
      self.PAPeriod:int = obj["PAPeriod"]
      """  could be Day/Period/Shift  """  
      self.EstCrewSize:int = obj["EstCrewSize"]
      """  Estimated level of staffing for this time period.  """  
      self.EstProdQty:int = obj["EstProdQty"]
      """  Estimated number of pieces produced for this period.  """  
      self.EstScrapQty:int = obj["EstScrapQty"]
      """  Estimated number of pieces scrapped for this period.  """  
      self.EstNonConfQty:int = obj["EstNonConfQty"]
      """  Estimated Non Conformance Quantity  """  
      self.EstReworkQty:int = obj["EstReworkQty"]
      """  Estimated number of pieces identified as rework for this period  """  
      self.ActCrewSize:int = obj["ActCrewSize"]
      """  Actual level of staffing for this time period.  """  
      self.ActProdQty:int = obj["ActProdQty"]
      """  Actual number of pieces produced for this period.  """  
      self.ActScrapQty:int = obj["ActScrapQty"]
      """  Actual number of pieces scrapped for this period.  """  
      self.ActNonConfQty:int = obj["ActNonConfQty"]
      """  Actual number of pieces non-conformance for this period.  """  
      self.ActReworkQty:int = obj["ActReworkQty"]
      """  Actual number of pieces identified as rework for this period.  """  
      self.EndTime:int = obj["EndTime"]
      """  End Time.  Stored as seconds from midnight  """  
      self.ActComment:str = obj["ActComment"]
      """  Production Activity Comment text.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.StartTime:int = obj["StartTime"]
      self.EndTimeDT:str = obj["EndTimeDT"]
      self.StartTimeFormatted:str = obj["StartTimeFormatted"]
      """  Stores the StartTime field value in "HH:MM" format.  """  
      self.EndTimeFormatted:str = obj["EndTimeFormatted"]
      """  Stores the EndTime field value in "HH:MM" format.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PActivityListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PAPlanID:str = obj["PAPlanID"]
      """  Plan Identifier  """  
      self.Description:str = obj["Description"]
      """  Defaults from PAPlan  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Approved:bool = obj["Approved"]
      """  Checkbox to indicate this is closed and no longer open for transactions.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  User ID of the person who checked the approved box.  Cannot be edited  """  
      self.AppDate:str = obj["AppDate"]
      """  System date of approval.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated Labor Hours  """  
      self.EstBurdenHrs:int = obj["EstBurdenHrs"]
      """  Estimated Burden Hours  """  
      self.EstIndirectHrs:int = obj["EstIndirectHrs"]
      """  Estimated Indirect Hours  """  
      self.EstReworkHrs:int = obj["EstReworkHrs"]
      """  Estimated Rework Hours  """  
      self.ActLaborHrs:int = obj["ActLaborHrs"]
      """  Actual Labor Hours  """  
      self.ActBurdenHrs:int = obj["ActBurdenHrs"]
      """  Actual Burden Hours  """  
      self.ActIndirectHrs:int = obj["ActIndirectHrs"]
      """  Actual Indirect Hours  """  
      self.ActReworkHrs:int = obj["ActReworkHrs"]
      """  Actual Rework Hours  """  
      self.ActID:int = obj["ActID"]
      """  When creating a new activity the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the activity # of the last record on file and then a 1 to it.  """  
      self.ActComments:str = obj["ActComments"]
      """  Activity Comments  """  
      self.ActivityDate:str = obj["ActivityDate"]
      """  Date for this the activity is being recorded.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResGrpDesc:str = obj["ResGrpDesc"]
      self.ResDesc:str = obj["ResDesc"]
      self.DisablDtlET:bool = obj["DisablDtlET"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PActivityListTableset:
   def __init__(self, obj):
      self.PActivityList:list[Erp_Tablesets_PActivityListRow] = obj["PActivityList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PActivityRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PAPlanID:str = obj["PAPlanID"]
      """  Plan Identifier  """  
      self.Description:str = obj["Description"]
      """  Defaults from PAPlan  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.Approved:bool = obj["Approved"]
      """  Checkbox to indicate this is closed and no longer open for transactions.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  User ID of the person who checked the approved box.  Cannot be edited  """  
      self.AppDate:str = obj["AppDate"]
      """  System date of approval.  """  
      self.EstLaborHours:int = obj["EstLaborHours"]
      """  Estimated Labor Hours  """  
      self.EstBurdenHrs:int = obj["EstBurdenHrs"]
      """  Estimated Burden Hours  """  
      self.EstIndirectHrs:int = obj["EstIndirectHrs"]
      """  Estimated Indirect Hours  """  
      self.EstReworkHrs:int = obj["EstReworkHrs"]
      """  Estimated Rework Hours  """  
      self.ActLaborHrs:int = obj["ActLaborHrs"]
      """  Actual Labor Hours  """  
      self.ActBurdenHrs:int = obj["ActBurdenHrs"]
      """  Actual Burden Hours  """  
      self.ActIndirectHrs:int = obj["ActIndirectHrs"]
      """  Actual Indirect Hours  """  
      self.ActReworkHrs:int = obj["ActReworkHrs"]
      """  Actual Rework Hours  """  
      self.ActID:int = obj["ActID"]
      """  When creating a new activity the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the activity # of the last record on file and then a 1 to it.  """  
      self.ActComments:str = obj["ActComments"]
      """  Activity Comments  """  
      self.ActivityDate:str = obj["ActivityDate"]
      """  Date for this the activity is being recorded.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ResGrpDesc:str = obj["ResGrpDesc"]
      self.ResDesc:str = obj["ResDesc"]
      self.DisablDtlET:bool = obj["DisablDtlET"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ProdActivityTableset:
   def __init__(self, obj):
      self.PActivity:list[Erp_Tablesets_PActivityRow] = obj["PActivity"]
      self.PActDtl:list[Erp_Tablesets_PActDtlRow] = obj["PActDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtProdActivityTableset:
   def __init__(self, obj):
      self.PActivity:list[Erp_Tablesets_PActivityRow] = obj["PActivity"]
      self.PActDtl:list[Erp_Tablesets_PActDtlRow] = obj["PActDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   actID
   """  
   def __init__(self, obj):
      self.actID:int = obj["actID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProdActivityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProdActivityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ProdActivityTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PActivityListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPActDtl_input:
   """ Required : 
   ds
   actID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      self.actID:int = obj["actID"]
      pass

class GetNewPActDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPActivity_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class GetNewPActivity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePActivity
   whereClausePActDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePActivity:str = obj["whereClausePActivity"]
      self.whereClausePActDtl:str = obj["whereClausePActDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProdActivityTableset] = obj["returnObj"]
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

class RefreshPActDtlEndTimeFormatted_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class RefreshPActDtlEndTimeFormatted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshPActDtlFormattedTimes_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class RefreshPActDtlFormattedTimes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Refresh_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class Refresh_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProdActivityTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtProdActivityTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProdActivityTableset] = obj["ds"]
      pass

      """  output parameters  """  

