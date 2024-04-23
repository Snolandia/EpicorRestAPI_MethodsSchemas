import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ARPIWriteOffSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ARPIWriteOffs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPIWriteOffs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPIWriteOffs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs",headers=creds) as resp:
           return await resp.json()

async def post_ARPIWriteOffs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPIWriteOffs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPIWriteOffs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPIWriteOff item
   Description: Calls GetByID to retrieve the ARPIWriteOff item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPIWriteOff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPIWriteOffs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPIWriteOff for the service
   Description: Calls UpdateExt to update ARPIWriteOff. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPIWriteOff
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPIWriteOffs_Company_GroupID_HeadNum(Company, GroupID, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPIWriteOff item
   Description: Call UpdateExt to delete ARPIWriteOff item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPIWriteOff
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPIWriteOffs_Company_GroupID_HeadNum_ARPNMoves(Company, GroupID, HeadNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARPNMoves items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNMoves1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNMoves",headers=creds) as resp:
           return await resp.json()

async def get_ARPIWriteOffs_Company_GroupID_HeadNum_ARPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNMove item
   Description: Calls GetByID to retrieve the ARPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMove1
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPIWriteOffs(" + Company + "," + GroupID + "," + HeadNum + ")/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNMoves(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNMoves items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNMoves
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves",headers=creds) as resp:
           return await resp.json()

async def post_ARPNMoves(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNMoves
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNMove item
   Description: Calls GetByID to retrieve the ARPNMove item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMove
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
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNMove for the service
   Description: Calls UpdateExt to update ARPNMove. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNMove
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNMoveRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNMoves_Company_GroupID_HeadNum_Seq(Company, GroupID, HeadNum, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNMove item
   Description: Call UpdateExt to delete ARPNMove item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNMove
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNMoves_Company_GroupID_HeadNum_Seq_ARPNMoveTGLCs(Company, GroupID, HeadNum, Seq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ARPNMoveTGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARPNMoveTGLCs1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/ARPNMoveTGLCs",headers=creds) as resp:
           return await resp.json()

async def get_ARPNMoves_Company_GroupID_HeadNum_Seq_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company, GroupID, HeadNum, Seq, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNMoveTGLC item
   Description: Calls GetByID to retrieve the ARPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMoveTGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoves(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + ")/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNMoveTGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNMoveTGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNMoveTGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs",headers=creds) as resp:
           return await resp.json()

async def post_ARPNMoveTGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNMoveTGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company, GroupID, HeadNum, Seq, TGLCTranNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNMoveTGLC item
   Description: Calls GetByID to retrieve the ARPNMoveTGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNMoveTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company, GroupID, HeadNum, Seq, TGLCTranNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNMoveTGLC for the service
   Description: Calls UpdateExt to update ARPNMoveTGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNMoveTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNMoveTGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNMoveTGLCs_Company_GroupID_HeadNum_Seq_TGLCTranNum(Company, GroupID, HeadNum, Seq, TGLCTranNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNMoveTGLC item
   Description: Call UpdateExt to delete ARPNMoveTGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNMoveTGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param GroupID: Desc: GroupID   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param Seq: Desc: Seq   Required: True
      :param TGLCTranNum: Desc: TGLCTranNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNMoveTGLCs(" + Company + "," + GroupID + "," + HeadNum + "," + Seq + "," + TGLCTranNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_ARPNLists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ARPNLists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARPNLists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists",headers=creds) as resp:
           return await resp.json()

async def post_ARPNLists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARPNLists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ARPNLists_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ARPNList item
   Description: Calls GetByID to retrieve the ARPNList item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARPNList
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ARPNLists_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ARPNList for the service
   Description: Calls UpdateExt to update ARPNList. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARPNList
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARPNListRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ARPNLists_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ARPNList item
   Description: Call UpdateExt to delete ARPNList item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARPNList
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/ARPNLists(" + SysRowID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARPNHeadListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseARPNHead, whereClauseARPNMove, whereClauseARPNMoveTGLC, whereClauseARPNList, whereClauseLegalNumGenOpts, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseARPNHead=" + whereClauseARPNHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNMove=" + whereClauseARPNMove
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNMoveTGLC=" + whereClauseARPNMoveTGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseARPNList=" + whereClauseARPNList
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List" + params,headers=creds) as resp:
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
passed on to each new A/P Adjustment (ARPNMove) record to process.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetARPNList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetARPNList
   OperationID: GetARPNList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetARPNList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARPNList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGroupIDForPI(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGroupIDForPI
   Description: This method will retrieve the GroupID for an ARPNHead record that's for the
ARPromNoteID supplied.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNMove1(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNMove1
   Description: This method is to be used in place of GetNewARPNMove.  This method asks for
vendor number and invoice number to link the A/R Invoice Header (ARPNHead)
to A/R Invoice Adjustment (ARPNMove).
   OperationID: GetNewARPNMove1
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNMove1_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNMove1_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNMove(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNMove
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNMove
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNMove_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNMove_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewARPNMoveTGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewARPNMoveTGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARPNMoveTGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewARPNMoveTGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARPNMoveTGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ARPIWriteOffSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNHeadRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNMoveRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARPNMoveTGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ARPNMoveTGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
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
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Receipt:int = obj["Receipt"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PITypeDescription:str = obj["PITypeDescription"]
      """  Type Description  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNListRow:
   def __init__(self, obj):
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      self.Company:str = obj["Company"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.CustID:str = obj["CustID"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.PIStage:str = obj["PIStage"]
      self.PIStatus:str = obj["PIStatus"]
      self.TranAmt:int = obj["TranAmt"]
      self.Type:str = obj["Type"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNMoveRow:
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
      """  Transaction Date  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EndorsedAPPNGroupID:str = obj["EndorsedAPPNGroupID"]
      """  Reference to Endorsed AP PI GroupID.  """  
      self.EndorsedAPPNHeadNum:int = obj["EndorsedAPPNHeadNum"]
      """  Reference to Endorsed AP PI HeadNum.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      """  PI status description  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  PI Type description  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNMoveTGLCRow:
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
      """  HeadNum for relation to ARPNMoveTGLC  """  
      self.Seq:int = obj["Seq"]
      """  Seq for relation to ARPNMoveTGLC  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID for relation to ARPNMoveTGLC  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
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
   ipID
   """  
   def __init__(self, obj):
      self.ipID:str = obj["ipID"]
      """  ipID  """  
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

class Erp_Tablesets_ARPIWriteOffTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ARPNMove:list[Erp_Tablesets_ARPNMoveRow] = obj["ARPNMove"]
      self.ARPNMoveTGLC:list[Erp_Tablesets_ARPNMoveTGLCRow] = obj["ARPNMoveTGLC"]
      self.ARPNList:list[Erp_Tablesets_ARPNListRow] = obj["ARPNList"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPNHeadListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.FullyPaid:bool = obj["FullyPaid"]
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
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
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Receipt:int = obj["Receipt"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      """  The Bank's full name.  """  
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      """  Full description of the bank account.  """  
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      """  Description  """  
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CustNumName:str = obj["CustNumName"]
      """  The full name of the customer.  """  
      self.CustNumBTName:str = obj["CustNumBTName"]
      """  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  """  
      self.CustNumCustID:str = obj["CustNumCustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  """  
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      """  Status Description  """  
      self.PITypeDescription:str = obj["PITypeDescription"]
      """  Type Description  """  
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      """  Description  """  
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      """  Full description for the Tax Region.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  Description  """  
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNHeadListTableset:
   def __init__(self, obj):
      self.ARPNHeadList:list[Erp_Tablesets_ARPNHeadListRow] = obj["ARPNHeadList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ARPNHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TranAmt:int = obj["TranAmt"]
      """  Transaction Amount  """  
      self.AppliedAmt:int = obj["AppliedAmt"]
      """  Applied Amount  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account ID  """  
      self.BankAmount:int = obj["BankAmount"]
      """  Bank Amount  """  
      self.BankSlip:str = obj["BankSlip"]
      """  Bank Slip Number of the promissory note.  """  
      self.BaseAmount:int = obj["BaseAmount"]
      """  Base Amount  """  
      self.CashbookLine:int = obj["CashbookLine"]
      """  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  """  
      self.CompBankAcctID:str = obj["CompBankAcctID"]
      """  Company Bank Account ID  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code  """  
      self.CustBankAcctID:str = obj["CustBankAcctID"]
      """  Customer Bank Account ID  """  
      self.CustID:str = obj["CustID"]
      """  Customer ID  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer Number  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DiscountAmt:int = obj["DiscountAmt"]
      """  Discount Amount. Base Currency.  """  
      self.DocAppliedAmt:int = obj["DocAppliedAmt"]
      """  Applied Amount. Document Currency.  """  
      self.DocUnAppliedAmt:int = obj["DocUnAppliedAmt"]
      """  Unapplied Amount. Document Currency.  """  
      self.DocTaxAmt:int = obj["DocTaxAmt"]
      """  Tax Amount. Document Currency.  """  
      self.DocTranAmt:int = obj["DocTranAmt"]
      """  Transaction Amount. Document Currency.  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Withholding Amount. Document Currency.  """  
      self.ExchangeRate:int = obj["ExchangeRate"]
      """  Exchange Rate  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  Get Default Tax ID's flag.  """  
      self.GLPosted:bool = obj["GLPosted"]
      """  Posted to GL flag  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number  """  
      self.Paid:bool = obj["Paid"]
      """  Paid flag  """  
      self.Posted:bool = obj["Posted"]
      """  Posted flag  """  
      self.ProcessCard:str = obj["ProcessCard"]
      """  Process Card  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Group code  """  
      self.RecalcBeforePost:bool = obj["RecalcBeforePost"]
      """  Recalculated before posting.  """  
      self.Rpt1AppliedAmt:int = obj["Rpt1AppliedAmt"]
      """  Applied Amount. Report Currency 1.  """  
      self.Rpt1TaxAmt:int = obj["Rpt1TaxAmt"]
      """  Tax Amount. Report Currency 1.  """  
      self.Rpt1TranAmt:int = obj["Rpt1TranAmt"]
      """  Transaction Amount. Report Currency 1.  """  
      self.Rpt1UnappliedAmt:int = obj["Rpt1UnappliedAmt"]
      """  Unapplied Amount. Report Currency 1.  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Withholding Amount. Report Currency 1.  """  
      self.Rpt2AppliedAmt:int = obj["Rpt2AppliedAmt"]
      """  Applied Amount. Report Currency 2.  """  
      self.Rpt2TaxAmt:int = obj["Rpt2TaxAmt"]
      """  Tax Amount. Report Currency 2.  """  
      self.Rpt2TranAmt:int = obj["Rpt2TranAmt"]
      """  Transaction Amount. Report Currency 2.  """  
      self.Rpt2UnappliedAmt:int = obj["Rpt2UnappliedAmt"]
      """  Unapplied Amount. Report Currency 2.  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Withholding Amount. Report Currency 2.  """  
      self.Rpt3AppliedAmt:int = obj["Rpt3AppliedAmt"]
      """  Applied Amount. Report Currency 3.  """  
      self.Rpt3TaxAmt:int = obj["Rpt3TaxAmt"]
      """  Tax Amount. Report Currency 3.  """  
      self.Rpt3TranAmt:int = obj["Rpt3TranAmt"]
      """  Transaction Amount. Report Currency 3.  """  
      self.Rpt3UnappliedAmt:int = obj["Rpt3UnappliedAmt"]
      """  Unapplied Amount. Report Currency 3.  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Withholding Amount. Report Currency 3.  """  
      self.Signed:bool = obj["Signed"]
      """  Signed flag  """  
      self.TaxAmt:int = obj["TaxAmt"]
      """  Tax Amount. Base Currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability  """  
      self.TotalARAmt:int = obj["TotalARAmt"]
      """  Total AR Amount  """  
      self.TransDate:str = obj["TransDate"]
      """  Transaction Date  """  
      self.UnappliedAmt:int = obj["UnappliedAmt"]
      """  Unapplied Amount. Base Currency.  """  
      self.Voided:bool = obj["Voided"]
      """  Voided Flag  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Withholding Amount. Base Currency.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.CompanyAddr1:str = obj["CompanyAddr1"]
      """  First company address line.  """  
      self.CompanyAddr2:str = obj["CompanyAddr2"]
      """  Second company address line.  """  
      self.CompanyAddr3:str = obj["CompanyAddr3"]
      """  Third company address line.  """  
      self.CompanyCity:str = obj["CompanyCity"]
      """  Company City portion of the address.  """  
      self.CompanyState:str = obj["CompanyState"]
      """  Company State portion of the address.  """  
      self.CompanyPostalCode:str = obj["CompanyPostalCode"]
      """  Company Postal Code or Zip Code portion of the address.  """  
      self.CompanyCountry:str = obj["CompanyCountry"]
      """  Company Country portion of the address.  """  
      self.CustomerName:str = obj["CustomerName"]
      """  Company Name  """  
      self.CustomerAddr1:str = obj["CustomerAddr1"]
      """  First customer address line.  """  
      self.CustomerAddr2:str = obj["CustomerAddr2"]
      """  Second customer address line.  """  
      self.CustomerAddr3:str = obj["CustomerAddr3"]
      """  Third customer address line.  """  
      self.CustomerState:str = obj["CustomerState"]
      """  Customer Stateportion of the address.  """  
      self.CustomerPostalCode:str = obj["CustomerPostalCode"]
      """  Customer City portion of the address.  """  
      self.CustomerCity:str = obj["CustomerCity"]
      """  Customer Postal Code or Zip Code portion of the address.  """  
      self.GroupID:str = obj["GroupID"]
      """  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  """  
      self.HeadNum:int = obj["HeadNum"]
      """  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  """  
      self.InvoiceNum:int = obj["InvoiceNum"]
      """  Reference to  invchead  """  
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      """  AR Payment Instrument ID  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The unique identifier of the fiscal calendar.  """  
      self.ReadyToCalc:bool = obj["ReadyToCalc"]
      """  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  """  
      self.TranType:str = obj["TranType"]
      """  Transaction Type  """  
      self.Sent:bool = obj["Sent"]
      """  Sent Flag  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IssueDate:str = obj["IssueDate"]
      """  Issue Date  """  
      self.DueDate:str = obj["DueDate"]
      """  Due date of the promissory note.  """  
      self.CompBankBranchCode:str = obj["CompBankBranchCode"]
      """  Bank/Branch Code for company's bank.  """  
      self.CompIBANCode:str = obj["CompIBANCode"]
      """  IBANCode for company's bank.  """  
      self.CustBankBranchCode:str = obj["CustBankBranchCode"]
      """  Bank/Branch Code for customer's bank.  """  
      self.CustIBANCode:str = obj["CustIBANCode"]
      """  IBAN Code for customer's bank.  """  
      self.AutoGenerated:bool = obj["AutoGenerated"]
      """  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  """  
      self.DirectDeposit:bool = obj["DirectDeposit"]
      """  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  """  
      self.ClearedAmt:int = obj["ClearedAmt"]
      """  Amount that the bank cleared the payment instrument for.  """  
      self.ClearedDate:str = obj["ClearedDate"]
      """  Date that the payment instrument was cleared in the system (System Set).  """  
      self.ClearedPending:bool = obj["ClearedPending"]
      """  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedPerson:str = obj["ClearedPerson"]
      """  Person who cleared the payment instrument (System Set).  """  
      self.ClearedPI:bool = obj["ClearedPI"]
      """  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  """  
      self.ClearedStmtEndDate:str = obj["ClearedStmtEndDate"]
      """  End Date of the Statement that the payment instrument was cleared on.  """  
      self.ClearedTime:str = obj["ClearedTime"]
      """  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  """  
      self.DocClearedAmt:int = obj["DocClearedAmt"]
      """  Amount that the bank cleared the check for.(Vendors Currency)  """  
      self.Rpt1ClearedAmt:int = obj["Rpt1ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt2ClearedAmt:int = obj["Rpt2ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.Rpt3ClearedAmt:int = obj["Rpt3ClearedAmt"]
      """  Reporting currency value of this field  """  
      self.CashBookNum:int = obj["CashBookNum"]
      """  This field identifies a bankslip.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      """  Indicates if the document has been printed.  """  
      self.CustCountryCode:int = obj["CustCountryCode"]
      """  Customer's country code  """  
      self.CustomerCountry:str = obj["CustomerCountry"]
      """  Customer country portion of the address.  """  
      self.PIStatus:str = obj["PIStatus"]
      """  Promissory Note Status  """  
      self.CurGroupID:str = obj["CurGroupID"]
      """  Current Group  """  
      self.PIStage:str = obj["PIStage"]
      """  Stage  """  
      self.ChgComment:str = obj["ChgComment"]
      """  Reason to change Company or Customer information  """  
      self.HoldReason:str = obj["HoldReason"]
      """  Hold from Application reason  """  
      self.LockRate:bool = obj["LockRate"]
      """  Lock Exchange Rate  """  
      self.ReferseRef:int = obj["ReferseRef"]
      """  Reference to reversed PI  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Reverse Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankClearedAmt:int = obj["BankClearedAmt"]
      """  BankClearedAmt  """  
      self.MXRecDate:str = obj["MXRecDate"]
      """  MXRecDate  """  
      self.TotalBankFee:int = obj["TotalBankFee"]
      """  TotalBankFee  """  
      self.DocTotalBankFee:int = obj["DocTotalBankFee"]
      """  DocTotalBankFee  """  
      self.Rpt1TotalBankFee:int = obj["Rpt1TotalBankFee"]
      """  Rpt1TotalBankFee  """  
      self.Rpt2TotalBankFee:int = obj["Rpt2TotalBankFee"]
      """  Rpt2TotalBankFee  """  
      self.Rpt3TotalBankFee:int = obj["Rpt3TotalBankFee"]
      """  Rpt3TotalBankFee  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.IssuerName:str = obj["IssuerName"]
      """  Issuer Name  """  
      self.SignedBy:str = obj["SignedBy"]
      """  Signed By  """  
      self.SignedDate:str = obj["SignedDate"]
      """  Signed Date  """  
      self.SigneeAddr1:str = obj["SigneeAddr1"]
      """  Signee Address 1  """  
      self.SigneeAddr2:str = obj["SigneeAddr2"]
      """  Signee Address 2  """  
      self.SigneeAddr3:str = obj["SigneeAddr3"]
      """  Signee Address 3  """  
      self.SigneeCity:str = obj["SigneeCity"]
      """  Signee City  """  
      self.SigneeState:str = obj["SigneeState"]
      """  Signee State  """  
      self.SigneeZip:str = obj["SigneeZip"]
      """  Signee Postal Code  """  
      self.SigneeCountryNum:int = obj["SigneeCountryNum"]
      """  Signee Country Number  """  
      self.SigneePhoneNum:str = obj["SigneePhoneNum"]
      """  Signee Phone  """  
      self.SigneeEMailAddress:str = obj["SigneeEMailAddress"]
      """  Signee Email Address  """  
      self.SigneeComment:str = obj["SigneeComment"]
      """  Signee Comment  """  
      self.DiscountChargeAmt:int = obj["DiscountChargeAmt"]
      """  DiscountChargeAmt  """  
      self.DocDiscountChargeAmt:int = obj["DocDiscountChargeAmt"]
      """  DocDiscountChargeAmt  """  
      self.Rpt1DiscountChargeAmt:int = obj["Rpt1DiscountChargeAmt"]
      """  Rpt1DiscountChargeAmt  """  
      self.Rpt2DiscountChargeAmt:int = obj["Rpt2DiscountChargeAmt"]
      """  Rpt2DiscountChargeAmt  """  
      self.Rpt3DiscountChargeAmt:int = obj["Rpt3DiscountChargeAmt"]
      """  Rpt3DiscountChargeAmt  """  
      self.SigneeBankName:str = obj["SigneeBankName"]
      """  Signee Bank Name  """  
      self.SigneeBankAcct:str = obj["SigneeBankAcct"]
      """  Signee Bank Account Number  """  
      self.SigneeBankIdentifier:str = obj["SigneeBankIdentifier"]
      """  Signee Bank Identifier  """  
      self.SigneeIBANCode:str = obj["SigneeIBANCode"]
      """  Signee IBAN Code  """  
      self.SigneeBankBranchCode:str = obj["SigneeBankBranchCode"]
      """  Signee Bank BranchCode  """  
      self.DiscountCashDate:str = obj["DiscountCashDate"]
      """  DiscountCashDate  """  
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.ApplyDate:str = obj["ApplyDate"]
      self.BankCurrencyCode:str = obj["BankCurrencyCode"]
      self.BankCurrSymbol:str = obj["BankCurrSymbol"]
      self.BankRecGainLoss:int = obj["BankRecGainLoss"]
      self.calcRate:bool = obj["calcRate"]
      """  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  """  
      self.CompanyBankAcct:str = obj["CompanyBankAcct"]
      self.CompanyBankIdentifier:str = obj["CompanyBankIdentifier"]
      self.CompanyBankName:str = obj["CompanyBankName"]
      self.CompBankBranchCodeDesc:str = obj["CompBankBranchCodeDesc"]
      self.CreditHold:bool = obj["CreditHold"]
      """  Customer Credit Hold flag  """  
      self.CurrencyDesc:str = obj["CurrencyDesc"]
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.CustBankBranchCodeDesc:str = obj["CustBankBranchCodeDesc"]
      self.CustomerBankAcct:str = obj["CustomerBankAcct"]
      self.CustomerBankIdentifier:str = obj["CustomerBankIdentifier"]
      self.CustomerBankName:str = obj["CustomerBankName"]
      self.DisableBankAcctIDPI:bool = obj["DisableBankAcctIDPI"]
      self.DisableBankAmt:bool = obj["DisableBankAmt"]
      """   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  """  
      self.DispGLAcct:str = obj["DispGLAcct"]
      """  Display GL Account  """  
      self.DocBankRecGainLoss:int = obj["DocBankRecGainLoss"]
      self.DocDiscount:int = obj["DocDiscount"]
      self.DocDiscountAmt:int = obj["DocDiscountAmt"]
      self.DocGainLossReal:int = obj["DocGainLossReal"]
      self.DocGainLossUnreal:int = obj["DocGainLossUnreal"]
      self.DocReceipt:int = obj["DocReceipt"]
      self.DocTranTaxAmt:int = obj["DocTranTaxAmt"]
      """  Transaction Amount less Tax Amount  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.FullyPaid:bool = obj["FullyPaid"]
      self.GainLossReal:int = obj["GainLossReal"]
      self.GainLossUnreal:int = obj["GainLossUnreal"]
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for miscellaneous shipments  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows is this invoice is blocked in RvLock.  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LockStatus:str = obj["LockStatus"]
      """  locked means can not be posted: an invoice is already in review journal or in posting process.  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      self.PITypeInitiation:str = obj["PITypeInitiation"]
      """  like PIType.Initiation  """  
      self.Receipt:int = obj["Receipt"]
      self.RevalueDate:str = obj["RevalueDate"]
      self.Rpt1BankRecGainLoss:int = obj["Rpt1BankRecGainLoss"]
      self.Rpt1DiscountAmt:int = obj["Rpt1DiscountAmt"]
      self.Rpt1GainLossReal:int = obj["Rpt1GainLossReal"]
      self.Rpt1GainLossUnreal:int = obj["Rpt1GainLossUnreal"]
      self.Rpt1Receipt:int = obj["Rpt1Receipt"]
      self.Rpt1TranTaxAmt:int = obj["Rpt1TranTaxAmt"]
      self.Rpt2BankRecGainLoss:int = obj["Rpt2BankRecGainLoss"]
      self.Rpt2DiscountAmt:int = obj["Rpt2DiscountAmt"]
      self.Rpt2GainLossReal:int = obj["Rpt2GainLossReal"]
      self.Rpt2GainLossUnreal:int = obj["Rpt2GainLossUnreal"]
      self.Rpt2Receipt:int = obj["Rpt2Receipt"]
      self.Rpt2TranTaxAmt:int = obj["Rpt2TranTaxAmt"]
      self.Rpt3BankRecGainLoss:int = obj["Rpt3BankRecGainLoss"]
      self.Rpt3DiscountAmt:int = obj["Rpt3DiscountAmt"]
      self.Rpt3GainLossReal:int = obj["Rpt3GainLossReal"]
      self.Rpt3GainLossUnreal:int = obj["Rpt3GainLossUnreal"]
      self.Rpt3Receipt:int = obj["Rpt3Receipt"]
      self.Rpt3TranTaxAmt:int = obj["Rpt3TranTaxAmt"]
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.StatusChgLegalNum:str = obj["StatusChgLegalNum"]
      self.StatusChgTranDocType:str = obj["StatusChgTranDocType"]
      self.TermsDesc:str = obj["TermsDesc"]
      self.TotalCashReceived:int = obj["TotalCashReceived"]
      self.TotalRoundDiff:int = obj["TotalRoundDiff"]
      self.TranTaxAmt:int = obj["TranTaxAmt"]
      self.TypeDesc:str = obj["TypeDesc"]
      self.XRateLabel:str = obj["XRateLabel"]
      self.BankTotalAmount:int = obj["BankTotalAmount"]
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      self.BaseCurrencyDesc:str = obj["BaseCurrencyDesc"]
      self.BaseCurrSymbol:str = obj["BaseCurrSymbol"]
      self.BillToName:str = obj["BillToName"]
      self.DocDiscountedAmt:int = obj["DocDiscountedAmt"]
      self.ARPNDtlExists:bool = obj["ARPNDtlExists"]
      """  for kinetic purposes  """  
      self.ARPNDtlInvoicePosted:bool = obj["ARPNDtlInvoicePosted"]
      """  for kinetic purposes  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankAcctDescription:str = obj["BankAcctDescription"]
      self.BankAcctBankName:str = obj["BankAcctBankName"]
      self.CashbookLineDescription:str = obj["CashbookLineDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CustNumInactive:bool = obj["CustNumInactive"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumName:str = obj["CustNumName"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.PIStatusStatusDesc:str = obj["PIStatusStatusDesc"]
      self.PITypeDescription:str = obj["PITypeDescription"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNListRow:
   def __init__(self, obj):
      self.ARPromNoteID:str = obj["ARPromNoteID"]
      self.Company:str = obj["Company"]
      self.CurGroupID:str = obj["CurGroupID"]
      self.CustID:str = obj["CustID"]
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.PIStage:str = obj["PIStage"]
      self.PIStatus:str = obj["PIStatus"]
      self.TranAmt:int = obj["TranAmt"]
      self.Type:str = obj["Type"]
      self.Selected:bool = obj["Selected"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNMoveRow:
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
      """  Transaction Date  """  
      self.CreateTime:int = obj["CreateTime"]
      """  Creation Time  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EndorsedAPPNGroupID:str = obj["EndorsedAPPNGroupID"]
      """  Reference to Endorsed AP PI GroupID.  """  
      self.EndorsedAPPNHeadNum:int = obj["EndorsedAPPNHeadNum"]
      """  Reference to Endorsed AP PI HeadNum.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.PIStatusDesc:str = obj["PIStatusDesc"]
      """  PI status description  """  
      self.PostErrMess:str = obj["PostErrMess"]
      """  Posting Error Message  """  
      self.PostToGL:bool = obj["PostToGL"]
      """  Indicates if posting GL transactions.  """  
      self.TypeDesc:str = obj["TypeDesc"]
      """  PI Type description  """  
      self.LegalNumMessage:str = obj["LegalNumMessage"]
      self.LegalNumStyle:str = obj["LegalNumStyle"]
      """  Indicates if the legal number is manually generated or system generated  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ARPNMoveTGLCRow:
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
      """  HeadNum for relation to ARPNMoveTGLC  """  
      self.Seq:int = obj["Seq"]
      """  Seq for relation to ARPNMoveTGLC  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID for relation to ARPNMoveTGLC  """  
      self.BitFlag:int = obj["BitFlag"]
      self.COADescription:str = obj["COADescription"]
      self.GLAccountAccountDesc:str = obj["GLAccountAccountDesc"]
      self.GLAccountGLAcctDisp:str = obj["GLAccountGLAcctDisp"]
      self.GLAccountGLShortAcct:str = obj["GLAccountGLShortAcct"]
      self.GLBookDescription:str = obj["GLBookDescription"]
      self.GLBookCurrencyCode:str = obj["GLBookCurrencyCode"]
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

class Erp_Tablesets_UpdExtARPIWriteOffTableset:
   def __init__(self, obj):
      self.ARPNHead:list[Erp_Tablesets_ARPNHeadRow] = obj["ARPNHead"]
      self.ARPNMove:list[Erp_Tablesets_ARPNMoveRow] = obj["ARPNMove"]
      self.ARPNMoveTGLC:list[Erp_Tablesets_ARPNMoveTGLCRow] = obj["ARPNMoveTGLC"]
      self.ARPNList:list[Erp_Tablesets_ARPNListRow] = obj["ARPNList"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetARPNList_input:
   """ Required : 
   ipPNID
   """  
   def __init__(self, obj):
      self.ipPNID:str = obj["ipPNID"]
      """  ipPNID  """  
      pass

class GetARPNList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["returnObj"]
      pass

class GetGroupIDForPI_input:
   """ Required : 
   arPromNoteID
   """  
   def __init__(self, obj):
      self.arPromNoteID:str = obj["arPromNoteID"]
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
      self.returnObj:list[Erp_Tablesets_ARPNHeadListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewARPNHead_input:
   """ Required : 
   ds
   groupID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      pass

class GetNewARPNHead_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNMove1_input:
   """ Required : 
   ds
   ipGroupID
   ipHeadNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      self.ipGroupID:str = obj["ipGroupID"]
      """  The Group ID for this A/R Promissory Note Head  """  
      self.ipHeadNum:int = obj["ipHeadNum"]
      """  The A/R Promissory Note Head Number  """  
      pass

class GetNewARPNMove1_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNMoveTGLC_input:
   """ Required : 
   ds
   groupID
   headNum
   seq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      self.seq:int = obj["seq"]
      pass

class GetNewARPNMoveTGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewARPNMove_input:
   """ Required : 
   ds
   groupID
   headNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      self.groupID:str = obj["groupID"]
      self.headNum:int = obj["headNum"]
      pass

class GetNewARPNMove_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPNByID_input:
   """ Required : 
   ipHeadNum
   ipPIType
   ipID
   ipCustID
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
      self.ipCustID:str = obj["ipCustID"]
      """  ipCustID  """  
      self.ipCurGroupID:str = obj["ipCurGroupID"]
      """  ipCurGroupID  """  
      self.ipNewPIType:str = obj["ipNewPIType"]
      """  ipNewPIType  """  
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

class GetPNByID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseARPNHead
   whereClauseARPNMove
   whereClauseARPNMoveTGLC
   whereClauseARPNList
   whereClauseLegalNumGenOpts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseARPNHead:str = obj["whereClauseARPNHead"]
      self.whereClauseARPNMove:str = obj["whereClauseARPNMove"]
      self.whereClauseARPNMoveTGLC:str = obj["whereClauseARPNMoveTGLC"]
      self.whereClauseARPNList:str = obj["whereClauseARPNList"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtARPIWriteOffTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtARPIWriteOffTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ARPIWriteOffTableset] = obj["ds"]
      pass

      """  output parameters  """  

