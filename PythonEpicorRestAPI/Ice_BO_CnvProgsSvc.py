import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.CnvProgsSvc
# Description: Represents the CnvProgs Service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CnvProgs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CnvProgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CnvProgs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CnvProgsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs",headers=creds) as resp:
           return await resp.json()

async def post_CnvProgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CnvProgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CnvProgs_SystemCode_ConversionID(SystemCode, ConversionID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CnvProg item
   Description: Calls GetByID to retrieve the CnvProg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CnvProg
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ConversionID: Desc: ConversionID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs(" + SystemCode + "," + ConversionID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CnvProgs_SystemCode_ConversionID(SystemCode, ConversionID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CnvProg for the service
   Description: Calls UpdateExt to update CnvProg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CnvProg
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ConversionID: Desc: ConversionID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.CnvProgsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs(" + SystemCode + "," + ConversionID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CnvProgs_SystemCode_ConversionID(SystemCode, ConversionID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CnvProg item
   Description: Call UpdateExt to delete CnvProg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CnvProg
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ConversionID: Desc: ConversionID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/CnvProgs(" + SystemCode + "," + ConversionID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ConverLogs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConverLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConverLogs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ConverLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs",headers=creds) as resp:
           return await resp.json()

async def post_ConverLogs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConverLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ConverLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ConverLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConverLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConverLog item
   Description: Calls GetByID to retrieve the ConverLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConverLog
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ConverLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs(" + SysTaskNum + "," + EntryNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConverLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConverLog for the service
   Description: Calls UpdateExt to update ConverLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConverLog
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ConverLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs(" + SysTaskNum + "," + EntryNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConverLogs_SysTaskNum_EntryNum(SysTaskNum, EntryNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConverLog item
   Description: Call UpdateExt to delete ConverLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConverLog
      :param SysTaskNum: Desc: SysTaskNum   Required: True   Allow empty value : True
      :param EntryNum: Desc: EntryNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/ConverLogs(" + SysTaskNum + "," + EntryNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.CnvProgsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCnvProgs, whereClauseConverLog, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCnvProgs=" + whereClauseCnvProgs
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseConverLog=" + whereClauseConverLog
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(systemCode, conversionID, epicorHeaders = None):
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
   params += "systemCode=" + systemCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "conversionID=" + conversionID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSystemCodes(epicorHeaders = None):
   """  
   Summary: Invoke method GetSystemCodes
   Description: Returns a  delimited list of system codes.
   OperationID: GetSystemCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemCodes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_AddPatchConversionRecords(epicorHeaders = None):
   """  
   Summary: Invoke method AddPatchConversionRecords
   Description: Adds update conversion records.
   OperationID: AddPatchConversionRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPatchConversionRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UpdatePatchConversionCache(epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePatchConversionCache
   Description: Reset conversion cache
   OperationID: UpdatePatchConversionCache
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePatchConversionCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_RunsConversion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunsConversion
   Description: Method to run conversion
   OperationID: RunsConversion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunsConversion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunsConversion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSeedData(epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSeedData
   Description: Ensures all conversion programs that update seed data are in the table ice.cnvprogs
   OperationID: UpdateSeedData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSeedData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UploadSettingsFileFromServerPath(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadSettingsFileFromServerPath
   Description: Uploads the settings file from server path and delete it after finish.
   OperationID: UploadSettingsFileFromServerPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadSettingsFileFromServerPath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadSettingsFileFromServerPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportSettingsFileToServerPath(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportSettingsFileToServerPath
   Description: Exports the settings file to a server path.
   OperationID: ExportSettingsFileToServerPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportSettingsFileToServerPath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSettingsFileToServerPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteSettingsFileFromServer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteSettingsFileFromServer
   Description: Deletes the settings file from the provided fileRelativePath.
   OperationID: DeleteSettingsFileFromServer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteSettingsFileFromServer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteSettingsFileFromServer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCnvProgs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCnvProgs
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCnvProgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCnvProgs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCnvProgs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewConverLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewConverLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewConverLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewConverLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewConverLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.CnvProgsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_CnvProgsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_CnvProgsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_CnvProgsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ConverLogRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ConverLogRow] = obj["value"]
      pass

class Ice_Tablesets_CnvProgsListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ConversionID:str = obj["ConversionID"]
      """  ConversionID  """  
      self.RunSequence:int = obj["RunSequence"]
      """  RunSequence  """  
      self.Program:str = obj["Program"]
      """  Program  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.LastRunLevel:str = obj["LastRunLevel"]
      """  LastRunLevel  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AutoRun:bool = obj["AutoRun"]
      """  AutoRun  """  
      self.InitialRun:bool = obj["InitialRun"]
      """  InitialRun  """  
      self.UserRun:bool = obj["UserRun"]
      """  UserRun  """  
      self.ReCoverable:bool = obj["ReCoverable"]
      """  ReCoverable  """  
      self.ReRunable:bool = obj["ReRunable"]
      """  ReRunable  """  
      self.RunInDisconnectedCRM:bool = obj["RunInDisconnectedCRM"]
      """  RunInDisconnectedCRM  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.LastRunOn:str = obj["LastRunOn"]
      """  LastRunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.RunLog:str = obj["RunLog"]
      """  RunLog  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.RunTaskNum:int = obj["RunTaskNum"]
      """  RunTaskNum  """  
      self.ConversionSetting:str = obj["ConversionSetting"]
      """  ConversionSetting  """  
      self.SettingFilename:str = obj["SettingFilename"]
      """  SettingFilename  """  
      self.SettingLastUpdated:str = obj["SettingLastUpdated"]
      """  SettingLastUpdated  """  
      self.SettingLastUpdatedBy:str = obj["SettingLastUpdatedBy"]
      """  SettingLastUpdatedBy  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.UserPromptProgram:str = obj["UserPromptProgram"]
      """  UserPromptProgram  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ConversionType:str = obj["ConversionType"]
      """  ConversionType  """  
      self.RunFrequency:str = obj["RunFrequency"]
      """  RunFrequency  """  
      self.InternalRunDate:str = obj["InternalRunDate"]
      """  InternalRunDate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CnvProgsRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ConversionID:str = obj["ConversionID"]
      """  ConversionID  """  
      self.RunSequence:int = obj["RunSequence"]
      """  RunSequence  """  
      self.Program:str = obj["Program"]
      """  Program  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.LastRunLevel:str = obj["LastRunLevel"]
      """  LastRunLevel  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AutoRun:bool = obj["AutoRun"]
      """  AutoRun  """  
      self.InitialRun:bool = obj["InitialRun"]
      """  InitialRun  """  
      self.UserRun:bool = obj["UserRun"]
      """  UserRun  """  
      self.ReCoverable:bool = obj["ReCoverable"]
      """  ReCoverable  """  
      self.ReRunable:bool = obj["ReRunable"]
      """  ReRunable  """  
      self.RunInDisconnectedCRM:bool = obj["RunInDisconnectedCRM"]
      """  RunInDisconnectedCRM  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.LastRunOn:str = obj["LastRunOn"]
      """  LastRunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.RunLog:str = obj["RunLog"]
      """  RunLog  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.RunTaskNum:int = obj["RunTaskNum"]
      """  RunTaskNum  """  
      self.ConversionSetting:str = obj["ConversionSetting"]
      """  ConversionSetting  """  
      self.SettingFilename:str = obj["SettingFilename"]
      """  SettingFilename  """  
      self.SettingLastUpdated:str = obj["SettingLastUpdated"]
      """  SettingLastUpdated  """  
      self.SettingLastUpdatedBy:str = obj["SettingLastUpdatedBy"]
      """  SettingLastUpdatedBy  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.UserPromptProgram:str = obj["UserPromptProgram"]
      """  UserPromptProgram  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ConversionType:str = obj["ConversionType"]
      """  ConversionType  """  
      self.RunFrequency:str = obj["RunFrequency"]
      """  RunFrequency  """  
      self.InternalRunDate:str = obj["InternalRunDate"]
      """  InternalRunDate  """  
      self.Exec:bool = obj["Exec"]
      """  Execute  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ConverLogRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.EntryNum:int = obj["EntryNum"]
      """  Entry Number  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  EnteredOn  """  
      self.IsError:bool = obj["IsError"]
      """  Error indicator  """  
      self.MsgText:str = obj["MsgText"]
      """  Message Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MsgType:str = obj["MsgType"]
      """  MsgType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddPatchConversionRecords_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   systemCode
   conversionID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.conversionID:str = obj["conversionID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteSettingsFileFromServer_input:
   """ Required : 
   systemCode
   conversionId
   fileRelativePath
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.conversionId:str = obj["conversionId"]
      """  The conversion identifier.  """  
      self.fileRelativePath:str = obj["fileRelativePath"]
      """  The server file relative path.  """  
      pass

class DeleteSettingsFileFromServer_output:
   def __init__(self, obj):
      pass

class ExportSettingsFileToServerPath_input:
   """ Required : 
   systemCode
   conversionId
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.conversionId:str = obj["conversionId"]
      """  The conversion identifier.  """  
      pass

class ExportSettingsFileToServerPath_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The file server relative path in next format: temp\{RandomFolderName}\{SettingsFilename}  """  
      pass

class GetByID_input:
   """ Required : 
   systemCode
   conversionID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.conversionID:str = obj["conversionID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CnvProgsTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_CnvProgsTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_CnvProgsTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_CnvProgsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCnvProgs_input:
   """ Required : 
   ds
   systemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_CnvProgsTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      pass

class GetNewCnvProgs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_CnvProgsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewConverLog_input:
   """ Required : 
   ds
   sysTaskNum
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_CnvProgsTableset] = obj["ds"]
      self.sysTaskNum:int = obj["sysTaskNum"]
      pass

class GetNewConverLog_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_CnvProgsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCnvProgs
   whereClauseConverLog
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCnvProgs:str = obj["whereClauseCnvProgs"]
      self.whereClauseConverLog:str = obj["whereClauseConverLog"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_CnvProgsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSystemCodes_output:
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

class Ice_Tablesets_CnvProgsListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ConversionID:str = obj["ConversionID"]
      """  ConversionID  """  
      self.RunSequence:int = obj["RunSequence"]
      """  RunSequence  """  
      self.Program:str = obj["Program"]
      """  Program  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.LastRunLevel:str = obj["LastRunLevel"]
      """  LastRunLevel  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AutoRun:bool = obj["AutoRun"]
      """  AutoRun  """  
      self.InitialRun:bool = obj["InitialRun"]
      """  InitialRun  """  
      self.UserRun:bool = obj["UserRun"]
      """  UserRun  """  
      self.ReCoverable:bool = obj["ReCoverable"]
      """  ReCoverable  """  
      self.ReRunable:bool = obj["ReRunable"]
      """  ReRunable  """  
      self.RunInDisconnectedCRM:bool = obj["RunInDisconnectedCRM"]
      """  RunInDisconnectedCRM  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.LastRunOn:str = obj["LastRunOn"]
      """  LastRunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.RunLog:str = obj["RunLog"]
      """  RunLog  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.RunTaskNum:int = obj["RunTaskNum"]
      """  RunTaskNum  """  
      self.ConversionSetting:str = obj["ConversionSetting"]
      """  ConversionSetting  """  
      self.SettingFilename:str = obj["SettingFilename"]
      """  SettingFilename  """  
      self.SettingLastUpdated:str = obj["SettingLastUpdated"]
      """  SettingLastUpdated  """  
      self.SettingLastUpdatedBy:str = obj["SettingLastUpdatedBy"]
      """  SettingLastUpdatedBy  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.UserPromptProgram:str = obj["UserPromptProgram"]
      """  UserPromptProgram  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ConversionType:str = obj["ConversionType"]
      """  ConversionType  """  
      self.RunFrequency:str = obj["RunFrequency"]
      """  RunFrequency  """  
      self.InternalRunDate:str = obj["InternalRunDate"]
      """  InternalRunDate  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CnvProgsListTableset:
   def __init__(self, obj):
      self.CnvProgsList:list[Ice_Tablesets_CnvProgsListRow] = obj["CnvProgsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_CnvProgsRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ConversionID:str = obj["ConversionID"]
      """  ConversionID  """  
      self.RunSequence:int = obj["RunSequence"]
      """  RunSequence  """  
      self.Program:str = obj["Program"]
      """  Program  """  
      self.RunLevel:str = obj["RunLevel"]
      """  RunLevel  """  
      self.LastRunLevel:str = obj["LastRunLevel"]
      """  LastRunLevel  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.AutoRun:bool = obj["AutoRun"]
      """  AutoRun  """  
      self.InitialRun:bool = obj["InitialRun"]
      """  InitialRun  """  
      self.UserRun:bool = obj["UserRun"]
      """  UserRun  """  
      self.ReCoverable:bool = obj["ReCoverable"]
      """  ReCoverable  """  
      self.ReRunable:bool = obj["ReRunable"]
      """  ReRunable  """  
      self.RunInDisconnectedCRM:bool = obj["RunInDisconnectedCRM"]
      """  RunInDisconnectedCRM  """  
      self.ProgStatus:str = obj["ProgStatus"]
      """  ProgStatus  """  
      self.LastRunOn:str = obj["LastRunOn"]
      """  LastRunOn  """  
      self.RunUserID:str = obj["RunUserID"]
      """  RunUserID  """  
      self.RunLog:str = obj["RunLog"]
      """  RunLog  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.RunTaskNum:int = obj["RunTaskNum"]
      """  RunTaskNum  """  
      self.ConversionSetting:str = obj["ConversionSetting"]
      """  ConversionSetting  """  
      self.SettingFilename:str = obj["SettingFilename"]
      """  SettingFilename  """  
      self.SettingLastUpdated:str = obj["SettingLastUpdated"]
      """  SettingLastUpdated  """  
      self.SettingLastUpdatedBy:str = obj["SettingLastUpdatedBy"]
      """  SettingLastUpdatedBy  """  
      self.ProgressPercent:int = obj["ProgressPercent"]
      """  ProgressPercent  """  
      self.UserPromptProgram:str = obj["UserPromptProgram"]
      """  UserPromptProgram  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ConversionType:str = obj["ConversionType"]
      """  ConversionType  """  
      self.RunFrequency:str = obj["RunFrequency"]
      """  RunFrequency  """  
      self.InternalRunDate:str = obj["InternalRunDate"]
      """  InternalRunDate  """  
      self.Exec:bool = obj["Exec"]
      """  Execute  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_CnvProgsTableset:
   def __init__(self, obj):
      self.CnvProgs:list[Ice_Tablesets_CnvProgsRow] = obj["CnvProgs"]
      self.ConverLog:list[Ice_Tablesets_ConverLogRow] = obj["ConverLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ConverLogRow:
   def __init__(self, obj):
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.EntryNum:int = obj["EntryNum"]
      """  Entry Number  """  
      self.EnteredOn:str = obj["EnteredOn"]
      """  EnteredOn  """  
      self.IsError:bool = obj["IsError"]
      """  Error indicator  """  
      self.MsgText:str = obj["MsgText"]
      """  Message Text  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MsgType:str = obj["MsgType"]
      """  MsgType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtCnvProgsTableset:
   def __init__(self, obj):
      self.CnvProgs:list[Ice_Tablesets_CnvProgsRow] = obj["CnvProgs"]
      self.ConverLog:list[Ice_Tablesets_ConverLogRow] = obj["ConverLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class RunsConversion_input:
   """ Required : 
   systemCode
   conversionID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The ssytem code.  """  
      self.conversionID:str = obj["conversionID"]
      """  The conversion ID to run.  """  
      pass

class RunsConversion_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtCnvProgsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtCnvProgsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdatePatchConversionCache_output:
   def __init__(self, obj):
      pass

class UpdateSeedData_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_CnvProgsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_CnvProgsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadSettingsFileFromServerPath_input:
   """ Required : 
   systemCode
   conversionId
   fileRelativePath
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.conversionId:str = obj["conversionId"]
      """  The conversion identifier.  """  
      self.fileRelativePath:str = obj["fileRelativePath"]
      """  The file relative path.  """  
      pass

class UploadSettingsFileFromServerPath_output:
   def __init__(self, obj):
      pass

