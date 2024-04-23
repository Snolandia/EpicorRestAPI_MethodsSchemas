import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ZBODefSvc
# Description: Service definition business object.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ZBODefs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZBODefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZBODefs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZBODefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs",headers=creds) as resp:
           return await resp.json()

async def post_ZBODefs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZBODefs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZBODefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZBODefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZBODefs_SystemCode_ClassName(SystemCode, ClassName, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZBODef item
   Description: Calls GetByID to retrieve the ZBODef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZBODef
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZBODefRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZBODefs_SystemCode_ClassName(SystemCode, ClassName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZBODef for the service
   Description: Calls UpdateExt to update ZBODef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZBODef
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZBODefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZBODefs_SystemCode_ClassName(SystemCode, ClassName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZBODef item
   Description: Call UpdateExt to delete ZBODef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZBODef
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZBODefs_SystemCode_ClassName_ZBODataSets(SystemCode, ClassName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZBODataSets items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZBODataSets1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZBODataSetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")/ZBODataSets",headers=creds) as resp:
           return await resp.json()

async def get_ZBODefs_SystemCode_ClassName_ZBODataSets_SystemCode_ClassName_DataSetSystemCode_DataSetID(SystemCode, ClassName, DataSetSystemCode, DataSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZBODataSet item
   Description: Calls GetByID to retrieve the ZBODataSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZBODataSet1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param DataSetSystemCode: Desc: DataSetSystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZBODataSetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")/ZBODataSets(" + SystemCode + "," + ClassName + "," + DataSetSystemCode + "," + DataSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZBODefs_SystemCode_ClassName_ZServiceLicenseTypes(SystemCode, ClassName, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get ZServiceLicenseTypes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZServiceLicenseTypes1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZServiceLicenseTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")/ZServiceLicenseTypes",headers=creds) as resp:
           return await resp.json()

async def get_ZBODefs_SystemCode_ClassName_ZServiceLicenseTypes_SystemCode_ClassName_LicenceTypeID(SystemCode, ClassName, LicenceTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZServiceLicenseType item
   Description: Calls GetByID to retrieve the ZServiceLicenseType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZServiceLicenseType1
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param LicenceTypeID: Desc: LicenceTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZServiceLicenseTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODefs(" + SystemCode + "," + ClassName + ")/ZServiceLicenseTypes(" + SystemCode + "," + ClassName + "," + LicenceTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZBODataSets(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZBODataSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZBODataSets
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZBODataSetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODataSets",headers=creds) as resp:
           return await resp.json()

async def post_ZBODataSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZBODataSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZBODataSetsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZBODataSetsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODataSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZBODataSets_SystemCode_ClassName_DataSetSystemCode_DataSetID(SystemCode, ClassName, DataSetSystemCode, DataSetID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZBODataSet item
   Description: Calls GetByID to retrieve the ZBODataSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZBODataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param DataSetSystemCode: Desc: DataSetSystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZBODataSetsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODataSets(" + SystemCode + "," + ClassName + "," + DataSetSystemCode + "," + DataSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZBODataSets_SystemCode_ClassName_DataSetSystemCode_DataSetID(SystemCode, ClassName, DataSetSystemCode, DataSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZBODataSet for the service
   Description: Calls UpdateExt to update ZBODataSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZBODataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param DataSetSystemCode: Desc: DataSetSystemCode   Required: True   Allow empty value : True
      :param DataSetID: Desc: DataSetID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZBODataSetsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODataSets(" + SystemCode + "," + ClassName + "," + DataSetSystemCode + "," + DataSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZBODataSets_SystemCode_ClassName_DataSetSystemCode_DataSetID(SystemCode, ClassName, DataSetSystemCode, DataSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZBODataSet item
   Description: Call UpdateExt to delete ZBODataSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZBODataSet
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param DataSetSystemCode: Desc: DataSetSystemCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZBODataSets(" + SystemCode + "," + ClassName + "," + DataSetSystemCode + "," + DataSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_ZServiceLicenseTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ZServiceLicenseTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZServiceLicenseTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZServiceLicenseTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZServiceLicenseTypes",headers=creds) as resp:
           return await resp.json()

async def post_ZServiceLicenseTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZServiceLicenseTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZServiceLicenseTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.ZServiceLicenseTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZServiceLicenseTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ZServiceLicenseTypes_SystemCode_ClassName_LicenceTypeID(SystemCode, ClassName, LicenceTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ZServiceLicenseType item
   Description: Calls GetByID to retrieve the ZServiceLicenseType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZServiceLicenseType
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param LicenceTypeID: Desc: LicenceTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.ZServiceLicenseTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZServiceLicenseTypes(" + SystemCode + "," + ClassName + "," + LicenceTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ZServiceLicenseTypes_SystemCode_ClassName_LicenceTypeID(SystemCode, ClassName, LicenceTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ZServiceLicenseType for the service
   Description: Calls UpdateExt to update ZServiceLicenseType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZServiceLicenseType
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param LicenceTypeID: Desc: LicenceTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZServiceLicenseTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZServiceLicenseTypes(" + SystemCode + "," + ClassName + "," + LicenceTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ZServiceLicenseTypes_SystemCode_ClassName_LicenceTypeID(SystemCode, ClassName, LicenceTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ZServiceLicenseType item
   Description: Call UpdateExt to delete ZServiceLicenseType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZServiceLicenseType
      :param SystemCode: Desc: SystemCode   Required: True   Allow empty value : True
      :param ClassName: Desc: ClassName   Required: True   Allow empty value : True
      :param LicenceTypeID: Desc: LicenceTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/ZServiceLicenseTypes(" + SystemCode + "," + ClassName + "," + LicenceTypeID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZBODefListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseZBODef, whereClauseZBODataSets, whereClauseZServiceLicenseType, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseZBODef=" + whereClauseZBODef
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZBODataSets=" + whereClauseZBODataSets
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseZServiceLicenseType=" + whereClauseZServiceLicenseType
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(systemCode, className, epicorHeaders = None):
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
   params += "className=" + className

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZBODef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZBODef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZBODef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZBODef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZBODef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZBODataSets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZBODataSets
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZBODataSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZBODataSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZBODataSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewZServiceLicenseType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewZServiceLicenseType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZServiceLicenseType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewZServiceLicenseType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZServiceLicenseType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ZBODefSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZBODataSetsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZBODataSetsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZBODefListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZBODefListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZBODefRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZBODefRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZServiceLicenseTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_ZServiceLicenseTypeRow] = obj["value"]
      pass

class Ice_Tablesets_ZBODataSetsRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  Class Name  """  
      self.DataSetSystemCode:str = obj["DataSetSystemCode"]
      """  DataSetSystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  Data Set ID  """  
      self.IsMainDataSet:bool = obj["IsMainDataSet"]
      """  Indicates DataSet as Main Data Set  """  
      self.IsListDataSet:bool = obj["IsListDataSet"]
      """  Indicates DataSet as List Data Set  """  
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

class Ice_Tablesets_ZBODefListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Object Namespace  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ClassType:str = obj["ClassType"]
      """  Class Type  """  
      self.RequiredModules:str = obj["RequiredModules"]
      """  A delimited list of the modules required by this object.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this Object is complete. If No then object cannot be generated. This is primarily used to exclude objects which are in the early stages development from mass regeneration.  """  
      self.Author:str = obj["Author"]
      """  Author  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation Date  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZBODefRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Object Namespace  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ClassType:str = obj["ClassType"]
      """  Class Type  """  
      self.RequiredModules:str = obj["RequiredModules"]
      """  A delimited list of the modules required by this object.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this Object is complete. If No then object cannot be generated. This is primarily used to exclude objects which are in the early stages development from mass regeneration.  """  
      self.Author:str = obj["Author"]
      """  Author  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation Date  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.AllowMultiRowUpdate:bool = obj["AllowMultiRowUpdate"]
      """  Allow Multi Row Update  """  
      self.UseCurrentCompany:bool = obj["UseCurrentCompany"]
      """  UseCurrentCompany  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HighVolumeImportEnabled:bool = obj["HighVolumeImportEnabled"]
      """  HighVolumeImportEnabled  """  
      self.EcfFlags:int = obj["EcfFlags"]
      """  EcfFlags  """  
      self.LicenseTypeDefaultAccess:int = obj["LicenseTypeDefaultAccess"]
      """  LicenseTypeDefaultAccess  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZServiceLicenseTypeRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  ClassName  """  
      self.LicenceTypeID:str = obj["LicenceTypeID"]
      """  LicenceTypeID  """  
      self.AccessLevel:int = obj["AccessLevel"]
      """  AccessLevel  """  
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
   systemCode
   className
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.className:str = obj["className"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   systemCode
   className
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      self.className:str = obj["className"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZBODefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZBODefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZBODefTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ZBODefListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewZBODataSets_input:
   """ Required : 
   ds
   systemCode
   className
   dataSetSystemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.className:str = obj["className"]
      self.dataSetSystemCode:str = obj["dataSetSystemCode"]
      pass

class GetNewZBODataSets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZBODef_input:
   """ Required : 
   ds
   systemCode
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      pass

class GetNewZBODef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewZServiceLicenseType_input:
   """ Required : 
   ds
   systemCode
   className
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      self.systemCode:str = obj["systemCode"]
      self.className:str = obj["className"]
      pass

class GetNewZServiceLicenseType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseZBODef
   whereClauseZBODataSets
   whereClauseZServiceLicenseType
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseZBODef:str = obj["whereClauseZBODef"]
      self.whereClauseZBODataSets:str = obj["whereClauseZBODataSets"]
      self.whereClauseZServiceLicenseType:str = obj["whereClauseZServiceLicenseType"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ZBODefTableset] = obj["returnObj"]
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

class Ice_Tablesets_UpdExtZBODefTableset:
   def __init__(self, obj):
      self.ZBODef:list[Ice_Tablesets_ZBODefRow] = obj["ZBODef"]
      self.ZBODataSets:list[Ice_Tablesets_ZBODataSetsRow] = obj["ZBODataSets"]
      self.ZServiceLicenseType:list[Ice_Tablesets_ZServiceLicenseTypeRow] = obj["ZServiceLicenseType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZBODataSetsRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  Class Name  """  
      self.DataSetSystemCode:str = obj["DataSetSystemCode"]
      """  DataSetSystemCode  """  
      self.DataSetID:str = obj["DataSetID"]
      """  Data Set ID  """  
      self.IsMainDataSet:bool = obj["IsMainDataSet"]
      """  Indicates DataSet as Main Data Set  """  
      self.IsListDataSet:bool = obj["IsListDataSet"]
      """  Indicates DataSet as List Data Set  """  
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

class Ice_Tablesets_ZBODefListRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Object Namespace  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ClassType:str = obj["ClassType"]
      """  Class Type  """  
      self.RequiredModules:str = obj["RequiredModules"]
      """  A delimited list of the modules required by this object.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this Object is complete. If No then object cannot be generated. This is primarily used to exclude objects which are in the early stages development from mass regeneration.  """  
      self.Author:str = obj["Author"]
      """  Author  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation Date  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZBODefListTableset:
   def __init__(self, obj):
      self.ZBODefList:list[Ice_Tablesets_ZBODefListRow] = obj["ZBODefList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZBODefRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Object Namespace  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.ClassType:str = obj["ClassType"]
      """  Class Type  """  
      self.RequiredModules:str = obj["RequiredModules"]
      """  A delimited list of the modules required by this object.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this Object is complete. If No then object cannot be generated. This is primarily used to exclude objects which are in the early stages development from mass regeneration.  """  
      self.Author:str = obj["Author"]
      """  Author  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Creation Date  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.AllowMultiRowUpdate:bool = obj["AllowMultiRowUpdate"]
      """  Allow Multi Row Update  """  
      self.UseCurrentCompany:bool = obj["UseCurrentCompany"]
      """  UseCurrentCompany  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HighVolumeImportEnabled:bool = obj["HighVolumeImportEnabled"]
      """  HighVolumeImportEnabled  """  
      self.EcfFlags:int = obj["EcfFlags"]
      """  EcfFlags  """  
      self.LicenseTypeDefaultAccess:int = obj["LicenseTypeDefaultAccess"]
      """  LicenseTypeDefaultAccess  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ZBODefTableset:
   def __init__(self, obj):
      self.ZBODef:list[Ice_Tablesets_ZBODefRow] = obj["ZBODef"]
      self.ZBODataSets:list[Ice_Tablesets_ZBODataSetsRow] = obj["ZBODataSets"]
      self.ZServiceLicenseType:list[Ice_Tablesets_ZServiceLicenseTypeRow] = obj["ZServiceLicenseType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ZServiceLicenseTypeRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      """  SystemCode  """  
      self.ClassName:str = obj["ClassName"]
      """  ClassName  """  
      self.LicenceTypeID:str = obj["LicenceTypeID"]
      """  LicenceTypeID  """  
      self.AccessLevel:int = obj["AccessLevel"]
      """  AccessLevel  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
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
      self.ds:list[Ice_Tablesets_UpdExtZBODefTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtZBODefTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ZBODefTableset] = obj["ds"]
      pass

      """  output parameters  """  

