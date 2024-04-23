import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ContextMenuDataSvc
# Description: Represents the ContextMenuDataSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuDatas(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContextMenuDatas items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuDatas
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas",headers=creds) as resp:
           return await resp.json()

async def post_ContextMenuDatas(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuDatas
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuDatas_LikeID_ContextTypeCode(LikeID, ContextTypeCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContextMenuData item
   Description: Calls GetByID to retrieve the ContextMenuData item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuData
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContextMenuDatas_LikeID_ContextTypeCode(LikeID, ContextTypeCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContextMenuData for the service
   Description: Calls UpdateExt to update ContextMenuData. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuData
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContextMenuDatas_LikeID_ContextTypeCode(LikeID, ContextTypeCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContextMenuData item
   Description: Call UpdateExt to delete ContextMenuData item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuData
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuDatas_LikeID_ContextTypeCode_ContextMenuItems(LikeID, ContextTypeCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ContextMenuItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ContextMenuItems1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")/ContextMenuItems",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuDatas_LikeID_ContextTypeCode_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID, ContextTypeCode, ContextMenuID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContextMenuItem item
   Description: Calls GetByID to retrieve the ContextMenuItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuItem1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuDatas(" + LikeID + "," + ContextTypeCode + ")/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContextMenuItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuItems
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems",headers=creds) as resp:
           return await resp.json()

async def post_ContextMenuItems(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID, ContextTypeCode, ContextMenuID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContextMenuItem item
   Description: Calls GetByID to retrieve the ContextMenuItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuItem
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID, ContextTypeCode, ContextMenuID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContextMenuItem for the service
   Description: Calls UpdateExt to update ContextMenuItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuItem
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID(LikeID, ContextTypeCode, ContextMenuID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContextMenuItem item
   Description: Call UpdateExt to delete ContextMenuItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuItem
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_AlternateKeyLikes(LikeID, ContextTypeCode, ContextMenuID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlternateKeyLikes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlternateKeyLikes1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/AlternateKeyLikes",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID, ContextTypeCode, ContextMenuID, LikeField, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternateKeyLike item
   Description: Calls GetByID to retrieve the AlternateKeyLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyLike1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_LaunchOptions(LikeID, ContextTypeCode, ContextMenuID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaunchOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaunchOptions1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LaunchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/LaunchOptions",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaunchOption item
   Description: Calls GetByID to retrieve the LaunchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaunchOption1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_SearchOptions(LikeID, ContextTypeCode, ContextMenuID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SearchOptions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SearchOptions1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SearchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/SearchOptions",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItems_LikeID_ContextTypeCode_ContextMenuID_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SearchOption item
   Description: Calls GetByID to retrieve the SearchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SearchOption1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItems(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + ")/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlternateKeyLikes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlternateKeyLikes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateKeyLikes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes",headers=creds) as resp:
           return await resp.json()

async def post_AlternateKeyLikes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateKeyLikes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID, ContextTypeCode, ContextMenuID, LikeField, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternateKeyLike item
   Description: Calls GetByID to retrieve the AlternateKeyLike item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyLike
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID, ContextTypeCode, ContextMenuID, LikeField, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlternateKeyLike for the service
   Description: Calls UpdateExt to update AlternateKeyLike. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternateKeyLike
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AlternateKeyLikeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlternateKeyLikes_LikeID_ContextTypeCode_ContextMenuID_LikeField(LikeID, ContextTypeCode, ContextMenuID, LikeField, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlternateKeyLike item
   Description: Call UpdateExt to delete AlternateKeyLike item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternateKeyLike
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param LikeField: Desc: LikeField   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyLikes(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + LikeField + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaunchOptions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaunchOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaunchOptions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LaunchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions",headers=creds) as resp:
           return await resp.json()

async def post_LaunchOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaunchOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaunchOption item
   Description: Calls GetByID to retrieve the LaunchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaunchOption
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaunchOption for the service
   Description: Calls UpdateExt to update LaunchOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaunchOption
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.LaunchOptionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaunchOption item
   Description: Call UpdateExt to delete LaunchOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaunchOption
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeyBindings(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlternateKeyBindings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlternateKeyBindings1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeyBindings",headers=creds) as resp:
           return await resp.json()

async def get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, AlternateKeyBinding1, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternateKeyBinding item
   Description: Calls GetByID to retrieve the AlternateKeyBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyBinding1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param AlternateKeyBinding1: Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeys(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get AlternateKeys items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AlternateKeys1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeys",headers=creds) as resp:
           return await resp.json()

async def get_LaunchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternateKey item
   Description: Calls GetByID to retrieve the AlternateKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKey1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/LaunchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlternateKeyBindings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlternateKeyBindings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateKeyBindings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings",headers=creds) as resp:
           return await resp.json()

async def post_AlternateKeyBindings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateKeyBindings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, AlternateKeyBinding1, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternateKeyBinding item
   Description: Calls GetByID to retrieve the AlternateKeyBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKeyBinding
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param AlternateKeyBinding1: Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, AlternateKeyBinding1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlternateKeyBinding for the service
   Description: Calls UpdateExt to update AlternateKeyBinding. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternateKeyBinding
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param AlternateKeyBinding1: Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AlternateKeyBindingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlternateKeyBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_AlternateKeyBinding1(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, AlternateKeyBinding1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlternateKeyBinding item
   Description: Call UpdateExt to delete AlternateKeyBinding item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternateKeyBinding
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param AlternateKeyBinding1: Desc: AlternateKeyBinding1   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeyBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + AlternateKeyBinding1 + ")",headers=creds) as resp:
           return await resp.json()

async def get_AlternateKeys(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlternateKeys items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlternateKeys
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.AlternateKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys",headers=creds) as resp:
           return await resp.json()

async def post_AlternateKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlternateKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlternateKey item
   Description: Calls GetByID to retrieve the AlternateKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlternateKey
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlternateKey for the service
   Description: Calls UpdateExt to update AlternateKey. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlternateKey
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.AlternateKeyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlternateKeys_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlternateKey item
   Description: Call UpdateExt to delete AlternateKey item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlternateKey
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/AlternateKeys(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")",headers=creds) as resp:
           return await resp.json()

async def get_SearchOptions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SearchOptions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SearchOptions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SearchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions",headers=creds) as resp:
           return await resp.json()

async def post_SearchOptions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SearchOptions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SearchOption item
   Description: Calls GetByID to retrieve the SearchOption item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SearchOption
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SearchOption for the service
   Description: Calls UpdateExt to update SearchOption. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SearchOption
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SearchOptionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SearchOption item
   Description: Call UpdateExt to delete SearchOption item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SearchOption
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseBindings(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhereClauseBindings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhereClauseBindings1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseBindings",headers=creds) as resp:
           return await resp.json()

async def get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhereClauseBinding item
   Description: Calls GetByID to retrieve the WhereClauseBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseBinding1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")",headers=creds) as resp:
           return await resp.json()

async def get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseTokens(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get WhereClauseTokens items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WhereClauseTokens1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseTokenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseTokens",headers=creds) as resp:
           return await resp.json()

async def get_SearchOptions_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, BindingToken, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhereClauseToken item
   Description: Calls GetByID to retrieve the WhereClauseToken item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseToken1
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param BindingToken: Desc: BindingToken   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/SearchOptions(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + ")/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhereClauseBindings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhereClauseBindings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhereClauseBindings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings",headers=creds) as resp:
           return await resp.json()

async def post_WhereClauseBindings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhereClauseBindings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhereClauseBinding item
   Description: Calls GetByID to retrieve the WhereClauseBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseBinding
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhereClauseBinding for the service
   Description: Calls UpdateExt to update WhereClauseBinding. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhereClauseBinding
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.WhereClauseBindingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhereClauseBindings_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhereClauseBinding item
   Description: Call UpdateExt to delete WhereClauseBinding item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhereClauseBinding
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseBindings(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + ")",headers=creds) as resp:
           return await resp.json()

async def get_WhereClauseTokens(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WhereClauseTokens items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WhereClauseTokens
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.WhereClauseTokenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens",headers=creds) as resp:
           return await resp.json()

async def post_WhereClauseTokens(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WhereClauseTokens
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, BindingToken, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WhereClauseToken item
   Description: Calls GetByID to retrieve the WhereClauseToken item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WhereClauseToken
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param BindingToken: Desc: BindingToken   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, BindingToken, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WhereClauseToken for the service
   Description: Calls UpdateExt to update WhereClauseToken. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WhereClauseToken
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param BindingToken: Desc: BindingToken   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.WhereClauseTokenRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WhereClauseTokens_LikeID_ContextTypeCode_ContextMenuID_CalledFrom_CurrentBinding_BindingToken(LikeID, ContextTypeCode, ContextMenuID, CalledFrom, CurrentBinding, BindingToken, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WhereClauseToken item
   Description: Call UpdateExt to delete WhereClauseToken item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WhereClauseToken
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ContextMenuID: Desc: ContextMenuID   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param CurrentBinding: Desc: CurrentBinding   Required: True   Allow empty value : True
      :param BindingToken: Desc: BindingToken   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/WhereClauseTokens(" + LikeID + "," + ContextTypeCode + "," + ContextMenuID + "," + CalledFrom + "," + CurrentBinding + "," + BindingToken + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItemTemps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContextMenuItemTemps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuItemTemps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuItemTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps",headers=creds) as resp:
           return await resp.json()

async def post_ContextMenuItemTemps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuItemTemps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuItemTemps_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContextMenuItemTemp item
   Description: Calls GetByID to retrieve the ContextMenuItemTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuItemTemp
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContextMenuItemTemps_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContextMenuItemTemp for the service
   Description: Calls UpdateExt to update ContextMenuItemTemp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuItemTemp
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuItemTempRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContextMenuItemTemps_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContextMenuItemTemp item
   Description: Call UpdateExt to delete ContextMenuItemTemp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuItemTemp
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuItemTemps(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuTemps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContextMenuTemps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextMenuTemps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps",headers=creds) as resp:
           return await resp.json()

async def post_ContextMenuTemps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextMenuTemps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContextMenuTemps_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContextMenuTemp item
   Description: Calls GetByID to retrieve the ContextMenuTemp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextMenuTemp
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContextMenuTemps_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContextMenuTemp for the service
   Description: Calls UpdateExt to update ContextMenuTemp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextMenuTemp
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextMenuTempRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContextMenuTemps_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContextMenuTemp item
   Description: Call UpdateExt to delete ContextMenuTemp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextMenuTemp
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextMenuTemps(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ContextValidations(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ContextValidations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ContextValidations
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextValidationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations",headers=creds) as resp:
           return await resp.json()

async def post_ContextValidations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ContextValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ContextValidations_LikeID_ContextTypeCode_ValidationAdapter(LikeID, ContextTypeCode, ValidationAdapter, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ContextValidation item
   Description: Calls GetByID to retrieve the ContextValidation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ContextValidation
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ValidationAdapter: Desc: ValidationAdapter   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations(" + LikeID + "," + ContextTypeCode + "," + ValidationAdapter + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ContextValidations_LikeID_ContextTypeCode_ValidationAdapter(LikeID, ContextTypeCode, ValidationAdapter, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ContextValidation for the service
   Description: Calls UpdateExt to update ContextValidation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ContextValidation
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ValidationAdapter: Desc: ValidationAdapter   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ContextValidationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations(" + LikeID + "," + ContextTypeCode + "," + ValidationAdapter + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ContextValidations_LikeID_ContextTypeCode_ValidationAdapter(LikeID, ContextTypeCode, ValidationAdapter, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ContextValidation item
   Description: Call UpdateExt to delete ContextValidation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ContextValidation
      :param LikeID: Desc: LikeID   Required: True   Allow empty value : True
      :param ContextTypeCode: Desc: ContextTypeCode   Required: True   Allow empty value : True
      :param ValidationAdapter: Desc: ValidationAdapter   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/ContextValidations(" + LikeID + "," + ContextTypeCode + "," + ValidationAdapter + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ContextMenuListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseContextMenu, whereClauseContextMenuItem, whereClauseAlternateKeyLike, whereClauseLaunchOption, whereClauseAlternateKeyBinding, whereClauseAlternateKey, whereClauseSearchOption, whereClauseWhereClauseBinding, whereClauseWhereClauseToken, whereClauseContextMenuItemTemp, whereClauseContextMenuTemp, whereClauseContextValidation, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseContextMenu=" + whereClauseContextMenu
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContextMenuItem=" + whereClauseContextMenuItem
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlternateKeyLike=" + whereClauseAlternateKeyLike
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaunchOption=" + whereClauseLaunchOption
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlternateKeyBinding=" + whereClauseAlternateKeyBinding
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAlternateKey=" + whereClauseAlternateKey
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSearchOption=" + whereClauseSearchOption
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhereClauseBinding=" + whereClauseWhereClauseBinding
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseWhereClauseToken=" + whereClauseWhereClauseToken
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContextMenuItemTemp=" + whereClauseContextMenuItemTemp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContextMenuTemp=" + whereClauseContextMenuTemp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseContextValidation=" + whereClauseContextValidation
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(likeID, contextTypeCode, epicorHeaders = None):
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
   params += "likeID=" + likeID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "contextTypeCode=" + contextTypeCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCustomRows(epicorHeaders = None):
   """  
   Summary: Invoke method GetCustomRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: GetCustomRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeList
   Description: Get the Context Menu as Collection of LikeListInfo records
   OperationID: GetContextMenuLikeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeListItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeListItem
   Description: Get the LikeListInfo item that represents the Context Menu Item
   OperationID: GetContextMenuLikeListItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeListItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeListItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeListItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeListItems
   Description: Get the list of LikeListInfo items that represent the Context Menu Items
   OperationID: GetContextMenuLikeListItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeListItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeListItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeDetailItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeDetailItem
   Description: Get the LikeListInfo item that represents the Detailed Context Menu Item with search
   OperationID: GetContextMenuLikeDetailItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeDetailItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeDetailItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeDetailItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeDetailItems
   Description: Get the list of LikeListInfo items that represent the Detailed Context Menu Item with search
   OperationID: GetContextMenuLikeDetailItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeDetailItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeDetailItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateContextMenuLikeItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateContextMenuLikeItems
   Description: Updates the context menu XML document based upon the update mode.
   OperationID: UpdateContextMenuLikeItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateContextMenuLikeItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateContextMenuLikeItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeItemForLayer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeItemForLayer
   Description: Gets the context menu item for the given like and all it's child nodes for the specified layer.
   OperationID: GetContextMenuLikeItemForLayer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeItemForLayer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeItemForLayer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeHeaderByLikeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeHeaderByLikeID
   Description: Gets the context menu item for the given like and all it's child nodes for the specified layer.
   OperationID: GetContextMenuLikeHeaderByLikeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeHeaderByLikeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeHeaderByLikeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuLikeHeader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuLikeHeader
   Description: Gets the context menu item for the given like and all it's child nodes for the specified layer.
   OperationID: GetContextMenuLikeHeader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuLikeHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuLikeHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddNewQuickSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNewQuickSearch
   Description: Adds a QS context menu item to the context menu XML stored in XXXDef.
   OperationID: AddNewQuickSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewQuickSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewQuickSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteQuickSearchOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteQuickSearchOption
   Description: Deletes the specified Quick Search from the context menu XML stored in XXXDef.
   OperationID: DeleteQuickSearchOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteQuickSearchOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteQuickSearchOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuDataList(epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuDataList
   Description: Get List of existing Context Menu data.
   OperationID: GetContextMenuDataList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuDataList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CustomGetByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomGetByID
   Description: Get By ID of existing ContextMenu from Temp.
   OperationID: CustomGetByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomGetByIDorError(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomGetByIDorError
   Description: Get By ID of existing ContextMenu from Temp.
   OperationID: CustomGetByIDorError
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomGetByIDorError_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByIDorError_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LikeIDChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LikeIDChanging
   Description: Likeid changing validataion.
   OperationID: LikeIDChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LikeIDChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LikeIDChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateLikeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLikeID
   Description: Checks if the LikeID string would make a valid XML node name
   OperationID: ValidateLikeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLikeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLikeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsValidLikeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidLikeID
   Description: Checks if the given LikeID does not start with a reserved key word used in the base Context Menu
   OperationID: IsValidLikeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidLikeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidLikeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContextMenuRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContextMenuRows
   OperationID: GetContextMenuRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContextMenuRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContextMenuRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomizationRights(epicorHeaders = None):
   """  
   Summary: Invoke method CustomizationRights
   Description: Return if user can customize.
   OperationID: CustomizationRights
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomizationRights_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewContextMenu(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContextMenu
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContextMenu
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContextMenu_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContextMenu_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContextMenuItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContextMenuItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContextMenuItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContextMenuItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContextMenuItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlternateKeyLike(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlternateKeyLike
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlternateKeyLike
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlternateKeyLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlternateKeyLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaunchOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaunchOption
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaunchOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaunchOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaunchOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlternateKeyBinding(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlternateKeyBinding
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlternateKeyBinding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlternateKeyBinding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlternateKeyBinding_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlternateKey(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlternateKey
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlternateKey
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlternateKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlternateKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSearchOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSearchOption
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSearchOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSearchOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSearchOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhereClauseBinding(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhereClauseBinding
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhereClauseBinding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhereClauseBinding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClauseBinding_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWhereClauseToken(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWhereClauseToken
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWhereClauseToken
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWhereClauseToken_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWhereClauseToken_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewContextValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewContextValidation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewContextValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewContextValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewContextValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ContextMenuDataSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyBindingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AlternateKeyBindingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyLikeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AlternateKeyLikeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_AlternateKeyRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_AlternateKeyRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ContextMenuItemRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuItemTempRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ContextMenuItemTempRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ContextMenuListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ContextMenuRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextMenuTempRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ContextMenuTempRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ContextValidationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ContextValidationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LaunchOptionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_LaunchOptionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SearchOptionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SearchOptionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseBindingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_WhereClauseBindingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_WhereClauseTokenRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_WhereClauseTokenRow] = obj["value"]
      pass

class Ice_Tablesets_AlternateKeyBindingRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.AlternateKeyBinding1:str = obj["AlternateKeyBinding1"]
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AlternateKeyLikeRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.LikeField:str = obj["LikeField"]
      """  LikeField  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AlternateKeyRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ContextValue:str = obj["ContextValue"]
      """  ContextValue  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextMenuItemRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.ContextMenuText:str = obj["ContextMenuText"]
      """  ContextMenuText  """  
      self.ProcessCall:str = obj["ProcessCall"]
      """  ProcessCall  """  
      self.ProcessType:str = obj["ProcessType"]
      """  ProcessType  """  
      self.MenuID:str = obj["MenuID"]
      """  MenuID  """  
      self.AdapterID:str = obj["AdapterID"]
      """  AdapterID  """  
      self.SearchMode:str = obj["SearchMode"]
      """  SearchMode  """  
      self.TrackerID:str = obj["TrackerID"]
      """  TrackerID  """  
      self.QSValidation:bool = obj["QSValidation"]
      """  QSValidation  """  
      self.QSBaseDefault:bool = obj["QSBaseDefault"]
      """  QSBaseDefault  """  
      self.QSContextDefault:bool = obj["QSContextDefault"]
      """  QSContextDefault  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MenuOrder:int = obj["MenuOrder"]
      """  MenuOrder  """  
      self.MenuEnabled:bool = obj["MenuEnabled"]
      """  MenuEnabled  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.TempID:str = obj["TempID"]
      """  Temporary ID to identify row.  """  
      self.ProcessCallOrg:str = obj["ProcessCallOrg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextMenuItemTempRow:
   def __init__(self, obj):
      self.AdapterID:str = obj["AdapterID"]
      """  AdapterID  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.ContextMenuText:str = obj["ContextMenuText"]
      """  ContextMenuText  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.MenuEnabled:bool = obj["MenuEnabled"]
      """  MenuEnabled  """  
      self.MenuID:str = obj["MenuID"]
      """  MenuID  """  
      self.MenuOrder:int = obj["MenuOrder"]
      """  MenuOrder  """  
      self.ProcessCall:str = obj["ProcessCall"]
      """  ProcessCall  """  
      self.ProcessType:str = obj["ProcessType"]
      """  ProcessType  """  
      self.QSBaseDefault:bool = obj["QSBaseDefault"]
      """  QSBaseDefault  """  
      self.QSContextDefault:bool = obj["QSContextDefault"]
      """  QSContextDefault  """  
      self.QSValidation:bool = obj["QSValidation"]
      """  QSValidation  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SearchMode:str = obj["SearchMode"]
      """  SearchMode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.TrackerID:str = obj["TrackerID"]
      """  TrackerID  """  
      self.UpdateType:str = obj["UpdateType"]
      """  UpdateType  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextMenuListRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
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

class Ice_Tablesets_ContextMenuRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
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

class Ice_Tablesets_ContextMenuTempRow:
   def __init__(self, obj):
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.UpdateType:str = obj["UpdateType"]
      """  UpdateType  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextValidationRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ValidationAdapter:str = obj["ValidationAdapter"]
      """  ValidationAdapter  """  
      self.ValidationType:str = obj["ValidationType"]
      """  ValidationType  """  
      self.RetrieverCombo:str = obj["RetrieverCombo"]
      """  RetrieverCombo  """  
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

class Ice_Tablesets_LaunchOptionRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.LaunchModal:bool = obj["LaunchModal"]
      """  LaunchModal  """  
      self.EpiReadOnly:bool = obj["EpiReadOnly"]
      """  EpiReadOnly  """  
      self.SuppressPublisher:bool = obj["SuppressPublisher"]
      """  SuppressPublisher  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ContextValue:str = obj["ContextValue"]
      """  ContextValue  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SearchOptionRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
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

class Ice_Tablesets_WhereClauseBindingRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.SearchTable:str = obj["SearchTable"]
      """  SearchTable  """  
      self.SearchTitle:str = obj["SearchTitle"]
      """  SearchTitle  """  
      self.WhereClauseString:str = obj["WhereClauseString"]
      """  WhereClauseString  """  
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

class Ice_Tablesets_WhereClauseTokenRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.BindingToken:str = obj["BindingToken"]
      """  BindingToken  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddNewQuickSearch_input:
   """ Required : 
   likeField
   quickSearchID
   description
   calledFrom
   isShared
   forValidation
   baseDefault
   contextDefault
   """  
   def __init__(self, obj):
      self.likeField:str = obj["likeField"]
      self.quickSearchID:str = obj["quickSearchID"]
      self.description:str = obj["description"]
      self.calledFrom:str = obj["calledFrom"]
      self.isShared:bool = obj["isShared"]
      self.forValidation:bool = obj["forValidation"]
      self.baseDefault:bool = obj["baseDefault"]
      self.contextDefault:bool = obj["contextDefault"]
      pass

class AddNewQuickSearch_output:
   def __init__(self, obj):
      pass

class CustomGetByID_input:
   """ Required : 
   likeID
   contextTypeCode
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      pass

class CustomGetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class CustomGetByIDorError_input:
   """ Required : 
   likeID
   contextTypeCode
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      pass

class CustomGetByIDorError_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class CustomizationRights_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   likeID
   contextTypeCode
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteQuickSearchOption_input:
   """ Required : 
   likeField
   quickSearchID
   description
   isShared
   """  
   def __init__(self, obj):
      self.likeField:str = obj["likeField"]
      self.quickSearchID:str = obj["quickSearchID"]
      self.description:str = obj["description"]
      self.isShared:bool = obj["isShared"]
      pass

class DeleteQuickSearchOption_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   likeID
   contextTypeCode
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class GetContextMenuDataList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class GetContextMenuLikeDetailItem_input:
   """ Required : 
   LikeId
   isEwa
   properties
   """  
   def __init__(self, obj):
      self.LikeId:str = obj["LikeId"]
      """  The Like Id for the requested Context Menu Item  """  
      self.isEwa:bool = obj["isEwa"]
      """  true when getting list for EWA  """  
      self.properties:list[Ice_BO_ContextMenuData_LikeSearchProperties] = obj["properties"]
      pass

class GetContextMenuLikeDetailItem_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ContextMenuData_LikeListInfo] = obj["returnObj"]
      pass

class GetContextMenuLikeDetailItems_input:
   """ Required : 
   LikeIds
   isEwa
   properties
   """  
   def __init__(self, obj):
      self.LikeIds:str = obj["LikeIds"]
      """  The list of Like Ids for the requested Context Menu Items  """  
      self.isEwa:bool = obj["isEwa"]
      """  true when getting list for EWA  """  
      self.properties:list[Ice_BO_ContextMenuData_LikeSearchProperties] = obj["properties"]
      pass

class GetContextMenuLikeDetailItems_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ContextMenuData_LikeListInfo] = obj["returnObj"]
      """  LikeListInfo record that represents the list of nodes from ContextMenu.xml  """  
      pass

class GetContextMenuLikeHeaderByLikeID_input:
   """ Required : 
   likeID
   customized
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.customized:bool = obj["customized"]
      """  True to only return base or customized, false returns all layers available (base, customized, personalized).  """  
      pass

class GetContextMenuLikeHeaderByLikeID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class GetContextMenuLikeHeader_input:
   """ Required : 
   likeID
   customized
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.customized:bool = obj["customized"]
      """  True to only return base or customized, false returns all layers available (base, customized, personalized).  """  
      pass

class GetContextMenuLikeHeader_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class GetContextMenuLikeItemForLayer_input:
   """ Required : 
   likeID
   customized
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      self.customized:bool = obj["customized"]
      """  True to only return base or customized, false returns all layers available (base, customized, personalized).  """  
      pass

class GetContextMenuLikeItemForLayer_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class GetContextMenuLikeListItem_input:
   """ Required : 
   LikeId
   isEwa
   """  
   def __init__(self, obj):
      self.LikeId:str = obj["LikeId"]
      """  The Like Id for the requested Context Menu Item  """  
      self.isEwa:bool = obj["isEwa"]
      """  true when getting list for EWA  """  
      pass

class GetContextMenuLikeListItem_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ContextMenuData_LikeListInfo] = obj["returnObj"]
      pass

class GetContextMenuLikeListItems_input:
   """ Required : 
   LikeIds
   isEwa
   """  
   def __init__(self, obj):
      self.LikeIds:str = obj["LikeIds"]
      """  The list of Like Ids for the requested Context Menu Items  """  
      self.isEwa:bool = obj["isEwa"]
      """  true when getting list for EWA  """  
      pass

class GetContextMenuLikeListItems_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ContextMenuData_LikeListInfo] = obj["returnObj"]
      """  LikeListInfo record that represents the list of nodes from ContextMenu.xml  """  
      pass

class GetContextMenuLikeList_input:
   """ Required : 
   isEwa
   """  
   def __init__(self, obj):
      self.isEwa:bool = obj["isEwa"]
      """  true when getting list for EWA  """  
      pass

class GetContextMenuLikeList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BO_ContextMenuData_LikeListInfo] = obj["returnObj"]
      """  Collection of LikeListInfo records that represents the ContextMenu.xml  """  
      pass

class GetContextMenuRows_input:
   """ Required : 
   whereClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      pass

class GetContextMenuRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

class GetCustomRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ContextMenuDataListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAlternateKeyBinding_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   calledFrom
   currentBinding
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      self.calledFrom:str = obj["calledFrom"]
      self.currentBinding:str = obj["currentBinding"]
      pass

class GetNewAlternateKeyBinding_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlternateKeyLike_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      pass

class GetNewAlternateKeyLike_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAlternateKey_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   calledFrom
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetNewAlternateKey_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContextMenuItem_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      pass

class GetNewContextMenuItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContextMenu_input:
   """ Required : 
   ds
   likeID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      pass

class GetNewContextMenu_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewContextValidation_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      pass

class GetNewContextValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaunchOption_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      pass

class GetNewLaunchOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSearchOption_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      pass

class GetNewSearchOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhereClauseBinding_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   calledFrom
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetNewWhereClauseBinding_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWhereClauseToken_input:
   """ Required : 
   ds
   likeID
   contextTypeCode
   contextMenuID
   calledFrom
   currentBinding
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      self.likeID:str = obj["likeID"]
      self.contextTypeCode:str = obj["contextTypeCode"]
      self.contextMenuID:str = obj["contextMenuID"]
      self.calledFrom:str = obj["calledFrom"]
      self.currentBinding:str = obj["currentBinding"]
      pass

class GetNewWhereClauseToken_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseContextMenu
   whereClauseContextMenuItem
   whereClauseAlternateKeyLike
   whereClauseLaunchOption
   whereClauseAlternateKeyBinding
   whereClauseAlternateKey
   whereClauseSearchOption
   whereClauseWhereClauseBinding
   whereClauseWhereClauseToken
   whereClauseContextMenuItemTemp
   whereClauseContextMenuTemp
   whereClauseContextValidation
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseContextMenu:str = obj["whereClauseContextMenu"]
      self.whereClauseContextMenuItem:str = obj["whereClauseContextMenuItem"]
      self.whereClauseAlternateKeyLike:str = obj["whereClauseAlternateKeyLike"]
      self.whereClauseLaunchOption:str = obj["whereClauseLaunchOption"]
      self.whereClauseAlternateKeyBinding:str = obj["whereClauseAlternateKeyBinding"]
      self.whereClauseAlternateKey:str = obj["whereClauseAlternateKey"]
      self.whereClauseSearchOption:str = obj["whereClauseSearchOption"]
      self.whereClauseWhereClauseBinding:str = obj["whereClauseWhereClauseBinding"]
      self.whereClauseWhereClauseToken:str = obj["whereClauseWhereClauseToken"]
      self.whereClauseContextMenuItemTemp:str = obj["whereClauseContextMenuItemTemp"]
      self.whereClauseContextMenuTemp:str = obj["whereClauseContextMenuTemp"]
      self.whereClauseContextValidation:str = obj["whereClauseContextValidation"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ContextMenuDataTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BO_ContextMenuData_LikeListInfo:
   def __init__(self, obj):
      self.Id:str = obj["Id"]
      self.UpdateType:str = obj["UpdateType"]
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      self.Items:list[Ice_BO_ContextMenuData_LikeListItem] = obj["Items"]
      self.Validation:list[Ice_BO_ContextMenuData_LikeValidation] = obj["Validation"]
      pass

class Ice_BO_ContextMenuData_LikeListItem:
   def __init__(self, obj):
      self.Caption:str = obj["Caption"]
      self.ProcessCall:str = obj["ProcessCall"]
      self.SearchMode:str = obj["SearchMode"]
      self.Guid:str = obj["Guid"]
      self.ProcessType:str = obj["ProcessType"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.QueryID:str = obj["QueryID"]
      self.UpdateType:str = obj["UpdateType"]
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      self.AdapterID:str = obj["AdapterID"]
      self.ProcessCallOrg:str = obj["ProcessCallOrg"]
      pass

class Ice_BO_ContextMenuData_LikeSearchProperties:
   def __init__(self, obj):
      self.searchForm:str = obj["searchForm"]
      self.deviceType:str = obj["deviceType"]
      self.mode:str = obj["mode"]
      self.layers:str = obj["layers"]
      pass

class Ice_BO_ContextMenuData_LikeValidation:
   def __init__(self, obj):
      self.ValidationAdapter:str = obj["ValidationAdapter"]
      self.ValidationType:str = obj["ValidationType"]
      self.RetrieverCombo:str = obj["RetrieverCombo"]
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

class Ice_Tablesets_AlternateKeyBindingRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.AlternateKeyBinding:str = obj["AlternateKeyBinding"]
      """  AlternateKeyBinding  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AlternateKeyLikeRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.LikeField:str = obj["LikeField"]
      """  LikeField  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AlternateKeyRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ContextValue:str = obj["ContextValue"]
      """  ContextValue  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextMenuDataListTableset:
   def __init__(self, obj):
      self.ContextMenuList:list[Ice_Tablesets_ContextMenuListRow] = obj["ContextMenuList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ContextMenuDataTableset:
   def __init__(self, obj):
      self.ContextMenu:list[Ice_Tablesets_ContextMenuRow] = obj["ContextMenu"]
      self.ContextMenuItem:list[Ice_Tablesets_ContextMenuItemRow] = obj["ContextMenuItem"]
      self.AlternateKeyLike:list[Ice_Tablesets_AlternateKeyLikeRow] = obj["AlternateKeyLike"]
      self.LaunchOption:list[Ice_Tablesets_LaunchOptionRow] = obj["LaunchOption"]
      self.AlternateKeyBinding:list[Ice_Tablesets_AlternateKeyBindingRow] = obj["AlternateKeyBinding"]
      self.AlternateKey:list[Ice_Tablesets_AlternateKeyRow] = obj["AlternateKey"]
      self.SearchOption:list[Ice_Tablesets_SearchOptionRow] = obj["SearchOption"]
      self.WhereClauseBinding:list[Ice_Tablesets_WhereClauseBindingRow] = obj["WhereClauseBinding"]
      self.WhereClauseToken:list[Ice_Tablesets_WhereClauseTokenRow] = obj["WhereClauseToken"]
      self.ContextMenuItemTemp:list[Ice_Tablesets_ContextMenuItemTempRow] = obj["ContextMenuItemTemp"]
      self.ContextMenuTemp:list[Ice_Tablesets_ContextMenuTempRow] = obj["ContextMenuTemp"]
      self.ContextValidation:list[Ice_Tablesets_ContextValidationRow] = obj["ContextValidation"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ContextMenuItemRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.ContextMenuText:str = obj["ContextMenuText"]
      """  ContextMenuText  """  
      self.ProcessCall:str = obj["ProcessCall"]
      """  ProcessCall  """  
      self.ProcessType:str = obj["ProcessType"]
      """  ProcessType  """  
      self.MenuID:str = obj["MenuID"]
      """  MenuID  """  
      self.AdapterID:str = obj["AdapterID"]
      """  AdapterID  """  
      self.SearchMode:str = obj["SearchMode"]
      """  SearchMode  """  
      self.TrackerID:str = obj["TrackerID"]
      """  TrackerID  """  
      self.QSValidation:bool = obj["QSValidation"]
      """  QSValidation  """  
      self.QSBaseDefault:bool = obj["QSBaseDefault"]
      """  QSBaseDefault  """  
      self.QSContextDefault:bool = obj["QSContextDefault"]
      """  QSContextDefault  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.MenuOrder:int = obj["MenuOrder"]
      """  MenuOrder  """  
      self.MenuEnabled:bool = obj["MenuEnabled"]
      """  MenuEnabled  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.TempID:str = obj["TempID"]
      """  Temporary ID to identify row.  """  
      self.ProcessCallOrg:str = obj["ProcessCallOrg"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextMenuItemTempRow:
   def __init__(self, obj):
      self.AdapterID:str = obj["AdapterID"]
      """  AdapterID  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.ContextMenuText:str = obj["ContextMenuText"]
      """  ContextMenuText  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.MenuEnabled:bool = obj["MenuEnabled"]
      """  MenuEnabled  """  
      self.MenuID:str = obj["MenuID"]
      """  MenuID  """  
      self.MenuOrder:int = obj["MenuOrder"]
      """  MenuOrder  """  
      self.ProcessCall:str = obj["ProcessCall"]
      """  ProcessCall  """  
      self.ProcessType:str = obj["ProcessType"]
      """  ProcessType  """  
      self.QSBaseDefault:bool = obj["QSBaseDefault"]
      """  QSBaseDefault  """  
      self.QSContextDefault:bool = obj["QSContextDefault"]
      """  QSContextDefault  """  
      self.QSValidation:bool = obj["QSValidation"]
      """  QSValidation  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.SearchMode:str = obj["SearchMode"]
      """  SearchMode  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.TrackerID:str = obj["TrackerID"]
      """  TrackerID  """  
      self.UpdateType:str = obj["UpdateType"]
      """  UpdateType  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextMenuListRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
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

class Ice_Tablesets_ContextMenuRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
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

class Ice_Tablesets_ContextMenuTempRow:
   def __init__(self, obj):
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.UpdateType:str = obj["UpdateType"]
      """  UpdateType  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ContextValidationRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ValidationAdapter:str = obj["ValidationAdapter"]
      """  ValidationAdapter  """  
      self.ValidationType:str = obj["ValidationType"]
      """  ValidationType  """  
      self.RetrieverCombo:str = obj["RetrieverCombo"]
      """  RetrieverCombo  """  
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

class Ice_Tablesets_LaunchOptionRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.LaunchModal:bool = obj["LaunchModal"]
      """  LaunchModal  """  
      self.EpiReadOnly:bool = obj["EpiReadOnly"]
      """  EpiReadOnly  """  
      self.SuppressPublisher:bool = obj["SuppressPublisher"]
      """  SuppressPublisher  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ContextValue:str = obj["ContextValue"]
      """  ContextValue  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SearchOptionRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
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

class Ice_Tablesets_UpdExtContextMenuDataTableset:
   def __init__(self, obj):
      self.ContextMenu:list[Ice_Tablesets_ContextMenuRow] = obj["ContextMenu"]
      self.ContextMenuItem:list[Ice_Tablesets_ContextMenuItemRow] = obj["ContextMenuItem"]
      self.AlternateKeyLike:list[Ice_Tablesets_AlternateKeyLikeRow] = obj["AlternateKeyLike"]
      self.LaunchOption:list[Ice_Tablesets_LaunchOptionRow] = obj["LaunchOption"]
      self.AlternateKeyBinding:list[Ice_Tablesets_AlternateKeyBindingRow] = obj["AlternateKeyBinding"]
      self.AlternateKey:list[Ice_Tablesets_AlternateKeyRow] = obj["AlternateKey"]
      self.SearchOption:list[Ice_Tablesets_SearchOptionRow] = obj["SearchOption"]
      self.WhereClauseBinding:list[Ice_Tablesets_WhereClauseBindingRow] = obj["WhereClauseBinding"]
      self.WhereClauseToken:list[Ice_Tablesets_WhereClauseTokenRow] = obj["WhereClauseToken"]
      self.ContextMenuItemTemp:list[Ice_Tablesets_ContextMenuItemTempRow] = obj["ContextMenuItemTemp"]
      self.ContextMenuTemp:list[Ice_Tablesets_ContextMenuTempRow] = obj["ContextMenuTemp"]
      self.ContextValidation:list[Ice_Tablesets_ContextValidationRow] = obj["ContextValidation"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_WhereClauseBindingRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.SearchTable:str = obj["SearchTable"]
      """  SearchTable  """  
      self.SearchTitle:str = obj["SearchTitle"]
      """  SearchTitle  """  
      self.WhereClauseString:str = obj["WhereClauseString"]
      """  WhereClauseString  """  
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

class Ice_Tablesets_WhereClauseTokenRow:
   def __init__(self, obj):
      self.LikeID:str = obj["LikeID"]
      """  LikeID  """  
      self.ContextTypeCode:str = obj["ContextTypeCode"]
      """  ContextTypeCode  """  
      self.ContextMenuID:str = obj["ContextMenuID"]
      """  ContextMenuID  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.CurrentBinding:str = obj["CurrentBinding"]
      """  CurrentBinding  """  
      self.BindingToken:str = obj["BindingToken"]
      """  BindingToken  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class IsValidLikeID_input:
   """ Required : 
   likeID
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      """  LikeID  """  
      pass

class IsValidLikeID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if not reserved, false otherwise  """  
      pass

class LikeIDChanging_input:
   """ Required : 
   likeID
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      pass

class LikeIDChanging_output:
   def __init__(self, obj):
      pass

class UpdateContextMenuLikeItems_input:
   """ Required : 
   contextMenuData
   updateMode
   """  
   def __init__(self, obj):
      self.contextMenuData:list[Ice_Tablesets_ContextMenuDataTableset] = obj["contextMenuData"]
      self.updateMode:str = obj["updateMode"]
      """  Valid options are 'Customize' and 'Personalize'  """  
      pass

class UpdateContextMenuLikeItems_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtContextMenuDataTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtContextMenuDataTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ContextMenuDataTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateLikeID_input:
   """ Required : 
   likeID
   """  
   def __init__(self, obj):
      self.likeID:str = obj["likeID"]
      """  LikeID  """  
      pass

class ValidateLikeID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  true if valid, false otherwise  """  
      pass

