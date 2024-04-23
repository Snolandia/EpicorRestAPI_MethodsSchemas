import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.APPIWriteOffSvc
# Description: A/P Promissory Note Write Off Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APPIWriteOffs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPIWriteOffs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPIWriteOffs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs",headers=creds) as resp:
           return await resp.json()

async def post_APPIWriteOffs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPIWriteOffs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPIWriteOffs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPIWriteOff item
   Description: Calls GetByID to retrieve the APPIWriteOff item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPIWriteOff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPIWriteOffs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPIWriteOff for the service
   Description: Calls UpdateExt to update APPIWriteOff. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPIWriteOff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPIWriteOffs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPIWriteOff item
   Description: Call UpdateExt to delete APPIWriteOff item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPIWriteOff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPIWriteOffs_Company_GroupID_HeadNum_APPNMoves(Company, GroupID, HeadNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APPNMoves items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNMoves1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/APPNMoves",headers=creds) as resp:
           return await resp.json()

async def get_APPIWriteOffs_Company_GroupID_HeadNum_APPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNMove item
   Description: Calls GetByID to retrieve the APPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMove1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNMoves(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPNMoves items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNMoves
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves",headers=creds) as resp:
           return await resp.json()

async def post_APPNMoves(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNMoves
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNMove item
   Description: Calls GetByID to retrieve the APPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMove
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPNMove for the service
   Description: Calls UpdateExt to update APPNMove. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNMove
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNMoveRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPNMove item
   Description: Call UpdateExt to delete APPNMove item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNMove
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNMoves_Company_GroupID_HeadNum_Seq_APPNMoveTGLCs(Company, GroupID, HeadNum, Seq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get APPNMoveTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APPNMoveTGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/APPNMoveTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_APPNMoves_Company_GroupID_HeadNum_Seq_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company, GroupID, HeadNum, Seq, SeqNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNMoveTGLC item
   Description: Calls GetByID to retrieve the APPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMoveTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNMoveTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPNMoveTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNMoveTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_APPNMoveTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNMoveTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company, GroupID, HeadNum, SeqNum, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNMoveTGLC item
   Description: Calls GetByID to retrieve the APPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNMoveTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company, GroupID, HeadNum, SeqNum, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPNMoveTGLC for the service
   Description: Calls UpdateExt to update APPNMoveTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNMoveTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNMoveTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPNMoveTGLCs_Company_GroupID_HeadNum_SeqNum_SysRowID(Company, GroupID, HeadNum, SeqNum, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPNMoveTGLC item
   Description: Call UpdateExt to delete APPNMoveTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNMoveTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + SeqNum + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPNLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPNLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPNLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists",headers=creds) as resp:
           return await resp.json()

async def post_APPNLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPNLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPNListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPNListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPNLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPNList item
   Description: Calls GetByID to retrieve the APPNList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPNList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPNListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPNLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPNList for the service
   Description: Calls UpdateExt to update APPNList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPNList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPNListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPNLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPNList item
   Description: Call UpdateExt to delete APPNList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPNList
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/APPNLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPNHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPPNHead, whereClauseAPPNMove, whereClauseAPPNMoveTGLC, whereClauseAPPNList, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseAPPNHead=" + whereClauseAPPNHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPNMove=" + whereClauseAPPNMove
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPNMoveTGLC=" + whereClauseAPPNMoveTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPNList=" + whereClauseAPPNList
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(groupID, headNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "groupID=" + groupID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "headNum=" + headNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckGLInterface(epicorHeaders = None):
   """  
   Summary: Invoke method CheckGLInterface
   Description: Call this method once to validate the G/L Interface.  This method checks for
GLSyst availability and if G/L is interfaced with A/P. If A/P is not interfaced
with G/L then user should be asked if okay to continue without posting to G/L.
This method will return a Message for the user if not interfaced else the Message
is blank. If the user do not wish to continue then exit this object. This method
also returns a logical flag to indicate if Posting to G/L.  This value should be
passed on to each new A/P Adjustment (APPNMove) record to process.
   OperationID: CheckGLInterface
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGLInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_CheckPNoteExisted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPNoteExisted
   OperationID: CheckPNoteExisted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPNoteExisted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPNoteExisted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPPNList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPPNList
   OperationID: GetAPPNList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPPNList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPPNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupIDForPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an APPNHead record that's for the
APPromNoteID supplied.
   OperationID: GetGroupIDForPI
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGroupIDForPI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGroupIDForPI_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNMove1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNMove1
   Description: This method is to be used in place of GetNewAPPNMove.  This method asks for
vendor number and invoice number to link the A/P Invoice Header (APPNHead)
to A/P Invoice Adjustment (APPNMove).
   OperationID: GetNewAPPNMove1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMove1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMove1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPNByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPNByID
   OperationID: GetPNByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPNByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPNByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNMove
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPPNMoveTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPPNMoveTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPPNMoveTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPPNMoveTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPPNMoveTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.APPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNMoveRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPNMoveTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPNMoveTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_APPNHeadListRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.VendBankName:str = obj["VendBankName"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.VoidDate:str = obj["VoidDate"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.TypeDesc:str = obj["TypeDesc"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.VendBankAcctIDBankName:str = obj["VendBankAcctIDBankName"]
      """  Supplier Bank Name  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.EndorsedARPNGroupID:str = obj["EndorsedARPNGroupID"]
      """  Reference to Endorsed AR PI GroupID.  """  
      self.EndorsedARPNHeadNum:int = obj["EndorsedARPNHeadNum"]
      """  Reference to Endorsed AR PI HeadNum.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.VendBankName:str = obj["VendBankName"]
      self.VoidDate:str = obj["VoidDate"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.AllocAmt:int = obj["AllocAmt"]
      self.EndorsedARPNStatus:str = obj["EndorsedARPNStatus"]
      """  Endorsed AR PI Status  """  
      self.EndorsedARPNStatusChgTranDocType:str = obj["EndorsedARPNStatusChgTranDocType"]
      """  Endorsed AR PI Status Change Transaction Document Type.  """  
      self.EndorsedARPNStatusChgLegalNum:str = obj["EndorsedARPNStatusChgLegalNum"]
      """  Endorsed AR PI Status Change Legal Number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNListRow:
   def __init__(self, obj):
      self.APPromNoteID:str = obj["APPromNoteID"]
      self.Company:str = obj["Company"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.VendorID:str = obj["VendorID"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.PIStage:str = obj["PIStage"]
      self.PIStatus:str = obj["PIStatus"]
      self.TranAPAmt:int = obj["TranAPAmt"]
      self.Type:str = obj["Type"]
      self.Selected:bool = obj["Selected"]
      """  To select row in grid  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNMoveRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.Seq:int = obj["Seq"]
      """  Movement Order  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group ID  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Status  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date created  """  
      self.CreateUser:str = obj["CreateUser"]
      """  Created By User  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Type:str = obj["Type"]
      """  Move Type  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.StatusDesc:str = obj["StatusDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNMoveTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum for relation to APPNMoveTGLC  """  
      self.Seq:int = obj["Seq"]
      """  Seq for relation to APPNMoveTGLC  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID for relation to APPNMoveTGLC  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckGLInterface_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.opPostToGL:bool = obj["opPostToGL"]
      pass

      """  output parameters  """  

class CheckPNoteExisted_input:
   """ Required : 
   ipPIStage
   ipID
   ipVendID
   """  
   def __init__(self, obj):
      self.ipPIStage:str = obj["ipPIStage"]
      """  ipPIType  """  
      self.ipID:str = obj["ipID"]
      """  ipID  """  
      self.ipVendID:str = obj["ipVendID"]
      """  ipVendID  """  
      pass

class CheckPNoteExisted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opRet:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APPIWriteOffTableset:
   def __init__(self, obj):
      self.APPNHead:list[Erp_Tablesets_APPNHeadRow] = obj["APPNHead"]
      self.APPNMove:list[Erp_Tablesets_APPNMoveRow] = obj["APPNMove"]
      self.APPNMoveTGLC:list[Erp_Tablesets_APPNMoveTGLCRow] = obj["APPNMoveTGLC"]
      self.APPNList:list[Erp_Tablesets_APPNListRow] = obj["APPNList"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APPNHeadListRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.VendBankName:str = obj["VendBankName"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.VoidDate:str = obj["VoidDate"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.TypeDesc:str = obj["TypeDesc"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalDate:str = obj["RevalDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      """  The Bank's full name.  """  
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      """  Full description of the bank account.  """  
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.VendBankAcctIDBankName:str = obj["VendBankAcctIDBankName"]
      """  Supplier Bank Name  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNHeadListTableset:
   def __init__(self, obj):
      self.APPNHeadList:list[Erp_Tablesets_APPNHeadListRow] = obj["APPNHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_APPNHeadRow:
   def __init__(self, obj):
      self.AppliedAmount:int = obj["AppliedAmount"]
      """  Applied Amount. Base Currency.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account of the promissory note.  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BankTotalAmt:int = obj["BankTotalAmt"]
      """  Bank Total Amount.  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  Cash book Number.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Bank Account ID of the company.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency code of the promissory note.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount amount in base currency.  """  
      self.DocPNAmt:int = obj["DocPNAmt"]
      """  Promissory Note amount in document currency.  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Entry Person.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate of the promissory note.  """  
      self.Paid:bool = obj["Paid"]
      """  Indicates if the promissory node is fully paid.  """  
      self.PNAmt:int = obj["PNAmt"]
      """  Promissory note amount in base currency.  """  
      self.Posted:bool = obj["Posted"]
      """  Indicates that the promissory note is posted.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group Code.  """  
      self.Rpt1PNAmt:int = obj["Rpt1PNAmt"]
      """  Promissory Note Amount in Report Currency 1.  """  
      self.Rpt1Discountamt:int = obj["Rpt1Discountamt"]
      """  Promissory Note Discount Amount in Report Currency 1.  """  
      self.Rpt1BankTotalAmt:int = obj["Rpt1BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 1.  """  
      self.Rpt2PNAmt:int = obj["Rpt2PNAmt"]
      """  Promissory Note Amount in Report Currency 2.  """  
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 2.  """  
      self.Rpt2BankTotalAmt:int = obj["Rpt2BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 2.  """  
      self.Rpt3PNAmt:int = obj["Rpt3PNAmt"]
      """  Promissory Note Amount in Report Currency 3.  """  
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      """  Promissory Note Discount Amount in Report Currency 3.  """  
      self.Rpt3BankTotalAmt:int = obj["Rpt3BankTotalAmt"]
      """  Promissory Note Bank Total Amount in Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Indicates that the promissory note is signed.  """  
      self.TotalAPAmt:int = obj["TotalAPAmt"]
      """  Total AP Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction date.  """  
      self.VendBankAcctID:str = obj["VendBankAcctID"]
      """  Supplier Bank Account ID  """  
      self.VendorID:str = obj["VendorID"]
      """  Supplier ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.APPromNoteID:str = obj["APPromNoteID"]
      """  AP Payment Instrument ID  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  G\L fiscal period that this check is posted to. Updated by the check printing process for system printed checks. For hand written checks it updated by check entry program based on the check date.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year that the check is posted to. Updated during the check printing process for system printed checks or updated based on the Check date for hand written checks.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.SupplierAddr1:str = obj["SupplierAddr1"]
      """  First supplier address line.  """  
      self.SupplierAddr2:str = obj["SupplierAddr2"]
      """  Second supplier address line.  """  
      self.SupplierAddr3:str = obj["SupplierAddr3"]
      """  Third supplier address line.  """  
      self.SupplierCity:str = obj["SupplierCity"]
      """  Company City portion of the address.  """  
      self.SupplierState:str = obj["SupplierState"]
      """  Supplier State portion of the address.  """  
      self.SupplierPostalCode:str = obj["SupplierPostalCode"]
      """  Supplier Postal Code or Zip Code portion of the address.  """  
      self.SupplierName:str = obj["SupplierName"]
      """  Supplier Name  """  
      self.SupplierCountry:str = obj["SupplierCountry"]
      """  Supplier Country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """   Payment Instrument Status -
Values are:
Empty string - not linked to a Payment Instrument
"O" (letter o) - Paid by outstanding Payment Instrument
"C" - Paid by collected Payment Instrument  """  
      self.Type:str = obj["Type"]
      """  Promissory Note Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBAN Code for company's bank.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.ForceDiscount:bool = obj["ForceDiscount"]
      """  When selected, this field will force the best discount percentage, according to the invoice?s terms definition, to be used.  """  
      self.PaymentTotal:int = obj["PaymentTotal"]
      """  Total paid amount in Base  """  
      self.Variance:int = obj["Variance"]
      """  Variance in Base currency - difference between the sum of the payments and the entered Payment Total  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.IsEnterTotal:bool = obj["IsEnterTotal"]
      """  Enter Totals flag  """  
      self.Rpt1Variance:int = obj["Rpt1Variance"]
      """  Variance in Rpt1 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt2Variance:int = obj["Rpt2Variance"]
      """  Variance in Rpt2 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.Rpt3Variance:int = obj["Rpt3Variance"]
      """  Variance in Rpt3 currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocVariance:int = obj["DocVariance"]
      """  Variance in payment currency - difference between the sum of the payments and the entered Payment Total  """  
      self.DocPaymentTotal:int = obj["DocPaymentTotal"]
      """  Total paid amount in payment currency  """  
      self.PaymentBankRate:int = obj["PaymentBankRate"]
      """  Exchange rate from the payment currency to the Bank currency  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  """  
      self.Rpt1PaymentTotal:int = obj["Rpt1PaymentTotal"]
      """  Total paid amount in Rpt1 currency  """  
      self.Rpt2PaymentTotal:int = obj["Rpt2PaymentTotal"]
      """  Total paid amount in Rpt2 currency  """  
      self.Rpt3PaymentTotal:int = obj["Rpt3PaymentTotal"]
      """  Total paid amount in Rpt3 currency  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.FirstHeadNum:int = obj["FirstHeadNum"]
      """  Reference to the first checkhed  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if manually printed.  If manual then user must enter the APPRomNoteID  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change the Customer or Company information  """  
      self.PymtCntr:bool = obj["PymtCntr"]
      """  Indicates APPRomNoteID was generated using AP CheckHed numbering  """  
      self.PIStage:str = obj["PIStage"]
      """  Payment Instrument Stage  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.SupplierCountryNum:int = obj["SupplierCountryNum"]
      """  SupplierCountryNum  """  
      self.EndorsedARPNGroupID:str = obj["EndorsedARPNGroupID"]
      """  Reference to Endorsed AR PI GroupID.  """  
      self.EndorsedARPNHeadNum:int = obj["EndorsedARPNHeadNum"]
      """  Reference to Endorsed AR PI HeadNum.  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.BankAccountEnabled:bool = obj["BankAccountEnabled"]
      """  Enable the Bank Account Search Button  """  
      self.BankCurrCode:str = obj["BankCurrCode"]
      """  Bank Currency Code  """  
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyCountryNum:int = obj["CompanyCountryNum"]
      """  Field to bring the Company Country Name  """  
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DocAllocAmt:int = obj["DocAllocAmt"]
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnterPaymentTotal:bool = obj["EnterPaymentTotal"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsFiltered:bool = obj["IsFiltered"]
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PaymentAmount:int = obj["PaymentAmount"]
      self.PaymentStatus:str = obj["PaymentStatus"]
      self.RevalDate:str = obj["RevalDate"]
      self.Rpt1AllocAmt:int = obj["Rpt1AllocAmt"]
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2AllocAmt:int = obj["Rpt2AllocAmt"]
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3AllocAmt:int = obj["Rpt3AllocAmt"]
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.VendBankAcct:str = obj["VendBankAcct"]
      self.VendBankIdentifier:str = obj["VendBankIdentifier"]
      self.VendBankName:str = obj["VendBankName"]
      self.VoidDate:str = obj["VoidDate"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.XRateLabelPaymentBank:str = obj["XRateLabelPaymentBank"]
      self.XRateLabelPaymentBase:str = obj["XRateLabelPaymentBase"]
      self.AllocAmt:int = obj["AllocAmt"]
      self.EndorsedARPNStatus:str = obj["EndorsedARPNStatus"]
      """  Endorsed AR PI Status  """  
      self.EndorsedARPNStatusChgTranDocType:str = obj["EndorsedARPNStatusChgTranDocType"]
      """  Endorsed AR PI Status Change Transaction Document Type.  """  
      self.EndorsedARPNStatusChgLegalNum:str = obj["EndorsedARPNStatusChgLegalNum"]
      """  Endorsed AR PI Status Change Legal Number.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctIDDescription:str = obj["BankAcctIDDescription"]
      self.BankAcctIDBankName:str = obj["BankAcctIDBankName"]
      self.BaseCurrSymbolCurrencyID:str = obj["BaseCurrSymbolCurrencyID"]
      self.BaseCurrSymbolCurrSymbol:str = obj["BaseCurrSymbolCurrSymbol"]
      self.BaseCurrSymbolCurrDesc:str = obj["BaseCurrSymbolCurrDesc"]
      self.BaseCurrSymbolDocumentDesc:str = obj["BaseCurrSymbolDocumentDesc"]
      self.BaseCurrSymbolCurrName:str = obj["BaseCurrSymbolCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNListRow:
   def __init__(self, obj):
      self.APPromNoteID:str = obj["APPromNoteID"]
      self.Company:str = obj["Company"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.VendorID:str = obj["VendorID"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.PIStage:str = obj["PIStage"]
      self.PIStatus:str = obj["PIStatus"]
      self.TranAPAmt:int = obj["TranAPAmt"]
      self.Type:str = obj["Type"]
      self.Selected:bool = obj["Selected"]
      """  To select row in grid  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNMoveRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CheckHedSeq". Which along with company and GroupID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing invoices to be entered, the user establishes a Group ID. All invoices belong to a group until the group is posted. The Group ID is assigned by the user.  The Group ID is used to selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  """  
      self.Seq:int = obj["Seq"]
      """  Movement Order  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group ID  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Status  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date created  """  
      self.CreateUser:str = obj["CreateUser"]
      """  Created By User  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.Type:str = obj["Type"]
      """  Move Type  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.StatusDesc:str = obj["StatusDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APPNMoveTGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "PORel" control this field would contain the related PO Number.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.   For example: For a "PORel" control this field would contain the related PO Line Number.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  For example: For a "PORel" control this field would contain the related PO Release Number.  The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.TGLCTranNum:int = obj["TGLCTranNum"]
      """  Internal identifier used to keep records unique for the related record.  The system generates this number by finding the last TranGLC record for the RelatedToFile-Key1-Key2 etc. and adding 1 to it.  """  
      self.GLAcctContext:str = obj["GLAcctContext"]
      """  String identifier of the account context.  """  
      self.BookID:str = obj["BookID"]
      """  Reference to an accounting book.  If not blank must be a valid entry in the GLBook table.  """  
      self.COACode:str = obj["COACode"]
      """  The chart of account code used by the book.  Will contain the Master COA when BookID is blank.  Reference only.  Used for integrity checking when updating/deleting a GL account.  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full account containing the non-dynamic segment values up to 200 characters.  Unique identifier for the GL Account.  """  
      self.UserCanModify:bool = obj["UserCanModify"]
      """  Indicates if the user can update or delete this record.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  Segement Value 1 of the account for this context.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  Segement Value 2 of the account for this context.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  Segement Value 3 of the account for this context.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  Segement Value 4 of the account for this context.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  Segement Value 5 of the account for this context.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  Segement Value 6 of the account for this context.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  Segement Value 7 of the account for this context.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  Segement Value 8 of the account for this context.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  Segement Value 9 of the account for this context.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  Segement Value 10 of the account for this context.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  Segement Value 11 of the account for this context.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  Segement Value 12 of the account for this context.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  Segement Value 13 of the account for this context.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  Segement Value 14 of the account for this context.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  Segement Value 15 of the account for this context.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  Segement Value 16 of the account for this context.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  Segement Value 17 of the account for this context.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  Segement Value 18 of the account for this context.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  Segement Value 19 of the account for this context.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  Segement Value 20 of the account for this context.  """  
      self.SysGLControlType:str = obj["SysGLControlType"]
      """  Unique Identifier of the system GL Control Type.  """  
      self.SysGLControlCode:str = obj["SysGLControlCode"]
      """  System generated GL Control Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year of the related GLJrnDtl.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  JournalCode of the related GLJrnDtl.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  Journal number of the related GLJrnDtl.  """  
      self.JournalLine:int = obj["JournalLine"]
      """  JournalLine of the related GLJrnDtl.  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction date of the transaction.  This is used in order to display the transactions in date order.  """  
      self.TranSource:str = obj["TranSource"]
      """   An internal code to identify the table of  the source transaction.
P = PartTran
L = LaborDtl
I = InvcHead
Note: The system does not combine TranSource when creating GLJrnDtl. That is, a specific GLJrnDtl record can only be related to one source.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  LaborHedSeq of the related LaborDtl.  Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  LaborDtlSeq of the related LaborDtl. Pertains only to source from LaborDtl (TranSource = "L")  """  
      self.SysDate:str = obj["SysDate"]
      """  System date of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.SysTime:int = obj["SysTime"]
      """  System time of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum of the related PartTran record.  Pertains only to source from PartTran (TranSource = "P")  """  
      self.ARInvoiceNum:int = obj["ARInvoiceNum"]
      """  InvoiceNum of the related InvcHead record.  Pertains only to source from PartTran (TranSource = "I")  """  
      self.TransAmt:int = obj["TransAmt"]
      """  Transaction amount that this transaction posted to the related GlJrnDtl.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Invoice Line Number associated with this GL Journal  """  
      self.SeqNum:int = obj["SeqNum"]
      """  The sequence number associated with this GL journal  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The Internal VendorNum that ties back to the Vendor master file.  This field is not directly maintainable.  """  
      self.APInvoiceNum:str = obj["APInvoiceNum"]
      """  Vendor's invoice number.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date record was created  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.CreditAmount:int = obj["CreditAmount"]
      """  Credit Amount.  """  
      self.DebitAmount:int = obj["DebitAmount"]
      """  Debit Amount.  """  
      self.BookCreditAmount:int = obj["BookCreditAmount"]
      """  BookCreditAmount  """  
      self.BookDebitAmount:int = obj["BookDebitAmount"]
      """  Book Debit Amount  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the document currency.  """  
      self.RecordType:str = obj["RecordType"]
      """   Indicates if this record contains account data only or reference data such as journal number, amounts, etc.  Valid  values are:
A - account data only
R - reference data  """  
      self.CorrAccUID:int = obj["CorrAccUID"]
      """  When a posting rule creates a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports. Support of reports that allow this being visible is not in the scope of this change.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  this field equals ABTUID which was created during posting  """  
      self.RuleUID:int = obj["RuleUID"]
      """  Technical identifier.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.IsModifiedByUser:bool = obj["IsModifiedByUser"]
      """  IsModifiedByUser  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MovementNum:int = obj["MovementNum"]
      """  MovementNum  """  
      self.MovementType:str = obj["MovementType"]
      """  MovementType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.HeadNum:int = obj["HeadNum"]
      """  HeadNum for relation to APPNMoveTGLC  """  
      self.Seq:int = obj["Seq"]
      """  Seq for relation to APPNMoveTGLC  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID for relation to APPNMoveTGLC  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAPPIWriteOffTableset:
   def __init__(self, obj):
      self.APPNHead:list[Erp_Tablesets_APPNHeadRow] = obj["APPNHead"]
      self.APPNMove:list[Erp_Tablesets_APPNMoveRow] = obj["APPNMove"]
      self.APPNMoveTGLC:list[Erp_Tablesets_APPNMoveTGLCRow] = obj["APPNMoveTGLC"]
      self.APPNList:list[Erp_Tablesets_APPNListRow] = obj["APPNList"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAPPNList_input:
   """ Required : 
   ipType
   ipPNID
   ipVendID
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      """  ipType  """  
      self.ipPNID:str = obj["ipPNID"]
      """  ipPNID  """  
      self.ipVendID:str = obj["ipVendID"]
      """  ipVendID  """  
      pass

class GetAPPNList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPIWriteOffTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPIWriteOffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APPIWriteOffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_APPIWriteOffTableset] = obj["returnObj"]
      pass

class GetGroupIDForPI_input:
   """ Required : 
   apPromNoteID
   """  
   def __init__(self, obj):
      self.apPromNoteID:str = obj["apPromNoteID"]
      """  AR Promissory Note ID  """  
      pass

class GetGroupIDForPI_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.groupID:str = obj["parameters"]
      self.headNum:int = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_APPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPPNHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewAPPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNMove1_input:
   """ Required : 
   ds
   ipGroupID
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID for this A/P Promissory Note Head  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  The A/P Promissory Note Head Number  """  
      pass

class GetNewAPPNMove1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNMoveTGLC_input:
   """ Required : 
   ds
   groupID
   headNum
   seqNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.seqNum:int = obj["seqNum"]
      pass

class GetNewAPPNMoveTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewAPPNMove_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewAPPNMove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPNByID_input:
   """ Required : 
   ipHeadNum
   ipPIType
   ipID
   ipVendID
   ipCurGroupID
   ipNewPIType
   ds
   """  
   def __init__(self, obj):
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  ipHeadNum  """  
      self.ipPIType:str = obj["ipPIType"]
      """  ipPIType  """  
      self.ipID:str = obj["ipID"]
      """  ipID  """  
      self.ipVendID:str = obj["ipVendID"]
      """  ipVendID  """  
      self.ipCurGroupID:str = obj["ipCurGroupID"]
      """  ipCurGroupID  """  
      self.ipNewPIType:str = obj["ipNewPIType"]
      """  ipNewPIType  """  
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

class GetPNByID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPPNHead
   whereClauseAPPNMove
   whereClauseAPPNMoveTGLC
   whereClauseAPPNList
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPPNHead:str = obj["whereClauseAPPNHead"]
      self.whereClauseAPPNMove:str = obj["whereClauseAPPNMove"]
      self.whereClauseAPPNMoveTGLC:str = obj["whereClauseAPPNMoveTGLC"]
      self.whereClauseAPPNList:str = obj["whereClauseAPPNList"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_APPIWriteOffTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtAPPIWriteOffTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAPPIWriteOffTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_APPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

