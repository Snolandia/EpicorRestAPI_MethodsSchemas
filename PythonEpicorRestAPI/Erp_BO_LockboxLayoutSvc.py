import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LockboxLayoutSvc
# Description: Main BO for Lockbox Layout UI.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LockboxLayouts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LockboxLayouts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LockboxLayouts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts",headers=creds) as resp:
           return await resp.json()

async def post_LockboxLayouts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LockboxLayouts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LockboxLayouts_Company_LayoutID(Company, LayoutID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LockboxLayout item
   Description: Calls GetByID to retrieve the LockboxLayout item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxLayout
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LockboxLayouts_Company_LayoutID(Company, LayoutID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LockboxLayout for the service
   Description: Calls UpdateExt to update LockboxLayout. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LockboxLayout
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LockboxLayouts_Company_LayoutID(Company, LayoutID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LockboxLayout item
   Description: Call UpdateExt to delete LockboxLayout item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LockboxLayout
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LockboxLayouts_Company_LayoutID_LockboxLayoutDtls(Company, LayoutID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LockboxLayoutDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LockboxLayoutDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")/LockboxLayoutDtls",headers=creds) as resp:
           return await resp.json()

async def get_LockboxLayouts_Company_LayoutID_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company, LayoutID, RecordTypeID, FieldID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LockboxLayoutDtl item
   Description: Calls GetByID to retrieve the LockboxLayoutDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxLayoutDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param RecordTypeID: Desc: RecordTypeID   Required: True   Allow empty value : True
      :param FieldID: Desc: FieldID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayouts(" + Company + "," + LayoutID + ")/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LockboxLayoutDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LockboxLayoutDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LockboxLayoutDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls",headers=creds) as resp:
           return await resp.json()

async def post_LockboxLayoutDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LockboxLayoutDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company, LayoutID, RecordTypeID, FieldID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LockboxLayoutDtl item
   Description: Calls GetByID to retrieve the LockboxLayoutDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LockboxLayoutDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param RecordTypeID: Desc: RecordTypeID   Required: True   Allow empty value : True
      :param FieldID: Desc: FieldID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company, LayoutID, RecordTypeID, FieldID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LockboxLayoutDtl for the service
   Description: Calls UpdateExt to update LockboxLayoutDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LockboxLayoutDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param RecordTypeID: Desc: RecordTypeID   Required: True   Allow empty value : True
      :param FieldID: Desc: FieldID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LockboxLayoutDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LockboxLayoutDtls_Company_LayoutID_RecordTypeID_FieldID(Company, LayoutID, RecordTypeID, FieldID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LockboxLayoutDtl item
   Description: Call UpdateExt to delete LockboxLayoutDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LockboxLayoutDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LayoutID: Desc: LayoutID   Required: True   Allow empty value : True
      :param RecordTypeID: Desc: RecordTypeID   Required: True   Allow empty value : True
      :param FieldID: Desc: FieldID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/LockboxLayoutDtls(" + Company + "," + LayoutID + "," + RecordTypeID + "," + FieldID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LockboxLayoutHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLockboxLayoutHead, whereClauseLockboxLayoutDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseLockboxLayoutHead=" + whereClauseLockboxLayoutHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLockboxLayoutDtl=" + whereClauseLockboxLayoutDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(layoutID, epicorHeaders = None):
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
   params += "layoutID=" + layoutID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnReadyToUseChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnReadyToUseChange
   Description: This method is called when the layout is set as Ready
   OperationID: OnReadyToUseChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnReadyToUseChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnReadyToUseChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLockboxLayoutHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLockboxLayoutHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLockboxLayoutHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLockboxLayoutHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLockboxLayoutHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLockboxLayoutDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLockboxLayoutDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLockboxLayoutDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLockboxLayoutDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLockboxLayoutDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LockboxLayoutSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LockboxLayoutDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LockboxLayoutHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LockboxLayoutHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LockboxLayoutHeadRow] = obj["value"]
      pass

class Erp_Tablesets_LockboxLayoutDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LayoutID:str = obj["LayoutID"]
      """  Read-only Layout ID  """  
      self.RecordTypeID:str = obj["RecordTypeID"]
      """  Value for record type selection  """  
      self.FieldID:str = obj["FieldID"]
      """  Read-only Field ID for field selection  """  
      self.Offset:int = obj["Offset"]
      """  The position in the Lockbox record where the field data starts.  """  
      self.Length:int = obj["Length"]
      """  Default is zero. Available are positive values not exceeding length of record.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndingPos:int = obj["EndingPos"]
      """   Ending position within the record string.
This is the sum of offset and length.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  This field will show the format for the given field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LayoutFldSchemaName:str = obj["LayoutFldSchemaName"]
      self.LayoutFldTableName:str = obj["LayoutFldTableName"]
      self.LayoutFldColumnName:str = obj["LayoutFldColumnName"]
      self.LayoutFldFieldName:str = obj["LayoutFldFieldName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxLayoutHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LayoutID:str = obj["LayoutID"]
      """  Initiates Lockbox Layout ID search.  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  Layout Description  """  
      self.DecPointPos:int = obj["DecPointPos"]
      """  Number of decimals in amount, acceptable values 0 to 3, Default is 2  """  
      self.ReadyToUse:bool = obj["ReadyToUse"]
      """  Indicates that the Layout is ready to be used in Lockbox Processing.  """  
      self.DateFormat:str = obj["DateFormat"]
      """  Default value  is ‘YYMMDD’ User can enter any value.  """  
      self.AutoPost:bool = obj["AutoPost"]
      """  Identifies if ‘postable’ Cash Receipt group is posted.  """  
      self.UnderPayAutoPost:bool = obj["UnderPayAutoPost"]
      """  Depreciated  """  
      self.ValidateTotals:bool = obj["ValidateTotals"]
      """  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  """  
      self.ErrorBatchDiscard:bool = obj["ErrorBatchDiscard"]
      """  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  """  
      self.AllowOnAcc:bool = obj["AllowOnAcc"]
      """  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  """  
      self.OnInvoiceErrorSetOnAcc:bool = obj["OnInvoiceErrorSetOnAcc"]
      """  Determine if lockbox should automatically accept an invoice payment with errors into the customer’s account, allowing the payment to be processed into the system without manual intervention.  """  
      self.AllowOverpayOnAcc:bool = obj["AllowOverpayOnAcc"]
      """  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxLayoutHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LayoutID:str = obj["LayoutID"]
      """  Initiates Lockbox Layout ID search.  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  Layout Description  """  
      self.DecPointPos:int = obj["DecPointPos"]
      """  Number of decimals in amount, acceptable values 0 to 3, Default is 2  """  
      self.ReadyToUse:bool = obj["ReadyToUse"]
      """  Indicates that the Layout is ready to be used in Lockbox Processing.  """  
      self.DateFormat:str = obj["DateFormat"]
      """  Default value  is ‘YYMMDD’ User can enter any value.  """  
      self.AutoPost:bool = obj["AutoPost"]
      """  Identifies if ‘postable’ Cash Receipt group is posted.  """  
      self.ValidateTotals:bool = obj["ValidateTotals"]
      """  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  """  
      self.ErrorBatchDiscard:bool = obj["ErrorBatchDiscard"]
      """  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  """  
      self.AllowOnAcc:bool = obj["AllowOnAcc"]
      """  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  """  
      self.AllowOverpayOnAcc:bool = obj["AllowOverpayOnAcc"]
      """  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RecordTypeID:str = obj["RecordTypeID"]
      self.TestFile:str = obj["TestFile"]
      """  Location of the file to test the layout.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ARSystAllowOverpaidInv:bool = obj["ARSystAllowOverpaidInv"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   layoutID
   """  
   def __init__(self, obj):
      self.layoutID:str = obj["layoutID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_LockboxLayoutDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LayoutID:str = obj["LayoutID"]
      """  Read-only Layout ID  """  
      self.RecordTypeID:str = obj["RecordTypeID"]
      """  Value for record type selection  """  
      self.FieldID:str = obj["FieldID"]
      """  Read-only Field ID for field selection  """  
      self.Offset:int = obj["Offset"]
      """  The position in the Lockbox record where the field data starts.  """  
      self.Length:int = obj["Length"]
      """  Default is zero. Available are positive values not exceeding length of record.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndingPos:int = obj["EndingPos"]
      """   Ending position within the record string.
This is the sum of offset and length.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  This field will show the format for the given field.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LayoutFldSchemaName:str = obj["LayoutFldSchemaName"]
      self.LayoutFldTableName:str = obj["LayoutFldTableName"]
      self.LayoutFldColumnName:str = obj["LayoutFldColumnName"]
      self.LayoutFldFieldName:str = obj["LayoutFldFieldName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxLayoutHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LayoutID:str = obj["LayoutID"]
      """  Initiates Lockbox Layout ID search.  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  Layout Description  """  
      self.DecPointPos:int = obj["DecPointPos"]
      """  Number of decimals in amount, acceptable values 0 to 3, Default is 2  """  
      self.ReadyToUse:bool = obj["ReadyToUse"]
      """  Indicates that the Layout is ready to be used in Lockbox Processing.  """  
      self.DateFormat:str = obj["DateFormat"]
      """  Default value  is ‘YYMMDD’ User can enter any value.  """  
      self.AutoPost:bool = obj["AutoPost"]
      """  Identifies if ‘postable’ Cash Receipt group is posted.  """  
      self.UnderPayAutoPost:bool = obj["UnderPayAutoPost"]
      """  Depreciated  """  
      self.ValidateTotals:bool = obj["ValidateTotals"]
      """  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  """  
      self.ErrorBatchDiscard:bool = obj["ErrorBatchDiscard"]
      """  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  """  
      self.AllowOnAcc:bool = obj["AllowOnAcc"]
      """  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  """  
      self.OnInvoiceErrorSetOnAcc:bool = obj["OnInvoiceErrorSetOnAcc"]
      """  Determine if lockbox should automatically accept an invoice payment with errors into the customer’s account, allowing the payment to be processed into the system without manual intervention.  """  
      self.AllowOverpayOnAcc:bool = obj["AllowOverpayOnAcc"]
      """  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxLayoutHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LayoutID:str = obj["LayoutID"]
      """  Initiates Lockbox Layout ID search.  """  
      self.LayoutDescription:str = obj["LayoutDescription"]
      """  Layout Description  """  
      self.DecPointPos:int = obj["DecPointPos"]
      """  Number of decimals in amount, acceptable values 0 to 3, Default is 2  """  
      self.ReadyToUse:bool = obj["ReadyToUse"]
      """  Indicates that the Layout is ready to be used in Lockbox Processing.  """  
      self.DateFormat:str = obj["DateFormat"]
      """  Default value  is ‘YYMMDD’ User can enter any value.  """  
      self.AutoPost:bool = obj["AutoPost"]
      """  Identifies if ‘postable’ Cash Receipt group is posted.  """  
      self.ValidateTotals:bool = obj["ValidateTotals"]
      """  Allows to determine if the system validates the File Total Amount/Record count and the Batch Total Amount/Check Count. If the totals or counts calculation fails at a File level, the entire file will be discarded.  """  
      self.ErrorBatchDiscard:bool = obj["ErrorBatchDiscard"]
      """  Allows to determine if the system logs a failed Batch Total/Count but may continue to validate and load the next batch instead of discarding the entire file if the batch validation fails.  """  
      self.AllowOnAcc:bool = obj["AllowOnAcc"]
      """  To determine if lockbox should accept payments with no invoice references on it and record them as “On Account” for the customer.  """  
      self.AllowOverpayOnAcc:bool = obj["AllowOverpayOnAcc"]
      """  Determine if I want the extra amount that was overpaid on any given invoice to be recorded as ‘On Account’ for the customer.  """  
      self.AllowOverpaidInv:bool = obj["AllowOverpaidInv"]
      """  Reference to “Allow Invoices to be overpaid” option available in Company Configuration under the Modules > All Modules > Localization > Detail screen). When true, lockbox posts any check that contains an overpayment on any of its invoices.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RecordTypeID:str = obj["RecordTypeID"]
      self.TestFile:str = obj["TestFile"]
      """  Location of the file to test the layout.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ARSystAllowOverpaidInv:bool = obj["ARSystAllowOverpaidInv"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LockboxLayoutListTableset:
   def __init__(self, obj):
      self.LockboxLayoutHeadList:list[Erp_Tablesets_LockboxLayoutHeadListRow] = obj["LockboxLayoutHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LockboxLayoutTableset:
   def __init__(self, obj):
      self.LockboxLayoutHead:list[Erp_Tablesets_LockboxLayoutHeadRow] = obj["LockboxLayoutHead"]
      self.LockboxLayoutDtl:list[Erp_Tablesets_LockboxLayoutDtlRow] = obj["LockboxLayoutDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtLockboxLayoutTableset:
   def __init__(self, obj):
      self.LockboxLayoutHead:list[Erp_Tablesets_LockboxLayoutHeadRow] = obj["LockboxLayoutHead"]
      self.LockboxLayoutDtl:list[Erp_Tablesets_LockboxLayoutDtlRow] = obj["LockboxLayoutDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   layoutID
   """  
   def __init__(self, obj):
      self.layoutID:str = obj["layoutID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LockboxLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LockboxLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LockboxLayoutTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LockboxLayoutListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLockboxLayoutDtl_input:
   """ Required : 
   ds
   layoutID
   recordTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      self.layoutID:str = obj["layoutID"]
      self.recordTypeID:str = obj["recordTypeID"]
      pass

class GetNewLockboxLayoutDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLockboxLayoutHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

class GetNewLockboxLayoutHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLockboxLayoutHead
   whereClauseLockboxLayoutDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLockboxLayoutHead:str = obj["whereClauseLockboxLayoutHead"]
      self.whereClauseLockboxLayoutDtl:str = obj["whereClauseLockboxLayoutDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LockboxLayoutTableset] = obj["returnObj"]
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

class OnReadyToUseChange_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

class OnReadyToUseChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLockboxLayoutTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLockboxLayoutTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LockboxLayoutTableset] = obj["ds"]
      pass

      """  output parameters  """  

