import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ZDataSetSvc
# Description: DataSet Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ZDataSets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZDataSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZDataSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets",headers=creds) as resp:
           return await resp.json()

async def post_ZDataSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZDataSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZDataSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZDataSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZDataSets_SystemCode_DataSetID(SystemCode, DataSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZDataSet item
   Description: Calls GetByID to retrieve the ZDataSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZDataSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZDataSets_SystemCode_DataSetID(SystemCode, DataSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZDataSet for the service
   Description: Calls UpdateExt to update ZDataSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZDataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZDataSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZDataSets_SystemCode_DataSetID(SystemCode, DataSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZDataSet item
   Description: Call UpdateExt to delete ZDataSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZDataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZDataSets_SystemCode_DataSetID_ZRelations(SystemCode, DataSetID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZRelations items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZRelations1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")/ZRelations",headers=creds) as resp:
           return await resp.json()

async def get_ZDataSets_SystemCode_DataSetID_ZRelations_SystemCode_DataSetID_RelationID(SystemCode, DataSetID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZRelation item
   Description: Calls GetByID to retrieve the ZRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZRelation1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")/ZRelations(" + SystemCode + "," + DataSetID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZDataSets_SystemCode_DataSetID_ZSubDataSets(SystemCode, DataSetID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZSubDataSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZSubDataSets1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZSubDataSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")/ZSubDataSets",headers=creds) as resp:
           return await resp.json()

async def get_ZDataSets_SystemCode_DataSetID_ZSubDataSets_SystemCode_ParentDataSetID_DataTableSystemCode_DataTableID(SystemCode, DataSetID, ParentDataSetID, DataTableSystemCode, DataTableID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZSubDataSet item
   Description: Calls GetByID to retrieve the ZSubDataSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZSubDataSet1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param ParentDataSetID: Desc: ParentDataSetID   Required: True   Allow empty value : True
      :param DataTableSystemCode: Desc: DataTableSystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZSubDataSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZDataSets(" + SystemCode + "," + DataSetID + ")/ZSubDataSets(" + SystemCode + "," + ParentDataSetID + "," + DataTableSystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZRelations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZRelations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations",headers=creds) as resp:
           return await resp.json()

async def post_ZRelations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZRelationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZRelationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZRelations_SystemCode_DataSetID_RelationID(SystemCode, DataSetID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZRelation item
   Description: Calls GetByID to retrieve the ZRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZRelation
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations(" + SystemCode + "," + DataSetID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZRelations_SystemCode_DataSetID_RelationID(SystemCode, DataSetID, RelationID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZRelation for the service
   Description: Calls UpdateExt to update ZRelation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZRelation
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZRelationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations(" + SystemCode + "," + DataSetID + "," + RelationID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZRelations_SystemCode_DataSetID_RelationID(SystemCode, DataSetID, RelationID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZRelation item
   Description: Call UpdateExt to delete ZRelation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZRelation
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations(" + SystemCode + "," + DataSetID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZRelations_SystemCode_DataSetID_RelationID_ZRelationFields(SystemCode, DataSetID, RelationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZRelationFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZRelationFields1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations(" + SystemCode + "," + DataSetID + "," + RelationID + ")/ZRelationFields",headers=creds) as resp:
           return await resp.json()

async def get_ZRelations_SystemCode_DataSetID_RelationID_ZRelationFields_SystemCode_DataSetID_RelationID_Seq(SystemCode, DataSetID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZRelationField item
   Description: Calls GetByID to retrieve the ZRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZRelationField1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelations(" + SystemCode + "," + DataSetID + "," + RelationID + ")/ZRelationFields(" + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZRelationFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZRelationFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZRelationFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelationFields",headers=creds) as resp:
           return await resp.json()

async def post_ZRelationFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZRelationFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZRelationFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZRelationFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelationFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZRelationFields_SystemCode_DataSetID_RelationID_Seq(SystemCode, DataSetID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZRelationField item
   Description: Calls GetByID to retrieve the ZRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZRelationField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelationFields(" + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZRelationFields_SystemCode_DataSetID_RelationID_Seq(SystemCode, DataSetID, RelationID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZRelationField for the service
   Description: Calls UpdateExt to update ZRelationField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZRelationField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZRelationFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelationFields(" + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZRelationFields_SystemCode_DataSetID_RelationID_Seq(SystemCode, DataSetID, RelationID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZRelationField item
   Description: Call UpdateExt to delete ZRelationField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZRelationField
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZRelationFields(" + SystemCode + "," + DataSetID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZSubDataSets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZSubDataSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZSubDataSets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZSubDataSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZSubDataSets",headers=creds) as resp:
           return await resp.json()

async def post_ZSubDataSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZSubDataSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZSubDataSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZSubDataSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZSubDataSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZSubDataSets_SystemCode_ParentDataSetID_DataTableSystemCode_DataTableID(SystemCode, ParentDataSetID, DataTableSystemCode, DataTableID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZSubDataSet item
   Description: Calls GetByID to retrieve the ZSubDataSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZSubDataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ParentDataSetID: Desc: ParentDataSetID   Required: True   Allow empty value : True
      :param DataTableSystemCode: Desc: DataTableSystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZSubDataSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZSubDataSets(" + SystemCode + "," + ParentDataSetID + "," + DataTableSystemCode + "," + DataTableID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZSubDataSets_SystemCode_ParentDataSetID_DataTableSystemCode_DataTableID(SystemCode, ParentDataSetID, DataTableSystemCode, DataTableID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZSubDataSet for the service
   Description: Calls UpdateExt to update ZSubDataSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZSubDataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ParentDataSetID: Desc: ParentDataSetID   Required: True   Allow empty value : True
      :param DataTableSystemCode: Desc: DataTableSystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZSubDataSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZSubDataSets(" + SystemCode + "," + ParentDataSetID + "," + DataTableSystemCode + "," + DataTableID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZSubDataSets_SystemCode_ParentDataSetID_DataTableSystemCode_DataTableID(SystemCode, ParentDataSetID, DataTableSystemCode, DataTableID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZSubDataSet item
   Description: Call UpdateExt to delete ZSubDataSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZSubDataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ParentDataSetID: Desc: ParentDataSetID   Required: True   Allow empty value : True
      :param DataTableSystemCode: Desc: DataTableSystemCode   Required: True   Allow empty value : True
      :param DataTableID: Desc: DataTableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/ZSubDataSets(" + SystemCode + "," + ParentDataSetID + "," + DataTableSystemCode + "," + DataTableID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataSetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseZDataSet, whereClauseZRelation, whereClauseZRelationField, whereClauseZSubDataSet, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseZDataSet=" + whereClauseZDataSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZRelation=" + whereClauseZRelation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZRelationField=" + whereClauseZRelationField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZSubDataSet=" + whereClauseZSubDataSet
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(systemCode, dataSetID, epicorHeaders = None):
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
   params += "dataSetID=" + dataSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRelationKeyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRelationKeyID
   Description: This method should be invoked when the KeyID in a parent table changes.
This method will validate the KeyID and pull in the new relation fields information.
   OperationID: ChangeRelationKeyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRelationKeyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRelationKeyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteRelationFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteRelationFields
   Description: Delete all fields from the table of relation fields
   OperationID: DeleteRelationFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteRelationFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRelationFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttachTables(epicorHeaders = None):
   """  
   Summary: Invoke method GetAttachTables
   Description: This method returns a list of attachment tables
   OperationID: GetAttachTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttachTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetAttachTableByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttachTableByID
   Description: This method returns a table of attachment tables
   OperationID: GetAttachTableByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttachTableByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttachTableByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelationFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelationFields
   Description: Get Relations Fields
   OperationID: GetRelationFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelationFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelationFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelations
   Description: Get Relations for DataSet
   OperationID: GetRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimaryTableID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimaryTableID
   Description: Gets the primary table identifier.
   OperationID: GetPrimaryTableID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryTableID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryTableID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZDataSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZDataSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZRelation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZRelation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZRelation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZRelation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZRelation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZRelationField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZRelationField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZRelationField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZRelationField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZRelationField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZSubDataSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZSubDataSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZSubDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZSubDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZSubDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZDataSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataSetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZDataSetListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZDataSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZRelationFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZRelationFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZRelationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZRelationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZSubDataSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZSubDataSetRow] = obj["value"]
      pass

class Ice_Tablesets_ZDataSetListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DSType:str = obj["DSType"]
      """   Dataset type defines the type of object that this dataset will be used with. This value corresponds with the values used for zBODef.ClassType.
Valid options are "BO", "Report" and "Process". This constrains what type of Object the dataset can be referenced in. The zBoDef.ClassType must equal the DSType.
This also constrains what type of zDataTables can be included in the dataset and what  The valid reference between Dataset and Tables are based on DSType and zDataTable.TableType. They are as follows:
BO - DB or TT
Report - RP 
Process - PP  
BO -  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataSetRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DSType:str = obj["DSType"]
      """   Dataset type defines the type of object that this dataset will be used with. This value corresponds with the values used for zBODef.ClassType.
Valid options are "BO", "Report" and "Process". This constrains what type of Object the dataset can be referenced in. The zBoDef.ClassType must equal the DSType.
This also constrains what type of zDataTables can be included in the dataset and what  The valid reference between Dataset and Tables are based on DSType and zDataTable.TableType. They are as follows:
BO - DB or TT
Report - RP 
Process - PP  
BO -  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZRelationFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Relation ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.ParentFieldName:str = obj["ParentFieldName"]
      """  Parent Field Name  """  
      self.ChildFieldName:str = obj["ChildFieldName"]
      """  Child Field Name  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between Parent and Child fields.  """  
      self.IsConst:bool = obj["IsConst"]
      """  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Type:int = obj["Type"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZRelationRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Relation ID  """  
      self.ParentSystemCode:str = obj["ParentSystemCode"]
      """  ParentSystemCode  """  
      self.ParentDataTableID:str = obj["ParentDataTableID"]
      """  Parent DataSet  """  
      self.ChildSystemCode:str = obj["ChildSystemCode"]
      """  ChildSystemCode  """  
      self.ChildDataTableID:str = obj["ChildDataTableID"]
      """  Chilc DataSet  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.Type:int = obj["Type"]
      """  Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZSubDataSetRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ParentDataSetID:str = obj["ParentDataSetID"]
      """  Parent DataSet  """  
      self.DataTableSystemCode:str = obj["DataTableSystemCode"]
      """  DataTableSystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.IsPrimaryTable:bool = obj["IsPrimaryTable"]
      """  Primary Table Flag  """  
      self.GenAttachments:bool = obj["GenAttachments"]
      """  Inidicates if a attachments datatable should be generated for this table in the dataset.  Table generated is a logical table for the physical Drawings table. It will have a name of parenttablenameAttachment (ex: CustomerAttachment)  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.ExcludeUpdate:bool = obj["ExcludeUpdate"]
      """  ExcludeUpdate  """  
      self.ExcludeGet:bool = obj["ExcludeGet"]
      """  ExcludeGet  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeRelationKeyID_input:
   """ Required : 
   systemCode
   dataSetID
   relationID
   newKeyID
   ds
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System code  """  
      self.dataSetID:str = obj["dataSetID"]
      """  The DataSetID we want to change Key with  """  
      self.relationID:str = obj["relationID"]
      """  The RelationID we want to change Key with  """  
      self.newKeyID:str = obj["newKeyID"]
      """  Proposed KeyID  """  
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

class ChangeRelationKeyID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteRelationFields_input:
   """ Required : 
   systemCode
   dataSetID
   pcRel
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System code  """  
      self.dataSetID:str = obj["dataSetID"]
      """  The DataSet Code  """  
      self.pcRel:str = obj["pcRel"]
      """  The Relation Code  """  
      pass

class DeleteRelationFields_output:
   def __init__(self, obj):
      pass

class GetAttachTableByID_input:
   """ Required : 
   DataTableID
   """  
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      pass

class GetAttachTableByID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  AttachTableList data set  """  
      pass

class GetAttachTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_AttachTableListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZDataSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZDataSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZDataSetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewZDataSet_input:
   """ Required : 
   ds
   systemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      pass

class GetNewZDataSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZRelationField_input:
   """ Required : 
   ds
   systemCode
   dataSetID
   relationID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      self.relationID:str = obj["relationID"]
      pass

class GetNewZRelationField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZRelation_input:
   """ Required : 
   ds
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.dataSetID:str = obj["dataSetID"]
      pass

class GetNewZRelation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZSubDataSet_input:
   """ Required : 
   ds
   systemCode
   parentDataSetID
   dataTableSystemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.parentDataSetID:str = obj["parentDataSetID"]
      self.dataTableSystemCode:str = obj["dataTableSystemCode"]
      pass

class GetNewZSubDataSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrimaryTableID_input:
   """ Required : 
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  The system code.  """  
      self.dataSetID:str = obj["dataSetID"]
      """  The data set identifier.  """  
      pass

class GetPrimaryTableID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The primary table identifier.  """  
      pass

class GetRelationFields_input:
   """ Required : 
   systemCode
   dataSetID
   relationID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System code  """  
      self.dataSetID:str = obj["dataSetID"]
      """  DataSet Code  """  
      self.relationID:str = obj["relationID"]
      """  The Relation Code  """  
      pass

class GetRelationFields_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataSetTableset] = obj["returnObj"]
      pass

class GetRelations_input:
   """ Required : 
   systemCode
   dataSetID
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System code  """  
      self.dataSetID:str = obj["dataSetID"]
      """  DataSet Code  """  
      pass

class GetRelations_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataSetTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseZDataSet
   whereClauseZRelation
   whereClauseZRelationField
   whereClauseZSubDataSet
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseZDataSet:str = obj["whereClauseZDataSet"]
      self.whereClauseZRelation:str = obj["whereClauseZRelation"]
      self.whereClauseZRelationField:str = obj["whereClauseZRelationField"]
      self.whereClauseZSubDataSet:str = obj["whereClauseZSubDataSet"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZDataSetTableset] = obj["returnObj"]
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

class Ice_Tablesets_AttachTableListRow:
   def __init__(self, obj):
      self.DataTableID:str = obj["DataTableID"]
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.GenAttachments:bool = obj["GenAttachments"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_AttachTableListTableset:
   def __init__(self, obj):
      self.AttachTableList:list[Ice_Tablesets_AttachTableListRow] = obj["AttachTableList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtZDataSetTableset:
   def __init__(self, obj):
      self.ZDataSet:list[Ice_Tablesets_ZDataSetRow] = obj["ZDataSet"]
      self.ZRelation:list[Ice_Tablesets_ZRelationRow] = obj["ZRelation"]
      self.ZRelationField:list[Ice_Tablesets_ZRelationFieldRow] = obj["ZRelationField"]
      self.ZSubDataSet:list[Ice_Tablesets_ZSubDataSetRow] = obj["ZSubDataSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZDataSetListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DSType:str = obj["DSType"]
      """   Dataset type defines the type of object that this dataset will be used with. This value corresponds with the values used for zBODef.ClassType.
Valid options are "BO", "Report" and "Process". This constrains what type of Object the dataset can be referenced in. The zBoDef.ClassType must equal the DSType.
This also constrains what type of zDataTables can be included in the dataset and what  The valid reference between Dataset and Tables are based on DSType and zDataTable.TableType. They are as follows:
BO - DB or TT
Report - RP 
Process - PP  
BO -  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataSetListTableset:
   def __init__(self, obj):
      self.ZDataSetList:list[Ice_Tablesets_ZDataSetListRow] = obj["ZDataSetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZDataSetRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DSType:str = obj["DSType"]
      """   Dataset type defines the type of object that this dataset will be used with. This value corresponds with the values used for zBODef.ClassType.
Valid options are "BO", "Report" and "Process". This constrains what type of Object the dataset can be referenced in. The zBoDef.ClassType must equal the DSType.
This also constrains what type of zDataTables can be included in the dataset and what  The valid reference between Dataset and Tables are based on DSType and zDataTable.TableType. They are as follows:
BO - DB or TT
Report - RP 
Process - PP  
BO -  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZDataSetTableset:
   def __init__(self, obj):
      self.ZDataSet:list[Ice_Tablesets_ZDataSetRow] = obj["ZDataSet"]
      self.ZRelation:list[Ice_Tablesets_ZRelationRow] = obj["ZRelation"]
      self.ZRelationField:list[Ice_Tablesets_ZRelationFieldRow] = obj["ZRelationField"]
      self.ZSubDataSet:list[Ice_Tablesets_ZSubDataSetRow] = obj["ZSubDataSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZRelationFieldRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Relation ID  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.ParentFieldName:str = obj["ParentFieldName"]
      """  Parent Field Name  """  
      self.ChildFieldName:str = obj["ChildFieldName"]
      """  Child Field Name  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between Parent and Child fields.  """  
      self.IsConst:bool = obj["IsConst"]
      """  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Type:int = obj["Type"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZRelationRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  DataSet ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Relation ID  """  
      self.ParentSystemCode:str = obj["ParentSystemCode"]
      """  ParentSystemCode  """  
      self.ParentDataTableID:str = obj["ParentDataTableID"]
      """  Parent DataSet  """  
      self.ChildSystemCode:str = obj["ChildSystemCode"]
      """  ChildSystemCode  """  
      self.ChildDataTableID:str = obj["ChildDataTableID"]
      """  Chilc DataSet  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.Type:int = obj["Type"]
      """  Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZSubDataSetRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ParentDataSetID:str = obj["ParentDataSetID"]
      """  Parent DataSet  """  
      self.DataTableSystemCode:str = obj["DataTableSystemCode"]
      """  DataTableSystemCode  """  
      self.DataTableID:str = obj["DataTableID"]
      """  DataTable ID  """  
      self.IsPrimaryTable:bool = obj["IsPrimaryTable"]
      """  Primary Table Flag  """  
      self.GenAttachments:bool = obj["GenAttachments"]
      """  Inidicates if a attachments datatable should be generated for this table in the dataset.  Table generated is a logical table for the physical Drawings table. It will have a name of parenttablenameAttachment (ex: CustomerAttachment)  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.ExcludeUpdate:bool = obj["ExcludeUpdate"]
      """  ExcludeUpdate  """  
      self.ExcludeGet:bool = obj["ExcludeGet"]
      """  ExcludeGet  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtZDataSetTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtZDataSetTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZDataSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

