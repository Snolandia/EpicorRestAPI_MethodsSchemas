import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysCubeDefSvc
# Description: Represents the SysCubeDef service
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SysCubeDefs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysCubeDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysCubeDefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysCubeDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs",headers=creds) as resp:
           return await resp.json()

async def post_SysCubeDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysCubeDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysCubeDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysCubeDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysCubeDefs_SysRowID(SysRowID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysCubeDef item
   Description: Calls GetByID to retrieve the SysCubeDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysCubeDef
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysCubeDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysCubeDefs_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysCubeDef for the service
   Description: Calls UpdateExt to update SysCubeDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysCubeDef
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysCubeDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysCubeDefs_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysCubeDef item
   Description: Call UpdateExt to delete SysCubeDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysCubeDef
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysCubeDefs_SysRowID_SysCubeParams(SysRowID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysCubeParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysCubeParams1
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysCubeParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs(" + SysRowID + ")/SysCubeParams",headers=creds) as resp:
           return await resp.json()

async def get_SysCubeDefs_SysRowID_SysCubeParams_ForeignSysRowID_Sequence(SysRowID, ForeignSysRowID, Sequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysCubeParam item
   Description: Calls GetByID to retrieve the SysCubeParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysCubeParam1
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysCubeParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeDefs(" + SysRowID + ")/SysCubeParams(" + ForeignSysRowID + "," + Sequence + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysCubeParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysCubeParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysCubeParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysCubeParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeParams",headers=creds) as resp:
           return await resp.json()

async def post_SysCubeParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysCubeParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysCubeParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysCubeParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysCubeParams_ForeignSysRowID_Sequence(ForeignSysRowID, Sequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysCubeParam item
   Description: Calls GetByID to retrieve the SysCubeParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysCubeParam
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysCubeParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeParams(" + ForeignSysRowID + "," + Sequence + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysCubeParams_ForeignSysRowID_Sequence(ForeignSysRowID, Sequence, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysCubeParam for the service
   Description: Calls UpdateExt to update SysCubeParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysCubeParam
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysCubeParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeParams(" + ForeignSysRowID + "," + Sequence + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysCubeParams_ForeignSysRowID_Sequence(ForeignSysRowID, Sequence, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysCubeParam item
   Description: Call UpdateExt to delete SysCubeParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysCubeParam
      :param ForeignSysRowID: Desc: ForeignSysRowID   Required: True   Allow empty value : True
      :param Sequence: Desc: Sequence   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/SysCubeParams(" + ForeignSysRowID + "," + Sequence + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysCubeDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysCubeDef, whereClauseSysCubeParam, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSysCubeDef=" + whereClauseSysCubeDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysCubeParam=" + whereClauseSysCubeParam
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(sysRowID, epicorHeaders = None):
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
   params += "sysRowID=" + sysRowID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Validate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Validate
   Description: Validate parameters prior to submitting to the agent or calling service directly.
   OperationID: Validate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Validate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Validate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysCubeDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysCubeDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysCubeDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysCubeDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysCubeDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysCubeParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysCubeParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysCubeParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysCubeParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysCubeParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysCubeDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysCubeDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysCubeDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysCubeDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysCubeDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysCubeParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysCubeParamRow] = obj["value"]
      pass

class Ice_Tablesets_SysCubeDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CubeID:str = obj["CubeID"]
      """  CubeID  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.RunDate:str = obj["RunDate"]
      """  RunDate  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsSummaryByBAQ:bool = obj["IsSummaryByBAQ"]
      """  IsSummaryByBAQ  """  
      self.IsSummaryByDate:bool = obj["IsSummaryByDate"]
      """  IsSummaryByDate  """  
      self.DeleteAction:str = obj["DeleteAction"]
      """  DeleteAction  """  
      self.Schedule:str = obj["Schedule"]
      """  Schedule  """  
      self.IsDynamic:bool = obj["IsDynamic"]
      """  IsDynamic  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.RunDateToken:str = obj["RunDateToken"]
      """  RunDateToken  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  AgentTaskNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCubeDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CubeID:str = obj["CubeID"]
      """  CubeID  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.RunDate:str = obj["RunDate"]
      """  RunDate  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsSummaryByBAQ:bool = obj["IsSummaryByBAQ"]
      """  IsSummaryByBAQ  """  
      self.IsSummaryByDate:bool = obj["IsSummaryByDate"]
      """  IsSummaryByDate  """  
      self.DeleteAction:str = obj["DeleteAction"]
      """  DeleteAction  """  
      self.Schedule:str = obj["Schedule"]
      """  Schedule  """  
      self.IsDynamic:bool = obj["IsDynamic"]
      """  IsDynamic  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.RunDateToken:str = obj["RunDateToken"]
      """  RunDateToken  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  AgentTaskNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCubeParamRow:
   def __init__(self, obj):
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.Dimension1ID:str = obj["Dimension1ID"]
      """  Dimension1ID  """  
      self.Dimension1:str = obj["Dimension1"]
      """  Dimension1  """  
      self.Dimension2ID:str = obj["Dimension2ID"]
      """  Dimension2ID  """  
      self.Dimension2:str = obj["Dimension2"]
      """  Dimension2  """  
      self.Dimension2Date:str = obj["Dimension2Date"]
      """  Dimension2Date  """  
      self.ValueDec01:str = obj["ValueDec01"]
      """  ValueDec01  """  
      self.ValueDec02:str = obj["ValueDec02"]
      """  ValueDec02  """  
      self.ValueDec03:str = obj["ValueDec03"]
      """  ValueDec03  """  
      self.ValueDec04:str = obj["ValueDec04"]
      """  ValueDec04  """  
      self.ValueDec05:str = obj["ValueDec05"]
      """  ValueDec05  """  
      self.ValueDec06:str = obj["ValueDec06"]
      """  ValueDec06  """  
      self.ValueDec07:str = obj["ValueDec07"]
      """  ValueDec07  """  
      self.ValueDec08:str = obj["ValueDec08"]
      """  ValueDec08  """  
      self.ValueDec09:str = obj["ValueDec09"]
      """  ValueDec09  """  
      self.ValueDec10:str = obj["ValueDec10"]
      """  ValueDec10  """  
      self.ValueInt01:str = obj["ValueInt01"]
      """  ValueInt01  """  
      self.ValueInt02:str = obj["ValueInt02"]
      """  ValueInt02  """  
      self.ValueInt03:str = obj["ValueInt03"]
      """  ValueInt03  """  
      self.ValueInt04:str = obj["ValueInt04"]
      """  ValueInt04  """  
      self.ValueInt05:str = obj["ValueInt05"]
      """  ValueInt05  """  
      self.SysShortChar01:str = obj["SysShortChar01"]
      """  SysShortChar01  """  
      self.SysShortChar02:str = obj["SysShortChar02"]
      """  SysShortChar02  """  
      self.SysShortChar03:str = obj["SysShortChar03"]
      """  SysShortChar03  """  
      self.SysShortChar04:str = obj["SysShortChar04"]
      """  SysShortChar04  """  
      self.SysShortChar05:str = obj["SysShortChar05"]
      """  SysShortChar05  """  
      self.SysShortChar06:str = obj["SysShortChar06"]
      """  SysShortChar06  """  
      self.SysShortChar07:str = obj["SysShortChar07"]
      """  SysShortChar07  """  
      self.SysShortChar08:str = obj["SysShortChar08"]
      """  SysShortChar08  """  
      self.SysShortChar09:str = obj["SysShortChar09"]
      """  SysShortChar09  """  
      self.SysShortChar10:str = obj["SysShortChar10"]
      """  SysShortChar10  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysCubeDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysCubeDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysCubeDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysCubeDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSysCubeDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysCubeDefTableset] = obj["ds"]
      pass

class GetNewSysCubeDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysCubeDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysCubeParam_input:
   """ Required : 
   ds
   foreignSysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysCubeDefTableset] = obj["ds"]
      self.foreignSysRowID:str = obj["foreignSysRowID"]
      pass

class GetNewSysCubeParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysCubeDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSysCubeDef
   whereClauseSysCubeParam
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysCubeDef:str = obj["whereClauseSysCubeDef"]
      self.whereClauseSysCubeParam:str = obj["whereClauseSysCubeParam"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysCubeDefTableset] = obj["returnObj"]
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

class Ice_Tablesets_SysCubeDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CubeID:str = obj["CubeID"]
      """  CubeID  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.RunDate:str = obj["RunDate"]
      """  RunDate  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsSummaryByBAQ:bool = obj["IsSummaryByBAQ"]
      """  IsSummaryByBAQ  """  
      self.IsSummaryByDate:bool = obj["IsSummaryByDate"]
      """  IsSummaryByDate  """  
      self.DeleteAction:str = obj["DeleteAction"]
      """  DeleteAction  """  
      self.Schedule:str = obj["Schedule"]
      """  Schedule  """  
      self.IsDynamic:bool = obj["IsDynamic"]
      """  IsDynamic  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.RunDateToken:str = obj["RunDateToken"]
      """  RunDateToken  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  AgentTaskNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCubeDefListTableset:
   def __init__(self, obj):
      self.SysCubeDefList:list[Ice_Tablesets_SysCubeDefListRow] = obj["SysCubeDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysCubeDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.CubeID:str = obj["CubeID"]
      """  CubeID  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.RunDate:str = obj["RunDate"]
      """  RunDate  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.IsSummaryByBAQ:bool = obj["IsSummaryByBAQ"]
      """  IsSummaryByBAQ  """  
      self.IsSummaryByDate:bool = obj["IsSummaryByDate"]
      """  IsSummaryByDate  """  
      self.DeleteAction:str = obj["DeleteAction"]
      """  DeleteAction  """  
      self.Schedule:str = obj["Schedule"]
      """  Schedule  """  
      self.IsDynamic:bool = obj["IsDynamic"]
      """  IsDynamic  """  
      self.IsRecurring:bool = obj["IsRecurring"]
      """  IsRecurring  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.RunDateToken:str = obj["RunDateToken"]
      """  RunDateToken  """  
      self.ProcessID:str = obj["ProcessID"]
      """  ProcessID  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      """  AgentTaskNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysCubeDefTableset:
   def __init__(self, obj):
      self.SysCubeDef:list[Ice_Tablesets_SysCubeDefRow] = obj["SysCubeDef"]
      self.SysCubeParam:list[Ice_Tablesets_SysCubeParamRow] = obj["SysCubeParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysCubeParamRow:
   def __init__(self, obj):
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      """  ForeignSysRowID  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.Dimension1ID:str = obj["Dimension1ID"]
      """  Dimension1ID  """  
      self.Dimension1:str = obj["Dimension1"]
      """  Dimension1  """  
      self.Dimension2ID:str = obj["Dimension2ID"]
      """  Dimension2ID  """  
      self.Dimension2:str = obj["Dimension2"]
      """  Dimension2  """  
      self.Dimension2Date:str = obj["Dimension2Date"]
      """  Dimension2Date  """  
      self.ValueDec01:str = obj["ValueDec01"]
      """  ValueDec01  """  
      self.ValueDec02:str = obj["ValueDec02"]
      """  ValueDec02  """  
      self.ValueDec03:str = obj["ValueDec03"]
      """  ValueDec03  """  
      self.ValueDec04:str = obj["ValueDec04"]
      """  ValueDec04  """  
      self.ValueDec05:str = obj["ValueDec05"]
      """  ValueDec05  """  
      self.ValueDec06:str = obj["ValueDec06"]
      """  ValueDec06  """  
      self.ValueDec07:str = obj["ValueDec07"]
      """  ValueDec07  """  
      self.ValueDec08:str = obj["ValueDec08"]
      """  ValueDec08  """  
      self.ValueDec09:str = obj["ValueDec09"]
      """  ValueDec09  """  
      self.ValueDec10:str = obj["ValueDec10"]
      """  ValueDec10  """  
      self.ValueInt01:str = obj["ValueInt01"]
      """  ValueInt01  """  
      self.ValueInt02:str = obj["ValueInt02"]
      """  ValueInt02  """  
      self.ValueInt03:str = obj["ValueInt03"]
      """  ValueInt03  """  
      self.ValueInt04:str = obj["ValueInt04"]
      """  ValueInt04  """  
      self.ValueInt05:str = obj["ValueInt05"]
      """  ValueInt05  """  
      self.SysShortChar01:str = obj["SysShortChar01"]
      """  SysShortChar01  """  
      self.SysShortChar02:str = obj["SysShortChar02"]
      """  SysShortChar02  """  
      self.SysShortChar03:str = obj["SysShortChar03"]
      """  SysShortChar03  """  
      self.SysShortChar04:str = obj["SysShortChar04"]
      """  SysShortChar04  """  
      self.SysShortChar05:str = obj["SysShortChar05"]
      """  SysShortChar05  """  
      self.SysShortChar06:str = obj["SysShortChar06"]
      """  SysShortChar06  """  
      self.SysShortChar07:str = obj["SysShortChar07"]
      """  SysShortChar07  """  
      self.SysShortChar08:str = obj["SysShortChar08"]
      """  SysShortChar08  """  
      self.SysShortChar09:str = obj["SysShortChar09"]
      """  SysShortChar09  """  
      self.SysShortChar10:str = obj["SysShortChar10"]
      """  SysShortChar10  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtSysCubeDefTableset:
   def __init__(self, obj):
      self.SysCubeDef:list[Ice_Tablesets_SysCubeDefRow] = obj["SysCubeDef"]
      self.SysCubeParam:list[Ice_Tablesets_SysCubeParamRow] = obj["SysCubeParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysCubeDefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysCubeDefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysCubeDefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysCubeDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Validate_input:
   """ Required : 
   SysCubeDefDataSet
   """  
   def __init__(self, obj):
      self.SysCubeDefDataSet      #schema had no properties on an object.
      pass

class Validate_output:
   def __init__(self, obj):
      pass

