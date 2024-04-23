import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.INGSTR2ReportExportSvc
# Description: INGSTR2ReportExport
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportExports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2ReportExports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2ReportExports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportExportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR2ReportExports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2ReportExports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportExports_Company_Key1(Company, Key1, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2ReportExport item
   Description: Calls GetByID to retrieve the INGSTR2ReportExport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportExport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports(" + Company + "," + Key1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR2ReportExports_Company_Key1(Company, Key1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR2ReportExport for the service
   Description: Calls UpdateExt to update INGSTR2ReportExport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2ReportExport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports(" + Company + "," + Key1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR2ReportExports_Company_Key1(Company, Key1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR2ReportExport item
   Description: Call UpdateExt to delete INGSTR2ReportExport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2ReportExport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports(" + Company + "," + Key1 + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportExports_Company_Key1_INGSTR2ReportExportDtls(Company, Key1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get INGSTR2ReportExportDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_INGSTR2ReportExportDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportExportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports(" + Company + "," + Key1 + ")/INGSTR2ReportExportDtls",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportExports_Company_Key1_INGSTR2ReportExportDtls_Company_Key1_IntKey1_Key2(Company, Key1, IntKey1, Key2, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2ReportExportDtl item
   Description: Calls GetByID to retrieve the INGSTR2ReportExportDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportExportDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExports(" + Company + "," + Key1 + ")/INGSTR2ReportExportDtls(" + Company + "," + Key1 + "," + IntKey1 + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportExportDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get INGSTR2ReportExportDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_INGSTR2ReportExportDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportExportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExportDtls",headers=creds) as resp:
           return await resp.json()

async def post_INGSTR2ReportExportDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_INGSTR2ReportExportDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExportDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_INGSTR2ReportExportDtls_Company_Key1_IntKey1_Key2(Company, Key1, IntKey1, Key2, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the INGSTR2ReportExportDtl item
   Description: Calls GetByID to retrieve the INGSTR2ReportExportDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_INGSTR2ReportExportDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExportDtls(" + Company + "," + Key1 + "," + IntKey1 + "," + Key2 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_INGSTR2ReportExportDtls_Company_Key1_IntKey1_Key2(Company, Key1, IntKey1, Key2, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update INGSTR2ReportExportDtl for the service
   Description: Calls UpdateExt to update INGSTR2ReportExportDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_INGSTR2ReportExportDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.INGSTR2ReportExportDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExportDtls(" + Company + "," + Key1 + "," + IntKey1 + "," + Key2 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_INGSTR2ReportExportDtls_Company_Key1_IntKey1_Key2(Company, Key1, IntKey1, Key2, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete INGSTR2ReportExportDtl item
   Description: Call UpdateExt to delete INGSTR2ReportExportDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_INGSTR2ReportExportDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param IntKey1: Desc: IntKey1   Required: True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/INGSTR2ReportExportDtls(" + Company + "," + Key1 + "," + IntKey1 + "," + Key2 + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.INGSTR2ReportExportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseINGSTR2ReportExport, whereClauseINGSTR2ReportExportDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseINGSTR2ReportExport=" + whereClauseINGSTR2ReportExport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseINGSTR2ReportExportDtl=" + whereClauseINGSTR2ReportExportDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(key1, epicorHeaders = None):
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
   params += "key1=" + key1

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckBeforeCreate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBeforeCreate
   Description: Validate if other reports exist for the period
   OperationID: CheckBeforeCreate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBeforeCreate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforeCreate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvoices(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvoices
   Description: Get Invoices to be included into report
   OperationID: GetInvoices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSubmit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSubmit
   Description: Submit/Reset report
   OperationID: ChangeSubmit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSubmit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSubmit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR2ReportExport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR2ReportExport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2ReportExport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2ReportExport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2ReportExport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewINGSTR2ReportExportDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewINGSTR2ReportExportDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewINGSTR2ReportExportDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewINGSTR2ReportExportDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewINGSTR2ReportExportDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.INGSTR2ReportExportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportExportDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2ReportExportDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportExportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2ReportExportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_INGSTR2ReportExportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_INGSTR2ReportExportRow] = obj["value"]
      pass

class Erp_Tablesets_INGSTR2ReportExportDtlRow:
   def __init__(self, obj):
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.IntKey1:int = obj["IntKey1"]
      """  Integer Key field 1  """  
      self.Key1:str = obj["Key1"]
      """  Character Key field 1  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.Key2:str = obj["Key2"]
      """  Character Key field 2  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.VendorNum:int = obj["VendorNum"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportExportListRow:
   def __init__(self, obj):
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportExportRow:
   def __init__(self, obj):
      self.ChangeDate:str = obj["ChangeDate"]
      """  When changed it?  """  
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Who changed it?  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.CreateDate:str = obj["CreateDate"]
      """  When added to the report?  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Who added this to the report?  """  
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.FromDate:str = obj["FromDate"]
      """  First date of the report period  """  
      self.Number01:int = obj["Number01"]
      self.InvNumSource:str = obj["InvNumSource"]
      """  What number: Invoice or Legal will be exported?  """  
      self.IsSubmitted:bool = obj["IsSubmitted"]
      """  If On, all fields on UI are disabled  """  
      self.MinimumInvTotal:int = obj["MinimumInvTotal"]
      """  Minimum Invoice Amount  """  
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.ReportDate:str = obj["ReportDate"]
      """  Report Date  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.ReportPeriod:str = obj["ReportPeriod"]
      """  MMYYYY  """  
      self.ResponseAckDate:str = obj["ResponseAckDate"]
      """  ResponseAckDate  """  
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.ResponseAckNum:str = obj["ResponseAckNum"]
      """  ResponseAckNum  """  
      self.ResponseStatus:str = obj["ResponseStatus"]
      """  ResponseStatus  """  
      self.SubmitDate:str = obj["SubmitDate"]
      """  Submit Date  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  Who submitted the report?  """  
      self.SupplierFilter:str = obj["SupplierFilter"]
      """  Supplier Filter  """  
      self.TaxLiabilityFilter:str = obj["TaxLiabilityFilter"]
      """  Tax Liability Filter  """  
      self.TaxTypeFilter:str = obj["TaxTypeFilter"]
      """  Tax Type Filter  """  
      self.ToDate:str = obj["ToDate"]
      """  Last date of the report period  """  
      self.Date06:str = obj["Date06"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SupplierIDFilter:str = obj["SupplierIDFilter"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeSubmit_input:
   """ Required : 
   sysRowID
   isSubmitted
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID of Report Header Record  """  
      self.isSubmitted:bool = obj["isSubmitted"]
      """  Submit value  """  
      pass

class ChangeSubmit_output:
   def __init__(self, obj):
      pass

class CheckBeforeCreate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

class CheckBeforeCreate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningText:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   key1
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_INGSTR2ReportExportDtlRow:
   def __init__(self, obj):
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.IntKey1:int = obj["IntKey1"]
      """  Integer Key field 1  """  
      self.Key1:str = obj["Key1"]
      """  Character Key field 1  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.Key2:str = obj["Key2"]
      """  Character Key field 2  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  InvoiceNum  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.VendorNum:int = obj["VendorNum"]
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportExportListRow:
   def __init__(self, obj):
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportExportListTableset:
   def __init__(self, obj):
      self.INGSTR2ReportExportList:list[Erp_Tablesets_INGSTR2ReportExportListRow] = obj["INGSTR2ReportExportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_INGSTR2ReportExportRow:
   def __init__(self, obj):
      self.ChangeDate:str = obj["ChangeDate"]
      """  When changed it?  """  
      self.Company:str = obj["Company"]
      """  Company Code  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Who changed it?  """  
      self.LocalName:str = obj["LocalName"]
      """  Localization Name  """  
      self.Key1:str = obj["Key1"]
      """  Key field 1  """  
      self.Key2:str = obj["Key2"]
      """  Key field 2  """  
      self.Key3:str = obj["Key3"]
      """  Key field 3  """  
      self.Key4:str = obj["Key4"]
      """  Key field 4  """  
      self.Key5:str = obj["Key5"]
      """  Key field 5  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Character01:str = obj["Character01"]
      """  Character01  """  
      self.Character02:str = obj["Character02"]
      self.CreateDate:str = obj["CreateDate"]
      """  When added to the report?  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Who added this to the report?  """  
      self.Character03:str = obj["Character03"]
      self.Character04:str = obj["Character04"]
      self.Character05:str = obj["Character05"]
      self.Character06:str = obj["Character06"]
      self.FromDate:str = obj["FromDate"]
      """  First date of the report period  """  
      self.Number01:int = obj["Number01"]
      self.InvNumSource:str = obj["InvNumSource"]
      """  What number: Invoice or Legal will be exported?  """  
      self.IsSubmitted:bool = obj["IsSubmitted"]
      """  If On, all fields on UI are disabled  """  
      self.MinimumInvTotal:int = obj["MinimumInvTotal"]
      """  Minimum Invoice Amount  """  
      self.Date01:str = obj["Date01"]
      """  not used  """  
      self.Date02:str = obj["Date02"]
      self.ReportDate:str = obj["ReportDate"]
      """  Report Date  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.Date03:str = obj["Date03"]
      self.Date04:str = obj["Date04"]
      self.ReportPeriod:str = obj["ReportPeriod"]
      """  MMYYYY  """  
      self.ResponseAckDate:str = obj["ResponseAckDate"]
      """  ResponseAckDate  """  
      self.Date05:str = obj["Date05"]
      self.CheckBox01:bool = obj["CheckBox01"]
      self.ResponseAckNum:str = obj["ResponseAckNum"]
      """  ResponseAckNum  """  
      self.ResponseStatus:str = obj["ResponseStatus"]
      """  ResponseStatus  """  
      self.SubmitDate:str = obj["SubmitDate"]
      """  Submit Date  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  Who submitted the report?  """  
      self.SupplierFilter:str = obj["SupplierFilter"]
      """  Supplier Filter  """  
      self.TaxLiabilityFilter:str = obj["TaxLiabilityFilter"]
      """  Tax Liability Filter  """  
      self.TaxTypeFilter:str = obj["TaxTypeFilter"]
      """  Tax Type Filter  """  
      self.ToDate:str = obj["ToDate"]
      """  Last date of the report period  """  
      self.Date06:str = obj["Date06"]
      self.ShortChar01:str = obj["ShortChar01"]
      self.ShortChar02:str = obj["ShortChar02"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SupplierIDFilter:str = obj["SupplierIDFilter"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_INGSTR2ReportExportTableset:
   def __init__(self, obj):
      self.INGSTR2ReportExport:list[Erp_Tablesets_INGSTR2ReportExportRow] = obj["INGSTR2ReportExport"]
      self.INGSTR2ReportExportDtl:list[Erp_Tablesets_INGSTR2ReportExportDtlRow] = obj["INGSTR2ReportExportDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtINGSTR2ReportExportTableset:
   def __init__(self, obj):
      self.INGSTR2ReportExport:list[Erp_Tablesets_INGSTR2ReportExportRow] = obj["INGSTR2ReportExport"]
      self.INGSTR2ReportExportDtl:list[Erp_Tablesets_INGSTR2ReportExportDtlRow] = obj["INGSTR2ReportExportDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   key1
   """  
   def __init__(self, obj):
      self.key1:str = obj["key1"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["returnObj"]
      pass

class GetInvoices_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      """  Report ID  """  
      pass

class GetInvoices_output:
   def __init__(self, obj):
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
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportExportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewINGSTR2ReportExportDtl_input:
   """ Required : 
   ds
   key1
   intKey1
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      self.key1:str = obj["key1"]
      self.intKey1:int = obj["intKey1"]
      pass

class GetNewINGSTR2ReportExportDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewINGSTR2ReportExport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

class GetNewINGSTR2ReportExport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseINGSTR2ReportExport
   whereClauseINGSTR2ReportExportDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseINGSTR2ReportExport:str = obj["whereClauseINGSTR2ReportExport"]
      self.whereClauseINGSTR2ReportExportDtl:str = obj["whereClauseINGSTR2ReportExportDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtINGSTR2ReportExportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtINGSTR2ReportExportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_INGSTR2ReportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

