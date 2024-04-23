import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GUINumSvc
# Description: Taiwan GUI Number Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GUINums(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GUINums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GUINums
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUINumHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums",headers=creds) as resp:
           return await resp.json()

async def post_GUINums(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GUINums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GUINumHedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GUINumHedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GUINums_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GUINum item
   Description: Calls GetByID to retrieve the GUINum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GUINum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GUINumHedRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GUINums_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GUINum for the service
   Description: Calls UpdateExt to update GUINum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GUINum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GUINumHedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GUINums_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GUINum item
   Description: Call UpdateExt to delete GUINum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GUINum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GUINums_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID_GUINumDtls(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get GUINumDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GUINumDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUINumDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + ")/GUINumDtls",headers=creds) as resp:
           return await resp.json()

async def get_GUINums_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID_GUINumDtls_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID_GroupID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, GroupID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GUINumDtl item
   Description: Calls GetByID to retrieve the GUINumDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GUINumDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GUINumDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINums(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + ")/GUINumDtls(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_GUINumDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GUINumDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GUINumDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUINumDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINumDtls",headers=creds) as resp:
           return await resp.json()

async def post_GUINumDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GUINumDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GUINumDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GUINumDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINumDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GUINumDtls_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID_GroupID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, GroupID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GUINumDtl item
   Description: Calls GetByID to retrieve the GUINumDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GUINumDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GUINumDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINumDtls(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + "," + GroupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GUINumDtls_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID_GroupID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, GroupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GUINumDtl for the service
   Description: Calls UpdateExt to update GUINumDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GUINumDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GUINumDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINumDtls(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + "," + GroupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GUINumDtls_Company_FiscalYear_FiscalYearSuffix_FiscalPeriod_TranDocTypeID_GroupID(Company, FiscalYear, FiscalYearSuffix, FiscalPeriod, TranDocTypeID, GroupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GUINumDtl item
   Description: Call UpdateExt to delete GUINumDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GUINumDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param FiscalYear: Desc: FiscalYear   Required: True
      :param FiscalYearSuffix: Desc: FiscalYearSuffix   Required: True   Allow empty value : True
      :param FiscalPeriod: Desc: FiscalPeriod   Required: True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/GUINumDtls(" + Company + "," + FiscalYear + "," + FiscalYearSuffix + "," + FiscalPeriod + "," + TranDocTypeID + "," + GroupID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GUINumHedListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGUINumHed, whereClauseGUINumDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGUINumHed=" + whereClauseGUINumHed
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseGUINumDtl=" + whereClauseGUINumDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(fiscalYear, fiscalYearSuffix, fiscalPeriod, tranDocTypeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True   Allow empty value : True
   Required: True
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
   params += "fiscalYear=" + fiscalYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYearSuffix=" + fiscalYearSuffix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalPeriod=" + fiscalPeriod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tranDocTypeID=" + tranDocTypeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeYearPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeYearPeriod
   Description: OnChangeYearPeriod handler
   OperationID: OnChangeYearPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeYearPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeYearPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranDocTypeID
   Description: OnChangeTranDocTypeID handler
   OperationID: OnChangeTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumber
   Description: GetLegalNumber method
   OperationID: GetLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumberForSalesOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumberForSalesOrder
   Description: GetLegalNumberForSalesOrder method should be called before showing GUI Legal Number assigning form for Sales Order
   OperationID: GetLegalNumberForSalesOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLegalNumberForSalesOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumberForSalesOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGUIYearOrPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGUIYearOrPeriod
   Description: OnChangeGUIYearOrPeriod handler
   OperationID: OnChangeGUIYearOrPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGUIYearOrPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGUIYearOrPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGUIGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGUIGroup
   Description: OnChangeGUIGroup handler
   OperationID: OnChangeGUIGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGUIGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGUIGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSeqNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSeqNum
   Description: OnChangeSeqNum handler
   OperationID: OnChangeSeqNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSeqNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSeqNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignLegalNumber
   Description: Assigns a legal number.
   OperationID: AssignLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidSalesOrderLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidSalesOrderLegalNumber
   Description: Void Sales Order Legal Number
   OperationID: VoidSalesOrderLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidSalesOrderLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidSalesOrderLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGUINumHed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGUINumHed
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGUINumHed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGUINumHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGUINumHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGUINumDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGUINumDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGUINumDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGUINumDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGUINumDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GUINumSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUINumDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GUINumDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUINumHedListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GUINumHedListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GUINumHedRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GUINumHedRow] = obj["value"]
      pass

class Erp_Tablesets_GUINumDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.StartSeq:int = obj["StartSeq"]
      """  StartSeq  """  
      self.EndSeq:int = obj["EndSeq"]
      """  EndSeq  """  
      self.CurrentSeq:int = obj["CurrentSeq"]
      """  CurrentSeq  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUINumHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.GenerationType:str = obj["GenerationType"]
      """  GenerationType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndDate:str = obj["EndDate"]
      self.Key:str = obj["Key"]
      self.StartDate:str = obj["StartDate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUINumHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.GenerationType:str = obj["GenerationType"]
      """  GenerationType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndDate:str = obj["EndDate"]
      self.Key:str = obj["Key"]
      self.StartDate:str = obj["StartDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignLegalNumber_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

class AssignLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GUILegalNumberRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.GenerationType:str = obj["GenerationType"]
      self.GUIFormatCode:str = obj["GUIFormatCode"]
      self.GUIGroup:str = obj["GUIGroup"]
      self.GUIPeriod:int = obj["GUIPeriod"]
      self.GUIYear:int = obj["GUIYear"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      self.SeqNum:int = obj["SeqNum"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.GUIYearSuffix:str = obj["GUIYearSuffix"]
      self.OrderNum:int = obj["OrderNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUILegalNumberTableset:
   def __init__(self, obj):
      self.GUILegalNumber:list[Erp_Tablesets_GUILegalNumberRow] = obj["GUILegalNumber"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GUINumDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.StartSeq:int = obj["StartSeq"]
      """  StartSeq  """  
      self.EndSeq:int = obj["EndSeq"]
      """  EndSeq  """  
      self.CurrentSeq:int = obj["CurrentSeq"]
      """  CurrentSeq  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUINumHedListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.GenerationType:str = obj["GenerationType"]
      """  GenerationType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndDate:str = obj["EndDate"]
      self.Key:str = obj["Key"]
      self.StartDate:str = obj["StartDate"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUINumHedRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  FiscalYear  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  FiscalYearSuffix  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  FiscalPeriod  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID  """  
      self.GenerationType:str = obj["GenerationType"]
      """  GenerationType  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EndDate:str = obj["EndDate"]
      self.Key:str = obj["Key"]
      self.StartDate:str = obj["StartDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GUINumListTableset:
   def __init__(self, obj):
      self.GUINumHedList:list[Erp_Tablesets_GUINumHedListRow] = obj["GUINumHedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GUINumTableset:
   def __init__(self, obj):
      self.GUINumHed:list[Erp_Tablesets_GUINumHedRow] = obj["GUINumHed"]
      self.GUINumDtl:list[Erp_Tablesets_GUINumDtlRow] = obj["GUINumDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGUINumTableset:
   def __init__(self, obj):
      self.GUINumHed:list[Erp_Tablesets_GUINumHedRow] = obj["GUINumHed"]
      self.GUINumDtl:list[Erp_Tablesets_GUINumDtlRow] = obj["GUINumDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GUINumTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GUINumTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GUINumTableset] = obj["returnObj"]
      pass

class GetLegalNumberForSalesOrder_input:
   """ Required : 
   Company
   OrderNum
   ds
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OrderNum:int = obj["OrderNum"]
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

class GetLegalNumberForSalesOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetLegalNumber_input:
   """ Required : 
   Company
   InvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InvoiceNum:int = obj["InvoiceNum"]
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

class GetLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_GUINumListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGUINumDtl_input:
   """ Required : 
   ds
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      pass

class GetNewGUINumDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewGUINumHed_input:
   """ Required : 
   ds
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      pass

class GetNewGUINumHed_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGUINumHed
   whereClauseGUINumDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGUINumHed:str = obj["whereClauseGUINumHed"]
      self.whereClauseGUINumDtl:str = obj["whereClauseGUINumDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GUINumTableset] = obj["returnObj"]
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

class OnChangeGUIGroup_input:
   """ Required : 
   GUIGroup
   ds
   """  
   def __init__(self, obj):
      self.GUIGroup:str = obj["GUIGroup"]
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

class OnChangeGUIGroup_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeGUIYearOrPeriod_input:
   """ Required : 
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

class OnChangeGUIYearOrPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSeqNum_input:
   """ Required : 
   SeqNum
   ds
   """  
   def __init__(self, obj):
      self.SeqNum:int = obj["SeqNum"]
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

class OnChangeSeqNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUILegalNumberTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranDocTypeID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

class OnChangeTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeYearPeriod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

class OnChangeYearPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGUINumTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGUINumTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GUINumTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidSalesOrderLegalNumber_input:
   """ Required : 
   orderNum
   voidReason
   """  
   def __init__(self, obj):
      self.orderNum:int = obj["orderNum"]
      self.voidReason:str = obj["voidReason"]
      pass

class VoidSalesOrderLegalNumber_output:
   def __init__(self, obj):
      pass

