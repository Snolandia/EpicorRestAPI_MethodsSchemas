import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PlasticPackagingTaxReportSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PlasticPackagingTaxReports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlasticPackagingTaxReports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlasticPackagingTaxReports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlasticPackagingTaxReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports",headers=creds) as resp:
           return await resp.json()

async def post_PlasticPackagingTaxReports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlasticPackagingTaxReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlasticPackagingTaxReports_Company_ReportID(Company, ReportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlasticPackagingTaxReport item
   Description: Calls GetByID to retrieve the PlasticPackagingTaxReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlasticPackagingTaxReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlasticPackagingTaxReports_Company_ReportID(Company, ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlasticPackagingTaxReport for the service
   Description: Calls UpdateExt to update PlasticPackagingTaxReport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlasticPackagingTaxReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports(" + Company + "," + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlasticPackagingTaxReports_Company_ReportID(Company, ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlasticPackagingTaxReport item
   Description: Call UpdateExt to delete PlasticPackagingTaxReport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlasticPackagingTaxReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlasticPackagingTaxReports_Company_ReportID_PlasticPackagingTaxReportDtls(Company, ReportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PlasticPackagingTaxReportDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlasticPackagingTaxReportDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlasticPackagingTaxReportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports(" + Company + "," + ReportID + ")/PlasticPackagingTaxReportDtls",headers=creds) as resp:
           return await resp.json()

async def get_PlasticPackagingTaxReports_Company_ReportID_PlasticPackagingTaxReportDtls_Company_ReportID_Type_ExemptReasonCode(Company, ReportID, Type, ExemptReasonCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlasticPackagingTaxReportDtl item
   Description: Calls GetByID to retrieve the PlasticPackagingTaxReportDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlasticPackagingTaxReportDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param ExemptReasonCode: Desc: ExemptReasonCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReports(" + Company + "," + ReportID + ")/PlasticPackagingTaxReportDtls(" + Company + "," + ReportID + "," + Type + "," + ExemptReasonCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PlasticPackagingTaxReportDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PlasticPackagingTaxReportDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlasticPackagingTaxReportDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlasticPackagingTaxReportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReportDtls",headers=creds) as resp:
           return await resp.json()

async def post_PlasticPackagingTaxReportDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlasticPackagingTaxReportDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReportDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PlasticPackagingTaxReportDtls_Company_ReportID_Type_ExemptReasonCode(Company, ReportID, Type, ExemptReasonCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PlasticPackagingTaxReportDtl item
   Description: Calls GetByID to retrieve the PlasticPackagingTaxReportDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlasticPackagingTaxReportDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param ExemptReasonCode: Desc: ExemptReasonCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReportDtls(" + Company + "," + ReportID + "," + Type + "," + ExemptReasonCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PlasticPackagingTaxReportDtls_Company_ReportID_Type_ExemptReasonCode(Company, ReportID, Type, ExemptReasonCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PlasticPackagingTaxReportDtl for the service
   Description: Calls UpdateExt to update PlasticPackagingTaxReportDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlasticPackagingTaxReportDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param ExemptReasonCode: Desc: ExemptReasonCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlasticPackagingTaxReportDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReportDtls(" + Company + "," + ReportID + "," + Type + "," + ExemptReasonCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PlasticPackagingTaxReportDtls_Company_ReportID_Type_ExemptReasonCode(Company, ReportID, Type, ExemptReasonCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PlasticPackagingTaxReportDtl item
   Description: Call UpdateExt to delete PlasticPackagingTaxReportDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlasticPackagingTaxReportDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param ExemptReasonCode: Desc: ExemptReasonCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/PlasticPackagingTaxReportDtls(" + Company + "," + ReportID + "," + Type + "," + ExemptReasonCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlasticPackagingTaxReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePlasticPackagingTaxReport, whereClausePlasticPackagingTaxReportDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePlasticPackagingTaxReport=" + whereClausePlasticPackagingTaxReport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePlasticPackagingTaxReportDtl=" + whereClausePlasticPackagingTaxReportDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPlasticTaxRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPlasticTaxRate
   OperationID: GetPlasticTaxRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlasticTaxRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlasticTaxRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Calculate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Calculate
   OperationID: Calculate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Calculate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Calculate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlasticPackagingTaxReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlasticPackagingTaxReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlasticPackagingTaxReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlasticPackagingTaxReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlasticPackagingTaxReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPlasticPackagingTaxReportDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPlasticPackagingTaxReportDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlasticPackagingTaxReportDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPlasticPackagingTaxReportDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlasticPackagingTaxReportDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PlasticPackagingTaxReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlasticPackagingTaxReportDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlasticPackagingTaxReportDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlasticPackagingTaxReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlasticPackagingTaxReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlasticPackagingTaxReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PlasticPackagingTaxReportRow] = obj["value"]
      pass

class Erp_Tablesets_PlasticPackagingTaxReportDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  ExemptReasonCode  """  
      self.Value:int = obj["Value"]
      """  Value  """  
      self.ManufacturedQty:int = obj["ManufacturedQty"]
      """  ManufacturedQty  """  
      self.ImportedQty:int = obj["ImportedQty"]
      """  ImportedQty  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Description:str = obj["Description"]
      self.TotalQty:int = obj["TotalQty"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlasticPackagingTaxReportListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlasticPackagingTaxReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UOMCode:str = obj["UOMCode"]
      """  UOMCode  """  
      self.DateFrom:str = obj["DateFrom"]
      """  DateFrom  """  
      self.DateTo:str = obj["DateTo"]
      """  DateTo  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.Manual:bool = obj["Manual"]
      """  Manual  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  SubmittedBy  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  SubmittedOn  """  
      self.SysDate:str = obj["SysDate"]
      """  SysDate  """  
      self.SysTime:int = obj["SysTime"]
      """  SysTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BaseUOMClassID:str = obj["BaseUOMClassID"]
      self.BitFlag:int = obj["BitFlag"]
      self.UOMCodeNumOfDec:int = obj["UOMCodeNumOfDec"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Calculate_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class Calculate_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PlasticPackagingTaxReportDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.ExemptReasonCode:str = obj["ExemptReasonCode"]
      """  ExemptReasonCode  """  
      self.Value:int = obj["Value"]
      """  Value  """  
      self.ManufacturedQty:int = obj["ManufacturedQty"]
      """  ManufacturedQty  """  
      self.ImportedQty:int = obj["ImportedQty"]
      """  ImportedQty  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Description:str = obj["Description"]
      self.TotalQty:int = obj["TotalQty"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlasticPackagingTaxReportListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlasticPackagingTaxReportListTableset:
   def __init__(self, obj):
      self.PlasticPackagingTaxReportList:list[Erp_Tablesets_PlasticPackagingTaxReportListRow] = obj["PlasticPackagingTaxReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PlasticPackagingTaxReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.UOMCode:str = obj["UOMCode"]
      """  UOMCode  """  
      self.DateFrom:str = obj["DateFrom"]
      """  DateFrom  """  
      self.DateTo:str = obj["DateTo"]
      """  DateTo  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.Submitted:bool = obj["Submitted"]
      """  Submitted  """  
      self.Manual:bool = obj["Manual"]
      """  Manual  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  SubmittedBy  """  
      self.SubmittedOn:str = obj["SubmittedOn"]
      """  SubmittedOn  """  
      self.SysDate:str = obj["SysDate"]
      """  SysDate  """  
      self.SysTime:int = obj["SysTime"]
      """  SysTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BaseUOMClassID:str = obj["BaseUOMClassID"]
      self.BitFlag:int = obj["BitFlag"]
      self.UOMCodeNumOfDec:int = obj["UOMCodeNumOfDec"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PlasticPackagingTaxReportTableset:
   def __init__(self, obj):
      self.PlasticPackagingTaxReport:list[Erp_Tablesets_PlasticPackagingTaxReportRow] = obj["PlasticPackagingTaxReport"]
      self.PlasticPackagingTaxReportDtl:list[Erp_Tablesets_PlasticPackagingTaxReportDtlRow] = obj["PlasticPackagingTaxReportDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPlasticPackagingTaxReportTableset:
   def __init__(self, obj):
      self.PlasticPackagingTaxReport:list[Erp_Tablesets_PlasticPackagingTaxReportRow] = obj["PlasticPackagingTaxReport"]
      self.PlasticPackagingTaxReportDtl:list[Erp_Tablesets_PlasticPackagingTaxReportDtlRow] = obj["PlasticPackagingTaxReportDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PlasticPackagingTaxReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPlasticPackagingTaxReportDtl_input:
   """ Required : 
   ds
   reportID
   type
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["ds"]
      self.reportID:str = obj["reportID"]
      self.type:str = obj["type"]
      pass

class GetNewPlasticPackagingTaxReportDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPlasticPackagingTaxReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["ds"]
      pass

class GetNewPlasticPackagingTaxReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPlasticTaxRate_input:
   """ Required : 
   reportUOMCode
   """  
   def __init__(self, obj):
      self.reportUOMCode:str = obj["reportUOMCode"]
      pass

class GetPlasticTaxRate_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClausePlasticPackagingTaxReport
   whereClausePlasticPackagingTaxReportDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePlasticPackagingTaxReport:str = obj["whereClausePlasticPackagingTaxReport"]
      self.whereClausePlasticPackagingTaxReportDtl:str = obj["whereClausePlasticPackagingTaxReportDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPlasticPackagingTaxReportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPlasticPackagingTaxReportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PlasticPackagingTaxReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

