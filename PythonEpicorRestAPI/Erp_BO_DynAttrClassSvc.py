import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DynAttrClassSvc
# Description: Dynamic Attribute Class Maintenance
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClasses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClasses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrClasses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClasses_Company_AttrClassID(Company, AttrClassID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClass item
   Description: Calls GetByID to retrieve the DynAttrClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrClasses_Company_AttrClassID(Company, AttrClassID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrClass for the service
   Description: Calls UpdateExt to update DynAttrClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrClasses_Company_AttrClassID(Company, AttrClassID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrClass item
   Description: Call UpdateExt to delete DynAttrClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClasses_Company_AttrClassID_DynAttrClassDtls(Company, AttrClassID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DynAttrClassDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrClassDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")/DynAttrClassDtls",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClasses_Company_AttrClassID_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtl item
   Description: Calls GetByID to retrieve the DynAttrClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClasses(" + Company + "," + AttrClassID + ")/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtls(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtls
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrClassDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtl item
   Description: Calls GetByID to retrieve the DynAttrClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrClassDtl for the service
   Description: Calls UpdateExt to update DynAttrClassDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrClassDtls_Company_AttrClassID_AttributeID(Company, AttrClassID, AttributeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrClassDtl item
   Description: Call UpdateExt to delete DynAttrClassDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtls_Company_AttrClassID_AttributeID_DynAttrClassDtlListVals(Company, AttrClassID, AttributeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DynAttrClassDtlListVals items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DynAttrClassDtlListVals1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")/DynAttrClassDtlListVals",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtls_Company_AttrClassID_AttributeID_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company, AttrClassID, AttributeID, Code, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlListVal item
   Description: Calls GetByID to retrieve the DynAttrClassDtlListVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlListVal1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtls(" + Company + "," + AttrClassID + "," + AttributeID + ")/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")",headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlListVals(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DynAttrClassDtlListVals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynAttrClassDtlListVals
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals",headers=creds) as resp:
           return await resp.json()

async def post_DynAttrClassDtlListVals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DynAttrClassDtlListVals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company, AttrClassID, AttributeID, Code, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DynAttrClassDtlListVal item
   Description: Calls GetByID to retrieve the DynAttrClassDtlListVal item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynAttrClassDtlListVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company, AttrClassID, AttributeID, Code, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DynAttrClassDtlListVal for the service
   Description: Calls UpdateExt to update DynAttrClassDtlListVal. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DynAttrClassDtlListVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DynAttrClassDtlListValRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DynAttrClassDtlListVals_Company_AttrClassID_AttributeID_Code(Company, AttrClassID, AttributeID, Code, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DynAttrClassDtlListVal item
   Description: Call UpdateExt to delete DynAttrClassDtlListVal item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DynAttrClassDtlListVal
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AttrClassID: Desc: AttrClassID   Required: True   Allow empty value : True
      :param AttributeID: Desc: AttributeID   Required: True   Allow empty value : True
      :param Code: Desc: Code   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/DynAttrClassDtlListVals(" + Company + "," + AttrClassID + "," + AttributeID + "," + Code + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DynAttrClassListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDynAttrClass, whereClauseDynAttrClassDtl, whereClauseDynAttrClassDtlListVal, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseDynAttrClass=" + whereClauseDynAttrClass
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrClassDtl=" + whereClauseDynAttrClassDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDynAttrClassDtlListVal=" + whereClauseDynAttrClassDtlListVal
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(attrClassID, epicorHeaders = None):
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
   params += "attrClassID=" + attrClassID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateDynAttrClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateDynAttrClass
   Description: Duplicates the current Dynamic Attribute Class
   OperationID: DuplicateDynAttrClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateDynAttrClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateDynAttrClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFieldDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFieldDataType
   Description: Used when the Data Type field of DynAttrClassDtl has been changed to a new value.
Resets all possible fields.
   OperationID: OnChangeFieldDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFieldDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFieldDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAttributeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAttributeID
   Description: Used when the AttributeID field has changed on DynAttrClassDtl record.
   OperationID: OnChangeAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAttributeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAttributeID
   Description: Used to check if the entered AttributeID is in the DynAttrMasterDtl record
   OperationID: CheckAttributeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAttributeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAttributeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBizType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBizType
   Description: Handles require changes to Attribute when the Business Type changes: sets the Required At list picker
   OperationID: ChangeBizType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBizType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBizType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUsedInPlanning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUsedInPlanning
   Description: Handles require changes to Attribute when the MRP changes: sets the Required At list picker
   OperationID: ChangeUsedInPlanning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUsedInPlanning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUsedInPlanning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRelatedToTableName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRelatedToTableName
   Description: Used when the RelatedToTableName field of DynAttrClass has been changed to a new value.
Resets all possible fields.
   OperationID: OnChangeRelatedToTableName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRelatedToTableName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRelatedToTableName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetDynAttrClassDtlIsExpressionDefined(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetDynAttrClassDtlIsExpressionDefined
   Description: Indicates if calculated expression has been entered.
   OperationID: SetDynAttrClassDtlIsExpressionDefined
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetDynAttrClassDtlIsExpressionDefined_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetDynAttrClassDtlIsExpressionDefined_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFormat
   Description: Validates data format
   OperationID: ValidateFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RegenerateAttributeSetHash(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RegenerateAttributeSetHash
   Description: Regenerates AttributeSetHash - specific for sets with calculated fields
   OperationID: RegenerateAttributeSetHash
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RegenerateAttributeSetHash_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RegenerateAttributeSetHash_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedToTableNameListFromLandingPage(epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedToTableNameListFromLandingPage
   Description: This method returns the list of Related To Table Names plus the value 'All' for use in the Landing Page.
   OperationID: GetRelatedToTableNameListFromLandingPage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedToTableNameListFromLandingPage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedToTableNameList(epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedToTableNameList
   Description: This method returns the list of Related To Table Names.
   OperationID: GetRelatedToTableNameList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedToTableNameList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrClassDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrClassDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClassDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClassDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClassDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDynAttrClassDtlListVal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDynAttrClassDtlListVal
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDynAttrClassDtlListVal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDynAttrClassDtlListVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDynAttrClassDtlListVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DynAttrClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlListValRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassDtlListValRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DynAttrClassRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DynAttrClassRow] = obj["value"]
      pass

class Erp_Tablesets_DynAttrClassDtlListValRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent attribute class.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class.  """  
      self.Code:str = obj["Code"]
      """  Code value that will be store in the DynAttrValue.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Description:str = obj["Description"]
      """  Description of list value that will show in list.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute List Value is Active. Default is false.  Once Active, the system will allow it to be used.  """  
      self.PlanningConvOperator:str = obj["PlanningConvOperator"]
      """  Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).  """  
      self.PlanningConvFactor:int = obj["PlanningConvFactor"]
      """  Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.  """  
      self.WhereAvailable:int = obj["WhereAvailable"]
      """  Indicates when this list value will be available for selecting during entry: Planning, Supply, Demand.  """  
      self.TheoreticalUOM:str = obj["TheoreticalUOM"]
      """  Theoretical UOM used by MRP for conversions to the related Actual quantity.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this attribute.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used when linked to a numeric input.  """  
      self.InitialCharacter:str = obj["InitialCharacter"]
      """  Initial character value.  """  
      self.InitialDate:str = obj["InitialDate"]
      """  Initial date value.  """  
      self.InitialDecimal:int = obj["InitialDecimal"]
      """  Initial decimal value.  """  
      self.InitialInteger:int = obj["InitialInteger"]
      """  Initial integer value.  """  
      self.InitialLogical:bool = obj["InitialLogical"]
      """  Initial logical value.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.MaxDecimal:int = obj["MaxDecimal"]
      """  The user defined maximum acceptable value when linked to a decimal input.  """  
      self.MaxInteger:int = obj["MaxInteger"]
      """  The user defined maximum acceptable value when linked to an integer input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MinDecimal:int = obj["MinDecimal"]
      """  The user defined minimum acceptable value when linked to a decimal input.  """  
      self.MinInteger:int = obj["MinInteger"]
      """  The user defined minimum acceptable value when linked to an integer input.  """  
      self.WebAttribute:bool = obj["WebAttribute"]
      """  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the business use of the field, valid values are "Quantity,UOM"  """  
      self.UOMAttributeID:str = obj["UOMAttributeID"]
      """  Attribute ID of related UOM linked to quantity.  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  If attribute is used in planning.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicated this attribute will be used as a calculated field.  """  
      self.PlanningBaseUOM:str = obj["PlanningBaseUOM"]
      """  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  """  
      self.PlanningType:str = obj["PlanningType"]
      """  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.IsActual:bool = obj["IsActual"]
      """  The actual transaction value for the attribute set.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  """  
      self.MasterDtlLinked:str = obj["MasterDtlLinked"]
      """  Resuable Attribute linked to this class attribute.  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Attributes are synch to this class attribute.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.IncludeListValueCodeInShortDesc:bool = obj["IncludeListValueCodeInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  """  
      self.IncludeListValueDescriptionInShortDesc:bool = obj["IncludeListValueDescriptionInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  """  
      self.InUse:bool = obj["InUse"]
      """  Used for setting Epi Shape to highlight attribute has been used.  """  
      self.ListValues:str = obj["ListValues"]
      """  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  """  
      self.IsFinalExpression:bool = obj["IsFinalExpression"]
      """  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  """  
      self.FinalExpressionUOM:str = obj["FinalExpressionUOM"]
      """  The UOM used with final expression, used to calculate inventory quantity.  """  
      self.RequiredAtAvailableCodes:str = obj["RequiredAtAvailableCodes"]
      """  List of available Required At codes.  """  
      self.RequiredAtAvailableDesc:str = obj["RequiredAtAvailableDesc"]
      """  List of available Required at descriptions.  """  
      self.RequiredAtSelectedCodes:str = obj["RequiredAtSelectedCodes"]
      """  List of Required At codes selected.  """  
      self.RequiredAtSelectedDesc:str = obj["RequiredAtSelectedDesc"]
      """  List of Required At descriptions selected.  """  
      self.IsExpressionDefined:bool = obj["IsExpressionDefined"]
      """  Indicates if this calculated field has a Formula Expression already been added or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  Determines how this class is used: Attributes, Characteristics.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.WebAttrClass:bool = obj["WebAttrClass"]
      """  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullExpression:str = obj["FullExpression"]
      """  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  """  
      self.CalculationType:str = obj["CalculationType"]
      """  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  """  
      self.GlobalAttrClassID:bool = obj["GlobalAttrClassID"]
      """  Determines whether or not this Attribute Class is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this Attribute Class record will receive global updates.  """  
      self.AttrClassType:str = obj["AttrClassType"]
      """  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  Determines how this class is used: Attributes, Characteristics.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.WebAttrClass:bool = obj["WebAttrClass"]
      """  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullExpression:str = obj["FullExpression"]
      """  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  """  
      self.CalculationType:str = obj["CalculationType"]
      """  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  """  
      self.NumberOfPiecesAction:str = obj["NumberOfPiecesAction"]
      """  Action to be taken when Number of Pieces Tolerance is not adhered to.  Valid values are STOP and NONE.  """  
      self.NumberOfPiecesTolerance:int = obj["NumberOfPiecesTolerance"]
      """  Acceptable tolerance both negative and positive when calculating Total Quantity from Number of Pieces results in a rounding variance.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.GlobalAttrClassID:bool = obj["GlobalAttrClassID"]
      """  Determines whether or not this Attribute Class is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this Attribute Class record will receive global updates.  """  
      self.AttrClassType:str = obj["AttrClassType"]
      """  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.EnableInventoryTracking:bool = obj["EnableInventoryTracking"]
      """  Contols when class inventory tracking can be changed.  """  
      self.EnableGlobalAttrClassID:bool = obj["EnableGlobalAttrClassID"]
      """  Controls when Global checkbox on an Attribute Class should be enabled so it may be modified.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Dynamic Attribute Class is Global (master or linked)  """  
      self.EnableWebAttrClass:bool = obj["EnableWebAttrClass"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBizType_input:
   """ Required : 
   bizType
   ds
   """  
   def __init__(self, obj):
      self.bizType:str = obj["bizType"]
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class ChangeBizType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUsedInPlanning_input:
   """ Required : 
   usedInPlanning
   ds
   """  
   def __init__(self, obj):
      self.usedInPlanning:bool = obj["usedInPlanning"]
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class ChangeUsedInPlanning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAttributeID_input:
   """ Required : 
   attributeID
   """  
   def __init__(self, obj):
      self.attributeID:str = obj["attributeID"]
      """  The AttributeID to check.  """  
      pass

class CheckAttributeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.promptMessage:str = obj["parameters"]
      self.activeFlag:bool = obj["activeFlag"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateDynAttrClass_input:
   """ Required : 
   sourceDynAttrClassID
   targetDynAttrClassID
   targetDynAttrClassDescription
   targetRelatedToTableName
   """  
   def __init__(self, obj):
      self.sourceDynAttrClassID:str = obj["sourceDynAttrClassID"]
      self.targetDynAttrClassID:str = obj["targetDynAttrClassID"]
      self.targetDynAttrClassDescription:str = obj["targetDynAttrClassDescription"]
      self.targetRelatedToTableName:str = obj["targetRelatedToTableName"]
      pass

class DuplicateDynAttrClass_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrClassTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_DynAttrClassDtlListValRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent attribute class.  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class.  """  
      self.Code:str = obj["Code"]
      """  Code value that will be store in the DynAttrValue.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Description:str = obj["Description"]
      """  Description of list value that will show in list.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute List Value is Active. Default is false.  Once Active, the system will allow it to be used.  """  
      self.PlanningConvOperator:str = obj["PlanningConvOperator"]
      """  Indicates the mathmatical operator that is used for performing the UOM Conversion. Options are "*" (Multiply) or "\" (Divide).  """  
      self.PlanningConvFactor:int = obj["PlanningConvFactor"]
      """  Value used to convert to/from base uom. Expressed as 1 of the specific UOM in Base UOM if ConvOperator = *, else 1 Base UOM in UOM. For example: A Class of "Lengths" might have meter(m) as it's base . Kilometer(km) would have a  conversion factor of 1000(m) with ConvOperator = *. Mandatory if UOMClass.PartSpecific = false. If it's the BaseUOM must have conversion factor of 1. Simplified usage:To convert a quantity to base UOM you multiply by the ConvFactor.  Example, with meters as base. ft to meters 10ft * 0.3048 = 3.048m .. To convert base to uom of yard you divide the quantiy in base by the ConvFactor. Ex: 3.048 / 0.9144 = 3.33333yd.  """  
      self.WhereAvailable:int = obj["WhereAvailable"]
      """  Indicates when this list value will be available for selecting during entry: Planning, Supply, Demand.  """  
      self.TheoreticalUOM:str = obj["TheoreticalUOM"]
      """  Theoretical UOM used by MRP for conversions to the related Actual quantity.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of parent Attribute Class  """  
      self.AttributeID:str = obj["AttributeID"]
      """  Unique ID of attribute for this class  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Use this field to enter a concise explanation for the current attribute. This value helps identify the purpose for any controls (fields, drop-down lists, check boxes, and so on).  """  
      self.FieldDataType:str = obj["FieldDataType"]
      """  Date type for this attribute field.  """  
      self.FieldFormat:str = obj["FieldFormat"]
      """  Format for the given date type for this attribute field.  """  
      self.FieldLabel:str = obj["FieldLabel"]
      """  Defines the field lablel for this attribute.  """  
      self.IncrPrec:int = obj["IncrPrec"]
      """  The value that determines the increments used when linked to a numeric input.  """  
      self.InitialCharacter:str = obj["InitialCharacter"]
      """  Initial character value.  """  
      self.InitialDate:str = obj["InitialDate"]
      """  Initial date value.  """  
      self.InitialDecimal:int = obj["InitialDecimal"]
      """  Initial decimal value.  """  
      self.InitialInteger:int = obj["InitialInteger"]
      """  Initial integer value.  """  
      self.InitialLogical:bool = obj["InitialLogical"]
      """  Initial logical value.  """  
      self.MaxDate:str = obj["MaxDate"]
      """  The user defined maximum acceptable value when linked to a date input.  """  
      self.MaxDecimal:int = obj["MaxDecimal"]
      """  The user defined maximum acceptable value when linked to a decimal input.  """  
      self.MaxInteger:int = obj["MaxInteger"]
      """  The user defined maximum acceptable value when linked to an integer input.  """  
      self.MinDate:str = obj["MinDate"]
      """  The user defined minimum acceptable value when linked to a date input.  """  
      self.MinDecimal:int = obj["MinDecimal"]
      """  The user defined minimum acceptable value when linked to a decimal input.  """  
      self.MinInteger:int = obj["MinInteger"]
      """  The user defined minimum acceptable value when linked to an integer input.  """  
      self.WebAttribute:bool = obj["WebAttribute"]
      """  Controls how attributes are synched to ECC and if they should be viewable on the web and used for searches.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BizType:str = obj["BizType"]
      """  Further defines the business use of the field, valid values are "Quantity,UOM"  """  
      self.UOMAttributeID:str = obj["UOMAttributeID"]
      """  Attribute ID of related UOM linked to quantity.  """  
      self.SortSeq:int = obj["SortSeq"]
      """  Controls the order attributes are displayed and updated.  """  
      self.UsedInPlanning:bool = obj["UsedInPlanning"]
      """  If attribute is used in planning.  """  
      self.IsCalculated:bool = obj["IsCalculated"]
      """  Indicated this attribute will be used as a calculated field.  """  
      self.PlanningBaseUOM:str = obj["PlanningBaseUOM"]
      """  Used in planning for MRP processing to calculate number of pieces.  When selecting an Attribute Class for a Part the Attribute Base UOM must match the Part UOM Class Base UOM.  """  
      self.PlanningType:str = obj["PlanningType"]
      """  Used in planning for MRP processing to calculate number of pieces.  Possible values: (T)heoretical which is a nominal value and depends on another attribute that is the actual transaction value, (A)ctual which is a nominal value with the conversion factor resulting in the actual transaction value, (B)oth Theoretical and Actual.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.IsActual:bool = obj["IsActual"]
      """  The actual transaction value for the attribute set.  """  
      self.IsViewable:bool = obj["IsViewable"]
      """  Indicates if this attribute will be visible in attribute entry.  """  
      self.IsReadOnly:bool = obj["IsReadOnly"]
      """  Indicates if this attribute will be read only in attribute entry.  """  
      self.MasterDtlLinked:str = obj["MasterDtlLinked"]
      """  Resuable Attribute linked to this class attribute.  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Attributes are synch to this class attribute.  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.IncludeListValueCodeInShortDesc:bool = obj["IncludeListValueCodeInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Code.  """  
      self.IncludeListValueDescriptionInShortDesc:bool = obj["IncludeListValueDescriptionInShortDesc"]
      """  Indicates when auto-generating Attribute Set Short Description, use the List Value Description.  """  
      self.InUse:bool = obj["InUse"]
      """  Used for setting Epi Shape to highlight attribute has been used.  """  
      self.ListValues:str = obj["ListValues"]
      """  This field hold list of values from the DynAttrClassDtlListVal table for the Attribute search,  """  
      self.IsFinalExpression:bool = obj["IsFinalExpression"]
      """  Indicates this calculated field is the final expression used for calculating inventory quantity.  When selecting the final expression, a Final Expression UOM must be selected.  """  
      self.FinalExpressionUOM:str = obj["FinalExpressionUOM"]
      """  The UOM used with final expression, used to calculate inventory quantity.  """  
      self.RequiredAtAvailableCodes:str = obj["RequiredAtAvailableCodes"]
      """  List of available Required At codes.  """  
      self.RequiredAtAvailableDesc:str = obj["RequiredAtAvailableDesc"]
      """  List of available Required at descriptions.  """  
      self.RequiredAtSelectedCodes:str = obj["RequiredAtSelectedCodes"]
      """  List of Required At codes selected.  """  
      self.RequiredAtSelectedDesc:str = obj["RequiredAtSelectedDesc"]
      """  List of Required At descriptions selected.  """  
      self.IsExpressionDefined:bool = obj["IsExpressionDefined"]
      """  Indicates if this calculated field has a Formula Expression already been added or not.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  Determines how this class is used: Attributes, Characteristics.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.WebAttrClass:bool = obj["WebAttrClass"]
      """  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullExpression:str = obj["FullExpression"]
      """  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  """  
      self.CalculationType:str = obj["CalculationType"]
      """  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  """  
      self.GlobalAttrClassID:bool = obj["GlobalAttrClassID"]
      """  Determines whether or not this Attribute Class is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this Attribute Class record will receive global updates.  """  
      self.AttrClassType:str = obj["AttrClassType"]
      """  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassListTableset:
   def __init__(self, obj):
      self.DynAttrClassList:list[Erp_Tablesets_DynAttrClassListRow] = obj["DynAttrClassList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DynAttrClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  Determines how this class is used: Attributes, Characteristics.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  Schema name for the related table.  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  Table name for the related table.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Attribute Class is Active. If not Active system will no longer allow it to be used.  """  
      self.Description:str = obj["Description"]
      """  Description.  """  
      self.WebAttrClass:bool = obj["WebAttrClass"]
      """  Controls how attribute classes are synched to ECC and if they should be viewable on the web.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.FullExpression:str = obj["FullExpression"]
      """  This columns has been obsoleted.  Full Expression used for calculating inventory quantities.  """  
      self.CalculationType:str = obj["CalculationType"]
      """  For Inventory Attribute Tracked parts it is the type used for calculating inventory quantities.  """  
      self.NumberOfPiecesAction:str = obj["NumberOfPiecesAction"]
      """  Action to be taken when Number of Pieces Tolerance is not adhered to.  Valid values are STOP and NONE.  """  
      self.NumberOfPiecesTolerance:int = obj["NumberOfPiecesTolerance"]
      """  Acceptable tolerance both negative and positive when calculating Total Quantity from Number of Pieces results in a rounding variance.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  Development use only.  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  Development use only.  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  Development use only.  """  
      self.GlobalAttrClassID:bool = obj["GlobalAttrClassID"]
      """  Determines whether or not this Attribute Class is shared between more than one company.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Determines whether or not this Attribute Class record will receive global updates.  """  
      self.AttrClassType:str = obj["AttrClassType"]
      """  Indicates the Attribute Class Type.  Valid values are ATTR (Attributes) and CHAR (Characteristics).  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a pre-defined System Attribute Class.  """  
      self.EnableInventoryTracking:bool = obj["EnableInventoryTracking"]
      """  Contols when class inventory tracking can be changed.  """  
      self.EnableGlobalAttrClassID:bool = obj["EnableGlobalAttrClassID"]
      """  Controls when Global checkbox on an Attribute Class should be enabled so it may be modified.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Dynamic Attribute Class is Global (master or linked)  """  
      self.EnableWebAttrClass:bool = obj["EnableWebAttrClass"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DynAttrClassTableset:
   def __init__(self, obj):
      self.DynAttrClass:list[Erp_Tablesets_DynAttrClassRow] = obj["DynAttrClass"]
      self.DynAttrClassDtl:list[Erp_Tablesets_DynAttrClassDtlRow] = obj["DynAttrClassDtl"]
      self.DynAttrClassDtlListVal:list[Erp_Tablesets_DynAttrClassDtlListValRow] = obj["DynAttrClassDtlListVal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RelatedToTableNameListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      self.DisplaySeq:int = obj["DisplaySeq"]
      self.DspRelatedToTableName:str = obj["DspRelatedToTableName"]
      """  Display name for RelatedToTableName  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RelatedToTableNameListTableset:
   def __init__(self, obj):
      self.RelatedToTableNameList:list[Erp_Tablesets_RelatedToTableNameListRow] = obj["RelatedToTableNameList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDynAttrClassTableset:
   def __init__(self, obj):
      self.DynAttrClass:list[Erp_Tablesets_DynAttrClassRow] = obj["DynAttrClass"]
      self.DynAttrClassDtl:list[Erp_Tablesets_DynAttrClassDtlRow] = obj["DynAttrClassDtl"]
      self.DynAttrClassDtlListVal:list[Erp_Tablesets_DynAttrClassDtlListValRow] = obj["DynAttrClassDtlListVal"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrClassTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DynAttrClassListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDynAttrClassDtlListVal_input:
   """ Required : 
   ds
   attrClassID
   attributeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      self.attrClassID:str = obj["attrClassID"]
      self.attributeID:str = obj["attributeID"]
      pass

class GetNewDynAttrClassDtlListVal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDynAttrClassDtl_input:
   """ Required : 
   ds
   attrClassID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      self.attrClassID:str = obj["attrClassID"]
      pass

class GetNewDynAttrClassDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDynAttrClass_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class GetNewDynAttrClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedToTableNameListFromLandingPage_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RelatedToTableNameListTableset] = obj["returnObj"]
      pass

class GetRelatedToTableNameList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RelatedToTableNameListTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseDynAttrClass
   whereClauseDynAttrClassDtl
   whereClauseDynAttrClassDtlListVal
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrClass:str = obj["whereClauseDynAttrClass"]
      self.whereClauseDynAttrClassDtl:str = obj["whereClauseDynAttrClassDtl"]
      self.whereClauseDynAttrClassDtlListVal:str = obj["whereClauseDynAttrClassDtlListVal"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DynAttrClassTableset] = obj["returnObj"]
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

class OnChangeAttributeID_input:
   """ Required : 
   attributeID
   ds
   """  
   def __init__(self, obj):
      self.attributeID:str = obj["attributeID"]
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class OnChangeAttributeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFieldDataType_input:
   """ Required : 
   newDataType
   ds
   """  
   def __init__(self, obj):
      self.newDataType:str = obj["newDataType"]
      """  The new data type value.  """  
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class OnChangeFieldDataType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRelatedToTableName_input:
   """ Required : 
   newRelatedToTableName
   ds
   """  
   def __init__(self, obj):
      self.newRelatedToTableName:str = obj["newRelatedToTableName"]
      """  The new RelatedToTableName value.  """  
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class OnChangeRelatedToTableName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RegenerateAttributeSetHash_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      pass

class RegenerateAttributeSetHash_output:
   def __init__(self, obj):
      pass

class SetDynAttrClassDtlIsExpressionDefined_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class SetDynAttrClassDtlIsExpressionDefined_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrClassTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDynAttrClassTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateFormat_input:
   """ Required : 
   newFieldFormat
   ds
   """  
   def __init__(self, obj):
      self.newFieldFormat:str = obj["newFieldFormat"]
      """  newFieldFormat  """  
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

class ValidateFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DynAttrClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

