import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.FinReportConfigSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_FinReportConfigs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FinReportConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FinReportConfigs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FinRepConfHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs",headers=creds) as resp:
           return await resp.json()

async def post_FinReportConfigs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FinReportConfigs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FinRepConfHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FinRepConfHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FinReportConfigs_Company_ConfigID(Company, ConfigID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FinReportConfig item
   Description: Calls GetByID to retrieve the FinReportConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FinReportConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FinRepConfHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FinReportConfigs_Company_ConfigID(Company, ConfigID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FinReportConfig for the service
   Description: Calls UpdateExt to update FinReportConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FinReportConfig
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FinRepConfHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs(" + Company + "," + ConfigID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FinReportConfigs_Company_ConfigID(Company, ConfigID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FinReportConfig item
   Description: Call UpdateExt to delete FinReportConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FinReportConfig
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs(" + Company + "," + ConfigID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FinReportConfigs_Company_ConfigID_FinRepConfLines(Company, ConfigID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FinRepConfLines items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FinRepConfLines1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FinRepConfLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs(" + Company + "," + ConfigID + ")/FinRepConfLines",headers=creds) as resp:
           return await resp.json()

async def get_FinReportConfigs_Company_ConfigID_FinRepConfLines_Company_ConfigID_LineNum(Company, ConfigID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FinRepConfLine item
   Description: Calls GetByID to retrieve the FinRepConfLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FinRepConfLine1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FinRepConfLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinReportConfigs(" + Company + "," + ConfigID + ")/FinRepConfLines(" + Company + "," + ConfigID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_FinRepConfLines(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FinRepConfLines items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FinRepConfLines
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FinRepConfLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinRepConfLines",headers=creds) as resp:
           return await resp.json()

async def post_FinRepConfLines(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FinRepConfLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FinRepConfLineRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FinRepConfLineRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinRepConfLines", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FinRepConfLines_Company_ConfigID_LineNum(Company, ConfigID, LineNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FinRepConfLine item
   Description: Calls GetByID to retrieve the FinRepConfLine item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FinRepConfLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FinRepConfLineRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinRepConfLines(" + Company + "," + ConfigID + "," + LineNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FinRepConfLines_Company_ConfigID_LineNum(Company, ConfigID, LineNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FinRepConfLine for the service
   Description: Calls UpdateExt to update FinRepConfLine. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FinRepConfLine
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param LineNum: Desc: LineNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FinRepConfLineRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinRepConfLines(" + Company + "," + ConfigID + "," + LineNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FinRepConfLines_Company_ConfigID_LineNum(Company, ConfigID, LineNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FinRepConfLine item
   Description: Call UpdateExt to delete FinRepConfLine item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FinRepConfLine
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/FinRepConfLines(" + Company + "," + ConfigID + "," + LineNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FinRepConfHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFinRepConfHead, whereClauseFinRepConfLine, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFinRepConfHead=" + whereClauseFinRepConfHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFinRepConfLine=" + whereClauseFinRepConfLine
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateReportConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateReportConfig
   Description: Function to duplicate existing Financial Report Configuration
(China Localization)
   OperationID: DuplicateReportConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateReportConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateReportConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportConfigExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportConfigExt
   Description: Write XML export file
   OperationID: ExportConfigExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportConfigExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportConfigExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportConfig
   Description: Write XML from FinReportConfig Export data
   OperationID: ExportConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportConfigExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportConfigExt
   Description: Import XML with Config Import Data into Database
   OperationID: ImportConfigExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportConfigExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportConfigExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportConfig(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportConfig
   Description: Import XML with Config Import Data into Database
   OperationID: ImportConfig
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfFormula(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfFormula
   Description: This method validates the Formula entered to FinRepConfLines.Character02 field.
   OperationID: OnChangeOfFormula
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnPreviewReportTypeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPreviewReportTypeChanged
   Description: /// This method returns default report style for selected Report Type
   OperationID: OnPreviewReportTypeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPreviewReportTypeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPreviewReportTypeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetReportTypeList
   Description: Function to retrieve the list of Financial Configuration Report types
   OperationID: GetReportTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetReportTypeListExt(epicorHeaders = None):
   """  
   Summary: Invoke method GetReportTypeListExt
   Description: Function to retrieve the list of Financial Configuration Report types
   OperationID: GetReportTypeListExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportTypeListExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RunReportDesignPreview(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunReportDesignPreview
   Description: This function runs Financial Report in Design Preview mode
   OperationID: RunReportDesignPreview
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunReportDesignPreview_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunReportDesignPreview_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunReportDesignPreviewExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunReportDesignPreviewExt
   Description: This function runs Financial Report in Design Preview mode
   OperationID: RunReportDesignPreviewExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunReportDesignPreviewExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunReportDesignPreviewExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFinRepConfHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFinRepConfHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFinRepConfHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFinRepConfHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFinRepConfHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFinRepConfLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFinRepConfLine
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFinRepConfLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFinRepConfLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFinRepConfLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.FinReportConfigSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FinRepConfHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FinRepConfHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FinRepConfHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FinRepConfHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FinRepConfLineRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FinRepConfLineRow] = obj["value"]
      pass

class Erp_Tablesets_FinRepConfHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  IsSystem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FinRepConfHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  IsSystem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FinRepConfLineRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LineNum:int = obj["LineNum"]
      """  LineNum  """  
      self.LabelID:str = obj["LabelID"]
      """  LabelID  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.RightSideStarts:bool = obj["RightSideStarts"]
      """  RightSideStarts  """  
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

class DuplicateReportConfig_input:
   """ Required : 
   sourceConfigID
   targetConfigID
   targetConfigDesc
   """  
   def __init__(self, obj):
      self.sourceConfigID:str = obj["sourceConfigID"]
      """  Source Configuration ID  """  
      self.targetConfigID:str = obj["targetConfigID"]
      """  Target Configuration ID  """  
      self.targetConfigDesc:str = obj["targetConfigDesc"]
      """  Target Configuration Description  """  
      pass

class DuplicateReportConfig_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class Erp_Tablesets_DynFieldAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.DataType:str = obj["DataType"]
      self.Required:bool = obj["Required"]
      self.ReadOnly:bool = obj["ReadOnly"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.LikeDataFieldSystemCode:str = obj["LikeDataFieldSystemCode"]
      self.LikeDataFieldTableID:str = obj["LikeDataFieldTableID"]
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      self.CurrencyCodeColumn:str = obj["CurrencyCodeColumn"]
      self.CurrencyType:str = obj["CurrencyType"]
      self.CurrencySource:str = obj["CurrencySource"]
      self.BizType:str = obj["BizType"]
      self.CGCCode:str = obj["CGCCode"]
      self.UomColumn:str = obj["UomColumn"]
      self.CodeDescriptionList:str = obj["CodeDescriptionList"]
      self.Seq:int = obj["Seq"]
      self.IsHidden:bool = obj["IsHidden"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynFieldHelpRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      self.FieldName:str = obj["FieldName"]
      self.Description:str = obj["Description"]
      self.DBTableName:str = obj["DBTableName"]
      self.DBFieldName:str = obj["DBFieldName"]
      self.External:bool = obj["External"]
      self.InitialValue:str = obj["InitialValue"]
      self.IsDescriptionField:bool = obj["IsDescriptionField"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynTableAttributesRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.DataTableID:str = obj["DataTableID"]
      """  The actual generic table name used by the BL  """  
      self.UniqueTableID:str = obj["UniqueTableID"]
      """  Unique identifier for the virtual schema  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynamicMetadataTableset:
   def __init__(self, obj):
      self.DynTableAttributes:list[Erp_Tablesets_DynTableAttributesRow] = obj["DynTableAttributes"]
      self.DynFieldAttributes:list[Erp_Tablesets_DynFieldAttributesRow] = obj["DynFieldAttributes"]
      self.DynFieldHelp:list[Erp_Tablesets_DynFieldHelpRow] = obj["DynFieldHelp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FinRepConfHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  IsSystem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FinRepConfHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.COACode:str = obj["COACode"]
      """  COACode  """  
      self.IsSystem:bool = obj["IsSystem"]
      """  IsSystem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FinRepConfLineRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.LineNum:int = obj["LineNum"]
      """  LineNum  """  
      self.LabelID:str = obj["LabelID"]
      """  LabelID  """  
      self.Formula:str = obj["Formula"]
      """  Formula  """  
      self.RightSideStarts:bool = obj["RightSideStarts"]
      """  RightSideStarts  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FinRepConfListTableset:
   def __init__(self, obj):
      self.FinRepConfHeadList:list[Erp_Tablesets_FinRepConfHeadListRow] = obj["FinRepConfHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FinReportConfigTableset:
   def __init__(self, obj):
      self.FinRepConfHead:list[Erp_Tablesets_FinRepConfHeadRow] = obj["FinRepConfHead"]
      self.FinRepConfLine:list[Erp_Tablesets_FinRepConfLineRow] = obj["FinRepConfLine"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtFinReportConfigTableset:
   def __init__(self, obj):
      self.FinRepConfHead:list[Erp_Tablesets_FinRepConfHeadRow] = obj["FinRepConfHead"]
      self.FinRepConfLine:list[Erp_Tablesets_FinRepConfLineRow] = obj["FinRepConfLine"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ExportConfigExt_input:
   """ Required : 
   configID
   fileName
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      self.fileName:str = obj["fileName"]
      """  File Name  """  
      pass

class ExportConfigExt_output:
   def __init__(self, obj):
      pass

class ExportConfig_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration to be exported  """  
      pass

class ExportConfig_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  XML with Export Data  """  
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
      self.returnObj:list[Erp_Tablesets_FinReportConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FinReportConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FinReportConfigTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FinRepConfListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFinRepConfHead_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FinReportConfigTableset] = obj["ds"]
      pass

class GetNewFinRepConfHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FinReportConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFinRepConfLine_input:
   """ Required : 
   ds
   configID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FinReportConfigTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      pass

class GetNewFinRepConfLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FinReportConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReportTypeListExt_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetReportTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.reportTypeList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFinRepConfHead
   whereClauseFinRepConfLine
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFinRepConfHead:str = obj["whereClauseFinRepConfHead"]
      self.whereClauseFinRepConfLine:str = obj["whereClauseFinRepConfLine"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FinReportConfigTableset] = obj["returnObj"]
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

class ImportConfigExt_input:
   """ Required : 
   fileName
   newConfigID
   overwriteExisting
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  XML file with Config Import Data  """  
      self.newConfigID:str = obj["newConfigID"]
      """  New ConfigID  """  
      self.overwriteExisting:bool = obj["overwriteExisting"]
      """  Overwrite existing configurations  """  
      pass

class ImportConfigExt_output:
   def __init__(self, obj):
      pass

class ImportConfig_input:
   """ Required : 
   configData
   newConfigID
   overwriteExisting
   """  
   def __init__(self, obj):
      self.configData:str = obj["configData"]
      """  XML with Config Import Data  """  
      self.newConfigID:str = obj["newConfigID"]
      """  New ConfigID  """  
      self.overwriteExisting:bool = obj["overwriteExisting"]
      """  Overwrite existing configurations  """  
      pass

class ImportConfig_output:
   def __init__(self, obj):
      pass

class OnChangeOfFormula_input:
   """ Required : 
   ipFormula
   """  
   def __init__(self, obj):
      self.ipFormula:str = obj["ipFormula"]
      """  The new proposed FinRepConfLines.Character03 value  """  
      pass

class OnChangeOfFormula_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.success:bool = obj["success"]
      pass

      """  output parameters  """  

class OnPreviewReportTypeChanged_input:
   """ Required : 
   reportType
   """  
   def __init__(self, obj):
      self.reportType:int = obj["reportType"]
      """  New selected report type  """  
      pass

class OnPreviewReportTypeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.reportStyleNum:int = obj["parameters"]
      pass

      """  output parameters  """  

class RunReportDesignPreviewExt_input:
   """ Required : 
   configID
   reportType
   reportStyleNum
   displayAmtAs
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  FinReportConfig to run report against  """  
      self.reportType:int = obj["reportType"]
      """  Type of report (0-BS/1-IS/2-CF)  """  
      self.reportStyleNum:int = obj["reportStyleNum"]
      """  Report Style number  """  
      self.displayAmtAs:str = obj["displayAmtAs"]
      """  Option to display Formula or hardcoded amount in preview  """  
      pass

class RunReportDesignPreviewExt_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Preview DataSet  """  
      pass

   def parameters(self, obj):
      self.dynamicMetadataDs:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDs"]
      pass

      """  output parameters  """  

class RunReportDesignPreview_input:
   """ Required : 
   configID
   reportType
   reportStyleNum
   displayAmtAs
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  FinReportConfig to run report against  """  
      self.reportType:int = obj["reportType"]
      """  Type of report (0-BS/1-IS/2-CF)  """  
      self.reportStyleNum:int = obj["reportStyleNum"]
      """  Report Style number  """  
      self.displayAmtAs:str = obj["displayAmtAs"]
      """  Option to display Formula or hardcoded amount in preview  """  
      pass

class RunReportDesignPreview_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Preview Result Table XML  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFinReportConfigTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtFinReportConfigTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_FinReportConfigTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_FinReportConfigTableset] = obj["ds"]
      pass

      """  output parameters  """  

