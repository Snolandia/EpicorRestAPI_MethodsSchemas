import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.RptDataDefSvc
# Description: Business Logic (create/update/delete...) for Report Data Definitions
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RptDataDefs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptDataDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptDataDefs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs",headers=creds) as resp:
           return await resp.json()

async def post_RptDataDefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptDataDefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptDataDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptDataDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptDataDefs_RptDefID(RptDefID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptDataDef item
   Description: Calls GetByID to retrieve the RptDataDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptDataDef
      :param RptDefID: Desc: RptDefID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptDataDefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs(" + RptDefID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptDataDefs_RptDefID(RptDefID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptDataDef for the service
   Description: Calls UpdateExt to update RptDataDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptDataDef
      :param RptDefID: Desc: RptDefID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptDataDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs(" + RptDefID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptDataDefs_RptDefID(RptDefID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptDataDef item
   Description: Call UpdateExt to delete RptDataDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptDataDef
      :param RptDefID: Desc: RptDefID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs(" + RptDefID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables",headers=creds) as resp:
           return await resp.json()

async def post_RptTables(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID(RptDefID, RptTableID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptTable item
   Description: Calls GetByID to retrieve the RptTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptTable
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptTables_RptDefID_RptTableID(RptDefID, RptTableID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptTable for the service
   Description: Calls UpdateExt to update RptTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptTable
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptTables_RptDefID_RptTableID(RptDefID, RptTableID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptTable item
   Description: Call UpdateExt to delete RptTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptTable
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptCalcFields(RptDefID, RptTableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptCalcFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptCalcFields1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCalcFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptCalcFields",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCalcField item
   Description: Calls GetByID to retrieve the RptCalcField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCalcField1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptExcludes(RptDefID, RptTableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptExcludes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptExcludes1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptExcludeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptExcludes",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, ZFieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptExclude item
   Description: Calls GetByID to retrieve the RptExclude item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptExclude1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZFieldName: Desc: ZFieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptLinkTables(RptDefID, RptTableID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptLinkTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptLinkTables1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptLinkTables",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptLinkTable item
   Description: Calls GetByID to retrieve the RptLinkTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkTable1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptWhereItems(RptDefID, RptTableID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptWhereItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptWhereItems1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptWhereItems",headers=creds) as resp:
           return await resp.json()

async def get_RptTables_RptDefID_RptTableID_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID, RptTableID, SystemCode, ZDataTableID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptWhereItem item
   Description: Calls GetByID to retrieve the RptWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptWhereItem1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptCalcFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptCalcFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCalcFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCalcFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields",headers=creds) as resp:
           return await resp.json()

async def post_RptCalcFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCalcFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCalcField item
   Description: Calls GetByID to retrieve the RptCalcField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCalcField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptCalcField for the service
   Description: Calls UpdateExt to update RptCalcField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCalcField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptCalcField item
   Description: Call UpdateExt to delete RptCalcField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCalcField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptExcludes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptExcludes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptExcludes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptExcludeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes",headers=creds) as resp:
           return await resp.json()

async def post_RptExcludes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptExcludes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, ZFieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptExclude item
   Description: Calls GetByID to retrieve the RptExclude item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptExclude
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZFieldName: Desc: ZFieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, ZFieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptExclude for the service
   Description: Calls UpdateExt to update RptExclude. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptExclude
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZFieldName: Desc: ZFieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID, RptTableID, SystemCode, ZDataTableID, ZFieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptExclude item
   Description: Call UpdateExt to delete RptExclude item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptExclude
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZFieldName: Desc: ZFieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptLinkTables(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptLinkTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptLinkTables
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables",headers=creds) as resp:
           return await resp.json()

async def post_RptLinkTables(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptLinkTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptLinkTable item
   Description: Calls GetByID to retrieve the RptLinkTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkTable
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptLinkTable for the service
   Description: Calls UpdateExt to update RptLinkTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptLinkTable
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptLinkTable item
   Description: Call UpdateExt to delete RptLinkTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptLinkTable
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_RptLinkFields(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptLinkFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptLinkFields1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")/RptLinkFields",headers=creds) as resp:
           return await resp.json()

async def get_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptLinkField item
   Description: Calls GetByID to retrieve the RptLinkField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkField1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptLinkFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptLinkFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptLinkFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields",headers=creds) as resp:
           return await resp.json()

async def post_RptLinkFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptLinkFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, FieldName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptLinkField item
   Description: Calls GetByID to retrieve the RptLinkField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, FieldName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptLinkField for the service
   Description: Calls UpdateExt to update RptLinkField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptLinkField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID, RptTableID, RptLinkID, SystemCode, ZDataTableID, ZLookupID, FieldName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptLinkField item
   Description: Call UpdateExt to delete RptLinkField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptLinkField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param RptLinkID: Desc: RptLinkID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param ZLookupID: Desc: ZLookupID   Required: True   Allow empty value : True
      :param FieldName: Desc: FieldName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptWhereItems(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptWhereItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptWhereItems
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems",headers=creds) as resp:
           return await resp.json()

async def post_RptWhereItems(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptWhereItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID, RptTableID, SystemCode, ZDataTableID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptWhereItem item
   Description: Calls GetByID to retrieve the RptWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptWhereItem
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID, RptTableID, SystemCode, ZDataTableID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptWhereItem for the service
   Description: Calls UpdateExt to update RptWhereItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptWhereItem
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID, RptTableID, SystemCode, ZDataTableID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptWhereItem item
   Description: Call UpdateExt to delete RptWhereItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptWhereItem
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ZDataTableID: Desc: ZDataTableID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaSets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptCriteriaSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaSets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets",headers=creds) as resp:
           return await resp.json()

async def post_RptCriteriaSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptCriteriaSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaSets_RptDefID_RptCriteriaSetID(RptDefID, RptCriteriaSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCriteriaSet item
   Description: Calls GetByID to retrieve the RptCriteriaSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaSet
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCriteriaSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets(" + RptDefID + "," + RptCriteriaSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptCriteriaSets_RptDefID_RptCriteriaSetID(RptDefID, RptCriteriaSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptCriteriaSet for the service
   Description: Calls UpdateExt to update RptCriteriaSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaSet
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets(" + RptDefID + "," + RptCriteriaSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptCriteriaSets_RptDefID_RptCriteriaSetID(RptDefID, RptCriteriaSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptCriteriaSet item
   Description: Call UpdateExt to delete RptCriteriaSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaSet
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets(" + RptDefID + "," + RptCriteriaSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaFilters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptCriteriaFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaFilters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters",headers=creds) as resp:
           return await resp.json()

async def post_RptCriteriaFilters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaFilters_RptDefID_RptCriteriaSetID_FilterID(RptDefID, RptCriteriaSetID, FilterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCriteriaFilter item
   Description: Calls GetByID to retrieve the RptCriteriaFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaFilter
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters(" + RptDefID + "," + RptCriteriaSetID + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptCriteriaFilters_RptDefID_RptCriteriaSetID_FilterID(RptDefID, RptCriteriaSetID, FilterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptCriteriaFilter for the service
   Description: Calls UpdateExt to update RptCriteriaFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaFilter
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters(" + RptDefID + "," + RptCriteriaSetID + "," + FilterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptCriteriaFilters_RptDefID_RptCriteriaSetID_FilterID(RptDefID, RptCriteriaSetID, FilterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptCriteriaFilter item
   Description: Call UpdateExt to delete RptCriteriaFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaFilter
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param FilterID: Desc: FilterID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters(" + RptDefID + "," + RptCriteriaSetID + "," + FilterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaMappings(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptCriteriaMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaMappings
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings",headers=creds) as resp:
           return await resp.json()

async def post_RptCriteriaMappings(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaMappings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaMappings_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID, RptCriteriaSetID, RptTableID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCriteriaMapping item
   Description: Calls GetByID to retrieve the RptCriteriaMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaMapping
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptCriteriaMappings_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID, RptCriteriaSetID, RptTableID, ParameterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptCriteriaMapping for the service
   Description: Calls UpdateExt to update RptCriteriaMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaMapping
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptCriteriaMappings_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID, RptCriteriaSetID, RptTableID, ParameterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptCriteriaMapping item
   Description: Call UpdateExt to delete RptCriteriaMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaMapping
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaPrompts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptCriteriaPrompts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaPrompts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaPromptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts",headers=creds) as resp:
           return await resp.json()

async def post_RptCriteriaPrompts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaPrompts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaPrompts_RptDefID_RptCriteriaSetID_PromptID(RptDefID, RptCriteriaSetID, PromptID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCriteriaPrompt item
   Description: Calls GetByID to retrieve the RptCriteriaPrompt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaPrompt
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param PromptID: Desc: PromptID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptCriteriaPrompts_RptDefID_RptCriteriaSetID_PromptID(RptDefID, RptCriteriaSetID, PromptID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptCriteriaPrompt for the service
   Description: Calls UpdateExt to update RptCriteriaPrompt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaPrompt
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param PromptID: Desc: PromptID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptCriteriaPrompts_RptDefID_RptCriteriaSetID_PromptID(RptDefID, RptCriteriaSetID, PromptID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptCriteriaPrompt item
   Description: Call UpdateExt to delete RptCriteriaPrompt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaPrompt
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param PromptID: Desc: PromptID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaPromptValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptCriteriaPromptValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaPromptValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaPromptValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues",headers=creds) as resp:
           return await resp.json()

async def post_RptCriteriaPromptValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaPromptValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptCriteriaPromptValues_RptDefID_RptCriteriaSetID_PromptID_ItemID(RptDefID, RptCriteriaSetID, PromptID, ItemID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptCriteriaPromptValue item
   Description: Calls GetByID to retrieve the RptCriteriaPromptValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaPromptValue
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param PromptID: Desc: PromptID   Required: True
      :param ItemID: Desc: ItemID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + "," + ItemID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptCriteriaPromptValues_RptDefID_RptCriteriaSetID_PromptID_ItemID(RptDefID, RptCriteriaSetID, PromptID, ItemID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptCriteriaPromptValue for the service
   Description: Calls UpdateExt to update RptCriteriaPromptValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaPromptValue
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param PromptID: Desc: PromptID   Required: True
      :param ItemID: Desc: ItemID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + "," + ItemID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptCriteriaPromptValues_RptDefID_RptCriteriaSetID_PromptID_ItemID(RptDefID, RptCriteriaSetID, PromptID, ItemID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptCriteriaPromptValue item
   Description: Call UpdateExt to delete RptCriteriaPromptValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaPromptValue
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param PromptID: Desc: PromptID   Required: True
      :param ItemID: Desc: ItemID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + "," + ItemID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptRelations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptRelations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations",headers=creds) as resp:
           return await resp.json()

async def post_RptRelations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptRelations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptRelationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptRelationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptRelations_RptDefID_RelationID(RptDefID, RelationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptRelation item
   Description: Calls GetByID to retrieve the RptRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptRelation
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptRelationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptRelations_RptDefID_RelationID(RptDefID, RelationID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptRelation for the service
   Description: Calls UpdateExt to update RptRelation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptRelation
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptRelationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptRelations_RptDefID_RelationID(RptDefID, RelationID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptRelation item
   Description: Call UpdateExt to delete RptRelation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptRelation
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptRelations_RptDefID_RelationID_RptRelationFields(RptDefID, RelationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RptRelationFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptRelationFields1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")/RptRelationFields",headers=creds) as resp:
           return await resp.json()

async def get_RptRelations_RptDefID_RelationID_RptRelationFields_RptDefID_RelationID_Seq(RptDefID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptRelationField item
   Description: Calls GetByID to retrieve the RptRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptRelationField1
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptRelationFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptRelationFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptRelationFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields",headers=creds) as resp:
           return await resp.json()

async def post_RptRelationFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptRelationFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptRelationFields_RptDefID_RelationID_Seq(RptDefID, RelationID, Seq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptRelationField item
   Description: Calls GetByID to retrieve the RptRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptRelationField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptRelationFields_RptDefID_RelationID_Seq(RptDefID, RelationID, Seq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptRelationField for the service
   Description: Calls UpdateExt to update RptRelationField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptRelationField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RelationID: Desc: RelationID   Required: True   Allow empty value : True
      :param Seq: Desc: Seq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptRelationFields_RptDefID_RelationID_Seq(RptDefID, RelationID, Seq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptRelationField item
   Description: Call UpdateExt to delete RptRelationField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptRelationField
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptLiterals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptLiterals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptLiterals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLiteralsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals",headers=creds) as resp:
           return await resp.json()

async def post_RptLiterals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptLiterals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptLiteralsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptLiteralsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptLiterals_RptDefID_LiteralName(RptDefID, LiteralName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptLiteral item
   Description: Calls GetByID to retrieve the RptLiteral item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLiteral
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param LiteralName: Desc: LiteralName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptLiteralsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals(" + RptDefID + "," + LiteralName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptLiterals_RptDefID_LiteralName(RptDefID, LiteralName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptLiteral for the service
   Description: Calls UpdateExt to update RptLiteral. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptLiteral
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param LiteralName: Desc: LiteralName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptLiteralsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals(" + RptDefID + "," + LiteralName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptLiterals_RptDefID_LiteralName(RptDefID, LiteralName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptLiteral item
   Description: Call UpdateExt to delete RptLiteral item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptLiteral
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param LiteralName: Desc: LiteralName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals(" + RptDefID + "," + LiteralName + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptDataSourceFields(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptDataSourceFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptDataSourceFields
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataSourceFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields",headers=creds) as resp:
           return await resp.json()

async def post_RptDataSourceFields(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptDataSourceFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptDataSourceFields_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptDataSourceField item
   Description: Calls GetByID to retrieve the RptDataSourceField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptDataSourceField
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptDataSourceFields_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptDataSourceField for the service
   Description: Calls UpdateExt to update RptDataSourceField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptDataSourceField
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptDataSourceFields_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptDataSourceField item
   Description: Call UpdateExt to delete RptDataSourceField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptDataSourceField
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_RptDataSourceParameters(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RptDataSourceParameters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptDataSourceParameters
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataSourceParameterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters",headers=creds) as resp:
           return await resp.json()

async def post_RptDataSourceParameters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptDataSourceParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RptDataSourceParameters_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID, RptCriteriaSetID, RptTableID, ParameterID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RptDataSourceParameter item
   Description: Calls GetByID to retrieve the RptDataSourceParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptDataSourceParameter
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RptDataSourceParameters_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID, RptCriteriaSetID, RptTableID, ParameterID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RptDataSourceParameter for the service
   Description: Calls UpdateExt to update RptDataSourceParameter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptDataSourceParameter
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RptDataSourceParameters_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID, RptCriteriaSetID, RptTableID, ParameterID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RptDataSourceParameter item
   Description: Call UpdateExt to delete RptDataSourceParameter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptDataSourceParameter
      :param RptDefID: Desc: RptDefID   Required: True   Allow empty value : True
      :param RptCriteriaSetID: Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      :param RptTableID: Desc: RptTableID   Required: True   Allow empty value : True
      :param ParameterID: Desc: ParameterID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataDefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRptDataDef, whereClauseRptTable, whereClauseRptCalcField, whereClauseRptExclude, whereClauseRptLinkTable, whereClauseRptLinkField, whereClauseRptWhereItem, whereClauseRptCriteriaSet, whereClauseRptCriteriaFilter, whereClauseRptCriteriaMapping, whereClauseRptCriteriaPrompt, whereClauseRptCriteriaPromptValue, whereClauseRptRelation, whereClauseRptRelationField, whereClauseRptLiterals, whereClauseRptDataSourceField, whereClauseRptDataSourceParameter, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRptDataDef=" + whereClauseRptDataDef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptTable=" + whereClauseRptTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptCalcField=" + whereClauseRptCalcField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptExclude=" + whereClauseRptExclude
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptLinkTable=" + whereClauseRptLinkTable
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptLinkField=" + whereClauseRptLinkField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptWhereItem=" + whereClauseRptWhereItem
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptCriteriaSet=" + whereClauseRptCriteriaSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptCriteriaFilter=" + whereClauseRptCriteriaFilter
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptCriteriaMapping=" + whereClauseRptCriteriaMapping
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptCriteriaPrompt=" + whereClauseRptCriteriaPrompt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptCriteriaPromptValue=" + whereClauseRptCriteriaPromptValue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptRelation=" + whereClauseRptRelation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptRelationField=" + whereClauseRptRelationField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptLiterals=" + whereClauseRptLiterals
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptDataSourceField=" + whereClauseRptDataSourceField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRptDataSourceParameter=" + whereClauseRptDataSourceParameter
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(rptDefID, epicorHeaders = None):
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
   params += "rptDefID=" + rptDefID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CreateRptCriteriaPromptsforSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateRptCriteriaPromptsforSelected
   Description: Create Report Criteria Prompts for each Report Mapping record selected.
   OperationID: CreateRptCriteriaPromptsforSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateRptCriteriaPromptsforSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRptCriteriaPromptsforSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DoesExistsRptCriteriaMappingbyRptTableID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoesExistsRptCriteriaMappingbyRptTableID
   Description: Check if exists RptCriteriaMapping records for a Report Data Source
   OperationID: DoesExistsRptCriteriaMappingbyRptTableID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoesExistsRptCriteriaMappingbyRptTableID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesExistsRptCriteriaMappingbyRptTableID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelationColumnList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelationColumnList
   Description: Get column list when building report relation between parent and child tables
   OperationID: GetRelationColumnList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelationColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelationColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetColumnTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetColumnTypeList
   Description: Column types list
   OperationID: Get_GetColumnTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetColumnTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetMappingTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetMappingTypeList
   Description: Mapping types list
   OperationID: Get_GetMappingTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMappingTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetEditorTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetEditorTypeList
   Description: Editor types list
   OperationID: Get_GetEditorTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEditorTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDataFromList(epicorHeaders = None):
   """  
   Summary: Invoke method GetDataFromList
   Description: Get values for Data From dropdown
   OperationID: GetDataFromList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetCriteriaMappingFPList(rptDefID, rptCriteriaSetID, mappingType, epicorHeaders = None):
   """  
   Summary: Invoke method GetCriteriaMappingFPList
   Description: Get list of controls according mapping type
   OperationID: Get_GetCriteriaMappingFPList
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCriteriaMappingFPList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rptDefID=" + rptDefID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "rptCriteriaSetID=" + rptCriteriaSetID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "mappingType=" + mappingType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAllCriteriaSets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAllCriteriaSets
   Description: Delete all criteria sets for a report data definition.
   OperationID: DeleteAllCriteriaSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteAllCriteriaSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAllCriteriaSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEICalculators(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEICalculators
   Description: Get Electronic Interface Calculator Names in tilde-separated string.
   OperationID: GetEICalculators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEICalculators_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEICalculators_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DoesRptExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoesRptExist
   Description: Check to see if report exists.
   OperationID: DoesRptExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoesRptExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesRptExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DoesRptCriteriaSetExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoesRptCriteriaSetExists
   Description: check to see if report criteria set already exists.
   OperationID: DoesRptCriteriaSetExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoesRptCriteriaSetExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesRptCriteriaSetExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateRpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateRpt
   Description: To create a new report data definition by duplicating from another.
Typically this is used to duplicate a system report definition so that it can be modified.
   OperationID: DuplicateRpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateRpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateRptCriteriaSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateRptCriteriaSet
   Description: Create a new report criteria set by duplicating from another.
   OperationID: DuplicateRptCriteriaSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateRptCriteriaSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRptCriteriaSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataDefUsedTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataDefUsedTables
   Description: Returns a DataSet with a list of tables and their fields in use on a Report Data Definition given a Report Definition ID.
   OperationID: GetDataDefUsedTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataDefUsedTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataDefUsedTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetOperatorList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetOperatorList
   Description: Gets the Operator List to compare FieldName against a constant or another field
   OperationID: GetOperatorList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetOperatorList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRptDataDefList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRptDataDefList
   Description: Gets the Report Data Definition List for a specific ReportID
   OperationID: GetRptDataDefList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRptDataDefList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRptDataDefList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReport
   Description: Exports the report.
   OperationID: ExportReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportReportEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportReportEx
   Description: Export the report with given name
   OperationID: ExportReportEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportReportEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReport
   Description: Imports the report.
   OperationID: ImportReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportReportEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportReportEx
   Description: Imports the report by given filename (with path).
   OperationID: ImportReportEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportReportEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldsUsedByReportTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldsUsedByReportTable
   Description: Returns a DataSet with a list of fields (including calculated fields) in use on a Report table within a Report Data Definition.
   OperationID: GetFieldsUsedByReportTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldsUsedByReportTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldsUsedByReportTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptTableEx(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptTableEx
   Description: Create new Rpt source (table, BAQ, EI) by sourceType, wrapper to GetNewRptTable
   OperationID: GetNewRptTableEx
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptTableEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptTableEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFieldType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFieldType
   Description: Get the data type of a data field.
   OperationID: GetFieldType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFieldType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataSourceType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataSourceType
   Description: Get DataSource Type for the RptTable record.
   OperationID: GetDataSourceType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataSourceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeQueryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeQueryID
   OperationID: OnChangeQueryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportDataSchema(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportDataSchema
   Description: Gets the schema for the report data.
   OperationID: GetReportDataSchema
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportDataSchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportDataSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportDataSchemaTablesAndFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportDataSchemaTablesAndFields
   Description: Gets the schema for the report data in a tableset to usable in REST calls.
   OperationID: GetReportDataSchemaTablesAndFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportDataSchemaTablesAndFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportDataSchemaTablesAndFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBreakTableList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBreakTableList
   Description: Get break table list (for report style combo box)
   OperationID: GetBreakTableList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBreakTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBreakTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPromptsAndFiltersForRptCriteriaSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPromptsAndFiltersForRptCriteriaSet
   Description: Returns the Prompts and Filters for the given Report Data Definition and Report Criteria Set.
   OperationID: GetPromptsAndFiltersForRptCriteriaSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPromptsAndFiltersForRptCriteriaSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPromptsAndFiltersForRptCriteriaSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTokenList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given data type.
   OperationID: GetTokenList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTokenList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExportElectronicInterface(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExportElectronicInterface
   Description: Export electronic interfaces as a DataSet.
   OperationID: ExportElectronicInterface
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExportElectronicInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportElectronicInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportElectronicInterface(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportElectronicInterface
   Description: Import electronic interfaces from a DataSet.
   OperationID: ImportElectronicInterface
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportElectronicInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportElectronicInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteElectronicInterface(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteElectronicInterface
   Description: Delete an electronic interface.
   OperationID: DeleteElectronicInterface
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteElectronicInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteElectronicInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetElectronicInterfaceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetElectronicInterfaceList
   Description: Calls the ERP Extension if present and returns a list of Electronic Interfaces.
   OperationID: GetElectronicInterfaceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetElectronicInterfaceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetElectronicInterfaceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDropDownPromptDisplayOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDropDownPromptDisplayOrder
   Description: Change display order value from a source drop down prompt item to a target one and vice versa.
   OperationID: ChangeDropDownPromptDisplayOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDropDownPromptDisplayOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropDownPromptDisplayOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDropDownPromptRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDropDownPromptRows
   Description: Get Drop down prompt rows.
   OperationID: GetDropDownPromptRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDropDownPromptRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDropDownPromptRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBAQDataSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBAQDataSource
   Description: Validates the BAQ data source is able to current company, throw en exception where exists any BAQ record not founded.
   OperationID: ValidateBAQDataSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBAQDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBAQDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRptLabels(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRptLabels
   Description: Validates that the number of labels does not exceed a maximum of 800 for system reports and 1020 for custom (non-system) reports.
   OperationID: ValidateRptLabels
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRptLabels_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRptLabels_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectLinkTables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectLinkTables
   Description: Get list of tables available for RptLinkTable selection
   OperationID: GetSelectLinkTables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectLinkTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectLinkTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptDataDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptDataDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptDataDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptDataDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptDataDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptCalcField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptCalcField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCalcField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptCalcField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCalcField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptExclude(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptExclude
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptExclude
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptExclude_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptExclude_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptLinkTable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptLinkTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptLinkTable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptLinkTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptLinkTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptLinkField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptLinkField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptLinkField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptLinkField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptLinkField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptWhereItem(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptWhereItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptWhereItem
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptWhereItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptWhereItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptCriteriaSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptCriteriaSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptCriteriaFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptCriteriaFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptCriteriaMapping(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptCriteriaMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaMapping
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptCriteriaPrompt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptCriteriaPrompt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaPrompt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaPrompt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaPrompt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptCriteriaPromptValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptCriteriaPromptValue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaPromptValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaPromptValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaPromptValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptRelation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptRelation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptRelation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptRelation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptRelation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptRelationField(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptRelationField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptRelationField
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptRelationField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptRelationField_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRptLiterals(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRptLiterals
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptLiterals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRptLiterals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptLiterals_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCalcFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptCalcFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaFilterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptCriteriaFilterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaMappingRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptCriteriaMappingRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptCriteriaPromptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptValueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptCriteriaPromptValueRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptCriteriaSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptDataDefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptDataDefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptDataSourceFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceParameterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptDataSourceParameterRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptExcludeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptExcludeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptLinkFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptLinkTableRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLiteralsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptLiteralsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationFieldRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptRelationFieldRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptRelationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptTableRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptTableRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptWhereItemRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_RptWhereItemRow] = obj["value"]
      pass

class Ice_Tablesets_RptCalcFieldRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.FieldName:str = obj["FieldName"]
      """  Name for Calculated Field.  When output to XML they will be written as Calc-fieldname in order to avoid conflicts with other fields in the table.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.DataType:str = obj["DataType"]
      """  Character, Date, Integer, Decimal, Logical  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldLength:int = obj["FieldLength"]
      """  Field Length  """  
      self.FieldPrecision:int = obj["FieldPrecision"]
      """  Field Precision  """  
      self.DecimalCurDepended:bool = obj["DecimalCurDepended"]
      """  Decimal Currency Dependent  """  
      self.DecimalValueType:str = obj["DecimalValueType"]
      """  Value Type: G - General, C - Cost, P - Price  """  
      self.DecimalCurrencyType:str = obj["DecimalCurrencyType"]
      """  Currency type: O - Own/Base Currency, G - Global Currency, D - Currency from Document  """  
      self.DecimalCurCodeField:str = obj["DecimalCurCodeField"]
      """  Decimal Currency code  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the Business use of the Field  """  
      self.ZFieldName:str = obj["ZFieldName"]
      """  Field Name from zdatatable  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptCriteriaFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.FilterID:int = obj["FilterID"]
      """  FilterID  """  
      self.FilterName:str = obj["FilterName"]
      """  FilterName  """  
      self.AdapterName:str = obj["AdapterName"]
      """  AdapterName  """  
      self.LookupField:str = obj["LookupField"]
      """  LookupField  """  
      self.FilterLabel:str = obj["FilterLabel"]
      """  FilterLabel  """  
      self.TabLabel:str = obj["TabLabel"]
      """  TabLabel  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  EpiGuid  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  DisplayOrder  """  
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

class Ice_Tablesets_RptCriteriaMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  RptTableID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.FilterID:int = obj["FilterID"]
      """  FilterID  """  
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

class Ice_Tablesets_RptCriteriaPromptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.PromptName:str = obj["PromptName"]
      """  PromptName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Label:str = obj["Label"]
      """  Label  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  EpiGuid  """  
      self.IsConstant:bool = obj["IsConstant"]
      """  IsConstant  """  
      self.ConstantValue:str = obj["ConstantValue"]
      """  ConstantValue  """  
      self.IsVisible:bool = obj["IsVisible"]
      """  IsVisible  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  DisplayOrder  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EditorType:str = obj["EditorType"]
      """  EditorType  """  
      self.DataFrom:str = obj["DataFrom"]
      """  DataFrom  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.DisplayColumn:str = obj["DisplayColumn"]
      """  DisplayColumn  """  
      self.ValueColumn:str = obj["ValueColumn"]
      """  ValueColumn  """  
      self.EFTHeadCompany:str = obj["EFTHeadCompany"]
      """  EFTHeadCompany  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.IsEmptyString:bool = obj["IsEmptyString"]
      """  Use an empty string on this column, instead of null.  """  
      self.EIName:str = obj["EIName"]
      self.EIDescription:str = obj["EIDescription"]
      self.DefaultValueInt:int = obj["DefaultValueInt"]
      self.DefaultValueNum:int = obj["DefaultValueNum"]
      self.DefaultValueDatetime:str = obj["DefaultValueDatetime"]
      self.IsDynamic:bool = obj["IsDynamic"]
      self.DefaultValueBit:bool = obj["DefaultValueBit"]
      self.ConstantValueBit:bool = obj["ConstantValueBit"]
      self.ConstantValueDatetime:str = obj["ConstantValueDatetime"]
      self.ConstantValueNum:int = obj["ConstantValueNum"]
      self.ConstantValueInt:int = obj["ConstantValueInt"]
      self.UseTypedValues:bool = obj["UseTypedValues"]
      self.DefaultValueDatetimeDynamic:str = obj["DefaultValueDatetimeDynamic"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptCriteriaPromptValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.ItemID:int = obj["ItemID"]
      """  ItemID  """  
      self.ItemValue:str = obj["ItemValue"]
      """  ItemValue  """  
      self.ItemDescription:str = obj["ItemDescription"]
      """  ItemDescription  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  DisplayOrder  """  
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

class Ice_Tablesets_RptCriteriaSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  IsDefault  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Data Definition Description  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  """  
      self.DuplicateOf:str = obj["DuplicateOf"]
      """  Used to identify which data definition was used for duplication.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DynamicReport:bool = obj["DynamicReport"]
      """  Flag to indicate Dynamic Report  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Data Definition Description  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  """  
      self.DuplicateOf:str = obj["DuplicateOf"]
      """  Used to identify which data definition was used for duplication.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.PrimaryTable:str = obj["PrimaryTable"]
      """  PrimaryTable  """  
      self.PrimaryKey1:str = obj["PrimaryKey1"]
      """  PrimaryKey1  """  
      self.PrimaryKey2:str = obj["PrimaryKey2"]
      """  PrimaryKey2  """  
      self.UseMultipleCriteria:bool = obj["UseMultipleCriteria"]
      """  UseMultipleCriteria  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataSourceFieldRow:
   def __init__(self, obj):
      self.FieldName:str = obj["FieldName"]
      self.QueryID:str = obj["QueryID"]
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Field Name  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataSourceParameterRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  RptTableID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.FilterID:int = obj["FilterID"]
      """  FilterID  """  
      self.Type:str = obj["Type"]
      """  Data source type.  """  
      self.ParamDataType:str = obj["ParamDataType"]
      """  Parameter data type.  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Flag to inditate if parameter is mandatory or not.  """  
      self.SkipIfEmpty:bool = obj["SkipIfEmpty"]
      self.ControlType:str = obj["ControlType"]
      """  Shows control type related to parameter: Prompt or Filter.  """  
      self.ControlName:str = obj["ControlName"]
      self.ControlDataType:str = obj["ControlDataType"]
      self.QueryEI:str = obj["QueryEI"]
      self.SysRevID:int = obj["SysRevID"]
      self.Selection:bool = obj["Selection"]
      self.SourceControlType:str = obj["SourceControlType"]
      """  Control type in the source of the parameter.  """  
      self.ControlNameDesc:str = obj["ControlNameDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptExcludeRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ZFieldName:str = obj["ZFieldName"]
      """  zField Name  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExcludeColumn:bool = obj["ExcludeColumn"]
      """  ExcludeColumn  """  
      self.ExcludeLabel:bool = obj["ExcludeLabel"]
      """  ExcludeLabel  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptLinkFieldRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.RptLinkID:str = obj["RptLinkID"]
      """  Report Link ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ZLookupID:str = obj["ZLookupID"]
      """  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  """  
      self.FieldName:str = obj["FieldName"]
      """  field name of the database table. DB Table is defined by  ZDataTable.DBTableName.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptLinkTableRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.RptLinkID:str = obj["RptLinkID"]
      """  Report Link ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ZLookupID:str = obj["ZLookupID"]
      """  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.ForeignRptTableID:str = obj["ForeignRptTableID"]
      """  Foreign Report Table ID  """  
      self.ForeignZTableID:str = obj["ForeignZTableID"]
      """  Foreign zTable ID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptLiteralsRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.LiteralName:str = obj["LiteralName"]
      """  Literal Name  """  
      self.LiteralValue:str = obj["LiteralValue"]
      """  Literal Value  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptRelationFieldRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Report Relation ID  """  
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptRelationRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Report Relation ID  """  
      self.ParentRptTableID:str = obj["ParentRptTableID"]
      """  Parent Report Table ID  """  
      self.ChildRptTableID:str = obj["ChildRptTableID"]
      """  ChildRptTableID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.WhichItem:str = obj["WhichItem"]
      """  Valid values are "each", "first", and "last".  """  
      self.JoinType:str = obj["JoinType"]
      """  "Outer" = outer-join, "" = inner-join  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SeqOrder:int = obj["SeqOrder"]
      """  Sequence Order to dump Relationships on the EDI Flat files.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptTableRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.SeqControl:int = obj["SeqControl"]
      """  Sequence Control  """  
      self.ParentRptTableID:str = obj["ParentRptTableID"]
      """  Parent Report Table ID  """  
      self.PrimaryTable:bool = obj["PrimaryTable"]
      """   Indicates if this is the Primary table of the generated Report Dataset.
Primary table defintions have an additional field, "RptLanguageID". 
The RptLanguageID field is used to link to the RptLabel table.
The RptLabel is not a database table,  it contains the translations for the literals and is present
only in the generated Report Dataset.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemTable:bool = obj["IsSystemTable"]
      """  IsSystemTable  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.EFTHeadCompany:str = obj["EFTHeadCompany"]
      """  EFTHeadCompany  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.TableType:str = obj["TableType"]
      """  DB Table Type  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.DataSourceDescription:str = obj["DataSourceDescription"]
      """  Data Source Description  """  
      self.DataSourceName:str = obj["DataSourceName"]
      """  Data Source Name  """  
      self.IsValidDataSource:bool = obj["IsValidDataSource"]
      """  True when data source is valid and available for current company and user, otherwise is false.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptWhereItemRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.IsConst:bool = obj["IsConst"]
      """  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  """  
      self.ToTableID:str = obj["ToTableID"]
      """  To Table ID  """  
      self.ToSystemCode:str = obj["ToSystemCode"]
      """  ToSystemCode  """  
      self.ToZTableID:str = obj["ToZTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ToFieldName:str = obj["ToFieldName"]
      """  To Field Name  """  
      self.AndOr:str = obj["AndOr"]
      """  And / Or  """  
      self.Neg:bool = obj["Neg"]
      """  Negative indicator  """  
      self.RValue:str = obj["RValue"]
      """  The constant value that will be used to compare against the selected field  """  
      self.NumLeftP:int = obj["NumLeftP"]
      """  Number of Left Parenthesis  """  
      self.NumRightP:int = obj["NumRightP"]
      """  Number of Right Parenthesis  """  
      self.ParentSeq:int = obj["ParentSeq"]
      """  Parent Sequence  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FromToday:bool = obj["FromToday"]
      self.FromTodayValue:int = obj["FromTodayValue"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.RValueDate:str = obj["RValueDate"]
      self.RValueNumber:int = obj["RValueNumber"]
      self.RValueChar:str = obj["RValueChar"]
      """  Constanst value caracter field  """  
      self.RValueBool:bool = obj["RValueBool"]
      """  Constant value Boolean  """  
      self.RValueInt:int = obj["RValueInt"]
      """  Constant Value Integer  """  
      self.FieldType:str = obj["FieldType"]
      """  Field Type  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeDropDownPromptDisplayOrder_input:
   """ Required : 
   ds
   rptDefID
   rptCriteriaSetID
   promptID
   sourceItemID
   targetItemID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      """  Report definition identifier  """  
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      """  Criteria Set identifier  """  
      self.promptID:int = obj["promptID"]
      """  Prompt identifier  """  
      self.sourceItemID:int = obj["sourceItemID"]
      """  Source item ID to change Display Order field  """  
      self.targetItemID:int = obj["targetItemID"]
      """  Target item ID to change Display order field  """  
      pass

class ChangeDropDownPromptDisplayOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CreateRptCriteriaPromptsforSelected_input:
   """ Required : 
   ds
   anyRptCriteriaPromptCrated
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.anyRptCriteriaPromptCrated:bool = obj["anyRptCriteriaPromptCrated"]
      pass

class CreateRptCriteriaPromptsforSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.anyRptCriteriaPromptCrated:bool = obj["anyRptCriteriaPromptCrated"]
      pass

      """  output parameters  """  

class DeleteAllCriteriaSets_input:
   """ Required : 
   ds
   rptDefID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      pass

class DeleteAllCriteriaSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   rptDefID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteElectronicInterface_input:
   """ Required : 
   companyID
   eftHeadUID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.eftHeadUID:int = obj["eftHeadUID"]
      pass

class DeleteElectronicInterface_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class DoesExistsRptCriteriaMappingbyRptTableID_input:
   """ Required : 
   rptDefID
   rptTableID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      pass

class DoesExistsRptCriteriaMappingbyRptTableID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DoesRptCriteriaSetExists_input:
   """ Required : 
   rptDefID
   rptCriteriaSetID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  The report definition identifier.  """  
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      """  ID for the new report criteria set.  """  
      pass

class DoesRptCriteriaSetExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DoesRptExist_input:
   """ Required : 
   rptDefID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  ID for the new report.  """  
      pass

class DoesRptExist_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  `true` if the report exists.  """  
      pass

class DuplicateRptCriteriaSet_input:
   """ Required : 
   sourceRptDefID
   sourceRptCriteriaSetID
   targetRptCriteriaSetID
   targetCriteriaDescription
   """  
   def __init__(self, obj):
      self.sourceRptDefID:str = obj["sourceRptDefID"]
      """  ID of report which contains the criteria set that will be duplicated.  """  
      self.sourceRptCriteriaSetID:str = obj["sourceRptCriteriaSetID"]
      """  ID of criteria set that will be duplicated.  """  
      self.targetRptCriteriaSetID:str = obj["targetRptCriteriaSetID"]
      """  ID for the new criteria set.  """  
      self.targetCriteriaDescription:str = obj["targetCriteriaDescription"]
      """  >Description that will be used for the new criteria set.
            if blank, the source description will be used.  """  
      pass

class DuplicateRptCriteriaSet_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataDefTableset] = obj["returnObj"]
      pass

class DuplicateRpt_input:
   """ Required : 
   sourceRptDefID
   targetRptDefID
   targetRptDescription
   """  
   def __init__(self, obj):
      self.sourceRptDefID:str = obj["sourceRptDefID"]
      """  Id of report that will be duplicated.  """  
      self.targetRptDefID:str = obj["targetRptDefID"]
      """  ID for the new report.  """  
      self.targetRptDescription:str = obj["targetRptDescription"]
      """  Description that will be used for the new report.
            if blank, the source description will be used.  """  
      pass

class DuplicateRpt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataDefTableset] = obj["returnObj"]
      pass

class ExportElectronicInterface_input:
   """ Required : 
   companyID
   eftHeadUID
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.eftHeadUID:int = obj["eftHeadUID"]
      pass

class ExportElectronicInterface_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class ExportReportEx_input:
   """ Required : 
   rptDefId
   exportFileName
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      """  The RptDataDefId to export  """  
      self.exportFileName:str = obj["exportFileName"]
      """  The name of the file to be created  """  
      pass

class ExportReportEx_output:
   def __init__(self, obj):
      pass

class ExportReport_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      """  The RptDefId to export.  """  
      pass

class ExportReport_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The export data.  """  
      pass

class GetBreakTableList_input:
   """ Required : 
   rptDefID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  RptDefID value.  """  
      pass

class GetBreakTableList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BreakTableListTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   rptDefID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_RptDataDefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_RptDataDefTableset] = obj["returnObj"]
      pass

class GetColumnTypeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCriteriaMappingFPList_input:
   """ Required : 
   rptDefID
   rptCriteriaSetID
   mappingType
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      self.mappingType:str = obj["mappingType"]
      pass

class GetCriteriaMappingFPList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptCriteriaMappingFPListTableset] = obj["returnObj"]
      pass

class GetDataDefUsedTables_input:
   """ Required : 
   rptDefID
   onlyDBTables
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  Report Definition ID  """  
      self.onlyDBTables:bool = obj["onlyDBTables"]
      """  Return Only DataBase Tables  """  
      pass

class GetDataDefUsedTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DefUsedTablesTableset] = obj["returnObj"]
      pass

class GetDataFromList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDataSourceType_input:
   """ Required : 
   ds
   rptDefID
   rptTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      pass

class GetDataSourceType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDropDownPromptRows_input:
   """ Required : 
   rptDefID
   rptCriteriaSetID
   promptID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  Report definition identifier.  """  
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      """  Criteria set identifier.  """  
      self.promptID:int = obj["promptID"]
      """  Prompt identifier.  """  
      pass

class GetDropDownPromptRows_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  Down prompt rows in a Data table.  """  
      pass

class GetEICalculators_input:
   """ Required : 
   eFTHeadCompany
   eFTHeadUID
   """  
   def __init__(self, obj):
      self.eFTHeadCompany:str = obj["eFTHeadCompany"]
      self.eFTHeadUID:int = obj["eFTHeadUID"]
      pass

class GetEICalculators_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetEditorTypeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetElectronicInterfaceList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The where clause.  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of the page.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page.  """  
      pass

class GetElectronicInterfaceList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ElectronicInterfacesListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetFieldType_input:
   """ Required : 
   systemCode
   dataTableID
   fieldName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.dataTableID:str = obj["dataTableID"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetFieldType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetFieldsUsedByReportTable_input:
   """ Required : 
   rptDefID
   reportTable
   systemCode
   zDataTableID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      """  Report Definition ID  """  
      self.reportTable:str = obj["reportTable"]
      """  Report table used on the data definition  """  
      self.systemCode:str = obj["systemCode"]
      """  System code of the report table  """  
      self.zDataTableID:str = obj["zDataTableID"]
      """  ZDatatableID of the report table  """  
      pass

class GetFieldsUsedByReportTable_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DefUsedTablesTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_RptDataDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMappingTypeList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewRptCalcField_input:
   """ Required : 
   ds
   rptDefID
   rptTableID
   systemCode
   zdataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      self.systemCode:str = obj["systemCode"]
      self.zdataTableID:str = obj["zdataTableID"]
      pass

class GetNewRptCalcField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptCriteriaFilter_input:
   """ Required : 
   ds
   rptDefID
   rptCriteriaSetID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      pass

class GetNewRptCriteriaFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptCriteriaMapping_input:
   """ Required : 
   ds
   rptDefID
   rptCriteriaSetID
   rptTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      self.rptTableID:str = obj["rptTableID"]
      pass

class GetNewRptCriteriaMapping_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptCriteriaPromptValue_input:
   """ Required : 
   ds
   rptDefID
   rptCriteriaSetID
   promptID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      self.promptID:int = obj["promptID"]
      pass

class GetNewRptCriteriaPromptValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptCriteriaPrompt_input:
   """ Required : 
   ds
   rptDefID
   rptCriteriaSetID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      pass

class GetNewRptCriteriaPrompt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptCriteriaSet_input:
   """ Required : 
   ds
   rptDefID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      pass

class GetNewRptCriteriaSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptDataDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

class GetNewRptDataDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptExclude_input:
   """ Required : 
   ds
   rptDefID
   rptTableID
   systemCode
   zdataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      self.systemCode:str = obj["systemCode"]
      self.zdataTableID:str = obj["zdataTableID"]
      pass

class GetNewRptExclude_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptLinkField_input:
   """ Required : 
   ds
   rptDefID
   rptTableID
   rptLinkID
   systemCode
   zdataTableID
   zlookupID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      self.rptLinkID:str = obj["rptLinkID"]
      self.systemCode:str = obj["systemCode"]
      self.zdataTableID:str = obj["zdataTableID"]
      self.zlookupID:str = obj["zlookupID"]
      pass

class GetNewRptLinkField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptLinkTable_input:
   """ Required : 
   ds
   rptDefID
   rptTableID
   rptLinkID
   systemCode
   zdataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      self.rptLinkID:str = obj["rptLinkID"]
      self.systemCode:str = obj["systemCode"]
      self.zdataTableID:str = obj["zdataTableID"]
      pass

class GetNewRptLinkTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptLiterals_input:
   """ Required : 
   ds
   rptDefID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      pass

class GetNewRptLiterals_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptRelationField_input:
   """ Required : 
   ds
   rptDefID
   relationID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.relationID:str = obj["relationID"]
      pass

class GetNewRptRelationField_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptRelation_input:
   """ Required : 
   ds
   rptDefID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      pass

class GetNewRptRelation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptTableEx_input:
   """ Required : 
   ds
   rptDefID
   dataSourceType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.dataSourceType:str = obj["dataSourceType"]
      pass

class GetNewRptTableEx_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptTable_input:
   """ Required : 
   ds
   rptDefID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      pass

class GetNewRptTable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRptWhereItem_input:
   """ Required : 
   ds
   rptDefID
   rptTableID
   systemCode
   zdataTableID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.rptDefID:str = obj["rptDefID"]
      self.rptTableID:str = obj["rptTableID"]
      self.systemCode:str = obj["systemCode"]
      self.zdataTableID:str = obj["zdataTableID"]
      pass

class GetNewRptWhereItem_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetOperatorList_input:
   """ Required : 
   fieldType
   """  
   def __init__(self, obj):
      self.fieldType:str = obj["fieldType"]
      """  Field Data-Type  """  
      pass

class GetOperatorList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.operatorList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPromptsAndFiltersForRptCriteriaSet_input:
   """ Required : 
   rptDataDef
   rptCriteriaSetID
   """  
   def __init__(self, obj):
      self.rptDataDef:str = obj["rptDataDef"]
      """  Report Data Definition Identifier.  """  
      self.rptCriteriaSetID:str = obj["rptCriteriaSetID"]
      """  Report Criteria Set Identifier.  """  
      pass

class GetPromptsAndFiltersForRptCriteriaSet_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptCriteriaDataTableset] = obj["returnObj"]
      pass

class GetRelationColumnList_input:
   """ Required : 
   rptDefID
   childRptTableID
   parentRptTableID
   """  
   def __init__(self, obj):
      self.rptDefID:str = obj["rptDefID"]
      self.childRptTableID:str = obj["childRptTableID"]
      self.parentRptTableID:str = obj["parentRptTableID"]
      pass

class GetRelationColumnList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RelationColumnListTableset] = obj["returnObj"]
      pass

class GetReportDataSchemaTablesAndFields_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      """  The RptDefID value.  """  
      pass

class GetReportDataSchemaTablesAndFields_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_DefUsedTablesTableset] = obj["returnObj"]
      pass

class GetReportDataSchema_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      """  The RptDefID value.  """  
      pass

class GetReportDataSchema_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      """  The schema for the report data.  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseRptDataDef
   whereClauseRptTable
   whereClauseRptCalcField
   whereClauseRptExclude
   whereClauseRptLinkTable
   whereClauseRptLinkField
   whereClauseRptWhereItem
   whereClauseRptCriteriaSet
   whereClauseRptCriteriaFilter
   whereClauseRptCriteriaMapping
   whereClauseRptCriteriaPrompt
   whereClauseRptCriteriaPromptValue
   whereClauseRptRelation
   whereClauseRptRelationField
   whereClauseRptLiterals
   whereClauseRptDataSourceField
   whereClauseRptDataSourceParameter
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRptDataDef:str = obj["whereClauseRptDataDef"]
      self.whereClauseRptTable:str = obj["whereClauseRptTable"]
      self.whereClauseRptCalcField:str = obj["whereClauseRptCalcField"]
      self.whereClauseRptExclude:str = obj["whereClauseRptExclude"]
      self.whereClauseRptLinkTable:str = obj["whereClauseRptLinkTable"]
      self.whereClauseRptLinkField:str = obj["whereClauseRptLinkField"]
      self.whereClauseRptWhereItem:str = obj["whereClauseRptWhereItem"]
      self.whereClauseRptCriteriaSet:str = obj["whereClauseRptCriteriaSet"]
      self.whereClauseRptCriteriaFilter:str = obj["whereClauseRptCriteriaFilter"]
      self.whereClauseRptCriteriaMapping:str = obj["whereClauseRptCriteriaMapping"]
      self.whereClauseRptCriteriaPrompt:str = obj["whereClauseRptCriteriaPrompt"]
      self.whereClauseRptCriteriaPromptValue:str = obj["whereClauseRptCriteriaPromptValue"]
      self.whereClauseRptRelation:str = obj["whereClauseRptRelation"]
      self.whereClauseRptRelationField:str = obj["whereClauseRptRelationField"]
      self.whereClauseRptLiterals:str = obj["whereClauseRptLiterals"]
      self.whereClauseRptDataSourceField:str = obj["whereClauseRptDataSourceField"]
      self.whereClauseRptDataSourceParameter:str = obj["whereClauseRptDataSourceParameter"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataDefTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRptDataDefList_input:
   """ Required : 
   WhereClause
   ReportID
   PageSize
   AbsolutePage
   """  
   def __init__(self, obj):
      self.WhereClause:str = obj["WhereClause"]
      """  Where clause.  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID.  """  
      self.PageSize:int = obj["PageSize"]
      """  Page size.  """  
      self.AbsolutePage:int = obj["AbsolutePage"]
      """  Absolute page.  """  
      pass

class GetRptDataDefList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_RptDataDefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.MorePages:bool = obj["MorePages"]
      pass

      """  output parameters  """  

class GetSelectLinkTables_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

class GetSelectLinkTables_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SelectLinkDataTableset] = obj["returnObj"]
      pass

class GetTokenList_input:
   """ Required : 
   tokenDataType
   """  
   def __init__(self, obj):
      self.tokenDataType:str = obj["tokenDataType"]
      """  Type of token for which you want the list of valid values.
            Valid Types are; Date, FiscalPeriod, FiscalYear  """  
      pass

class GetTokenList_output:
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

class Ice_Tablesets_BreakTableListTableset:
   def __init__(self, obj):
      self.BreakTable:list[Ice_Tablesets_BreakTableRow] = obj["BreakTable"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BreakTableRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Table name  """  
      self.SystemCode:str = obj["SystemCode"]
      """  System Code  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DefUsedFieldsRow:
   def __init__(self, obj):
      self.FieldName:str = obj["FieldName"]
      """  Name of field used by the Data Definition  """  
      self.TableName:str = obj["TableName"]
      """  Name of table used by the Data Defintion  """  
      self.DataType:str = obj["DataType"]
      """  Field type (character, date, decimal, integer, logical)  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DefUsedTablesRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      """  Name of table used by the Data Defintion  """  
      self.TableType:str = obj["TableType"]
      """  Indicates the type of table (DB, TT, RPT).  """  
      self.LinkTable:bool = obj["LinkTable"]
      """  Flag indicating if this is a Link Table.  """  
      self.Sequence:int = obj["Sequence"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_DefUsedTablesTableset:
   def __init__(self, obj):
      self.DefUsedTables:list[Ice_Tablesets_DefUsedTablesRow] = obj["DefUsedTables"]
      self.DefUsedFields:list[Ice_Tablesets_DefUsedFieldsRow] = obj["DefUsedFields"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ElectronicInterfaceListRow:
   def __init__(self, obj):
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  From ERP.EFTHeadUID  """  
      self.Name:str = obj["Name"]
      """  ERP.EFTHead/Name  """  
      self.Description:str = obj["Description"]
      """  ERP.EFTHead/Description  """  
      self.Type:int = obj["Type"]
      """  ERP.EFTHead/Type  """  
      self.Company:str = obj["Company"]
      """  ERP.EFTHead/Company  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ElectronicInterfacesListTableset:
   def __init__(self, obj):
      self.ElectronicInterfaceList:list[Ice_Tablesets_ElectronicInterfaceListRow] = obj["ElectronicInterfaceList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RelationColumnListRow:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.TableName:str = obj["TableName"]
      self.IsParentTableColumn:bool = obj["IsParentTableColumn"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RelationColumnListTableset:
   def __init__(self, obj):
      self.RelationColumnList:list[Ice_Tablesets_RelationColumnListRow] = obj["RelationColumnList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptCalcFieldRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.FieldName:str = obj["FieldName"]
      """  Name for Calculated Field.  When output to XML they will be written as Calc-fieldname in order to avoid conflicts with other fields in the table.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.DataType:str = obj["DataType"]
      """  Character, Date, Integer, Decimal, Logical  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Field Format  """  
      self.FieldLength:int = obj["FieldLength"]
      """  Field Length  """  
      self.FieldPrecision:int = obj["FieldPrecision"]
      """  Field Precision  """  
      self.DecimalCurDepended:bool = obj["DecimalCurDepended"]
      """  Decimal Currency Dependent  """  
      self.DecimalValueType:str = obj["DecimalValueType"]
      """  Value Type: G - General, C - Cost, P - Price  """  
      self.DecimalCurrencyType:str = obj["DecimalCurrencyType"]
      """  Currency type: O - Own/Base Currency, G - Global Currency, D - Currency from Document  """  
      self.DecimalCurCodeField:str = obj["DecimalCurCodeField"]
      """  Decimal Currency code  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the Business use of the Field  """  
      self.ZFieldName:str = obj["ZFieldName"]
      """  Field Name from zdatatable  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptCriteriaDataTableset:
   def __init__(self, obj):
      self.RptDataDef:list[Ice_Tablesets_RptDataDefRow] = obj["RptDataDef"]
      self.RptCriteriaFilter:list[Ice_Tablesets_RptCriteriaFilterRow] = obj["RptCriteriaFilter"]
      self.RptCriteriaPrompt:list[Ice_Tablesets_RptCriteriaPromptRow] = obj["RptCriteriaPrompt"]
      self.RptCriteriaSet:list[Ice_Tablesets_RptCriteriaSetRow] = obj["RptCriteriaSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptCriteriaFilterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.FilterID:int = obj["FilterID"]
      """  FilterID  """  
      self.FilterName:str = obj["FilterName"]
      """  FilterName  """  
      self.AdapterName:str = obj["AdapterName"]
      """  AdapterName  """  
      self.LookupField:str = obj["LookupField"]
      """  LookupField  """  
      self.FilterLabel:str = obj["FilterLabel"]
      """  FilterLabel  """  
      self.TabLabel:str = obj["TabLabel"]
      """  TabLabel  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  EpiGuid  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  DisplayOrder  """  
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

class Ice_Tablesets_RptCriteriaMappingFPListRow:
   def __init__(self, obj):
      self.ID:str = obj["ID"]
      self.Name:str = obj["Name"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptCriteriaMappingFPListTableset:
   def __init__(self, obj):
      self.RptCriteriaMappingFPList:list[Ice_Tablesets_RptCriteriaMappingFPListRow] = obj["RptCriteriaMappingFPList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptCriteriaMappingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  RptTableID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.FilterID:int = obj["FilterID"]
      """  FilterID  """  
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

class Ice_Tablesets_RptCriteriaPromptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.PromptName:str = obj["PromptName"]
      """  PromptName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Label:str = obj["Label"]
      """  Label  """  
      self.DefaultValue:str = obj["DefaultValue"]
      """  DefaultValue  """  
      self.EpiGuid:str = obj["EpiGuid"]
      """  EpiGuid  """  
      self.IsConstant:bool = obj["IsConstant"]
      """  IsConstant  """  
      self.ConstantValue:str = obj["ConstantValue"]
      """  ConstantValue  """  
      self.IsVisible:bool = obj["IsVisible"]
      """  IsVisible  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  DisplayOrder  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EditorType:str = obj["EditorType"]
      """  EditorType  """  
      self.DataFrom:str = obj["DataFrom"]
      """  DataFrom  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.DisplayColumn:str = obj["DisplayColumn"]
      """  DisplayColumn  """  
      self.ValueColumn:str = obj["ValueColumn"]
      """  ValueColumn  """  
      self.EFTHeadCompany:str = obj["EFTHeadCompany"]
      """  EFTHeadCompany  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.IsEmptyString:bool = obj["IsEmptyString"]
      """  Use an empty string on this column, instead of null.  """  
      self.EIName:str = obj["EIName"]
      self.EIDescription:str = obj["EIDescription"]
      self.DefaultValueInt:int = obj["DefaultValueInt"]
      self.DefaultValueNum:int = obj["DefaultValueNum"]
      self.DefaultValueDatetime:str = obj["DefaultValueDatetime"]
      self.IsDynamic:bool = obj["IsDynamic"]
      self.DefaultValueBit:bool = obj["DefaultValueBit"]
      self.ConstantValueBit:bool = obj["ConstantValueBit"]
      self.ConstantValueDatetime:str = obj["ConstantValueDatetime"]
      self.ConstantValueNum:int = obj["ConstantValueNum"]
      self.ConstantValueInt:int = obj["ConstantValueInt"]
      self.UseTypedValues:bool = obj["UseTypedValues"]
      self.DefaultValueDatetimeDynamic:str = obj["DefaultValueDatetimeDynamic"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptCriteriaPromptValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.ItemID:int = obj["ItemID"]
      """  ItemID  """  
      self.ItemValue:str = obj["ItemValue"]
      """  ItemValue  """  
      self.ItemDescription:str = obj["ItemDescription"]
      """  ItemDescription  """  
      self.DisplayOrder:int = obj["DisplayOrder"]
      """  DisplayOrder  """  
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

class Ice_Tablesets_RptCriteriaSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  IsDefault  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataDefListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Data Definition Description  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  """  
      self.DuplicateOf:str = obj["DuplicateOf"]
      """  Used to identify which data definition was used for duplication.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DynamicReport:bool = obj["DynamicReport"]
      """  Flag to indicate Dynamic Report  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataDefListTableset:
   def __init__(self, obj):
      self.RptDataDefList:list[Ice_Tablesets_RptDataDefListRow] = obj["RptDataDefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptDataDefRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Data Definition Description  """  
      self.SystemRpt:bool = obj["SystemRpt"]
      """   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  """  
      self.DuplicateOf:str = obj["DuplicateOf"]
      """  Used to identify which data definition was used for duplication.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.PrimaryTable:str = obj["PrimaryTable"]
      """  PrimaryTable  """  
      self.PrimaryKey1:str = obj["PrimaryKey1"]
      """  PrimaryKey1  """  
      self.PrimaryKey2:str = obj["PrimaryKey2"]
      """  PrimaryKey2  """  
      self.UseMultipleCriteria:bool = obj["UseMultipleCriteria"]
      """  UseMultipleCriteria  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataDefTableset:
   def __init__(self, obj):
      self.RptDataDef:list[Ice_Tablesets_RptDataDefRow] = obj["RptDataDef"]
      self.RptTable:list[Ice_Tablesets_RptTableRow] = obj["RptTable"]
      self.RptCalcField:list[Ice_Tablesets_RptCalcFieldRow] = obj["RptCalcField"]
      self.RptExclude:list[Ice_Tablesets_RptExcludeRow] = obj["RptExclude"]
      self.RptLinkTable:list[Ice_Tablesets_RptLinkTableRow] = obj["RptLinkTable"]
      self.RptLinkField:list[Ice_Tablesets_RptLinkFieldRow] = obj["RptLinkField"]
      self.RptWhereItem:list[Ice_Tablesets_RptWhereItemRow] = obj["RptWhereItem"]
      self.RptCriteriaSet:list[Ice_Tablesets_RptCriteriaSetRow] = obj["RptCriteriaSet"]
      self.RptCriteriaFilter:list[Ice_Tablesets_RptCriteriaFilterRow] = obj["RptCriteriaFilter"]
      self.RptCriteriaMapping:list[Ice_Tablesets_RptCriteriaMappingRow] = obj["RptCriteriaMapping"]
      self.RptCriteriaPrompt:list[Ice_Tablesets_RptCriteriaPromptRow] = obj["RptCriteriaPrompt"]
      self.RptCriteriaPromptValue:list[Ice_Tablesets_RptCriteriaPromptValueRow] = obj["RptCriteriaPromptValue"]
      self.RptRelation:list[Ice_Tablesets_RptRelationRow] = obj["RptRelation"]
      self.RptRelationField:list[Ice_Tablesets_RptRelationFieldRow] = obj["RptRelationField"]
      self.RptLiterals:list[Ice_Tablesets_RptLiteralsRow] = obj["RptLiterals"]
      self.RptDataSourceField:list[Ice_Tablesets_RptDataSourceFieldRow] = obj["RptDataSourceField"]
      self.RptDataSourceParameter:list[Ice_Tablesets_RptDataSourceParameterRow] = obj["RptDataSourceParameter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_RptDataSourceFieldRow:
   def __init__(self, obj):
      self.FieldName:str = obj["FieldName"]
      self.QueryID:str = obj["QueryID"]
      self.DBTableName:str = obj["DBTableName"]
      """  Database Table Name  """  
      self.DBFieldName:str = obj["DBFieldName"]
      """  Database Field Name  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.LikeDataFieldName:str = obj["LikeDataFieldName"]
      """  Like Data Field Name  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Field Label  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptDataSourceParameterRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  RptDefID  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  RptTableID  """  
      self.ParameterID:str = obj["ParameterID"]
      """  ParameterID  """  
      self.PromptID:int = obj["PromptID"]
      """  PromptID  """  
      self.FilterID:int = obj["FilterID"]
      """  FilterID  """  
      self.Type:str = obj["Type"]
      """  Data source type.  """  
      self.ParamDataType:str = obj["ParamDataType"]
      """  Parameter data type.  """  
      self.IsMandatory:bool = obj["IsMandatory"]
      """  Flag to inditate if parameter is mandatory or not.  """  
      self.SkipIfEmpty:bool = obj["SkipIfEmpty"]
      self.ControlType:str = obj["ControlType"]
      """  Shows control type related to parameter: Prompt or Filter.  """  
      self.ControlName:str = obj["ControlName"]
      self.ControlDataType:str = obj["ControlDataType"]
      self.QueryEI:str = obj["QueryEI"]
      self.SysRevID:int = obj["SysRevID"]
      self.Selection:bool = obj["Selection"]
      self.SourceControlType:str = obj["SourceControlType"]
      """  Control type in the source of the parameter.  """  
      self.ControlNameDesc:str = obj["ControlNameDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptExcludeRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ZFieldName:str = obj["ZFieldName"]
      """  zField Name  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExcludeColumn:bool = obj["ExcludeColumn"]
      """  ExcludeColumn  """  
      self.ExcludeLabel:bool = obj["ExcludeLabel"]
      """  ExcludeLabel  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptLinkFieldRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.RptLinkID:str = obj["RptLinkID"]
      """  Report Link ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ZLookupID:str = obj["ZLookupID"]
      """  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  """  
      self.FieldName:str = obj["FieldName"]
      """  field name of the database table. DB Table is defined by  ZDataTable.DBTableName.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptLinkTableRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  Report Table ID  """  
      self.RptLinkID:str = obj["RptLinkID"]
      """  Report Link ID  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ZLookupID:str = obj["ZLookupID"]
      """  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.ForeignRptTableID:str = obj["ForeignRptTableID"]
      """  Foreign Report Table ID  """  
      self.ForeignZTableID:str = obj["ForeignZTableID"]
      """  Foreign zTable ID  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptLiteralsRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.LiteralName:str = obj["LiteralName"]
      """  Literal Name  """  
      self.LiteralValue:str = obj["LiteralValue"]
      """  Literal Value  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptRelationFieldRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Report Relation ID  """  
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
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptRelationRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RelationID:str = obj["RelationID"]
      """  Report Relation ID  """  
      self.ParentRptTableID:str = obj["ParentRptTableID"]
      """  Parent Report Table ID  """  
      self.ChildRptTableID:str = obj["ChildRptTableID"]
      """  ChildRptTableID  """  
      self.KeyID:str = obj["KeyID"]
      """  Key ID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.WhichItem:str = obj["WhichItem"]
      """  Valid values are "each", "first", and "last".  """  
      self.JoinType:str = obj["JoinType"]
      """  "Outer" = outer-join, "" = inner-join  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SeqOrder:int = obj["SeqOrder"]
      """  Sequence Order to dump Relationships on the EDI Flat files.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptTableRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.SeqControl:int = obj["SeqControl"]
      """  Sequence Control  """  
      self.ParentRptTableID:str = obj["ParentRptTableID"]
      """  Parent Report Table ID  """  
      self.PrimaryTable:bool = obj["PrimaryTable"]
      """   Indicates if this is the Primary table of the generated Report Dataset.
Primary table defintions have an additional field, "RptLanguageID". 
The RptLanguageID field is used to link to the RptLabel table.
The RptLabel is not a database table,  it contains the translations for the literals and is present
only in the generated Report Dataset.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemTable:bool = obj["IsSystemTable"]
      """  IsSystemTable  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID  """  
      self.EFTHeadCompany:str = obj["EFTHeadCompany"]
      """  EFTHeadCompany  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  EFTHeadUID  """  
      self.TableType:str = obj["TableType"]
      """  DB Table Type  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.DataSourceDescription:str = obj["DataSourceDescription"]
      """  Data Source Description  """  
      self.DataSourceName:str = obj["DataSourceName"]
      """  Data Source Name  """  
      self.IsValidDataSource:bool = obj["IsValidDataSource"]
      """  True when data source is valid and available for current company and user, otherwise is false.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_RptWhereItemRow:
   def __init__(self, obj):
      self.RptDefID:str = obj["RptDefID"]
      """  Report Data Definition ID  """  
      self.RptTableID:str = obj["RptTableID"]
      """  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  """  
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ZDataTableID:str = obj["ZDataTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.Seq:int = obj["Seq"]
      """  Sequence  """  
      self.FieldName:str = obj["FieldName"]
      """  Field Name  """  
      self.CompOp:str = obj["CompOp"]
      """  Operator to use for relation between left value and right value.  """  
      self.IsConst:bool = obj["IsConst"]
      """  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  """  
      self.ToTableID:str = obj["ToTableID"]
      """  To Table ID  """  
      self.ToSystemCode:str = obj["ToSystemCode"]
      """  ToSystemCode  """  
      self.ToZTableID:str = obj["ToZTableID"]
      """  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  """  
      self.ToFieldName:str = obj["ToFieldName"]
      """  To Field Name  """  
      self.AndOr:str = obj["AndOr"]
      """  And / Or  """  
      self.Neg:bool = obj["Neg"]
      """  Negative indicator  """  
      self.RValue:str = obj["RValue"]
      """  The constant value that will be used to compare against the selected field  """  
      self.NumLeftP:int = obj["NumLeftP"]
      """  Number of Left Parenthesis  """  
      self.NumRightP:int = obj["NumRightP"]
      """  Number of Right Parenthesis  """  
      self.ParentSeq:int = obj["ParentSeq"]
      """  Parent Sequence  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FromToday:bool = obj["FromToday"]
      self.FromTodayValue:int = obj["FromTodayValue"]
      self.LeftP:str = obj["LeftP"]
      self.RightP:str = obj["RightP"]
      self.RValueDate:str = obj["RValueDate"]
      self.RValueNumber:int = obj["RValueNumber"]
      self.RValueChar:str = obj["RValueChar"]
      """  Constanst value caracter field  """  
      self.RValueBool:bool = obj["RValueBool"]
      """  Constant value Boolean  """  
      self.RValueInt:int = obj["RValueInt"]
      """  Constant Value Integer  """  
      self.FieldType:str = obj["FieldType"]
      """  Field Type  """  
      self.DataSourceType:str = obj["DataSourceType"]
      """  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SelectLinkDataTableset:
   def __init__(self, obj):
      self.SelectLinkTable:list[Ice_Tablesets_SelectLinkTableRow] = obj["SelectLinkTable"]
      self.SelectLinkField:list[Ice_Tablesets_SelectLinkFieldRow] = obj["SelectLinkField"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SelectLinkFieldRow:
   def __init__(self, obj):
      self.FieldName:str = obj["FieldName"]
      self.LookupID:str = obj["LookupID"]
      self.RowSelected:bool = obj["RowSelected"]
      self.RptTableID:str = obj["RptTableID"]
      self.SystemCode:str = obj["SystemCode"]
      self.ZDataTableID:str = obj["ZDataTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SelectLinkTableRow:
   def __init__(self, obj):
      self.LookupID:str = obj["LookupID"]
      """  Lookup ID from ZLookupLink  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.RptTableID:str = obj["RptTableID"]
      self.SystemCode:str = obj["SystemCode"]
      self.ZDataTableID:str = obj["ZDataTableID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtRptDataDefTableset:
   def __init__(self, obj):
      self.RptDataDef:list[Ice_Tablesets_RptDataDefRow] = obj["RptDataDef"]
      self.RptTable:list[Ice_Tablesets_RptTableRow] = obj["RptTable"]
      self.RptCalcField:list[Ice_Tablesets_RptCalcFieldRow] = obj["RptCalcField"]
      self.RptExclude:list[Ice_Tablesets_RptExcludeRow] = obj["RptExclude"]
      self.RptLinkTable:list[Ice_Tablesets_RptLinkTableRow] = obj["RptLinkTable"]
      self.RptLinkField:list[Ice_Tablesets_RptLinkFieldRow] = obj["RptLinkField"]
      self.RptWhereItem:list[Ice_Tablesets_RptWhereItemRow] = obj["RptWhereItem"]
      self.RptCriteriaSet:list[Ice_Tablesets_RptCriteriaSetRow] = obj["RptCriteriaSet"]
      self.RptCriteriaFilter:list[Ice_Tablesets_RptCriteriaFilterRow] = obj["RptCriteriaFilter"]
      self.RptCriteriaMapping:list[Ice_Tablesets_RptCriteriaMappingRow] = obj["RptCriteriaMapping"]
      self.RptCriteriaPrompt:list[Ice_Tablesets_RptCriteriaPromptRow] = obj["RptCriteriaPrompt"]
      self.RptCriteriaPromptValue:list[Ice_Tablesets_RptCriteriaPromptValueRow] = obj["RptCriteriaPromptValue"]
      self.RptRelation:list[Ice_Tablesets_RptRelationRow] = obj["RptRelation"]
      self.RptRelationField:list[Ice_Tablesets_RptRelationFieldRow] = obj["RptRelationField"]
      self.RptLiterals:list[Ice_Tablesets_RptLiteralsRow] = obj["RptLiterals"]
      self.RptDataSourceField:list[Ice_Tablesets_RptDataSourceFieldRow] = obj["RptDataSourceField"]
      self.RptDataSourceParameter:list[Ice_Tablesets_RptDataSourceParameterRow] = obj["RptDataSourceParameter"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class ImportElectronicInterface_input:
   """ Required : 
   version
   data
   """  
   def __init__(self, obj):
      self.version:str = obj["version"]
      self.data      #schema had no properties on an object.
      pass

class ImportElectronicInterface_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class ImportReportEx_input:
   """ Required : 
   importFileName
   """  
   def __init__(self, obj):
      self.importFileName:str = obj["importFileName"]
      """  The file name with report data to import.  """  
      pass

class ImportReportEx_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The RDDs name of imported file.  """  
      pass

class ImportReport_input:
   """ Required : 
   reportData
   """  
   def __init__(self, obj):
      self.reportData:str = obj["reportData"]
      """  The report data to import.  """  
      pass

class ImportReport_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The RDDs imported.  """  
      pass

class OnChangeQueryID_input:
   """ Required : 
   ds
   queryID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.queryID:str = obj["queryID"]
      pass

class OnChangeQueryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      self.queryID:str = obj["parameters"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtRptDataDefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtRptDataDefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_RptDataDefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBAQDataSource_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      pass

class ValidateBAQDataSource_output:
   def __init__(self, obj):
      pass

class ValidateRptLabels_input:
   """ Required : 
   rptDefId
   """  
   def __init__(self, obj):
      self.rptDefId:str = obj["rptDefId"]
      pass

class ValidateRptLabels_output:
   def __init__(self, obj):
      pass

