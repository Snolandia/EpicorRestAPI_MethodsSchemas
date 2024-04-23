import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DynAttrValueSetSvc
# Description: Dynamic Attributes Set core service
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValueSets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValueSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrValueSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValueSets_Company_AttributeSetID(Company, AttributeSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrValueSet item
   Description: Calls GetByID to retrieve the DynAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrValueSets_Company_AttributeSetID(Company, AttributeSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrValueSet for the service
   Description: Calls UpdateExt to update DynAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrValueSets_Company_AttributeSetID(Company, AttributeSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrValueSet item
   Description: Call UpdateExt to delete DynAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValueSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValueSets_Company_AttributeSetID_DynAttrValueSetLangDescs(Company, AttributeSetID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DynAttrValueSetLangDescs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrValueSetLangDescs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetLangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")/DynAttrValueSetLangDescs",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValueSets_Company_AttributeSetID_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company, AttributeSetID, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrValueSetLangDesc item
   Description: Calls GetByID to retrieve the DynAttrValueSetLangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValueSetLangDesc1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSets(" + Company + "," + AttributeSetID + ")/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValueSetLangDescs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrValueSetLangDescs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValueSetLangDescs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetLangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrValueSetLangDescs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValueSetLangDescs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company, AttributeSetID, LangNameID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrValueSetLangDesc item
   Description: Calls GetByID to retrieve the DynAttrValueSetLangDesc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValueSetLangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company, AttributeSetID, LangNameID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrValueSetLangDesc for the service
   Description: Calls UpdateExt to update DynAttrValueSetLangDesc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValueSetLangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueSetLangDescRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrValueSetLangDescs_Company_AttributeSetID_LangNameID(Company, AttributeSetID, LangNameID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrValueSetLangDesc item
   Description: Call UpdateExt to delete DynAttrValueSetLangDesc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValueSetLangDesc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttributeSetID: Desc: AttributeSetID   Required: True
      :param LangNameID: Desc: LangNameID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValueSetLangDescs(" + Company + "," + AttributeSetID + "," + LangNameID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company, RelatedToSchemaName, RelatedToTableName, RelatedToSysRowID, AttrClassID, AttributeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrValue item
   Description: Calls GetByID to retrieve the DynAttrValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToTableName: Desc: RelatedToTableName   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company, RelatedToSchemaName, RelatedToTableName, RelatedToSysRowID, AttrClassID, AttributeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrValue for the service
   Description: Calls UpdateExt to update DynAttrValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToTableName: Desc: RelatedToTableName   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrValueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrValues_Company_RelatedToSchemaName_RelatedToTableName_RelatedToSysRowID_AttrClassID_AttributeID(Company, RelatedToSchemaName, RelatedToTableName, RelatedToSysRowID, AttrClassID, AttributeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrValue item
   Description: Call UpdateExt to delete DynAttrValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrValue
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToTableName: Desc: RelatedToTableName   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrValues(" + Company + "," + RelatedToSchemaName + "," + RelatedToTableName + "," + RelatedToSysRowID + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlComboValues(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtlComboValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlComboValues
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlComboValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrClassDtlComboValues(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlComboValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlComboValues_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlComboValue item
   Description: Calls GetByID to retrieve the DynAttrClassDtlComboValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlComboValue
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrClassDtlComboValues_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrClassDtlComboValue for the service
   Description: Calls UpdateExt to update DynAttrClassDtlComboValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlComboValue
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlComboValuesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrClassDtlComboValues_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrClassDtlComboValue item
   Description: Call UpdateExt to delete DynAttrClassDtlComboValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlComboValue
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/DynAttrClassDtlComboValues(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrValueSetListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynAttrValueSet, whereClauseDynAttrValue, whereClauseDynAttrValueSetLangDesc, whereClauseDynAttrClassDtlComboValues, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDynAttrValueSet=" + whereClauseDynAttrValueSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrValue=" + whereClauseDynAttrValue
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrValueSetLangDesc=" + whereClauseDynAttrValueSetLangDesc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrClassDtlComboValues=" + whereClauseDynAttrClassDtlComboValues
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(attributeSetID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "attributeSetID=" + attributeSetID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAttributeValuesRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAttributeValuesRow
   Description: Gets new inverted row of a full set of DynAttrValue, returns both types of attributes: dynamic attributes, inventory dynamic attributes.
Method is dependent on a populated InventoryDynAttrValueSummaryRow with minimum populated values: AttrClassID, RelatedToSchemaName, RelatedToTableName.
If used for Inventory Attributes then either RelatedToSysRowID or PartNum must be supplied.
   OperationID: GetNewAttributeValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAttributeValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAttributeValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAttributeValuesRowWithOutDynamicMetaDataDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAttributeValuesRowWithOutDynamicMetaDataDS
   Description: Gets new inverted row of a full set of DynAttrValue, returns both types of attributes: dynamic attributes, inventory dynamic attributes.
Method is dependent on a populated InventoryDynAttrValueSummaryRow with minimum populated values: AttrClassID, RelatedToSchemaName, RelatedToTableName.
If used for Inventory Attributes then either RelatedToSysRowID or PartNum must be supplied.
   OperationID: GetNewAttributeValuesRowWithOutDynamicMetaDataDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAttributeValuesRowWithOutDynamicMetaDataDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAttributeValuesRowWithOutDynamicMetaDataDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInventoryDynAttrValuesRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInventoryDynAttrValuesRow
   Description: Used with Inventory Attributes Entry to create full set of DynAttrValue as inverted table.
   OperationID: GetNewInventoryDynAttrValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInventoryDynAttrValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInventoryDynAttrValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInventoryDynAttrValueSummary(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInventoryDynAttrValueSummary
   Description: Gets new InventoryDynAttrValueSummary that can be used in later request for any additional parameters required.  Helper for summary totals.
   OperationID: GetNewInventoryDynAttrValueSummary
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInventoryDynAttrValueSummary_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInventoryDynAttrValueSummary_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDDynAttrValueSetDataSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDDynAttrValueSetDataSet
   Description: Returns the DynAttrValueSetTableset as an inverted dynamic Dataset
   OperationID: GetByIDDynAttrValueSetDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDDynAttrValueSetDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDDynAttrValueSetDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrValueSetDataSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrValueSetDataSet
   Description: Used with Dynamic Attribute Set Maintenance to create full dataset with all needed DynAttrValue columns.  The DynAttrValue rows have been inverted to columns.
For new sets the whole set most be created at the same time, a valid attribute class ID must be supplied.
   OperationID: GetNewDynAttrValueSetDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSetDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSetDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrValueSetTableset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrValueSetTableset
   Description: Used with Dynamic Attribute Set Maintenance to create full dataset with all needed DynAttrValue rows.
For new sets the whole set most be created at the same time, a valid attribute class ID must be supplied.
   OperationID: GetNewDynAttrValueSetTableset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSetTableset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSetTableset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFullDynAttrValueSetDataSetByAttrClassID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFullDynAttrValueSetDataSetByAttrClassID
   Description: Returns dynamically built DataSet for all DynAttrValueSet for given attribute class.
   OperationID: GetFullDynAttrValueSetDataSetByAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullDynAttrValueSetDataSetByAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullDynAttrValueSetDataSetByAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFullDynAttrValueSetDataSetByList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFullDynAttrValueSetDataSetByList
   Description: Returns dynamically built DataSet for all DynAttrValueSet for given AttributeSetID list.
   OperationID: GetFullDynAttrValueSetDataSetByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullDynAttrValueSetDataSetByList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullDynAttrValueSetDataSetByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DynAttrValueColumnChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DynAttrValueColumnChanging
   Description: Column value change for dynamic attribute.
   OperationID: DynAttrValueColumnChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DynAttrValueColumnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DynAttrValueColumnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDynAttrValueColumn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDynAttrValueColumn
   Description: Column value change for dynamic attribute.
This method does NOT support BPM.
   OperationID: OnChangeDynAttrValueColumn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDynAttrValueColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDynAttrValueColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttributeValuesColumnObject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttributeValuesColumnObject
   Description: Column value change for dynamic attribute where we are passing the dataset as an object such that we can apply the schema attributes
and avoid data type inferrance causing passed decimal values to become Integers.
This method does NOT support BPM, write BPM against OnChangeDynAttrValueColumn.
This method used by Dynamic Attribute Value Entry.
   OperationID: OnChangeAttributeValuesColumnObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeValuesColumnObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeValuesColumnObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDynAttrValueSetColumnObject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDynAttrValueSetColumnObject
   Description: Column value change for dynamic attribute where we are passing the dataset as an object such that we can apply the schema attributes
and avoid data type inferrance causing passed decimal values to become Integers.
This method does NOT support BPM, write BPM against OnChangeDynAttrValueColumn.
This method used by Dynamic Attribute Value Set Maintenance.
   OperationID: OnChangeDynAttrValueSetColumnObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDynAttrValueSetColumnObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDynAttrValueSetColumnObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributeValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributeValues
   Description: Returns dataset of all related attribute values.
This method is used to return both types of attributes: dynamic attributes, inventory dynamic attributes.
   OperationID: GetAttributeValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributeValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAttributeValuesWithOutDynamicMetaDataDS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAttributeValuesWithOutDynamicMetaDataDS
   Description: Returns dataset of all related attribute values.
This method is used to return both types of attributes: dynamic attributes, inventory dynamic attributes.
   OperationID: GetAttributeValuesWithOutDynamicMetaDataDS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAttributeValuesWithOutDynamicMetaDataDS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAttributeValuesWithOutDynamicMetaDataDS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryDynAttrValueParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryDynAttrValueParams
   Description: Returns dataset of inventory detail information and all related inventory dynamic attribute values.
   OperationID: GetInventoryDynAttrValueParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryDynAttrValueParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryDynAttrValueParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultsFromSelectedTemplate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultsFromSelectedTemplate
   Description: Defaults attribute values from the selected template attribute set
   OperationID: GetDefaultsFromSelectedTemplate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultsFromSelectedTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsFromSelectedTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshDynAttrValuesRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshDynAttrValuesRow
   Description: Refreshes inverted dynamic attribute row
   OperationID: RefreshDynAttrValuesRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshDynAttrValuesRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshDynAttrValuesRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MasterUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MasterUpdate
   Description: Update which takes a whole dataset and first tries to find existing attribute set based on exact match of all attribute values and if found returns the id.
If one is not found will create the parent DynAttrValueSet and all child DynAttrValue records.
   OperationID: MasterUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MasterUpdateFromMultiCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MasterUpdateFromMultiCompany
   Description: To be called from Multi-Company (Direct) Server Process exclusively
Update which takes a whole dataset and first tries to find existing attribute set based on exact match of all attribute values.
If an existing attribute set is not found, one will be created with the parent DynAttrValueSet and all child DynAttrValue records.
Regardless whether an existing attribute set is found or a new one is created, the related AttributeSetID is returned.
   OperationID: MasterUpdateFromMultiCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterUpdateFromMultiCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterUpdateFromMultiCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MasterUpdateDynAttrValueSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MasterUpdateDynAttrValueSet
   Description: Update which takes a whole dataset and first tries to find existing attribute set based on exact match of all attribute values.
If an existing attribute set is not found, one will be created with the parent DynAttrValueSet and all child DynAttrValue records.
Regardless whether an existing attribute set is found or a new one is created, the related AttributeSetID is returned.
Set will be marked as Active and HasBeenUsed.
   OperationID: MasterUpdateDynAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterUpdateDynAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterUpdateDynAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDynAttrValueSetDataSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDynAttrValueSetDataSet
   Description: Update Dynamic Attribute Value Set using a dynamically built DataTable
   OperationID: UpdateDynAttrValueSetDataSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynAttrValueSetDataSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynAttrValueSetDataSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDynAttrValueSetDataSetObject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDynAttrValueSetDataSetObject
   Description: Update Dynamic Attribute Value Set using a dynamically built DataTable
Passing dataset as an object such that we can apply the dynamic schema attributes and void dataType inferrance causing decimal values to become integers
   OperationID: UpdateDynAttrValueSetDataSetObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDynAttrValueSetDataSetObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDynAttrValueSetDataSetObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAttributeValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeValues
   Description: Update dynamic attribute values using a dynamically built inverted DataTable
This method is used to modify both types of attributes: dynamic attributes, inventory dynamic attributes.
   OperationID: UpdateAttributeValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAttributeValuesObject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeValuesObject
   Description: Update dynamic attribute values using a dynamically built inverted DataTable
This method is used to modify both types of attributes: dynamic attributes, inventory dynamic attributes.
Passing dataset as an object such that we can apply the dynamic schema attributes and void dataType inferrance causing decimal values to become integers
   OperationID: UpdateAttributeValuesObject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeValuesObject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeValuesObject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDynAttrValueSetPlanningKeys(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDynAttrValueSetPlanningKeys
   Description: Returns PlanningAttributeSetSeq and PlanningAttributeSetHash based on attribute values
   OperationID: GetDynAttrValueSetPlanningKeys
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDynAttrValueSetPlanningKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDynAttrValueSetPlanningKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateEntityAttributeSetFromConfigurator(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateEntityAttributeSetFromConfigurator
   Description: Updates the target entity attribute set from a product configuration.
   OperationID: UpdateEntityAttributeSetFromConfigurator
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateEntityAttributeSetFromConfigurator_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateEntityAttributeSetFromConfigurator_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateInventoryAttributes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateInventoryAttributes
   Description: Updates attribute set and line detail using dynamically built DataTable
   OperationID: UpdateInventoryAttributes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateInventoryAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateInventoryAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AssignDataFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AssignDataFields
   Description: Assigns all data fields for related data type and perform validation on the field value.
   OperationID: AssignDataFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AssignDataFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignDataFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAttributeChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAttributeChange
   Description: Method to return message if attributes or qty don't match linked SO on PO for BTO sales order.
   OperationID: CheckAttributeChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAttributeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAttributeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateSalesOrderComponentAttribute(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateSalesOrderComponentAttribute
   Description: Method to update the Quantity per Kit if the Quantity is modified in Attribute screen for Sales Kit Components in Sales Order.
   OperationID: UpdateSalesOrderComponentAttribute
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateSalesOrderComponentAttribute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSalesOrderComponentAttribute_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShortDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShortDescription
   Description: Used to validate a new attribute set based on AttrClassIS and ShortDescription.
This is only used by the UI when creating new set and not used when creating by an inventory transaction.
   OperationID: ValidateShortDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShortDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShortDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateUniqueDynAttrValueSetByShortDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateUniqueDynAttrValueSetByShortDescription
   Description: Validates and returns the AttributeSetID if unique set based on short description
   OperationID: ValidateUniqueDynAttrValueSetByShortDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateUniqueDynAttrValueSetByShortDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateUniqueDynAttrValueSetByShortDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrValueSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrValue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrValueSetLangDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrValueSetLangDesc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrValueSetLangDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrValueSetLangDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrValueSetLangDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrValueSetSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlComboValuesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassDtlComboValuesRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrValueRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetLangDescRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrValueSetLangDescRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrValueSetListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrValueSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrValueSetRow] = obj["value"]
      pass

class Erp_Tablesets_DynAttrClassDtlComboValuesRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeID:str = obj["AttributeID"]
      self.Code:str = obj["Code"]
      self.Description:str = obj["Description"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.DataCharacter:str = obj["DataCharacter"]
      """  Character Data.  """  
      self.DataDate:str = obj["DataDate"]
      """  Date Data.  """  
      self.DataDecimal:int = obj["DataDecimal"]
      """  Decimal Data.  """  
      self.DataInteger:int = obj["DataInteger"]
      """  Integer Data.  """  
      self.DataLogical:bool = obj["DataLogical"]
      """  Logical Data.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicates this value is a result of a calculation.  """  
      self.IsActual:bool = obj["IsActual"]
      """  Used for planning to indicates for the set that this was the Actual quantity at that point in time.  """  
      self.FieldValue:str = obj["FieldValue"]
      self.TransportValue:str = obj["TransportValue"]
      self.Active:bool = obj["Active"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.HasBeenVerified:bool = obj["HasBeenVerified"]
      """  System controlled to validate all dynamic attribute values against the set hash key.  If the value has been verified it will not perform the validation again.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this calculated field will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  Controlled by setup on attribute detail in Dynamic Attribute Class Maintenance.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetLangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID.  """  
      self.Description:str = obj["Description"]
      """  Language Description for Attribute Set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  Language Short Description for Attribute Set.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Description:str = obj["Description"]
      """  Description of values in set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Description:str = obj["Description"]
      """  Description of values in set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeSetHash:str = obj["AttributeSetHash"]
      """  Hash key of Attribute IDs and values (excluding calculated attributes), and Full Expression.  """  
      self.Active:bool = obj["Active"]
      """  Set to true when the user has determined that the Attribute Set is active.  """  
      self.HasBeenUsed:bool = obj["HasBeenUsed"]
      """  Set to true with the system has determined that the Attribute Set has been used, indicating that it cannot be modified except for the user-defined short description.  """  
      self.ExpressionResultQty:int = obj["ExpressionResultQty"]
      """  Result quantity calculated from a user created expression.  """  
      self.ExpressionResultUOM:str = obj["ExpressionResultUOM"]
      """  The UOM related to the Expression Result Qty.  """  
      self.FullExpression:str = obj["FullExpression"]
      """  Full user maintained expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      """  The unique identifier of the Dynamic Attribute Planning Set.  """  
      self.PlanningAttributeSetHash:str = obj["PlanningAttributeSetHash"]
      """  Hash key of the Company, AttrClassID, Planning Attributes and Planning Attribute Values.  """  
      self.IsPlanningAttributeSet:bool = obj["IsPlanningAttributeSet"]
      """  Indicates the set is used by planning.  """  
      self.WhereAvailable:int = obj["WhereAvailable"]
      """  Indicates when this attribute set will be available for selecting during entry: Planning, Supply, Demand.  This is system maintained based on changes made in Dynamic Attribute Class Maintenance and is not directly user maintainable.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  Used in 11.1.100 for additional Hash Key including calculated fields.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.RequiredAt:int = obj["RequiredAt"]
      """  Indicates where this Attribute Set is required.  """  
      self.TemplateWhereAvailable:int = obj["TemplateWhereAvailable"]
      """  Indicates when this set is available as a template for selecting during Attribute Entry: Supply, Demand, Both.  """  
      self.AttributeSetHashAllValues:str = obj["AttributeSetHashAllValues"]
      """  Hash key of all the Attribute IDs and values, without Full Expression.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttrClassIDDescription:str = obj["AttrClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AssignDataFields_input:
   """ Required : 
   relatedToEntity
   fieldValue
   ttDynAttrValue
   """  
   def __init__(self, obj):
      self.relatedToEntity:str = obj["relatedToEntity"]
      self.fieldValue      #schema had no properties on an object.
      self.ttDynAttrValue:list[Erp_Tablesets_DynAttrValueRow] = obj["ttDynAttrValue"]
      pass

class AssignDataFields_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ttDynAttrValue:list[Erp_Tablesets_DynAttrValueRow] = obj["ttDynAttrValue"]
      pass

      """  output parameters  """  

class CheckAttributeChange_input:
   """ Required : 
   remainingQty
   attributeSetID
   poRelSysRowID
   """  
   def __init__(self, obj):
      self.remainingQty:int = obj["remainingQty"]
      """  remainingQty  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  attributeSetID  """  
      self.poRelSysRowID:str = obj["poRelSysRowID"]
      """  PO to validate  """  
      pass

class CheckAttributeChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.notifySalesQtyMsg:str = obj["parameters"]
      self.notifySalesAttributeMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   attributeSetID
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DynAttrValueColumnChanging_input:
   """ Required : 
   attrClassID
   attributeChanging
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.attributeChanging:str = obj["attributeChanging"]
      self.ds:list[Erp_Tablesets_AttributeChangingTableset] = obj["ds"]
      pass

class DynAttrValueColumnChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AttributeChangingTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_AttributeChangingParamsRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeChanging:str = obj["AttributeChanging"]
      """  Attribute that is changing initiating the on change event.  """  
      self.AttributeChangingID:int = obj["AttributeChangingID"]
      """  Unique identifier of set of attributes.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of related table being modified.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AttributeChangingTableset:
   def __init__(self, obj):
      self.AttributeChangingParams:list[Erp_Tablesets_AttributeChangingParamsRow] = obj["AttributeChangingParams"]
      self.AttributeChangingValues:list[Erp_Tablesets_AttributeChangingValuesRow] = obj["AttributeChangingValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AttributeChangingValuesRow:
   def __init__(self, obj):
      self.AttributeChangingID:int = obj["AttributeChangingID"]
      """  Unique identifier of set of attributes.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.AttributeValue:str = obj["AttributeValue"]
      """  Value of attribute converted to string.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DataType:str = obj["DataType"]
      """  Date Type.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassDtlComboValuesRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeID:str = obj["AttributeID"]
      self.Code:str = obj["Code"]
      self.Description:str = obj["Description"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Attribute ID.  """  
      self.DataCharacter:str = obj["DataCharacter"]
      """  Character Data.  """  
      self.DataDate:str = obj["DataDate"]
      """  Date Data.  """  
      self.DataDecimal:int = obj["DataDecimal"]
      """  Decimal Data.  """  
      self.DataInteger:int = obj["DataInteger"]
      """  Integer Data.  """  
      self.DataLogical:bool = obj["DataLogical"]
      """  Logical Data.  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicates this value is a result of a calculation.  """  
      self.IsActual:bool = obj["IsActual"]
      """  Used for planning to indicates for the set that this was the Actual quantity at that point in time.  """  
      self.FieldValue:str = obj["FieldValue"]
      self.TransportValue:str = obj["TransportValue"]
      self.Active:bool = obj["Active"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.FieldFormat:str = obj["FieldFormat"]
      self.AttributeValueSeq:int = obj["AttributeValueSeq"]
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.HasBeenVerified:bool = obj["HasBeenVerified"]
      """  System controlled to validate all dynamic attribute values against the set hash key.  If the value has been verified it will not perform the validation again.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this calculated field will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  Controlled by setup on attribute detail in Dynamic Attribute Class Maintenance.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetLangDescRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language ID.  """  
      self.Description:str = obj["Description"]
      """  Language Description for Attribute Set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  Language Short Description for Attribute Set.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Description:str = obj["Description"]
      """  Description of values in set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetListTableset:
   def __init__(self, obj):
      self.DynAttrValueSetList:list[Erp_Tablesets_DynAttrValueSetListRow] = obj["DynAttrValueSetList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DynAttrValueSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Description:str = obj["Description"]
      """  Description of values in set.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set which will be visible throughout the system and is to be used in selecting an Attribute Set to go along with the Part.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeSetHash:str = obj["AttributeSetHash"]
      """  Hash key of Attribute IDs and values (excluding calculated attributes), and Full Expression.  """  
      self.Active:bool = obj["Active"]
      """  Set to true when the user has determined that the Attribute Set is active.  """  
      self.HasBeenUsed:bool = obj["HasBeenUsed"]
      """  Set to true with the system has determined that the Attribute Set has been used, indicating that it cannot be modified except for the user-defined short description.  """  
      self.ExpressionResultQty:int = obj["ExpressionResultQty"]
      """  Result quantity calculated from a user created expression.  """  
      self.ExpressionResultUOM:str = obj["ExpressionResultUOM"]
      """  The UOM related to the Expression Result Qty.  """  
      self.FullExpression:str = obj["FullExpression"]
      """  Full user maintained expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      """  The unique identifier of the Dynamic Attribute Planning Set.  """  
      self.PlanningAttributeSetHash:str = obj["PlanningAttributeSetHash"]
      """  Hash key of the Company, AttrClassID, Planning Attributes and Planning Attribute Values.  """  
      self.IsPlanningAttributeSet:bool = obj["IsPlanningAttributeSet"]
      """  Indicates the set is used by planning.  """  
      self.WhereAvailable:int = obj["WhereAvailable"]
      """  Indicates when this attribute set will be available for selecting during entry: Planning, Supply, Demand.  This is system maintained based on changes made in Dynamic Attribute Class Maintenance and is not directly user maintainable.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  Used in 11.1.100 for additional Hash Key including calculated fields.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.RequiredAt:int = obj["RequiredAt"]
      """  Indicates where this Attribute Set is required.  """  
      self.TemplateWhereAvailable:int = obj["TemplateWhereAvailable"]
      """  Indicates when this set is available as a template for selecting during Attribute Entry: Supply, Demand, Both.  """  
      self.AttributeSetHashAllValues:str = obj["AttributeSetHashAllValues"]
      """  Hash key of all the Attribute IDs and values, without Full Expression.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AttrClassIDDescription:str = obj["AttrClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrValueSetTableset:
   def __init__(self, obj):
      self.DynAttrValueSet:list[Erp_Tablesets_DynAttrValueSetRow] = obj["DynAttrValueSet"]
      self.DynAttrValue:list[Erp_Tablesets_DynAttrValueRow] = obj["DynAttrValue"]
      self.DynAttrValueSetLangDesc:list[Erp_Tablesets_DynAttrValueSetLangDescRow] = obj["DynAttrValueSetLangDesc"]
      self.DynAttrClassDtlComboValues:list[Erp_Tablesets_DynAttrClassDtlComboValuesRow] = obj["DynAttrClassDtlComboValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class Erp_Tablesets_InvTransParamsTableset:
   def __init__(self, obj):
      self.InvTransfer:list[Erp_Tablesets_InvTransferRow] = obj["InvTransfer"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InvTransferRow:
   def __init__(self, obj):
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.FromOnHandQty:int = obj["FromOnHandQty"]
      self.ToOnHandQty:int = obj["ToOnHandQty"]
      self.TransferQty:int = obj["TransferQty"]
      """  Transfer Quantity entered for this inventory transfer.  """  
      self.Company:str = obj["Company"]
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  The Warehouse the part is being transferred To.  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  The Warehouse Bin the part is being transferred From.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  The Warehouse Bin the part is being transferred To.  """  
      self.FromLotNumber:str = obj["FromLotNumber"]
      """  The Lot number that is being transferred.  """  
      self.ToLotNumber:str = obj["ToLotNumber"]
      """  The Lot number that is being transferred to.  """  
      self.PartNum:str = obj["PartNum"]
      """  The Part Number selected for inventory transfer.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Plant than owns the FromWarehouseCode  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Plant that owns the ToWarehouseCode  """  
      self.FromOnHandUOM:str = obj["FromOnHandUOM"]
      self.TransferQtyUOM:str = obj["TransferQtyUOM"]
      """  The unit of measure the quantify of this transfer is specified in.  """  
      self.ToOnHandUOM:str = obj["ToOnHandUOM"]
      self.Plant:str = obj["Plant"]
      self.Plant2:str = obj["Plant2"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InventoryDynAttrValueParamsTableset:
   def __init__(self, obj):
      self.InventoryDynAttrValueSummary:list[Erp_Tablesets_InventoryDynAttrValueSummaryRow] = obj["InventoryDynAttrValueSummary"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InventoryDynAttrValueSummaryRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      self.Company:str = obj["Company"]
      self.DualQty:int = obj["DualQty"]
      self.DualUM:str = obj["DualUM"]
      self.IUM:str = obj["IUM"]
      self.OurQty:int = obj["OurQty"]
      self.LineDesc:str = obj["LineDesc"]
      self.PartNum:str = obj["PartNum"]
      self.RemainingDualQty:int = obj["RemainingDualQty"]
      self.RemainingOurQty:int = obj["RemainingOurQty"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  SysRowID for the related to table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.EnteredDualQty:int = obj["EnteredDualQty"]
      self.EnteredOurQty:int = obj["EnteredOurQty"]
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  Indicates if this Attribute Class has an MRP tracking attribute.  """  
      self.ErrorType:int = obj["ErrorType"]
      """  Error number  """  
      self.ErrorMsg:str = obj["ErrorMsg"]
      """  Error message  """  
      self.NeedToUpdate:bool = obj["NeedToUpdate"]
      """  True if need to update  """  
      self.TemplateWhereAvailable:int = obj["TemplateWhereAvailable"]
      """  Indicates what level sets are available as a template for selecting during Attribute Entry: Supply, Demand, Both.  """  
      self.ServiceError:bool = obj["ServiceError"]
      """  Exception was thrown when calling a service.  """  
      self.ServiceErrorMessage:str = obj["ServiceErrorMessage"]
      """  Exception message that thrown when calling a service.  """  
      self.EntityAction1:str = obj["EntityAction1"]
      """  Action specific to an entity, which will control how Inventory Attribute Entry closes and action to follow.  """  
      self.EntityAction2:str = obj["EntityAction2"]
      """  Action specific to an entity, which will control how Inventory Attribute Entry closes and action to follow.  """  
      self.EntityActionMessage1:str = obj["EntityActionMessage1"]
      """  Action Message specific to an entity, which will show at closing of the Inventory Attribute Entry.  """  
      self.EntityActionMessage2:str = obj["EntityActionMessage2"]
      """  Action Message specific to an entity, which will show at closing of the Inventory Attribute Entry.  """  
      self.EntityActionMessageTitle1:str = obj["EntityActionMessageTitle1"]
      """  Action Message Title specific to an entity, can be blank and standard defaults will be used.  """  
      self.EntityActionMessageTitle2:str = obj["EntityActionMessageTitle2"]
      """  Action Message Title specific to an entity, can be blank and standard defaults will be used.  """  
      self.PerformUpdateOnClose:bool = obj["PerformUpdateOnClose"]
      """  Final update needs to be performed on window close.  """  
      self.ShowSummaryInformation:bool = obj["ShowSummaryInformation"]
      """  Show summary information for part and totals  """  
      self.PerformAttributeOnChangeEvent:bool = obj["PerformAttributeOnChangeEvent"]
      """  Perform attribute changing events.  It is determined if executed if approved BPMs exist.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  This is only used when using single update.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  This is only used when using single update.  """  
      self.CommittedSplitQty:int = obj["CommittedSplitQty"]
      """  Split quantity that was successfully posted.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDynAttrValueSetTableset:
   def __init__(self, obj):
      self.DynAttrValueSet:list[Erp_Tablesets_DynAttrValueSetRow] = obj["DynAttrValueSet"]
      self.DynAttrValue:list[Erp_Tablesets_DynAttrValueRow] = obj["DynAttrValue"]
      self.DynAttrValueSetLangDesc:list[Erp_Tablesets_DynAttrValueSetLangDescRow] = obj["DynAttrValueSetLangDesc"]
      self.DynAttrClassDtlComboValues:list[Erp_Tablesets_DynAttrClassDtlComboValuesRow] = obj["DynAttrClassDtlComboValues"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAttributeValuesWithOutDynamicMetaDataDS_input:
   """ Required : 
   attrClassID
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   invTransferParams
   inventoryDynAttrValueParamsTS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.invTransferParams:list[Erp_Tablesets_InvTransParamsTableset] = obj["invTransferParams"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      pass

class GetAttributeValuesWithOutDynamicMetaDataDS_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      pass

      """  output parameters  """  

class GetAttributeValues_input:
   """ Required : 
   attrClassID
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   invTransferParams
   inventoryDynAttrValueParamsTS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.invTransferParams:list[Erp_Tablesets_InvTransParamsTableset] = obj["invTransferParams"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      pass

class GetAttributeValues_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetByIDDynAttrValueSetDataSet_input:
   """ Required : 
   attributeSetID
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GetByIDDynAttrValueSetDataSet_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   attributeSetID
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["returnObj"]
      pass

class GetDefaultsFromSelectedTemplate_input:
   """ Required : 
   dynAttrValueDS
   templateAttributeSetID
   """  
   def __init__(self, obj):
      self.dynAttrValueDS      #schema had no properties on an object.
      self.templateAttributeSetID:int = obj["templateAttributeSetID"]
      pass

class GetDefaultsFromSelectedTemplate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dynAttrValueDS: UNKNOW TYPE(error 2338) = obj["dynAttrValueDS"]
      pass

      """  output parameters  """  

class GetDynAttrValueSetPlanningKeys_input:
   """ Required : 
   attrClassID
   attributeIDs
   attributeValues
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.attributeIDs:str = obj["attributeIDs"]
      self.attributeValues:str = obj["attributeValues"]
      pass

class GetDynAttrValueSetPlanningKeys_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.planningAttributeSetSeq:int = obj["parameters"]
      self.planningAttributeSetHash:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFullDynAttrValueSetDataSetByAttrClassID_input:
   """ Required : 
   attrClassID
   schemaOnly
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.schemaOnly:bool = obj["schemaOnly"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GetFullDynAttrValueSetDataSetByAttrClassID_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetFullDynAttrValueSetDataSetByList_input:
   """ Required : 
   attrClassID
   attributeIDList
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.attributeIDList:int = obj["attributeIDList"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GetFullDynAttrValueSetDataSetByList_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetInventoryDynAttrValueParams_input:
   """ Required : 
   attrClassID
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   invTransferParams
   inventoryDynAttrValueParamsTS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.invTransferParams:list[Erp_Tablesets_InvTransParamsTableset] = obj["invTransferParams"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      pass

class GetInventoryDynAttrValueParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.inventoryDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["inventoryDynAttrValueDS"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrValueSetListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAttributeValuesRowWithOutDynamicMetaDataDS_input:
   """ Required : 
   inventoryDynAttrValueParamsTS
   inventoryDynAttrValueDS
   """  
   def __init__(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.inventoryDynAttrValueDS      #schema had no properties on an object.
      pass

class GetNewAttributeValuesRowWithOutDynamicMetaDataDS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.inventoryDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["inventoryDynAttrValueDS"]
      pass

      """  output parameters  """  

class GetNewAttributeValuesRow_input:
   """ Required : 
   inventoryDynAttrValueParamsTS
   inventoryDynAttrValueDS
   """  
   def __init__(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.inventoryDynAttrValueDS      #schema had no properties on an object.
      pass

class GetNewAttributeValuesRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.inventoryDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["inventoryDynAttrValueDS"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetNewDynAttrValueSetDataSet_input:
   """ Required : 
   atrClassID
   ds
   dynamicMetadataDS
   """  
   def __init__(self, obj):
      self.atrClassID:str = obj["atrClassID"]
      self.ds      #schema had no properties on an object.
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

class GetNewDynAttrValueSetDataSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds: UNKNOW TYPE(error 2338) = obj["ds"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetNewDynAttrValueSetLangDesc_input:
   """ Required : 
   ds
   attributeSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetNewDynAttrValueSetLangDesc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDynAttrValueSetTableset_input:
   """ Required : 
   attrClassID
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

class GetNewDynAttrValueSetTableset_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDynAttrValueSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

class GetNewDynAttrValueSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDynAttrValue_input:
   """ Required : 
   ds
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   attrClassID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.attrClassID:str = obj["attrClassID"]
      pass

class GetNewDynAttrValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInventoryDynAttrValueSummary_input:
   """ Required : 
   attrClassID
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   inventoryDynAttrValueParamsTS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      pass

class GetNewInventoryDynAttrValueSummary_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      pass

      """  output parameters  """  

class GetNewInventoryDynAttrValuesRow_input:
   """ Required : 
   relatedToSchemaName
   relatedToTableName
   relatedToSysRowID
   inventoryDynAttrValueDS
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToTableName:str = obj["relatedToTableName"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.inventoryDynAttrValueDS      #schema had no properties on an object.
      pass

class GetNewInventoryDynAttrValuesRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["inventoryDynAttrValueDS"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynAttrValueSet
   whereClauseDynAttrValue
   whereClauseDynAttrValueSetLangDesc
   whereClauseDynAttrClassDtlComboValues
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
      self.whereClauseDynAttrValue:str = obj["whereClauseDynAttrValue"]
      self.whereClauseDynAttrValueSetLangDesc:str = obj["whereClauseDynAttrValueSetLangDesc"]
      self.whereClauseDynAttrClassDtlComboValues:str = obj["whereClauseDynAttrClassDtlComboValues"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["returnObj"]
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

class MasterUpdateDynAttrValueSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

class MasterUpdateDynAttrValueSet_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MasterUpdateFromMultiCompany_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

class MasterUpdateFromMultiCompany_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MasterUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

class MasterUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeAttributeValuesColumnObject_input:
   """ Required : 
   attrClassID
   columnName
   columnValue
   inventoryDynAttrValueParamsTS
   modifiedDynAttrValueDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.columnName:str = obj["columnName"]
      self.columnValue:str = obj["columnValue"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.modifiedDynAttrValueDS      #schema had no properties on an object.
      pass

class OnChangeAttributeValuesColumnObject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.modifiedDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["modifiedDynAttrValueDS"]
      pass

      """  output parameters  """  

class OnChangeDynAttrValueColumn_input:
   """ Required : 
   columnName
   columnValue
   modifiedDynAttrValueDS
   """  
   def __init__(self, obj):
      self.columnName:str = obj["columnName"]
      self.columnValue:str = obj["columnValue"]
      self.modifiedDynAttrValueDS      #schema had no properties on an object.
      pass

class OnChangeDynAttrValueColumn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.modifiedDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["modifiedDynAttrValueDS"]
      pass

      """  output parameters  """  

class OnChangeDynAttrValueSetColumnObject_input:
   """ Required : 
   attrClassID
   columnName
   columnValue
   modifiedDynAttrValueDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.columnName:str = obj["columnName"]
      self.columnValue:str = obj["columnValue"]
      self.modifiedDynAttrValueDS      #schema had no properties on an object.
      pass

class OnChangeDynAttrValueSetColumnObject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.modifiedDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["modifiedDynAttrValueDS"]
      pass

      """  output parameters  """  

class RefreshDynAttrValuesRow_input:
   """ Required : 
   dynAttrValueDS
   """  
   def __init__(self, obj):
      self.dynAttrValueDS      #schema had no properties on an object.
      pass

class RefreshDynAttrValuesRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dynAttrValueDS: UNKNOW TYPE(error 2338) = obj["dynAttrValueDS"]
      pass

      """  output parameters  """  

class UpdateAttributeValuesObject_input:
   """ Required : 
   attrClassID
   commitLineDtl
   invTrasferParams
   inventoryDynAttrValueParamsTS
   dynAttrValueDS
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.commitLineDtl:bool = obj["commitLineDtl"]
      self.invTrasferParams:list[Erp_Tablesets_InvTransParamsTableset] = obj["invTrasferParams"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.dynAttrValueDS      #schema had no properties on an object.
      pass

class UpdateAttributeValuesObject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.dynAttrValueDS: UNKNOW TYPE(error 2338) = obj["dynAttrValueDS"]
      pass

      """  output parameters  """  

class UpdateAttributeValues_input:
   """ Required : 
   commitLineDtl
   invTrasferParams
   inventoryDynAttrValueParamsTS
   dynAttrValueDS
   """  
   def __init__(self, obj):
      self.commitLineDtl:bool = obj["commitLineDtl"]
      self.invTrasferParams:list[Erp_Tablesets_InvTransParamsTableset] = obj["invTrasferParams"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.dynAttrValueDS      #schema had no properties on an object.
      pass

class UpdateAttributeValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.dynAttrValueDS: UNKNOW TYPE(error 2338) = obj["dynAttrValueDS"]
      pass

      """  output parameters  """  

class UpdateDynAttrValueSetDataSetObject_input:
   """ Required : 
   attrClassID
   ds
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.ds      #schema had no properties on an object.
      pass

class UpdateDynAttrValueSetDataSetObject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds: UNKNOW TYPE(error 2338) = obj["ds"]
      pass

      """  output parameters  """  

class UpdateDynAttrValueSetDataSet_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds      #schema had no properties on an object.
      pass

class UpdateDynAttrValueSetDataSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds: UNKNOW TYPE(error 2338) = obj["ds"]
      pass

      """  output parameters  """  

class UpdateEntityAttributeSetFromConfigurator_input:
   """ Required : 
   targetEntityTableName
   targetEntitySysRowID
   dynAttrValueSetDS
   """  
   def __init__(self, obj):
      self.targetEntityTableName:str = obj["targetEntityTableName"]
      self.targetEntitySysRowID:str = obj["targetEntitySysRowID"]
      self.dynAttrValueSetDS:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["dynAttrValueSetDS"]
      pass

class UpdateEntityAttributeSetFromConfigurator_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dynAttrValueSetDS:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["dynAttrValueSetDS"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrValueSetTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrValueSetTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateInventoryAttributes_input:
   """ Required : 
   commitLineDtl
   inventoryDynAttrValueParamsTS
   modifiedDynAttrValueDS
   invTrasferParams
   """  
   def __init__(self, obj):
      self.commitLineDtl:bool = obj["commitLineDtl"]
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.modifiedDynAttrValueDS      #schema had no properties on an object.
      self.invTrasferParams:list[Erp_Tablesets_InvTransParamsTableset] = obj["invTrasferParams"]
      pass

class UpdateInventoryAttributes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryDynAttrValueParamsTS:list[Erp_Tablesets_InventoryDynAttrValueParamsTableset] = obj["inventoryDynAttrValueParamsTS"]
      self.updatedDynAttrValueDS: UNKNOW TYPE(error 2338) = obj["updatedDynAttrValueDS"]
      pass

      """  output parameters  """  

class UpdateSalesOrderComponentAttribute_input:
   """ Required : 
   orderDtlSysRowID
   orderQty
   """  
   def __init__(self, obj):
      self.orderDtlSysRowID:str = obj["orderDtlSysRowID"]
      """  Order number to validate  """  
      self.orderQty:int = obj["orderQty"]
      """  New Order Quantity for Sales Kit Component  """  
      pass

class UpdateSalesOrderComponentAttribute_output:
   def __init__(self, obj):
      pass

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrValueSetTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateShortDescription_input:
   """ Required : 
   attrClassID
   shortDescription
   attributeSetID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.shortDescription:str = obj["shortDescription"]
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class ValidateShortDescription_output:
   def __init__(self, obj):
      pass

class ValidateUniqueDynAttrValueSetByShortDescription_input:
   """ Required : 
   attrClassID
   shortDescription
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      self.shortDescription:str = obj["shortDescription"]
      pass

class ValidateUniqueDynAttrValueSetByShortDescription_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      pass

      """  output parameters  """  

