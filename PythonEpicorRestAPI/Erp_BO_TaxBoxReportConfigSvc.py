import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TaxBoxReportConfigSvc
# Description: Tax Box Report Configuration Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxReportConfigs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxBoxReportConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxBoxReportConfigs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxReportConfigHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs",headers=creds) as resp:
           return await resp.json()

async def post_TaxBoxReportConfigs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxBoxReportConfigs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxReportConfigs_Company_ConfigID(Company, ConfigID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBoxReportConfig item
   Description: Calls GetByID to retrieve the TaxBoxReportConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxReportConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxBoxReportConfigs_Company_ConfigID(Company, ConfigID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxBoxReportConfig for the service
   Description: Calls UpdateExt to update TaxBoxReportConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxBoxReportConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs(" + Company + "," + ConfigID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxBoxReportConfigs_Company_ConfigID(Company, ConfigID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxBoxReportConfig item
   Description: Call UpdateExt to delete TaxBoxReportConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxBoxReportConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxReportConfigs_Company_ConfigID_TaxBoxReportConfigDtls(Company, ConfigID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxBoxReportConfigDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxBoxReportConfigDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxReportConfigDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs(" + Company + "," + ConfigID + ")/TaxBoxReportConfigDtls",headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxReportConfigs_Company_ConfigID_TaxBoxReportConfigDtls_Company_ConfigID_LineNum(Company, ConfigID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBoxReportConfigDtl item
   Description: Calls GetByID to retrieve the TaxBoxReportConfigDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxReportConfigDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigs(" + Company + "," + ConfigID + ")/TaxBoxReportConfigDtls(" + Company + "," + ConfigID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxReportConfigDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxBoxReportConfigDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxBoxReportConfigDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxReportConfigDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigDtls",headers=creds) as resp:
           return await resp.json()

async def post_TaxBoxReportConfigDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxBoxReportConfigDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxBoxReportConfigDtls_Company_ConfigID_LineNum(Company, ConfigID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxBoxReportConfigDtl item
   Description: Calls GetByID to retrieve the TaxBoxReportConfigDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxBoxReportConfigDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigDtls(" + Company + "," + ConfigID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxBoxReportConfigDtls_Company_ConfigID_LineNum(Company, ConfigID, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxBoxReportConfigDtl for the service
   Description: Calls UpdateExt to update TaxBoxReportConfigDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxBoxReportConfigDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxBoxReportConfigDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigDtls(" + Company + "," + ConfigID + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxBoxReportConfigDtls_Company_ConfigID_LineNum(Company, ConfigID, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxBoxReportConfigDtl item
   Description: Call UpdateExt to delete TaxBoxReportConfigDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxBoxReportConfigDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/TaxBoxReportConfigDtls(" + Company + "," + ConfigID + "," + LineNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxBoxReportConfigHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseTaxBoxReportConfigHead, whereClauseTaxBoxReportConfigDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseTaxBoxReportConfigHead=" + whereClauseTaxBoxReportConfigHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseTaxBoxReportConfigDtl=" + whereClauseTaxBoxReportConfigDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(configID, epicorHeaders = None):
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
   params += "configID=" + configID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxBoxCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxBoxCodeDescList
   Description: Get Code/Description list for Tax Box specific properties
   OperationID: GetTaxBoxCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxBoxCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxBoxCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxBoxCodeDescListApart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxBoxCodeDescListApart
   Description: Get Code/Description list for Tax Box specific properties
   OperationID: GetTaxBoxCodeDescListApart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxBoxCodeDescListApart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxBoxCodeDescListApart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertLine
   Description: Insert new line before existing one. New line will get the number of line it's inserted before, subsequent line numbers are incremented.
Function also updates all formulas referencing to lines with changed numbers.
   OperationID: InsertLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PasteLinesData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PasteLinesData
   Description: Paste Lines data from Clipboard. This function overrides ICE PasteInsert/PasteUpdate to correctly process Lines references change.
   OperationID: PasteLinesData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PasteLinesData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PasteLinesData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxBoxReportConfigHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxBoxReportConfigHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxBoxReportConfigHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBoxReportConfigHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBoxReportConfigHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxBoxReportConfigDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxBoxReportConfigDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxBoxReportConfigDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxBoxReportConfigDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxBoxReportConfigDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TaxBoxReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxReportConfigDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxBoxReportConfigDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxReportConfigHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxBoxReportConfigHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxBoxReportConfigHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxBoxReportConfigHeadRow] = obj["value"]
      pass

class Erp_Tablesets_TaxBoxReportConfigDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LineNum:int = obj["LineNum"]
      """  LineNum  """  
      self.ReportLineNumCaption:str = obj["ReportLineNumCaption"]
      """  ReportLineNumCaption  """  
      self.ReportLineCaption:str = obj["ReportLineCaption"]
      """  ReportLineCaption  """  
      self.FormulaType:str = obj["FormulaType"]
      """  FormulaType  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Hidden:bool = obj["Hidden"]
      """  Hidden  """  
      self.SuppressNegValue:bool = obj["SuppressNegValue"]
      """  SuppressNegValue  """  
      self.SuppressZeroValue:bool = obj["SuppressZeroValue"]
      """  SuppressZeroValue  """  
      self.ManualTaxBox:str = obj["ManualTaxBox"]
      """  ManualTaxBox  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FormulaDisplayText:str = obj["FormulaDisplayText"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxReportConfigHeadListRow:
   def __init__(self, obj):
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  EffectiveFrom  """  
      self.Active:bool = obj["Active"]
      """  Active  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxReportConfigHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  EffectiveFrom  """  
      self.Active:bool = obj["Active"]
      """  Active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_TaxBoxReportConfigDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LineNum:int = obj["LineNum"]
      """  LineNum  """  
      self.ReportLineNumCaption:str = obj["ReportLineNumCaption"]
      """  ReportLineNumCaption  """  
      self.ReportLineCaption:str = obj["ReportLineCaption"]
      """  ReportLineCaption  """  
      self.FormulaType:str = obj["FormulaType"]
      """  FormulaType  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.Hidden:bool = obj["Hidden"]
      """  Hidden  """  
      self.SuppressNegValue:bool = obj["SuppressNegValue"]
      """  SuppressNegValue  """  
      self.SuppressZeroValue:bool = obj["SuppressZeroValue"]
      """  SuppressZeroValue  """  
      self.ManualTaxBox:str = obj["ManualTaxBox"]
      """  ManualTaxBox  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FormulaDisplayText:str = obj["FormulaDisplayText"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxReportConfigHeadListRow:
   def __init__(self, obj):
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  EffectiveFrom  """  
      self.Active:bool = obj["Active"]
      """  Active  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxReportConfigHeadListTableset:
   def __init__(self, obj):
      self.TaxBoxReportConfigHeadList:list[Erp_Tablesets_TaxBoxReportConfigHeadListRow] = obj["TaxBoxReportConfigHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TaxBoxReportConfigHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  EffectiveFrom  """  
      self.Active:bool = obj["Active"]
      """  Active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxBoxReportConfigTableset:
   def __init__(self, obj):
      self.TaxBoxReportConfigHead:list[Erp_Tablesets_TaxBoxReportConfigHeadRow] = obj["TaxBoxReportConfigHead"]
      self.TaxBoxReportConfigDtl:list[Erp_Tablesets_TaxBoxReportConfigDtlRow] = obj["TaxBoxReportConfigDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtTaxBoxReportConfigTableset:
   def __init__(self, obj):
      self.TaxBoxReportConfigHead:list[Erp_Tablesets_TaxBoxReportConfigHeadRow] = obj["TaxBoxReportConfigHead"]
      self.TaxBoxReportConfigDtl:list[Erp_Tablesets_TaxBoxReportConfigDtlRow] = obj["TaxBoxReportConfigDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_TaxBoxReportConfigHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewTaxBoxReportConfigDtl_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewTaxBoxReportConfigDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxBoxReportConfigHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["ds"]
      pass

class GetNewTaxBoxReportConfigHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseTaxBoxReportConfigHead
   whereClauseTaxBoxReportConfigDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseTaxBoxReportConfigHead:str = obj["whereClauseTaxBoxReportConfigHead"]
      self.whereClauseTaxBoxReportConfigDtl:str = obj["whereClauseTaxBoxReportConfigDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaxBoxCodeDescListApart_input:
   """ Required : 
   valueType
   """  
   def __init__(self, obj):
      self.valueType:int = obj["valueType"]
      """  0-Source Model
1-Line Type
2-AmountType  """  
      pass

class GetTaxBoxCodeDescListApart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.codes:str = obj["parameters"]
      self.descriptions:str = obj["parameters"]
      self.len:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetTaxBoxCodeDescList_input:
   """ Required : 
   valueType
   """  
   def __init__(self, obj):
      self.valueType:int = obj["valueType"]
      """  0-Source Model
            1-Line Type
            2-AmountType  """  
      pass

class GetTaxBoxCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

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

class InsertLine_input:
   """ Required : 
   configID
   insertBeforeLineNum
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration being updated  """  
      self.insertBeforeLineNum:int = obj["insertBeforeLineNum"]
      """  Number of line before which the new line should be inserted  """  
      pass

class InsertLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newLineNumber:int = obj["parameters"]
      pass

      """  output parameters  """  

class PasteLinesData_input:
   """ Required : 
   configID
   clipboardData
   isUpdate
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Config for which lines are pasted  """  
      self.clipboardData:str = obj["clipboardData"]
      """  Data pasted from Clipboard  """  
      self.isUpdate:bool = obj["isUpdate"]
      """  Is Paste Update mode  """  
      pass

class PasteLinesData_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxBoxReportConfigTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtTaxBoxReportConfigTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaxBoxReportConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

