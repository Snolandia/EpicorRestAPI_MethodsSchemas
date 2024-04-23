import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AssetAddEntrySvc
# Description: FA Asset Addition Entry Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AssetAddEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AssetAddEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetAddEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries",headers=creds) as resp:
           return await resp.json()

async def post_AssetAddEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetAddEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AssetAddEntries_Company_AssetNum_AdditionNum(Company, AssetNum, AdditionNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AssetAddEntry item
   Description: Calls GetByID to retrieve the AssetAddEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetAddEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AssetAddEntries_Company_AssetNum_AdditionNum(Company, AssetNum, AdditionNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AssetAddEntry for the service
   Description: Calls UpdateExt to update AssetAddEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetAddEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAAdditionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AssetAddEntries_Company_AssetNum_AdditionNum(Company, AssetNum, AdditionNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AssetAddEntry item
   Description: Call UpdateExt to delete AssetAddEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetAddEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAddRegs(Company, AssetNum, AdditionNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FAAddRegs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAAddRegs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAddRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAddRegs",headers=creds) as resp:
           return await resp.json()

async def get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company, AssetNum, AdditionNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAAddReg item
   Description: Calls GetByID to retrieve the FAAddReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAddReg1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAdditionAttches(Company, AssetNum, AdditionNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get FAAdditionAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAAdditionAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAdditionAttches",headers=creds) as resp:
           return await resp.json()

async def get_AssetAddEntries_Company_AssetNum_AdditionNum_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company, AssetNum, AdditionNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAAdditionAttch item
   Description: Calls GetByID to retrieve the FAAdditionAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAdditionAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/AssetAddEntries(" + Company + "," + AssetNum + "," + AdditionNum + ")/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAAddRegs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAAddRegs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAAddRegs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAddRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs",headers=creds) as resp:
           return await resp.json()

async def post_FAAddRegs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAAddRegs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company, AssetNum, AdditionNum, AssetRegID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAAddReg item
   Description: Calls GetByID to retrieve the FAAddReg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAddReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company, AssetNum, AdditionNum, AssetRegID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAAddReg for the service
   Description: Calls UpdateExt to update FAAddReg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAAddReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAAddRegRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAAddRegs_Company_AssetNum_AdditionNum_AssetRegID(Company, AssetNum, AdditionNum, AssetRegID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAAddReg item
   Description: Call UpdateExt to delete FAAddReg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAAddReg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param AssetRegID: Desc: AssetRegID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAddRegs(" + Company + "," + AssetNum + "," + AdditionNum + "," + AssetRegID + ")",headers=creds) as resp:
           return await resp.json()

async def get_FAAdditionAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get FAAdditionAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAAdditionAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches",headers=creds) as resp:
           return await resp.json()

async def post_FAAdditionAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAAdditionAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company, AssetNum, AdditionNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the FAAdditionAttch item
   Description: Calls GetByID to retrieve the FAAdditionAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAAdditionAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company, AssetNum, AdditionNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update FAAdditionAttch for the service
   Description: Calls UpdateExt to update FAAdditionAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAAdditionAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAAdditionAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_FAAdditionAttches_Company_AssetNum_AdditionNum_DrawingSeq(Company, AssetNum, AdditionNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete FAAdditionAttch item
   Description: Call UpdateExt to delete FAAdditionAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAAdditionAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param AssetNum: Desc: AssetNum   Required: True   Allow empty value : True
      :param AdditionNum: Desc: AdditionNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/FAAdditionAttches(" + Company + "," + AssetNum + "," + AdditionNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SelectedSerialNumbers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SelectedSerialNumbers
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers",headers=creds) as resp:
           return await resp.json()

async def post_SelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SelectedSerialNumber item
   Description: Calls GetByID to retrieve the SelectedSerialNumber item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SelectedSerialNumber for the service
   Description: Calls UpdateExt to update SelectedSerialNumber. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SelectedSerialNumbersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SelectedSerialNumbers_Company_PartNum_SerialNumber(Company, PartNum, SerialNumber, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SelectedSerialNumber item
   Description: Call UpdateExt to delete SelectedSerialNumber item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SelectedSerialNumber
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param SerialNumber: Desc: SerialNumber   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
           return await resp.json()

async def get_SNFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SNFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SNFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats",headers=creds) as resp:
           return await resp.json()

async def post_SNFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SNFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SNFormat item
   Description: Calls GetByID to retrieve the SNFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SNFormat for the service
   Description: Calls UpdateExt to update SNFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SNFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SNFormats_Company_PartNum_Plant(Company, PartNum, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SNFormat item
   Description: Call UpdateExt to delete SNFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SNFormat
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAAdditionListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseFAAddition, whereClauseFAAdditionAttch, whereClauseFAAddReg, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseFAAddition=" + whereClauseFAAddition
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFAAdditionAttch=" + whereClauseFAAdditionAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseFAAddReg=" + whereClauseFAAddReg
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSelectedSerialNumbers=" + whereClauseSelectedSerialNumbers
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSNFormat=" + whereClauseSNFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(assetNum, additionNum, epicorHeaders = None):
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
   params += "assetNum=" + assetNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "additionNum=" + additionNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckAssetTransactions(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckAssetTransactions
   Description: Checks if there are any transactions for this Asset marked as Ready To Post
   OperationID: CheckAssetTransactions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckAssetTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearReadyToPost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearReadyToPost
   Description: Clears Ready To Post flag on Asset transactions with SysRowID different from the one provided
   OperationID: ClearReadyToPost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveAdded(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveAdded
   Description: To be called on leave of FAAddition.Added field to update costs based on
new exchange rate derived from this apply date.
   OperationID: LeaveAdded
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAdded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAdded_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveAdditionCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveAdditionCost
   Description: To be called on leave of addition cost field to update the Book Value field.
   OperationID: LeaveAdditionCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAdditionCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAdditionCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveAdditionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveAdditionType
   Description: To be called on leave of AdditionType field
   OperationID: LeaveAdditionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveAdditionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveAdditionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveGrantAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveGrantAmt
   Description: To be called on leave of grant amount field to update the Book Value field.
   OperationID: LeaveGrantAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveGrantAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveGrantAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveInvoiceLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveInvoiceLine
   Description: Called on the leave of FAAddition.InvoiceLine for validation purpose.
   OperationID: LeaveInvoiceLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveInvoiceNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveInvoiceNum
   Description: Called on the leave of Invoice Number for validation purpose.
   OperationID: LeaveInvoiceNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveJobNum
   Description: To be called on leave of Job Number field for validating an existing Job.
   OperationID: LeaveJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveLotNum
   Description: To be called on leave of FAAddition.LotNum field
   OperationID: LeaveLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeavePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeavePartNum
   Description: To be called on leave of FAAddition.PartNum field
   OperationID: LeavePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeavePONum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeavePONum
   Description: To be called on leave of VendorID field to validate an existing PO
   OperationID: LeavePONum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeavePONum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeavePONum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveRegCurrDepreciation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveRegCurrDepreciation
   Description: To be called on leave of FAAddReg.CurrDepreciation field to update the Book Value field.
   OperationID: LeaveRegCurrDepreciation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegCurrDepreciation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegCurrDepreciation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveRegCurrGrantDep(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveRegCurrGrantDep
   Description: To be called on leave of FAAddReg.CurrGrantDep field to update the Grant Book Value field.
   OperationID: LeaveRegCurrGrantDep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegCurrGrantDep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegCurrGrantDep_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveRegPrevDepreciation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveRegPrevDepreciation
   Description: To be called on leave of FAAddReg.PrevDepreciation field to update the Book Value field.
   OperationID: LeaveRegPrevDepreciation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegPrevDepreciation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegPrevDepreciation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveRegPrevGrantDep(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveRegPrevGrantDep
   Description: To be called on leave of FAAddReg.PrevGrantDep field to update the Grant Book Value field.
   OperationID: LeaveRegPrevGrantDep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveRegPrevGrantDep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveRegPrevGrantDep_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveTransferQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveTransferQty
   Description: To be called on leave of FAAddition.TransferQty field. This qty is always expressed in IUM.
   OperationID: LeaveTransferQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveTransferQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveTransferQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveVendorID
   Description: To be called on leave of VendorID field to validate an existing Vendor
   OperationID: LeaveVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LeaveWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LeaveWarehouse
   Description: To be called on leave of FAAddition.WarehouseCode field.
   OperationID: LeaveWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LeaveWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LeaveWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: To be called before Update
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePlaceInServDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePlaceInServDate
   OperationID: ChangePlaceInServDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePlaceInServDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePlaceInServDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:  sets up the parameters for invoking the Serial Number Selection form
Notes:
<param name="ds">Asset Addition DataSet</param><returns>The SelectSerialNumbersParams dataset</returns>
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number scanned in the serial number selection form is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will retrieve the serial numbers for FAAddition record and
update the SelectedSerialNumbers table with these records.
   OperationID: GetSelectedSerialNumbers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAAddition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAAddition
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAAddition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAAddition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAAddition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAAdditionAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAAdditionAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAAdditionAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAAdditionAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAAdditionAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewFAAddReg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewFAAddReg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAAddReg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewFAAddReg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAAddReg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AssetAddEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAddRegRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAAddRegRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAAdditionAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAAdditionListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAAdditionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_FAAdditionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SNFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["value"]
      pass

class Erp_Tablesets_FAAddRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.PrevDepreciation:int = obj["PrevDepreciation"]
      """  The depreciation already applied to this addition in another system in previous years. Applies to inter-group transfers only.  """  
      self.CurrDepreciation:int = obj["CurrDepreciation"]
      """  The depreciation already applied to this addition in another system within the same holding company for this year. This amount is only posted to the balance sheet and not as charge to the P&L, because the the charge has already been charged in a sister company.  """  
      self.BookValue:int = obj["BookValue"]
      """  Book Value of the addition is a calculated field. It is Addition Cost minus previous years Addition Depreciation minus current year Addition Depreciation.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.PrevGrantDep:int = obj["PrevGrantDep"]
      """  The Grant Depreciation already applied to the grant addition from another system for previous years. Applies to inter-group transfers only.  """  
      self.CurrGrantDep:int = obj["CurrGrantDep"]
      """  The Grant Depreciation already applied to the grant addition from another system for the current year. Applies to inter-group transfers only.  """  
      self.DocPrevDepreciation:int = obj["DocPrevDepreciation"]
      """  The depreciation already applied to this addition in another system in previous years in the specified currency. Applies to inter-group transfers only.  """  
      self.DocCurrDepreciation:int = obj["DocCurrDepreciation"]
      """  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  This is the Addition Book Value in the specified currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.DocPrevGrantDep:int = obj["DocPrevGrantDep"]
      """  The previous years grant depreciation for this addition in the specified currency.  """  
      self.DocCurrGrantDep:int = obj["DocCurrGrantDep"]
      """  The current year grant depreciation for this addition in the specified currency.  """  
      self.Rpt1PrevDepreciation:int = obj["Rpt1PrevDepreciation"]
      """  Reporting currency value of the previous years addition depreciation.  """  
      self.Rpt1CurrDepreciation:int = obj["Rpt1CurrDepreciation"]
      """  Reporting currency value of the current year addition depreciation.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  Reporting currency value of the addition book value.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.Rpt1PrevGrantDep:int = obj["Rpt1PrevGrantDep"]
      """  Reporting currency value of the previous years addition grant depreciation.  """  
      self.Rpt1CurrGrantDep:int = obj["Rpt1CurrGrantDep"]
      """  Reporting currency value of the current year addition grant depreciation.  """  
      self.Rpt2PrevDepreciation:int = obj["Rpt2PrevDepreciation"]
      """  Reporting currency value of the previous years addition depreciation.  """  
      self.Rpt2CurrDepreciation:int = obj["Rpt2CurrDepreciation"]
      """  Reporting currency value of the current year addition depreciation.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  Reporting currency value of the addition book value.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.Rpt2PrevGrantDep:int = obj["Rpt2PrevGrantDep"]
      """  Reporting currency value of the previous years addition grant depreciation.  """  
      self.Rpt2CurrGrantDep:int = obj["Rpt2CurrGrantDep"]
      """  Reporting currency value of the current year addition grant depreciation.  """  
      self.Rpt3PrevDepreciation:int = obj["Rpt3PrevDepreciation"]
      """  Reporting currency value of the previous years addition depreciation.  """  
      self.Rpt3CurrDepreciation:int = obj["Rpt3CurrDepreciation"]
      """  Reporting currency value of the current year addition depreciation.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  Reporting currency value of the addition book value.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.Rpt3PrevGrantDep:int = obj["Rpt3PrevGrantDep"]
      """  Reporting currency value of the previous years addtion grant depreciation.  """  
      self.Rpt3CurrGrantDep:int = obj["Rpt3CurrGrantDep"]
      """  Reporting currency value of the current year addition grant depreciation.  """  
      self.AdditionCost:int = obj["AdditionCost"]
      """  The cost added to the asset.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.DocAdditionCost:int = obj["DocAdditionCost"]
      """  The cost added to the asset in the currency specified.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1AdditionCost:int = obj["Rpt1AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2AdditionCost:int = obj["Rpt2AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3AdditionCost:int = obj["Rpt3AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.AdditionCostLimit:int = obj["AdditionCostLimit"]
      """  The cost added to the asset.  """  
      self.DocAdditionCostLimit:int = obj["DocAdditionCostLimit"]
      """  The cost added to the asset in the currency specified.  """  
      self.Rpt1AdditionCostLimit:int = obj["Rpt1AdditionCostLimit"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2AdditionCostLimit:int = obj["Rpt2AdditionCostLimit"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3AdditionCostLimit:int = obj["Rpt3AdditionCostLimit"]
      """  Reporting currency value of the Addition Cost.  """  
      self.CostVariance:int = obj["CostVariance"]
      """  The cost added to the asset.  """  
      self.DocCostVariance:int = obj["DocCostVariance"]
      """  The cost added to the asset in the currency specified.  """  
      self.Rpt1CostVariance:int = obj["Rpt1CostVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2CostVariance:int = obj["Rpt2CostVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3CostVariance:int = obj["Rpt3CostVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.GrantVariance:int = obj["GrantVariance"]
      """  The cost added to the asset.  """  
      self.DocGrantVariance:int = obj["DocGrantVariance"]
      """  The cost added to the asset in the currency specified.  """  
      self.Rpt1GrantVariance:int = obj["Rpt1GrantVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantVariance:int = obj["Rpt2GrantVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantVariance:int = obj["Rpt3GrantVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InclCurrPerDepn:bool = obj["InclCurrPerDepn"]
      """  InclCurrPerDepn  """  
      self.AffectsAssetLife:bool = obj["AffectsAssetLife"]
      """  Affects Asset Life  """  
      self.NewAssetLife:int = obj["NewAssetLife"]
      """  New Asset Estimated Life  """  
      self.NewLifeModifier:str = obj["NewLifeModifier"]
      """  New Life Modifier. Available Values (PERIODS or YEARS)  """  
      self.DisableInclCurrPerDepn:bool = obj["DisableInclCurrPerDepn"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.CurrCode:str = obj["CurrCode"]
      """  Currency Code  """  
      self.CurrAssetLife:int = obj["CurrAssetLife"]
      """  Current Asset Estimated Life  """  
      self.CurrLifeModifier:str = obj["CurrLifeModifier"]
      """  Current Life Modifier  """  
      self.CurrAssetLifeDisplay:str = obj["CurrAssetLifeDisplay"]
      """  Current Asset Estimated Life  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FAssetAssetDescription:str = obj["FAssetAssetDescription"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAAdditionAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.AdditionNum:int = obj["AdditionNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAAdditionListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition of an asset.  """  
      self.Added:str = obj["Added"]
      """  The date of Addition  """  
      self.AdditionCost:int = obj["AdditionCost"]
      """  The cost added to the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Addition.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor of the Addition. Defaulted from the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The Vendors invoice number. Defaulted from the Asset.  """  
      self.PONum:int = obj["PONum"]
      """  The vendors PO number of the Addition. Defaulted from the asset.  """  
      self.JobNum:str = obj["JobNum"]
      """  The jobnumber that created the Addition. Defaulted from the asset.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  A freeform field to indicate the location of the addition.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the addition.  """  
      self.Model:str = obj["Model"]
      """  The model number of addition.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the addition.  """  
      self.NewAsset:bool = obj["NewAsset"]
      """  Indicator to express if this addition is bought new.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the addition to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the addition is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the addition is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the addition is allowed to be posted to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.AdditionType:str = obj["AdditionType"]
      """  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice Line of the related or linked AP Invoice.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this addition transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.DocAdditionCost:int = obj["DocAdditionCost"]
      """  The cost added to the asset in the currency specified.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1AdditionCost:int = obj["Rpt1AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2AdditionCost:int = obj["Rpt2AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3AdditionCost:int = obj["Rpt3AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.InterGroup:bool = obj["InterGroup"]
      """  Indicates if the miscellaneous addition is for an Inter-Group addition.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  AssetSeq - used to setup relationship with FAsset table  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.WhseDescription:str = obj["WhseDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAAdditionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition of an asset.  """  
      self.Added:str = obj["Added"]
      """  The date of Addition  """  
      self.AdditionCost:int = obj["AdditionCost"]
      """  The cost added to the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Addition.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor of the Addition. Defaulted from the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The Vendors invoice number. Defaulted from the Asset.  """  
      self.PONum:int = obj["PONum"]
      """  The vendors PO number of the Addition. Defaulted from the asset.  """  
      self.JobNum:str = obj["JobNum"]
      """  The jobnumber that created the Addition. Defaulted from the asset.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  A freeform field to indicate the location of the addition.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the addition.  """  
      self.Model:str = obj["Model"]
      """  The model number of addition.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the addition.  """  
      self.NewAsset:bool = obj["NewAsset"]
      """  Indicator to express if this addition is bought new.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the addition to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the addition is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the addition is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the addition is allowed to be posted to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.AdditionType:str = obj["AdditionType"]
      """  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice Line of the related or linked AP Invoice.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this addition transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.DocAdditionCost:int = obj["DocAdditionCost"]
      """  The cost added to the asset in the currency specified.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1AdditionCost:int = obj["Rpt1AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2AdditionCost:int = obj["Rpt2AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3AdditionCost:int = obj["Rpt3AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.InterGroup:bool = obj["InterGroup"]
      """  Indicates if the miscellaneous addition is for an Inter-Group addition.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.COIsOneTime:bool = obj["COIsOneTime"]
      """  COIsOneTime  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  AssetSeq - used to setup relationship with FAsset table  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether the serial numbers are required in AssetAddEntry  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.SuppressDateWarning:bool = obj["SuppressDateWarning"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.WhseDescription:str = obj["WhseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat1:str = obj["SNFormat1"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangePlaceInServDate_input:
   """ Required : 
   dateKind
   ds
   """  
   def __init__(self, obj):
      self.dateKind:str = obj["dateKind"]
      """  Acquired date of Place In Service date  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class ChangePlaceInServDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAssetTransactions_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class CheckAssetTransactions_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: an empty string  """  
      pass

class ClearReadyToPost_input:
   """ Required : 
   assetNum
   sysRowID
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  Asset ID  """  
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID to be excluded from search  """  
      pass

class ClearReadyToPost_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   assetNum
   additionNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.additionNum:int = obj["additionNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AssetAddEntryTableset:
   def __init__(self, obj):
      self.FAAddition:list[Erp_Tablesets_FAAdditionRow] = obj["FAAddition"]
      self.FAAdditionAttch:list[Erp_Tablesets_FAAdditionAttchRow] = obj["FAAdditionAttch"]
      self.FAAddReg:list[Erp_Tablesets_FAAddRegRow] = obj["FAAddReg"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAAddRegRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition of an asset.  """  
      self.AssetRegID:str = obj["AssetRegID"]
      """  Identifier of the Asset Register.  """  
      self.PrevDepreciation:int = obj["PrevDepreciation"]
      """  The depreciation already applied to this addition in another system in previous years. Applies to inter-group transfers only.  """  
      self.CurrDepreciation:int = obj["CurrDepreciation"]
      """  The depreciation already applied to this addition in another system within the same holding company for this year. This amount is only posted to the balance sheet and not as charge to the P&L, because the the charge has already been charged in a sister company.  """  
      self.BookValue:int = obj["BookValue"]
      """  Book Value of the addition is a calculated field. It is Addition Cost minus previous years Addition Depreciation minus current year Addition Depreciation.  """  
      self.GrantBookValue:int = obj["GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.PrevGrantDep:int = obj["PrevGrantDep"]
      """  The Grant Depreciation already applied to the grant addition from another system for previous years. Applies to inter-group transfers only.  """  
      self.CurrGrantDep:int = obj["CurrGrantDep"]
      """  The Grant Depreciation already applied to the grant addition from another system for the current year. Applies to inter-group transfers only.  """  
      self.DocPrevDepreciation:int = obj["DocPrevDepreciation"]
      """  The depreciation already applied to this addition in another system in previous years in the specified currency. Applies to inter-group transfers only.  """  
      self.DocCurrDepreciation:int = obj["DocCurrDepreciation"]
      """  The depreciation already applied to this addition in another system within the same holding company for this year in the specified currency.  """  
      self.DocBookValue:int = obj["DocBookValue"]
      """  This is the Addition Book Value in the specified currency.  """  
      self.DocGrantBookValue:int = obj["DocGrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.DocPrevGrantDep:int = obj["DocPrevGrantDep"]
      """  The previous years grant depreciation for this addition in the specified currency.  """  
      self.DocCurrGrantDep:int = obj["DocCurrGrantDep"]
      """  The current year grant depreciation for this addition in the specified currency.  """  
      self.Rpt1PrevDepreciation:int = obj["Rpt1PrevDepreciation"]
      """  Reporting currency value of the previous years addition depreciation.  """  
      self.Rpt1CurrDepreciation:int = obj["Rpt1CurrDepreciation"]
      """  Reporting currency value of the current year addition depreciation.  """  
      self.Rpt1BookValue:int = obj["Rpt1BookValue"]
      """  Reporting currency value of the addition book value.  """  
      self.Rpt1GrantBookValue:int = obj["Rpt1GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.Rpt1PrevGrantDep:int = obj["Rpt1PrevGrantDep"]
      """  Reporting currency value of the previous years addition grant depreciation.  """  
      self.Rpt1CurrGrantDep:int = obj["Rpt1CurrGrantDep"]
      """  Reporting currency value of the current year addition grant depreciation.  """  
      self.Rpt2PrevDepreciation:int = obj["Rpt2PrevDepreciation"]
      """  Reporting currency value of the previous years addition depreciation.  """  
      self.Rpt2CurrDepreciation:int = obj["Rpt2CurrDepreciation"]
      """  Reporting currency value of the current year addition depreciation.  """  
      self.Rpt2BookValue:int = obj["Rpt2BookValue"]
      """  Reporting currency value of the addition book value.  """  
      self.Rpt2GrantBookValue:int = obj["Rpt2GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.Rpt2PrevGrantDep:int = obj["Rpt2PrevGrantDep"]
      """  Reporting currency value of the previous years addition grant depreciation.  """  
      self.Rpt2CurrGrantDep:int = obj["Rpt2CurrGrantDep"]
      """  Reporting currency value of the current year addition grant depreciation.  """  
      self.Rpt3PrevDepreciation:int = obj["Rpt3PrevDepreciation"]
      """  Reporting currency value of the previous years addition depreciation.  """  
      self.Rpt3CurrDepreciation:int = obj["Rpt3CurrDepreciation"]
      """  Reporting currency value of the current year addition depreciation.  """  
      self.Rpt3BookValue:int = obj["Rpt3BookValue"]
      """  Reporting currency value of the addition book value.  """  
      self.Rpt3GrantBookValue:int = obj["Rpt3GrantBookValue"]
      """  Grant Book Value of the addition is a calculated field. It is Grant Amount minus previous years Addition Grant Depreciation minus current year Addition Grant Depreciation.  """  
      self.Rpt3PrevGrantDep:int = obj["Rpt3PrevGrantDep"]
      """  Reporting currency value of the previous years addtion grant depreciation.  """  
      self.Rpt3CurrGrantDep:int = obj["Rpt3CurrGrantDep"]
      """  Reporting currency value of the current year addition grant depreciation.  """  
      self.AdditionCost:int = obj["AdditionCost"]
      """  The cost added to the asset.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.DocAdditionCost:int = obj["DocAdditionCost"]
      """  The cost added to the asset in the currency specified.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1AdditionCost:int = obj["Rpt1AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2AdditionCost:int = obj["Rpt2AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3AdditionCost:int = obj["Rpt3AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.AdditionCostLimit:int = obj["AdditionCostLimit"]
      """  The cost added to the asset.  """  
      self.DocAdditionCostLimit:int = obj["DocAdditionCostLimit"]
      """  The cost added to the asset in the currency specified.  """  
      self.Rpt1AdditionCostLimit:int = obj["Rpt1AdditionCostLimit"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2AdditionCostLimit:int = obj["Rpt2AdditionCostLimit"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3AdditionCostLimit:int = obj["Rpt3AdditionCostLimit"]
      """  Reporting currency value of the Addition Cost.  """  
      self.CostVariance:int = obj["CostVariance"]
      """  The cost added to the asset.  """  
      self.DocCostVariance:int = obj["DocCostVariance"]
      """  The cost added to the asset in the currency specified.  """  
      self.Rpt1CostVariance:int = obj["Rpt1CostVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2CostVariance:int = obj["Rpt2CostVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3CostVariance:int = obj["Rpt3CostVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.GrantVariance:int = obj["GrantVariance"]
      """  The cost added to the asset.  """  
      self.DocGrantVariance:int = obj["DocGrantVariance"]
      """  The cost added to the asset in the currency specified.  """  
      self.Rpt1GrantVariance:int = obj["Rpt1GrantVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantVariance:int = obj["Rpt2GrantVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantVariance:int = obj["Rpt3GrantVariance"]
      """  Reporting currency value of the Addition Cost.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.InclCurrPerDepn:bool = obj["InclCurrPerDepn"]
      """  InclCurrPerDepn  """  
      self.AffectsAssetLife:bool = obj["AffectsAssetLife"]
      """  Affects Asset Life  """  
      self.NewAssetLife:int = obj["NewAssetLife"]
      """  New Asset Estimated Life  """  
      self.NewLifeModifier:str = obj["NewLifeModifier"]
      """  New Life Modifier. Available Values (PERIODS or YEARS)  """  
      self.DisableInclCurrPerDepn:bool = obj["DisableInclCurrPerDepn"]
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.CurrCode:str = obj["CurrCode"]
      """  Currency Code  """  
      self.CurrAssetLife:int = obj["CurrAssetLife"]
      """  Current Asset Estimated Life  """  
      self.CurrLifeModifier:str = obj["CurrLifeModifier"]
      """  Current Life Modifier  """  
      self.CurrAssetLifeDisplay:str = obj["CurrAssetLifeDisplay"]
      """  Current Asset Estimated Life  """  
      self.BitFlag:int = obj["BitFlag"]
      self.FAssetAssetDescription:str = obj["FAssetAssetDescription"]
      self.FAssetRegDescription:str = obj["FAssetRegDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAAdditionAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.AssetNum:str = obj["AssetNum"]
      self.AdditionNum:int = obj["AdditionNum"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAAdditionListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition of an asset.  """  
      self.Added:str = obj["Added"]
      """  The date of Addition  """  
      self.AdditionCost:int = obj["AdditionCost"]
      """  The cost added to the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Addition.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor of the Addition. Defaulted from the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The Vendors invoice number. Defaulted from the Asset.  """  
      self.PONum:int = obj["PONum"]
      """  The vendors PO number of the Addition. Defaulted from the asset.  """  
      self.JobNum:str = obj["JobNum"]
      """  The jobnumber that created the Addition. Defaulted from the asset.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  A freeform field to indicate the location of the addition.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the addition.  """  
      self.Model:str = obj["Model"]
      """  The model number of addition.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the addition.  """  
      self.NewAsset:bool = obj["NewAsset"]
      """  Indicator to express if this addition is bought new.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the addition to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the addition is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the addition is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the addition is allowed to be posted to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.AdditionType:str = obj["AdditionType"]
      """  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice Line of the related or linked AP Invoice.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this addition transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.DocAdditionCost:int = obj["DocAdditionCost"]
      """  The cost added to the asset in the currency specified.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1AdditionCost:int = obj["Rpt1AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2AdditionCost:int = obj["Rpt2AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3AdditionCost:int = obj["Rpt3AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.InterGroup:bool = obj["InterGroup"]
      """  Indicates if the miscellaneous addition is for an Inter-Group addition.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  AssetSeq - used to setup relationship with FAsset table  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.PartPartDescription:str = obj["PartPartDescription"]
      """  Describes the Part.  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartIUM:str = obj["PartIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartSalesUM:str = obj["PartSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      """  Long Description of a unit of measure. Mandatory.  """  
      self.WhseDescription:str = obj["WhseDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_FAAdditionListTableset:
   def __init__(self, obj):
      self.FAAdditionList:list[Erp_Tablesets_FAAdditionListRow] = obj["FAAdditionList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_FAAdditionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company of the Addition.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Asset number of the Addition.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition of an asset.  """  
      self.Added:str = obj["Added"]
      """  The date of Addition  """  
      self.AdditionCost:int = obj["AdditionCost"]
      """  The cost added to the asset.  """  
      self.Description:str = obj["Description"]
      """  Description of the Addition.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The vendor of the Addition. Defaulted from the asset.  """  
      self.VendorName:str = obj["VendorName"]
      """  The Vendorname of the vendor of the addtion. The Vendor name can be entered without entering a vendor. Defaulted from the asset.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The Vendors invoice number. Defaulted from the Asset.  """  
      self.PONum:int = obj["PONum"]
      """  The vendors PO number of the Addition. Defaulted from the asset.  """  
      self.JobNum:str = obj["JobNum"]
      """  The jobnumber that created the Addition. Defaulted from the asset.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  The warehouse where the addition is stored. This is for information purposes only. In the warehouse tracker no assets can be tracked.  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin where the addition is stored. This is for information purposes only. In the bin tracker no assets can be tracked.  """  
      self.Location:str = obj["Location"]
      """  A freeform field to indicate the location of the addition.  """  
      self.Manufacturer:str = obj["Manufacturer"]
      """  The original manufacturer of the addition.  """  
      self.Model:str = obj["Model"]
      """  The model number of addition.  """  
      self.Serialno:str = obj["Serialno"]
      """  The serial number of the addition.  """  
      self.NewAsset:bool = obj["NewAsset"]
      """  Indicator to express if this addition is bought new.  """  
      self.Posted:bool = obj["Posted"]
      """  Flag to indicate that the addition is posted to the GL. After posting modification of the addition is not allowed.  """  
      self.PostDate:str = obj["PostDate"]
      """  Posting date of the addition to the GL.  """  
      self.PostedBy:str = obj["PostedBy"]
      """  The addition is posted by the user.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  The GL journal to which the addition is posted.  """  
      self.JournalNum:int = obj["JournalNum"]
      """  The GL journal number to which the addition is posted.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of posting of the addition to the GL.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The fiscal period of posting of the addition to the GL.  """  
      self.ReadyToPost:bool = obj["ReadyToPost"]
      """  Flag to indicat that the addition is allowed to be posted to the GL.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.GrantAmt:int = obj["GrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge.  """  
      self.AdditionType:str = obj["AdditionType"]
      """  Indicates the type of asset addition activity.  Valid values are: "PURCHASE", "TRANSFER" or "MISC".  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Unique identifier of the currency rate group.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The Invoice Line of the related or linked AP Invoice.  """  
      self.PartNum:str = obj["PartNum"]
      """  Identifies the part number transferred from stock to asset.  This field is only required if the Addition Type is "Transfer".  """  
      self.TransferQty:int = obj["TransferQty"]
      """  Transferred Quantity reported for this addition transfer.  """  
      self.TransferUOM:str = obj["TransferUOM"]
      """  Unit of Measure for the transferred quantity.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number of the transferred part.  """  
      self.DocAdditionCost:int = obj["DocAdditionCost"]
      """  The cost added to the asset in the currency specified.  """  
      self.DocGrantAmt:int = obj["DocGrantAmt"]
      """  The Grant Amount awarded to an asset to reduce the depreciation charge in the currency specified.  """  
      self.Rpt1AdditionCost:int = obj["Rpt1AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt1GrantAmt:int = obj["Rpt1GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt2AdditionCost:int = obj["Rpt2AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt2GrantAmt:int = obj["Rpt2GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.Rpt3AdditionCost:int = obj["Rpt3AdditionCost"]
      """  Reporting currency value of the Addition Cost.  """  
      self.Rpt3GrantAmt:int = obj["Rpt3GrantAmt"]
      """  Reporting currency value of the Grant Amount.  """  
      self.InterGroup:bool = obj["InterGroup"]
      """  Indicates if the miscellaneous addition is for an Inter-Group addition.  """  
      self.LocID:str = obj["LocID"]
      """  Location ID.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code to uniquely identify the Equipment.  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.TransferUnits:int = obj["TransferUnits"]
      """  This is the equivalent number of units for the transferred qty for this asset addition.  There is no unit of measure conversion involved during update of this field.  The user is responsible for the "conversion" of transferred qty to asset units.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HdrCostRecorded:bool = obj["HdrCostRecorded"]
      """  Indicates that the transaction is reflected in FAsset costs.  """  
      self.RecordedRegList:str = obj["RecordedRegList"]
      """  List of Asset Registers in which the transaction is reflected.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.COIsOneTime:bool = obj["COIsOneTime"]
      """  COIsOneTime  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AssetSeq:int = obj["AssetSeq"]
      """  AssetSeq - used to setup relationship with FAsset table  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Indicates whether the serial numbers are required in AssetAddEntry  """  
      self.IsLcked:bool = obj["IsLcked"]
      """  shows if is this addition transaction is blocked in RvLock.  """  
      self.SuppressDateWarning:bool = obj["SuppressDateWarning"]
      self.LockStatus:str = obj["LockStatus"]
      """  Locked means can not be updated or deleted: the addition activity is already in review journal or in posting process.  """  
      self.RvnJrnUID:int = obj["RvnJrnUID"]
      """  Review Journal UID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.UOMUOMDesc:str = obj["UOMUOMDesc"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.WhseDescription:str = obj["WhseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtAssetAddEntryTableset:
   def __init__(self, obj):
      self.FAAddition:list[Erp_Tablesets_FAAdditionRow] = obj["FAAddition"]
      self.FAAdditionAttch:list[Erp_Tablesets_FAAdditionAttchRow] = obj["FAAdditionAttch"]
      self.FAAddReg:list[Erp_Tablesets_FAAddRegRow] = obj["FAAddReg"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   assetNum
   additionNum
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      self.additionNum:int = obj["additionNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetAddEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetAddEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AssetAddEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_FAAdditionListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewFAAddReg_input:
   """ Required : 
   ds
   assetNum
   additionNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.additionNum:int = obj["additionNum"]
      pass

class GetNewFAAddReg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAAdditionAttch_input:
   """ Required : 
   ds
   assetNum
   additionNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      self.additionNum:int = obj["additionNum"]
      pass

class GetNewFAAdditionAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewFAAddition_input:
   """ Required : 
   ds
   assetNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.assetNum:str = obj["assetNum"]
      pass

class GetNewFAAddition_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseFAAddition
   whereClauseFAAdditionAttch
   whereClauseFAAddReg
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseFAAddition:str = obj["whereClauseFAAddition"]
      self.whereClauseFAAdditionAttch:str = obj["whereClauseFAAdditionAttch"]
      self.whereClauseFAAddReg:str = obj["whereClauseFAAddReg"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AssetAddEntryTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectedSerialNumbers_input:
   """ Required : 
   company
   assetNum
   additionNum
   ds
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The Asset Number  """  
      self.assetNum:str = obj["assetNum"]
      """  The Asset Number  """  
      self.additionNum:int = obj["additionNum"]
      """  The Addition number  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
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

class LeaveAdded_input:
   """ Required : 
   ipAdded
   ds
   """  
   def __init__(self, obj):
      self.ipAdded:str = obj["ipAdded"]
      """  Added Date that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveAdded_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warning:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveAdditionCost_input:
   """ Required : 
   ipAdditionCost
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipAdditionCost:int = obj["ipAdditionCost"]
      """  AdditionCost that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveAdditionCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveAdditionType_input:
   """ Required : 
   ipAdditionType
   ds
   """  
   def __init__(self, obj):
      self.ipAdditionType:str = obj["ipAdditionType"]
      """  addition type that was selected.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveAdditionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.oSerialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveGrantAmt_input:
   """ Required : 
   ipGrantAmt
   ipbaseordoc
   ds
   """  
   def __init__(self, obj):
      self.ipGrantAmt:int = obj["ipGrantAmt"]
      """  GrantAmt that was entered.  """  
      self.ipbaseordoc:str = obj["ipbaseordoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveGrantAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveInvoiceLine_input:
   """ Required : 
   ipInvoiceLine
   ds
   """  
   def __init__(self, obj):
      self.ipInvoiceLine:int = obj["ipInvoiceLine"]
      """  Invoice Line Number that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveInvoiceLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveInvoiceNum_input:
   """ Required : 
   ipInvoiceNum
   ds
   """  
   def __init__(self, obj):
      self.ipInvoiceNum:str = obj["ipInvoiceNum"]
      """  Invoice Number that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveInvoiceNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveJobNum_input:
   """ Required : 
   IP_JobNum
   ds
   """  
   def __init__(self, obj):
      self.IP_JobNum:str = obj["IP_JobNum"]
      """  Job Number that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveLotNum_input:
   """ Required : 
   ipLotNum
   ds
   """  
   def __init__(self, obj):
      self.ipLotNum:str = obj["ipLotNum"]
      """  Lot Number that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeavePONum_input:
   """ Required : 
   IP_PONum
   ds
   """  
   def __init__(self, obj):
      self.IP_PONum:int = obj["IP_PONum"]
      """  PO Number that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeavePONum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeavePartNum_input:
   """ Required : 
   ipPartNum
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  partnum that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeavePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.oSerialWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveRegCurrDepreciation_input:
   """ Required : 
   ipAssetNum
   ipAdditionNum
   ipAssetRegID
   ipCurrDepreciation
   ipAdditionCost
   ipGrantAmt
   ipBaseOrDoc
   ds
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  asset number  """  
      self.ipAdditionNum:int = obj["ipAdditionNum"]
      """  asset addition number  """  
      self.ipAssetRegID:str = obj["ipAssetRegID"]
      """  asset register ID  """  
      self.ipCurrDepreciation:int = obj["ipCurrDepreciation"]
      """  current depreciation that was entered.  """  
      self.ipAdditionCost:int = obj["ipAdditionCost"]
      """  addition cost  """  
      self.ipGrantAmt:int = obj["ipGrantAmt"]
      """  grant amount  """  
      self.ipBaseOrDoc:str = obj["ipBaseOrDoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveRegCurrDepreciation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveRegCurrGrantDep_input:
   """ Required : 
   ipAssetNum
   ipAdditionNum
   ipAssetRegID
   ipCurrGrantDep
   ipGrantAmt
   ipBaseOrDoc
   ds
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  asset number  """  
      self.ipAdditionNum:int = obj["ipAdditionNum"]
      """  asset addition number  """  
      self.ipAssetRegID:str = obj["ipAssetRegID"]
      """  asset register ID  """  
      self.ipCurrGrantDep:int = obj["ipCurrGrantDep"]
      """  current depreciation that was entered.  """  
      self.ipGrantAmt:int = obj["ipGrantAmt"]
      """  grant amount  """  
      self.ipBaseOrDoc:str = obj["ipBaseOrDoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveRegCurrGrantDep_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveRegPrevDepreciation_input:
   """ Required : 
   ipAssetNum
   ipAdditionNum
   ipAssetRegID
   ipPrevDepreciation
   ipAdditionCost
   ipGrantAmt
   ipBaseOrDoc
   ds
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  asset number  """  
      self.ipAdditionNum:int = obj["ipAdditionNum"]
      """  asset addition number  """  
      self.ipAssetRegID:str = obj["ipAssetRegID"]
      """  asset register ID  """  
      self.ipPrevDepreciation:int = obj["ipPrevDepreciation"]
      """  previous years depreciation that was entered.  """  
      self.ipAdditionCost:int = obj["ipAdditionCost"]
      """  addition cost  """  
      self.ipGrantAmt:int = obj["ipGrantAmt"]
      """  grant amount  """  
      self.ipBaseOrDoc:str = obj["ipBaseOrDoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveRegPrevDepreciation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveRegPrevGrantDep_input:
   """ Required : 
   ipAssetNum
   ipAdditionNum
   ipAssetRegID
   ipPrevGrantDep
   ipGrantAmt
   ipBaseOrDoc
   ds
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  asset number  """  
      self.ipAdditionNum:int = obj["ipAdditionNum"]
      """  asset addition number  """  
      self.ipAssetRegID:str = obj["ipAssetRegID"]
      """  asset register ID  """  
      self.ipPrevGrantDep:int = obj["ipPrevGrantDep"]
      """  current depreciation that was entered.  """  
      self.ipGrantAmt:int = obj["ipGrantAmt"]
      """  grant amount  """  
      self.ipBaseOrDoc:str = obj["ipBaseOrDoc"]
      """  The field type - base or doc  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveRegPrevGrantDep_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveTransferQty_input:
   """ Required : 
   ipTransferQty
   ds
   """  
   def __init__(self, obj):
      self.ipTransferQty:int = obj["ipTransferQty"]
      """  Transfer Qty that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveTransferQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.errorMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class LeaveVendorID_input:
   """ Required : 
   IP_VendorID
   ds
   """  
   def __init__(self, obj):
      self.IP_VendorID:str = obj["IP_VendorID"]
      """  VendorID or SupplierID that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class LeaveWarehouse_input:
   """ Required : 
   ipWarehouseCode
   ds
   """  
   def __init__(self, obj):
      self.ipWarehouseCode:str = obj["ipWarehouseCode"]
      """  Warehouse Code that was entered.  """  
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class LeaveWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.returnMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetAddEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAssetAddEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AssetAddEntryTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

