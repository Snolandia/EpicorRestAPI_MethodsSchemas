import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InspDataTrackerSvc
# Description: The InspDataTracker business object is used to display resulting InspResults
data after the InspResultEntry process has been executing.
            
bo/InspDataTracker/InspDataTracker.p
Brock Mulqueen
10/06/09
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_InspDataTrackers(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspDataTrackers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspDataTrackers
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers",headers=creds) as resp:
           return await resp.json()

async def post_InspDataTrackers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspDataTrackers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspDataTrackers_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspDataTracker item
   Description: Calls GetByID to retrieve the InspDataTracker item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspDataTracker
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspDataTrackers_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspDataTracker for the service
   Description: Calls UpdateExt to update InspDataTracker. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspDataTracker
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspDataTrackers_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspDataTracker item
   Description: Call UpdateExt to delete InspDataTracker item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspDataTracker
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspDataTrackers_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsAttches(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspResultsAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsAttches",headers=creds) as resp:
           return await resp.json()

async def get_InspDataTrackers_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsAttch item
   Description: Calls GetByID to retrieve the InspResultsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspDataTrackers(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsAttches",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsAttch item
   Description: Calls GetByID to retrieve the InspResultsAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsAttch for the service
   Description: Calls UpdateExt to update InspResultsAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsAttch item
   Description: Call UpdateExt to delete InspResultsAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsChars(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsChars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsChars
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCharRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsChars(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsChars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsChar item
   Description: Calls GetByID to retrieve the InspResultsChar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsChar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsChar for the service
   Description: Calls UpdateExt to update InspResultsChar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsChar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCharRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsChar item
   Description: Call UpdateExt to delete InspResultsChar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsChar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCharAttches(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspResultsCharAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsCharAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCharAttches",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsCharAttch item
   Description: Calls GetByID to retrieve the InspResultsCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCharAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCharAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsCharAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsCharAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCharAttches",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsCharAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsCharAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCharAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsCharAttch item
   Description: Calls GetByID to retrieve the InspResultsCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCharAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsCharAttch for the service
   Description: Calls UpdateExt to update InspResultsCharAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsCharAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCharAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsCharAttch item
   Description: Call UpdateExt to delete InspResultsCharAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsCharAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCheckBoxes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsCheckBoxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsCheckBoxes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCheckBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsCheckBoxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsCheckBoxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsCheckBox item
   Description: Calls GetByID to retrieve the InspResultsCheckBox item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCheckBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsCheckBox for the service
   Description: Calls UpdateExt to update InspResultsCheckBox. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsCheckBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsCheckBox item
   Description: Call UpdateExt to delete InspResultsCheckBox item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsCheckBox
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCheckBoxAttches(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspResultsCheckBoxAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsCheckBoxAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCheckBoxAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCheckBoxAttches",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCheckBoxes_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsCheckBoxAttch item
   Description: Calls GetByID to retrieve the InspResultsCheckBoxAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCheckBoxAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxes(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCheckBoxAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsCheckBoxAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsCheckBoxAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsCheckBoxAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxAttches",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsCheckBoxAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsCheckBoxAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsCheckBoxAttch item
   Description: Calls GetByID to retrieve the InspResultsCheckBoxAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsCheckBoxAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsCheckBoxAttch for the service
   Description: Calls UpdateExt to update InspResultsCheckBoxAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsCheckBoxAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsCheckBoxAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsCheckBoxAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsCheckBoxAttch item
   Description: Call UpdateExt to delete InspResultsCheckBoxAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsCheckBoxAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsCheckBoxAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsDates(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsDates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsDates
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsDateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsDates(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsDate item
   Description: Calls GetByID to retrieve the InspResultsDate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsDate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsDate for the service
   Description: Calls UpdateExt to update InspResultsDate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsDate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsDateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsDate item
   Description: Call UpdateExt to delete InspResultsDate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsDate
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsDateAttches(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspResultsDateAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsDateAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsDateAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsDateAttches",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsDates_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsDateAttch item
   Description: Calls GetByID to retrieve the InspResultsDateAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsDateAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDates(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsDateAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsDateAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsDateAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsDateAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDateAttches",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsDateAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsDateAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDateAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsDateAttch item
   Description: Calls GetByID to retrieve the InspResultsDateAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsDateAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsDateAttch for the service
   Description: Calls UpdateExt to update InspResultsDateAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsDateAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsDateAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsDateAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsDateAttch item
   Description: Call UpdateExt to delete InspResultsDateAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsDateAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsDateAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsNums(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsNums items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsNums
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsNumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsNums(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsNums
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsNum item
   Description: Calls GetByID to retrieve the InspResultsNum item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsNum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsNum for the service
   Description: Calls UpdateExt to update InspResultsNum. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsNum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsNumRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsNum item
   Description: Call UpdateExt to delete InspResultsNum item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsNum
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsNumAttches(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspResultsNumAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsNumAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsNumAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsNumAttches",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsNums_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsNumAttch item
   Description: Calls GetByID to retrieve the InspResultsNumAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsNumAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNums(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsNumAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsNumAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsNumAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsNumAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNumAttches",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsNumAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsNumAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNumAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsNumAttch item
   Description: Calls GetByID to retrieve the InspResultsNumAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsNumAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsNumAttch for the service
   Description: Calls UpdateExt to update InspResultsNumAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsNumAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsNumAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsNumAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsNumAttch item
   Description: Call UpdateExt to delete InspResultsNumAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsNumAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsNumAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsShortChars(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsShortChars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsShortChars
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsShortCharRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsShortChars(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsShortChars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsShortChar item
   Description: Calls GetByID to retrieve the InspResultsShortChar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsShortChar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsShortChar for the service
   Description: Calls UpdateExt to update InspResultsShortChar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsShortChar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsShortChar item
   Description: Call UpdateExt to delete InspResultsShortChar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsShortChar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsShortCharAttches(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get InspResultsShortCharAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InspResultsShortCharAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsShortCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsShortCharAttches",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsShortChars_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsShortCharAttch item
   Description: Calls GetByID to retrieve the InspResultsShortCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsShortCharAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortChars(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + ")/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_InspResultsShortCharAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get InspResultsShortCharAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InspResultsShortCharAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsShortCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortCharAttches",headers=creds) as resp:
           return await resp.json()

async def post_InspResultsShortCharAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InspResultsShortCharAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortCharAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the InspResultsShortCharAttch item
   Description: Calls GetByID to retrieve the InspResultsShortCharAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InspResultsShortCharAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update InspResultsShortCharAttch for the service
   Description: Calls UpdateExt to update InspResultsShortCharAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InspResultsShortCharAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.InspResultsShortCharAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_InspResultsShortCharAttches_Company_InspPlanType_File_Key1_Key2_Key3_Key4_Key5_SampleNumber_InspectDate_InspectTime_DrawingSeq(Company, InspPlanType, File, Key1, Key2, Key3, Key4, Key5, SampleNumber, InspectDate, InspectTime, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete InspResultsShortCharAttch item
   Description: Call UpdateExt to delete InspResultsShortCharAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InspResultsShortCharAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param InspPlanType: Desc: InspPlanType   Required: True   Allow empty value : True
      :param File: Desc: File   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param SampleNumber: Desc: SampleNumber   Required: True
      :param InspectDate: Desc: InspectDate   Required: True   Allow empty value : True
      :param InspectTime: Desc: InspectTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/InspResultsShortCharAttches(" + Company + "," + InspPlanType + "," + File + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + SampleNumber + "," + InspectDate + "," + InspectTime + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InspResultsListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseInspResults, whereClauseInspResultsAttch, whereClauseInspResultsChar, whereClauseInspResultsCharAttch, whereClauseInspResultsCheckBox, whereClauseInspResultsCheckBoxAttch, whereClauseInspResultsDate, whereClauseInspResultsDateAttch, whereClauseInspResultsNum, whereClauseInspResultsNumAttch, whereClauseInspResultsShortChar, whereClauseInspResultsShortCharAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseInspResults=" + whereClauseInspResults
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsAttch=" + whereClauseInspResultsAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsChar=" + whereClauseInspResultsChar
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsCharAttch=" + whereClauseInspResultsCharAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsCheckBox=" + whereClauseInspResultsCheckBox
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsCheckBoxAttch=" + whereClauseInspResultsCheckBoxAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsDate=" + whereClauseInspResultsDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsDateAttch=" + whereClauseInspResultsDateAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsNum=" + whereClauseInspResultsNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsNumAttch=" + whereClauseInspResultsNumAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsShortChar=" + whereClauseInspResultsShortChar
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseInspResultsShortCharAttch=" + whereClauseInspResultsShortCharAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(inspPlanType, file, key1, key2, key3, key4, key5, sampleNumber, inspectDate, inspectTime, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "inspPlanType=" + inspPlanType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "file=" + file
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key1=" + key1
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key2=" + key2
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key3=" + key3
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key4=" + key4
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "key5=" + key5
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sampleNumber=" + sampleNumber
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inspectDate=" + inspectDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "inspectTime=" + inspectTime

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetDisplayColumns(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDisplayColumns
   Description: Generate Columns that will be displayed in the grid
   OperationID: GetDisplayColumns
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDisplayColumns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisplayColumns_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInspDataParams(epicorHeaders = None):
   """  
   Summary: Invoke method GetInspDataParams
   Description: Get new ttInspDataParams record
   OperationID: GetInspDataParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspDataParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInspPlanPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInspPlanPartNum
   Description: This method validates the proposed InspPlanNum and updates the related fields.
   OperationID: OnChangeInspPlanPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspPlanPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspPlanPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeInspType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeInspType
   Description: This method wil assign values depending the inspection type selection
This method should be run when the InspDataParam.InspType field changes.
   OperationID: OnChangeInspType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeInspType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeInspType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobAsm
   Description: This method validates the ProposedAssemblySeq, then updates related fields:
            
This method should be run when the InspDataParam.AssemblySeq field changes.
   OperationID: OnChangeJobAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the JobNum, then updates related fields:
This method should be run when the InspDataParam.JobNum field changes.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobOpr
   Description: This method validates the piProposedOprSeq, then updates related fields:
            
This method should be run when the InspDataParam.OprSeq field changes.
   OperationID: OnChangeJobOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeNCMID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeNCMID
   Description: This method validates the non conformance transaction ID, then updates related fields
This method should be run when the InspDataParam.NCMTranID field changes.
   OperationID: OnChangeNCMID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNCMID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNCMID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PackSlipChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PackSlipChanged
   Description: This method validates the piProposedPackSlip, then updates related fields.
            
This method should be run when the InspDataParam.PackSlip field changes.
   OperationID: PackSlipChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PackSlipChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PackSlipChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PackLineChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PackLineChanged
   Description: This method validates the piProposedPackLine
///
   OperationID: PackLineChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PackLineChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PackLineChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePackSlip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePackSlip
   Description: This method validates the piProposedPackSlip, then updates related fields.
            
This method should be run when the InspDataParam.PackSlip field changes.
   OperationID: OnChangePackSlip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePackSlip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePackSlip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: This method validates the piProposedPartNum, then updates related fields.
            
This method should be run when the InspDataParam.PartNum field changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSpecID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSpecID
   Description: This method validates the proposed SpecID and updates the related fields.
   OperationID: OnChangeSpecID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSpecID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSpecID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeVendorID
   Description: This method validates the proposed VendorID, then updates related fields.
   OperationID: OnChangeVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveValues
   Description: Retrieve records that will be displayed in the grid.
   OperationID: RetrieveValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClickToolRetrieveValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClickToolRetrieveValues
   Description: Gets inspection results for entry
   OperationID: ClickToolRetrieveValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClickToolRetrieveValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClickToolRetrieveValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentPlanRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentPlanRev
   Description: To return the default inspection plan revision
   OperationID: GetCurrentPlanRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentPlanRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentPlanRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrentSpecRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrentSpecRev
   Description: To return the default specification revision
   OperationID: GetCurrentSpecRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCurrentSpecRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrentSpecRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInspPlanRevs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInspPlanRevs
   Description: To return the revList values of a given inspection plan
   OperationID: GetInspPlanRevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInspPlanRevs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInspPlanRevs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSpecRevs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSpecRevs
   Description: To return the revList values of a given specification
   OperationID: GetSpecRevs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSpecRevs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSpecRevs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResults
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsChar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsChar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsChar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsChar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsChar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsCharAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsCharAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsCharAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsCharAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsCharAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsCheckBox(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsCheckBox
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsCheckBox
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsCheckBox_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsCheckBox_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsCheckBoxAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsCheckBoxAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsCheckBoxAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsCheckBoxAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsCheckBoxAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsDate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsDateAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsDateAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsDateAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsDateAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsDateAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsNum
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsNumAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsNumAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsNumAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsNumAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsNumAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsShortChar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsShortChar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsShortChar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsShortChar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsShortChar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInspResultsShortCharAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInspResultsShortCharAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInspResultsShortCharAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInspResultsShortCharAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInspResultsShortCharAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InspDataTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsCharAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCharRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsCharRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsCheckBoxAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsCheckBoxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsCheckBoxRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsDateAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsDateRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsDateRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsNumAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsNumRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsNumRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsShortCharAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InspResultsShortCharRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_InspResultsShortCharRow] = obj["value"]
      pass

class Erp_Tablesets_InspResultsAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsCharAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsCharRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Character001:str = obj["Character001"]
      """  Character001  """  
      self.Character002:str = obj["Character002"]
      """  Character002  """  
      self.Character003:str = obj["Character003"]
      """  Character003  """  
      self.Character004:str = obj["Character004"]
      """  Character004  """  
      self.Character005:str = obj["Character005"]
      """  Character005  """  
      self.Character006:str = obj["Character006"]
      """  Character006  """  
      self.Character007:str = obj["Character007"]
      """  Character007  """  
      self.Character008:str = obj["Character008"]
      """  Character008  """  
      self.Character009:str = obj["Character009"]
      """  Character009  """  
      self.Character010:str = obj["Character010"]
      """  Character010  """  
      self.Character011:str = obj["Character011"]
      """  Character011  """  
      self.Character012:str = obj["Character012"]
      """  Character012  """  
      self.Character013:str = obj["Character013"]
      """  Character013  """  
      self.Character014:str = obj["Character014"]
      """  Character014  """  
      self.Character015:str = obj["Character015"]
      """  Character015  """  
      self.Character016:str = obj["Character016"]
      """  Character016  """  
      self.Character017:str = obj["Character017"]
      """  Character017  """  
      self.Character018:str = obj["Character018"]
      """  Character018  """  
      self.Character019:str = obj["Character019"]
      """  Character019  """  
      self.Character020:str = obj["Character020"]
      """  Character020  """  
      self.Character021:str = obj["Character021"]
      """  Character021  """  
      self.Character022:str = obj["Character022"]
      """  Character022  """  
      self.Character023:str = obj["Character023"]
      """  Character023  """  
      self.Character024:str = obj["Character024"]
      """  Character024  """  
      self.Character025:str = obj["Character025"]
      """  Character025  """  
      self.Character026:str = obj["Character026"]
      """  Character026  """  
      self.Character027:str = obj["Character027"]
      """  Character027  """  
      self.Character028:str = obj["Character028"]
      """  Character028  """  
      self.Character029:str = obj["Character029"]
      """  Character029  """  
      self.Character030:str = obj["Character030"]
      """  Character030  """  
      self.Character031:str = obj["Character031"]
      """  Character031  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsCheckBoxAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsCheckBoxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.CheckBox001:bool = obj["CheckBox001"]
      """  CheckBox001  """  
      self.CheckBox002:bool = obj["CheckBox002"]
      """  CheckBox002  """  
      self.CheckBox003:bool = obj["CheckBox003"]
      """  CheckBox003  """  
      self.CheckBox004:bool = obj["CheckBox004"]
      """  CheckBox004  """  
      self.CheckBox005:bool = obj["CheckBox005"]
      """  CheckBox005  """  
      self.CheckBox006:bool = obj["CheckBox006"]
      """  CheckBox006  """  
      self.CheckBox007:bool = obj["CheckBox007"]
      """  CheckBox007  """  
      self.CheckBox008:bool = obj["CheckBox008"]
      """  CheckBox008  """  
      self.CheckBox009:bool = obj["CheckBox009"]
      """  CheckBox009  """  
      self.CheckBox010:bool = obj["CheckBox010"]
      """  CheckBox010  """  
      self.CheckBox011:bool = obj["CheckBox011"]
      """  CheckBox011  """  
      self.CheckBox012:bool = obj["CheckBox012"]
      """  CheckBox012  """  
      self.CheckBox013:bool = obj["CheckBox013"]
      """  CheckBox013  """  
      self.CheckBox014:bool = obj["CheckBox014"]
      """  CheckBox014  """  
      self.CheckBox015:bool = obj["CheckBox015"]
      """  CheckBox015  """  
      self.CheckBox016:bool = obj["CheckBox016"]
      """  CheckBox016  """  
      self.CheckBox017:bool = obj["CheckBox017"]
      """  CheckBox017  """  
      self.CheckBox018:bool = obj["CheckBox018"]
      """  CheckBox018  """  
      self.CheckBox019:bool = obj["CheckBox019"]
      """  CheckBox019  """  
      self.CheckBox020:bool = obj["CheckBox020"]
      """  CheckBox020  """  
      self.CheckBox021:bool = obj["CheckBox021"]
      """  CheckBox021  """  
      self.CheckBox022:bool = obj["CheckBox022"]
      """  CheckBox022  """  
      self.CheckBox023:bool = obj["CheckBox023"]
      """  CheckBox023  """  
      self.CheckBox024:bool = obj["CheckBox024"]
      """  CheckBox024  """  
      self.CheckBox025:bool = obj["CheckBox025"]
      """  CheckBox025  """  
      self.CheckBox026:bool = obj["CheckBox026"]
      """  CheckBox026  """  
      self.CheckBox027:bool = obj["CheckBox027"]
      """  CheckBox027  """  
      self.CheckBox028:bool = obj["CheckBox028"]
      """  CheckBox028  """  
      self.CheckBox029:bool = obj["CheckBox029"]
      """  CheckBox029  """  
      self.CheckBox030:bool = obj["CheckBox030"]
      """  CheckBox030  """  
      self.CheckBox031:bool = obj["CheckBox031"]
      """  CheckBox031  """  
      self.CheckBox032:bool = obj["CheckBox032"]
      """  CheckBox032  """  
      self.CheckBox033:bool = obj["CheckBox033"]
      """  CheckBox033  """  
      self.CheckBox034:bool = obj["CheckBox034"]
      """  CheckBox034  """  
      self.CheckBox035:bool = obj["CheckBox035"]
      """  CheckBox035  """  
      self.CheckBox036:bool = obj["CheckBox036"]
      """  CheckBox036  """  
      self.CheckBox037:bool = obj["CheckBox037"]
      """  CheckBox037  """  
      self.CheckBox038:bool = obj["CheckBox038"]
      """  CheckBox038  """  
      self.CheckBox039:bool = obj["CheckBox039"]
      """  CheckBox039  """  
      self.CheckBox040:bool = obj["CheckBox040"]
      """  CheckBox040  """  
      self.CheckBox041:bool = obj["CheckBox041"]
      """  CheckBox041  """  
      self.CheckBox042:bool = obj["CheckBox042"]
      """  CheckBox042  """  
      self.CheckBox043:bool = obj["CheckBox043"]
      """  CheckBox043  """  
      self.CheckBox044:bool = obj["CheckBox044"]
      """  CheckBox044  """  
      self.CheckBox045:bool = obj["CheckBox045"]
      """  CheckBox045  """  
      self.CheckBox046:bool = obj["CheckBox046"]
      """  CheckBox046  """  
      self.CheckBox047:bool = obj["CheckBox047"]
      """  CheckBox047  """  
      self.CheckBox048:bool = obj["CheckBox048"]
      """  CheckBox048  """  
      self.CheckBox049:bool = obj["CheckBox049"]
      """  CheckBox049  """  
      self.CheckBox050:bool = obj["CheckBox050"]
      """  CheckBox050  """  
      self.CheckBox051:bool = obj["CheckBox051"]
      """  CheckBox051  """  
      self.CheckBox052:bool = obj["CheckBox052"]
      """  CheckBox052  """  
      self.CheckBox053:bool = obj["CheckBox053"]
      """  CheckBox053  """  
      self.CheckBox054:bool = obj["CheckBox054"]
      """  CheckBox054  """  
      self.CheckBox055:bool = obj["CheckBox055"]
      """  CheckBox055  """  
      self.CheckBox056:bool = obj["CheckBox056"]
      """  CheckBox056  """  
      self.CheckBox057:bool = obj["CheckBox057"]
      """  CheckBox057  """  
      self.CheckBox058:bool = obj["CheckBox058"]
      """  CheckBox058  """  
      self.CheckBox059:bool = obj["CheckBox059"]
      """  CheckBox059  """  
      self.CheckBox060:bool = obj["CheckBox060"]
      """  CheckBox060  """  
      self.CheckBox061:bool = obj["CheckBox061"]
      """  CheckBox061  """  
      self.CheckBox062:bool = obj["CheckBox062"]
      """  CheckBox062  """  
      self.CheckBox063:bool = obj["CheckBox063"]
      """  CheckBox063  """  
      self.CheckBox064:bool = obj["CheckBox064"]
      """  CheckBox064  """  
      self.CheckBox065:bool = obj["CheckBox065"]
      """  CheckBox065  """  
      self.CheckBox066:bool = obj["CheckBox066"]
      """  CheckBox066  """  
      self.CheckBox067:bool = obj["CheckBox067"]
      """  CheckBox067  """  
      self.CheckBox068:bool = obj["CheckBox068"]
      """  CheckBox068  """  
      self.CheckBox069:bool = obj["CheckBox069"]
      """  CheckBox069  """  
      self.CheckBox070:bool = obj["CheckBox070"]
      """  CheckBox070  """  
      self.CheckBox071:bool = obj["CheckBox071"]
      """  CheckBox071  """  
      self.CheckBox072:bool = obj["CheckBox072"]
      """  CheckBox072  """  
      self.CheckBox073:bool = obj["CheckBox073"]
      """  CheckBox073  """  
      self.CheckBox074:bool = obj["CheckBox074"]
      """  CheckBox074  """  
      self.CheckBox075:bool = obj["CheckBox075"]
      """  CheckBox075  """  
      self.CheckBox076:bool = obj["CheckBox076"]
      """  CheckBox076  """  
      self.CheckBox077:bool = obj["CheckBox077"]
      """  CheckBox077  """  
      self.CheckBox078:bool = obj["CheckBox078"]
      """  CheckBox078  """  
      self.CheckBox079:bool = obj["CheckBox079"]
      """  CheckBox079  """  
      self.CheckBox080:bool = obj["CheckBox080"]
      """  CheckBox080  """  
      self.CheckBox081:bool = obj["CheckBox081"]
      """  CheckBox081  """  
      self.CheckBox082:bool = obj["CheckBox082"]
      """  CheckBox082  """  
      self.CheckBox083:bool = obj["CheckBox083"]
      """  CheckBox083  """  
      self.CheckBox084:bool = obj["CheckBox084"]
      """  CheckBox084  """  
      self.CheckBox085:bool = obj["CheckBox085"]
      """  CheckBox085  """  
      self.CheckBox086:bool = obj["CheckBox086"]
      """  CheckBox086  """  
      self.CheckBox087:bool = obj["CheckBox087"]
      """  CheckBox087  """  
      self.CheckBox088:bool = obj["CheckBox088"]
      """  CheckBox088  """  
      self.CheckBox089:bool = obj["CheckBox089"]
      """  CheckBox089  """  
      self.CheckBox090:bool = obj["CheckBox090"]
      """  CheckBox090  """  
      self.CheckBox091:bool = obj["CheckBox091"]
      """  CheckBox091  """  
      self.CheckBox092:bool = obj["CheckBox092"]
      """  CheckBox092  """  
      self.CheckBox093:bool = obj["CheckBox093"]
      """  CheckBox093  """  
      self.CheckBox094:bool = obj["CheckBox094"]
      """  CheckBox094  """  
      self.CheckBox095:bool = obj["CheckBox095"]
      """  CheckBox095  """  
      self.CheckBox096:bool = obj["CheckBox096"]
      """  CheckBox096  """  
      self.CheckBox097:bool = obj["CheckBox097"]
      """  CheckBox097  """  
      self.CheckBox098:bool = obj["CheckBox098"]
      """  CheckBox098  """  
      self.CheckBox099:bool = obj["CheckBox099"]
      """  CheckBox099  """  
      self.CheckBox100:bool = obj["CheckBox100"]
      """  CheckBox100  """  
      self.CheckBox101:bool = obj["CheckBox101"]
      """  CheckBox101  """  
      self.CheckBox102:bool = obj["CheckBox102"]
      """  CheckBox102  """  
      self.CheckBox103:bool = obj["CheckBox103"]
      """  CheckBox103  """  
      self.CheckBox104:bool = obj["CheckBox104"]
      """  CheckBox104  """  
      self.CheckBox105:bool = obj["CheckBox105"]
      """  CheckBox105  """  
      self.CheckBox106:bool = obj["CheckBox106"]
      """  CheckBox106  """  
      self.CheckBox107:bool = obj["CheckBox107"]
      """  CheckBox107  """  
      self.CheckBox108:bool = obj["CheckBox108"]
      """  CheckBox108  """  
      self.CheckBox109:bool = obj["CheckBox109"]
      """  CheckBox109  """  
      self.CheckBox110:bool = obj["CheckBox110"]
      """  CheckBox110  """  
      self.CheckBox111:bool = obj["CheckBox111"]
      """  CheckBox111  """  
      self.CheckBox112:bool = obj["CheckBox112"]
      """  CheckBox112  """  
      self.CheckBox113:bool = obj["CheckBox113"]
      """  CheckBox113  """  
      self.CheckBox114:bool = obj["CheckBox114"]
      """  CheckBox114  """  
      self.CheckBox115:bool = obj["CheckBox115"]
      """  CheckBox115  """  
      self.CheckBox116:bool = obj["CheckBox116"]
      """  CheckBox116  """  
      self.CheckBox117:bool = obj["CheckBox117"]
      """  CheckBox117  """  
      self.CheckBox118:bool = obj["CheckBox118"]
      """  CheckBox118  """  
      self.CheckBox119:bool = obj["CheckBox119"]
      """  CheckBox119  """  
      self.CheckBox120:bool = obj["CheckBox120"]
      """  CheckBox120  """  
      self.CheckBox121:bool = obj["CheckBox121"]
      """  CheckBox121  """  
      self.CheckBox122:bool = obj["CheckBox122"]
      """  CheckBox122  """  
      self.CheckBox123:bool = obj["CheckBox123"]
      """  CheckBox123  """  
      self.CheckBox124:bool = obj["CheckBox124"]
      """  CheckBox124  """  
      self.CheckBox125:bool = obj["CheckBox125"]
      """  CheckBox125  """  
      self.CheckBox126:bool = obj["CheckBox126"]
      """  CheckBox126  """  
      self.CheckBox127:bool = obj["CheckBox127"]
      """  CheckBox127  """  
      self.CheckBox128:bool = obj["CheckBox128"]
      """  CheckBox128  """  
      self.CheckBox129:bool = obj["CheckBox129"]
      """  CheckBox129  """  
      self.CheckBox130:bool = obj["CheckBox130"]
      """  CheckBox130  """  
      self.CheckBox131:bool = obj["CheckBox131"]
      """  CheckBox131  """  
      self.CheckBox132:bool = obj["CheckBox132"]
      """  CheckBox132  """  
      self.CheckBox133:bool = obj["CheckBox133"]
      """  CheckBox133  """  
      self.CheckBox134:bool = obj["CheckBox134"]
      """  CheckBox134  """  
      self.CheckBox135:bool = obj["CheckBox135"]
      """  CheckBox135  """  
      self.CheckBox136:bool = obj["CheckBox136"]
      """  CheckBox136  """  
      self.CheckBox137:bool = obj["CheckBox137"]
      """  CheckBox137  """  
      self.CheckBox138:bool = obj["CheckBox138"]
      """  CheckBox138  """  
      self.CheckBox139:bool = obj["CheckBox139"]
      """  CheckBox139  """  
      self.CheckBox140:bool = obj["CheckBox140"]
      """  CheckBox140  """  
      self.CheckBox141:bool = obj["CheckBox141"]
      """  CheckBox141  """  
      self.CheckBox142:bool = obj["CheckBox142"]
      """  CheckBox142  """  
      self.CheckBox143:bool = obj["CheckBox143"]
      """  CheckBox143  """  
      self.CheckBox144:bool = obj["CheckBox144"]
      """  CheckBox144  """  
      self.CheckBox145:bool = obj["CheckBox145"]
      """  CheckBox145  """  
      self.CheckBox146:bool = obj["CheckBox146"]
      """  CheckBox146  """  
      self.CheckBox147:bool = obj["CheckBox147"]
      """  CheckBox147  """  
      self.CheckBox148:bool = obj["CheckBox148"]
      """  CheckBox148  """  
      self.CheckBox149:bool = obj["CheckBox149"]
      """  CheckBox149  """  
      self.CheckBox150:bool = obj["CheckBox150"]
      """  CheckBox150  """  
      self.CheckBox151:bool = obj["CheckBox151"]
      """  CheckBox151  """  
      self.CheckBox152:bool = obj["CheckBox152"]
      """  CheckBox152  """  
      self.CheckBox153:bool = obj["CheckBox153"]
      """  CheckBox153  """  
      self.CheckBox154:bool = obj["CheckBox154"]
      """  CheckBox154  """  
      self.CheckBox155:bool = obj["CheckBox155"]
      """  CheckBox155  """  
      self.CheckBox156:bool = obj["CheckBox156"]
      """  CheckBox156  """  
      self.CheckBox157:bool = obj["CheckBox157"]
      """  CheckBox157  """  
      self.CheckBox158:bool = obj["CheckBox158"]
      """  CheckBox158  """  
      self.CheckBox159:bool = obj["CheckBox159"]
      """  CheckBox159  """  
      self.CheckBox160:bool = obj["CheckBox160"]
      """  CheckBox160  """  
      self.CheckBox161:bool = obj["CheckBox161"]
      """  CheckBox161  """  
      self.CheckBox162:bool = obj["CheckBox162"]
      """  CheckBox162  """  
      self.CheckBox163:bool = obj["CheckBox163"]
      """  CheckBox163  """  
      self.CheckBox164:bool = obj["CheckBox164"]
      """  CheckBox164  """  
      self.CheckBox165:bool = obj["CheckBox165"]
      """  CheckBox165  """  
      self.CheckBox166:bool = obj["CheckBox166"]
      """  CheckBox166  """  
      self.CheckBox167:bool = obj["CheckBox167"]
      """  CheckBox167  """  
      self.CheckBox168:bool = obj["CheckBox168"]
      """  CheckBox168  """  
      self.CheckBox169:bool = obj["CheckBox169"]
      """  CheckBox169  """  
      self.CheckBox170:bool = obj["CheckBox170"]
      """  CheckBox170  """  
      self.CheckBox171:bool = obj["CheckBox171"]
      """  CheckBox171  """  
      self.CheckBox172:bool = obj["CheckBox172"]
      """  CheckBox172  """  
      self.CheckBox173:bool = obj["CheckBox173"]
      """  CheckBox173  """  
      self.CheckBox174:bool = obj["CheckBox174"]
      """  CheckBox174  """  
      self.CheckBox175:bool = obj["CheckBox175"]
      """  CheckBox175  """  
      self.CheckBox176:bool = obj["CheckBox176"]
      """  CheckBox176  """  
      self.CheckBox177:bool = obj["CheckBox177"]
      """  CheckBox177  """  
      self.CheckBox178:bool = obj["CheckBox178"]
      """  CheckBox178  """  
      self.CheckBox179:bool = obj["CheckBox179"]
      """  CheckBox179  """  
      self.CheckBox180:bool = obj["CheckBox180"]
      """  CheckBox180  """  
      self.CheckBox181:bool = obj["CheckBox181"]
      """  CheckBox181  """  
      self.CheckBox182:bool = obj["CheckBox182"]
      """  CheckBox182  """  
      self.CheckBox183:bool = obj["CheckBox183"]
      """  CheckBox183  """  
      self.CheckBox184:bool = obj["CheckBox184"]
      """  CheckBox184  """  
      self.CheckBox185:bool = obj["CheckBox185"]
      """  CheckBox185  """  
      self.CheckBox186:bool = obj["CheckBox186"]
      """  CheckBox186  """  
      self.CheckBox187:bool = obj["CheckBox187"]
      """  CheckBox187  """  
      self.CheckBox188:bool = obj["CheckBox188"]
      """  CheckBox188  """  
      self.CheckBox189:bool = obj["CheckBox189"]
      """  CheckBox189  """  
      self.CheckBox190:bool = obj["CheckBox190"]
      """  CheckBox190  """  
      self.CheckBox191:bool = obj["CheckBox191"]
      """  CheckBox191  """  
      self.CheckBox192:bool = obj["CheckBox192"]
      """  CheckBox192  """  
      self.CheckBox193:bool = obj["CheckBox193"]
      """  CheckBox193  """  
      self.CheckBox194:bool = obj["CheckBox194"]
      """  CheckBox194  """  
      self.CheckBox195:bool = obj["CheckBox195"]
      """  CheckBox195  """  
      self.CheckBox196:bool = obj["CheckBox196"]
      """  CheckBox196  """  
      self.CheckBox197:bool = obj["CheckBox197"]
      """  CheckBox197  """  
      self.CheckBox198:bool = obj["CheckBox198"]
      """  CheckBox198  """  
      self.CheckBox199:bool = obj["CheckBox199"]
      """  CheckBox199  """  
      self.CheckBox200:bool = obj["CheckBox200"]
      """  CheckBox200  """  
      self.CheckBox201:bool = obj["CheckBox201"]
      """  CheckBox201  """  
      self.CheckBox202:bool = obj["CheckBox202"]
      """  CheckBox202  """  
      self.CheckBox203:bool = obj["CheckBox203"]
      """  CheckBox203  """  
      self.CheckBox204:bool = obj["CheckBox204"]
      """  CheckBox204  """  
      self.CheckBox205:bool = obj["CheckBox205"]
      """  CheckBox205  """  
      self.CheckBox206:bool = obj["CheckBox206"]
      """  CheckBox206  """  
      self.CheckBox207:bool = obj["CheckBox207"]
      """  CheckBox207  """  
      self.CheckBox208:bool = obj["CheckBox208"]
      """  CheckBox208  """  
      self.CheckBox209:bool = obj["CheckBox209"]
      """  CheckBox209  """  
      self.CheckBox210:bool = obj["CheckBox210"]
      """  CheckBox210  """  
      self.CheckBox211:bool = obj["CheckBox211"]
      """  CheckBox211  """  
      self.CheckBox212:bool = obj["CheckBox212"]
      """  CheckBox212  """  
      self.CheckBox213:bool = obj["CheckBox213"]
      """  CheckBox213  """  
      self.CheckBox214:bool = obj["CheckBox214"]
      """  CheckBox214  """  
      self.CheckBox215:bool = obj["CheckBox215"]
      """  CheckBox215  """  
      self.CheckBox216:bool = obj["CheckBox216"]
      """  CheckBox216  """  
      self.CheckBox217:bool = obj["CheckBox217"]
      """  CheckBox217  """  
      self.CheckBox218:bool = obj["CheckBox218"]
      """  CheckBox218  """  
      self.CheckBox219:bool = obj["CheckBox219"]
      """  CheckBox219  """  
      self.CheckBox220:bool = obj["CheckBox220"]
      """  CheckBox220  """  
      self.CheckBox221:bool = obj["CheckBox221"]
      """  CheckBox221  """  
      self.CheckBox222:bool = obj["CheckBox222"]
      """  CheckBox222  """  
      self.CheckBox223:bool = obj["CheckBox223"]
      """  CheckBox223  """  
      self.CheckBox224:bool = obj["CheckBox224"]
      """  CheckBox224  """  
      self.CheckBox225:bool = obj["CheckBox225"]
      """  CheckBox225  """  
      self.CheckBox226:bool = obj["CheckBox226"]
      """  CheckBox226  """  
      self.CheckBox227:bool = obj["CheckBox227"]
      """  CheckBox227  """  
      self.CheckBox228:bool = obj["CheckBox228"]
      """  CheckBox228  """  
      self.CheckBox229:bool = obj["CheckBox229"]
      """  CheckBox229  """  
      self.CheckBox230:bool = obj["CheckBox230"]
      """  CheckBox230  """  
      self.CheckBox231:bool = obj["CheckBox231"]
      """  CheckBox231  """  
      self.CheckBox232:bool = obj["CheckBox232"]
      """  CheckBox232  """  
      self.CheckBox233:bool = obj["CheckBox233"]
      """  CheckBox233  """  
      self.CheckBox234:bool = obj["CheckBox234"]
      """  CheckBox234  """  
      self.CheckBox235:bool = obj["CheckBox235"]
      """  CheckBox235  """  
      self.CheckBox236:bool = obj["CheckBox236"]
      """  CheckBox236  """  
      self.CheckBox237:bool = obj["CheckBox237"]
      """  CheckBox237  """  
      self.CheckBox238:bool = obj["CheckBox238"]
      """  CheckBox238  """  
      self.CheckBox239:bool = obj["CheckBox239"]
      """  CheckBox239  """  
      self.CheckBox240:bool = obj["CheckBox240"]
      """  CheckBox240  """  
      self.CheckBox241:bool = obj["CheckBox241"]
      """  CheckBox241  """  
      self.CheckBox242:bool = obj["CheckBox242"]
      """  CheckBox242  """  
      self.CheckBox243:bool = obj["CheckBox243"]
      """  CheckBox243  """  
      self.CheckBox244:bool = obj["CheckBox244"]
      """  CheckBox244  """  
      self.CheckBox245:bool = obj["CheckBox245"]
      """  CheckBox245  """  
      self.CheckBox246:bool = obj["CheckBox246"]
      """  CheckBox246  """  
      self.CheckBox247:bool = obj["CheckBox247"]
      """  CheckBox247  """  
      self.CheckBox248:bool = obj["CheckBox248"]
      """  CheckBox248  """  
      self.CheckBox249:bool = obj["CheckBox249"]
      """  CheckBox249  """  
      self.CheckBox250:bool = obj["CheckBox250"]
      """  CheckBox250  """  
      self.CheckBox251:bool = obj["CheckBox251"]
      """  CheckBox251  """  
      self.CheckBox252:bool = obj["CheckBox252"]
      """  CheckBox252  """  
      self.CheckBox253:bool = obj["CheckBox253"]
      """  CheckBox253  """  
      self.CheckBox254:bool = obj["CheckBox254"]
      """  CheckBox254  """  
      self.CheckBox255:bool = obj["CheckBox255"]
      """  CheckBox255  """  
      self.CheckBox256:bool = obj["CheckBox256"]
      """  CheckBox256  """  
      self.CheckBox257:bool = obj["CheckBox257"]
      """  CheckBox257  """  
      self.CheckBox258:bool = obj["CheckBox258"]
      """  CheckBox258  """  
      self.CheckBox259:bool = obj["CheckBox259"]
      """  CheckBox259  """  
      self.CheckBox260:bool = obj["CheckBox260"]
      """  CheckBox260  """  
      self.CheckBox261:bool = obj["CheckBox261"]
      """  CheckBox261  """  
      self.CheckBox262:bool = obj["CheckBox262"]
      """  CheckBox262  """  
      self.CheckBox263:bool = obj["CheckBox263"]
      """  CheckBox263  """  
      self.CheckBox264:bool = obj["CheckBox264"]
      """  CheckBox264  """  
      self.CheckBox265:bool = obj["CheckBox265"]
      """  CheckBox265  """  
      self.CheckBox266:bool = obj["CheckBox266"]
      """  CheckBox266  """  
      self.CheckBox267:bool = obj["CheckBox267"]
      """  CheckBox267  """  
      self.CheckBox268:bool = obj["CheckBox268"]
      """  CheckBox268  """  
      self.CheckBox269:bool = obj["CheckBox269"]
      """  CheckBox269  """  
      self.CheckBox270:bool = obj["CheckBox270"]
      """  CheckBox270  """  
      self.CheckBox271:bool = obj["CheckBox271"]
      """  CheckBox271  """  
      self.CheckBox272:bool = obj["CheckBox272"]
      """  CheckBox272  """  
      self.CheckBox273:bool = obj["CheckBox273"]
      """  CheckBox273  """  
      self.CheckBox274:bool = obj["CheckBox274"]
      """  CheckBox274  """  
      self.CheckBox275:bool = obj["CheckBox275"]
      """  CheckBox275  """  
      self.CheckBox276:bool = obj["CheckBox276"]
      """  CheckBox276  """  
      self.CheckBox277:bool = obj["CheckBox277"]
      """  CheckBox277  """  
      self.CheckBox278:bool = obj["CheckBox278"]
      """  CheckBox278  """  
      self.CheckBox279:bool = obj["CheckBox279"]
      """  CheckBox279  """  
      self.CheckBox280:bool = obj["CheckBox280"]
      """  CheckBox280  """  
      self.CheckBox281:bool = obj["CheckBox281"]
      """  CheckBox281  """  
      self.CheckBox282:bool = obj["CheckBox282"]
      """  CheckBox282  """  
      self.CheckBox283:bool = obj["CheckBox283"]
      """  CheckBox283  """  
      self.CheckBox284:bool = obj["CheckBox284"]
      """  CheckBox284  """  
      self.CheckBox285:bool = obj["CheckBox285"]
      """  CheckBox285  """  
      self.CheckBox286:bool = obj["CheckBox286"]
      """  CheckBox286  """  
      self.CheckBox287:bool = obj["CheckBox287"]
      """  CheckBox287  """  
      self.CheckBox288:bool = obj["CheckBox288"]
      """  CheckBox288  """  
      self.CheckBox289:bool = obj["CheckBox289"]
      """  CheckBox289  """  
      self.CheckBox290:bool = obj["CheckBox290"]
      """  CheckBox290  """  
      self.CheckBox291:bool = obj["CheckBox291"]
      """  CheckBox291  """  
      self.CheckBox292:bool = obj["CheckBox292"]
      """  CheckBox292  """  
      self.CheckBox293:bool = obj["CheckBox293"]
      """  CheckBox293  """  
      self.CheckBox294:bool = obj["CheckBox294"]
      """  CheckBox294  """  
      self.CheckBox295:bool = obj["CheckBox295"]
      """  CheckBox295  """  
      self.CheckBox296:bool = obj["CheckBox296"]
      """  CheckBox296  """  
      self.CheckBox297:bool = obj["CheckBox297"]
      """  CheckBox297  """  
      self.CheckBox298:bool = obj["CheckBox298"]
      """  CheckBox298  """  
      self.CheckBox299:bool = obj["CheckBox299"]
      """  CheckBox299  """  
      self.CheckBox300:bool = obj["CheckBox300"]
      """  CheckBox300  """  
      self.CheckBox301:bool = obj["CheckBox301"]
      """  CheckBox301  """  
      self.CheckBox302:bool = obj["CheckBox302"]
      """  CheckBox302  """  
      self.CheckBox303:bool = obj["CheckBox303"]
      """  CheckBox303  """  
      self.CheckBox304:bool = obj["CheckBox304"]
      """  CheckBox304  """  
      self.CheckBox305:bool = obj["CheckBox305"]
      """  CheckBox305  """  
      self.CheckBox306:bool = obj["CheckBox306"]
      """  CheckBox306  """  
      self.CheckBox307:bool = obj["CheckBox307"]
      """  CheckBox307  """  
      self.CheckBox308:bool = obj["CheckBox308"]
      """  CheckBox308  """  
      self.CheckBox309:bool = obj["CheckBox309"]
      """  CheckBox309  """  
      self.CheckBox310:bool = obj["CheckBox310"]
      """  CheckBox310  """  
      self.CheckBox311:bool = obj["CheckBox311"]
      """  CheckBox311  """  
      self.CheckBox312:bool = obj["CheckBox312"]
      """  CheckBox312  """  
      self.CheckBox313:bool = obj["CheckBox313"]
      """  CheckBox313  """  
      self.CheckBox314:bool = obj["CheckBox314"]
      """  CheckBox314  """  
      self.CheckBox315:bool = obj["CheckBox315"]
      """  CheckBox315  """  
      self.CheckBox316:bool = obj["CheckBox316"]
      """  CheckBox316  """  
      self.CheckBox317:bool = obj["CheckBox317"]
      """  CheckBox317  """  
      self.CheckBox318:bool = obj["CheckBox318"]
      """  CheckBox318  """  
      self.CheckBox319:bool = obj["CheckBox319"]
      """  CheckBox319  """  
      self.CheckBox320:bool = obj["CheckBox320"]
      """  CheckBox320  """  
      self.CheckBox321:bool = obj["CheckBox321"]
      """  CheckBox321  """  
      self.CheckBox322:bool = obj["CheckBox322"]
      """  CheckBox322  """  
      self.CheckBox323:bool = obj["CheckBox323"]
      """  CheckBox323  """  
      self.CheckBox324:bool = obj["CheckBox324"]
      """  CheckBox324  """  
      self.CheckBox325:bool = obj["CheckBox325"]
      """  CheckBox325  """  
      self.CheckBox326:bool = obj["CheckBox326"]
      """  CheckBox326  """  
      self.CheckBox327:bool = obj["CheckBox327"]
      """  CheckBox327  """  
      self.CheckBox328:bool = obj["CheckBox328"]
      """  CheckBox328  """  
      self.CheckBox329:bool = obj["CheckBox329"]
      """  CheckBox329  """  
      self.CheckBox330:bool = obj["CheckBox330"]
      """  CheckBox330  """  
      self.CheckBox331:bool = obj["CheckBox331"]
      """  CheckBox331  """  
      self.CheckBox332:bool = obj["CheckBox332"]
      """  CheckBox332  """  
      self.CheckBox333:bool = obj["CheckBox333"]
      """  CheckBox333  """  
      self.CheckBox334:bool = obj["CheckBox334"]
      """  CheckBox334  """  
      self.CheckBox335:bool = obj["CheckBox335"]
      """  CheckBox335  """  
      self.CheckBox336:bool = obj["CheckBox336"]
      """  CheckBox336  """  
      self.CheckBox337:bool = obj["CheckBox337"]
      """  CheckBox337  """  
      self.CheckBox338:bool = obj["CheckBox338"]
      """  CheckBox338  """  
      self.CheckBox339:bool = obj["CheckBox339"]
      """  CheckBox339  """  
      self.CheckBox340:bool = obj["CheckBox340"]
      """  CheckBox340  """  
      self.CheckBox341:bool = obj["CheckBox341"]
      """  CheckBox341  """  
      self.CheckBox342:bool = obj["CheckBox342"]
      """  CheckBox342  """  
      self.CheckBox343:bool = obj["CheckBox343"]
      """  CheckBox343  """  
      self.CheckBox344:bool = obj["CheckBox344"]
      """  CheckBox344  """  
      self.CheckBox345:bool = obj["CheckBox345"]
      """  CheckBox345  """  
      self.CheckBox346:bool = obj["CheckBox346"]
      """  CheckBox346  """  
      self.CheckBox347:bool = obj["CheckBox347"]
      """  CheckBox347  """  
      self.CheckBox348:bool = obj["CheckBox348"]
      """  CheckBox348  """  
      self.CheckBox349:bool = obj["CheckBox349"]
      """  CheckBox349  """  
      self.CheckBox350:bool = obj["CheckBox350"]
      """  CheckBox350  """  
      self.CheckBox351:bool = obj["CheckBox351"]
      """  CheckBox351  """  
      self.CheckBox352:bool = obj["CheckBox352"]
      """  CheckBox352  """  
      self.CheckBox353:bool = obj["CheckBox353"]
      """  CheckBox353  """  
      self.CheckBox354:bool = obj["CheckBox354"]
      """  CheckBox354  """  
      self.CheckBox355:bool = obj["CheckBox355"]
      """  CheckBox355  """  
      self.CheckBox356:bool = obj["CheckBox356"]
      """  CheckBox356  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsDateAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsDateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Date001:str = obj["Date001"]
      """  Date001  """  
      self.Date002:str = obj["Date002"]
      """  Date002  """  
      self.Date003:str = obj["Date003"]
      """  Date003  """  
      self.Date004:str = obj["Date004"]
      """  Date004  """  
      self.Date005:str = obj["Date005"]
      """  Date005  """  
      self.Date006:str = obj["Date006"]
      """  Date006  """  
      self.Date007:str = obj["Date007"]
      """  Date007  """  
      self.Date008:str = obj["Date008"]
      """  Date008  """  
      self.Date009:str = obj["Date009"]
      """  Date009  """  
      self.Date010:str = obj["Date010"]
      """  Date010  """  
      self.Date011:str = obj["Date011"]
      """  Date011  """  
      self.Date012:str = obj["Date012"]
      """  Date012  """  
      self.Date013:str = obj["Date013"]
      """  Date013  """  
      self.Date014:str = obj["Date014"]
      """  Date014  """  
      self.Date015:str = obj["Date015"]
      """  Date015  """  
      self.Date016:str = obj["Date016"]
      """  Date016  """  
      self.Date017:str = obj["Date017"]
      """  Date017  """  
      self.Date018:str = obj["Date018"]
      """  Date018  """  
      self.Date019:str = obj["Date019"]
      """  Date019  """  
      self.Date020:str = obj["Date020"]
      """  Date020  """  
      self.Date021:str = obj["Date021"]
      """  Date021  """  
      self.Date022:str = obj["Date022"]
      """  Date022  """  
      self.Date023:str = obj["Date023"]
      """  Date023  """  
      self.Date024:str = obj["Date024"]
      """  Date024  """  
      self.Date025:str = obj["Date025"]
      """  Date025  """  
      self.Date026:str = obj["Date026"]
      """  Date026  """  
      self.Date027:str = obj["Date027"]
      """  Date027  """  
      self.Date028:str = obj["Date028"]
      """  Date028  """  
      self.Date029:str = obj["Date029"]
      """  Date029  """  
      self.Date030:str = obj["Date030"]
      """  Date030  """  
      self.Date031:str = obj["Date031"]
      """  Date031  """  
      self.Date032:str = obj["Date032"]
      """  Date032  """  
      self.Date033:str = obj["Date033"]
      """  Date033  """  
      self.Date034:str = obj["Date034"]
      """  Date034  """  
      self.Date035:str = obj["Date035"]
      """  Date035  """  
      self.Date036:str = obj["Date036"]
      """  Date036  """  
      self.Date037:str = obj["Date037"]
      """  Date037  """  
      self.Date038:str = obj["Date038"]
      """  Date038  """  
      self.Date039:str = obj["Date039"]
      """  Date039  """  
      self.Date040:str = obj["Date040"]
      """  Date040  """  
      self.Date041:str = obj["Date041"]
      """  Date041  """  
      self.Date042:str = obj["Date042"]
      """  Date042  """  
      self.Date043:str = obj["Date043"]
      """  Date043  """  
      self.Date044:str = obj["Date044"]
      """  Date044  """  
      self.Date045:str = obj["Date045"]
      """  Date045  """  
      self.Date046:str = obj["Date046"]
      """  Date046  """  
      self.Date047:str = obj["Date047"]
      """  Date047  """  
      self.Date051:str = obj["Date051"]
      """  Date051  """  
      self.Date052:str = obj["Date052"]
      """  Date052  """  
      self.Date053:str = obj["Date053"]
      """  Date053  """  
      self.Date054:str = obj["Date054"]
      """  Date054  """  
      self.Date055:str = obj["Date055"]
      """  Date055  """  
      self.Date056:str = obj["Date056"]
      """  Date056  """  
      self.Date057:str = obj["Date057"]
      """  Date057  """  
      self.Date058:str = obj["Date058"]
      """  Date058  """  
      self.Date059:str = obj["Date059"]
      """  Date059  """  
      self.Date060:str = obj["Date060"]
      """  Date060  """  
      self.Date061:str = obj["Date061"]
      """  Date061  """  
      self.Date062:str = obj["Date062"]
      """  Date062  """  
      self.Date063:str = obj["Date063"]
      """  Date063  """  
      self.Date064:str = obj["Date064"]
      """  Date064  """  
      self.Date065:str = obj["Date065"]
      """  Date065  """  
      self.Date066:str = obj["Date066"]
      """  Date066  """  
      self.Date067:str = obj["Date067"]
      """  Date067  """  
      self.Date068:str = obj["Date068"]
      """  Date068  """  
      self.Date069:str = obj["Date069"]
      """  Date069  """  
      self.Date070:str = obj["Date070"]
      """  Date070  """  
      self.Date071:str = obj["Date071"]
      """  Date071  """  
      self.Date072:str = obj["Date072"]
      """  Date072  """  
      self.Date073:str = obj["Date073"]
      """  Date073  """  
      self.Date074:str = obj["Date074"]
      """  Date074  """  
      self.Date075:str = obj["Date075"]
      """  Date075  """  
      self.Date076:str = obj["Date076"]
      """  Date076  """  
      self.Date077:str = obj["Date077"]
      """  Date077  """  
      self.Date078:str = obj["Date078"]
      """  Date078  """  
      self.Date079:str = obj["Date079"]
      """  Date079  """  
      self.Date080:str = obj["Date080"]
      """  Date080  """  
      self.Date081:str = obj["Date081"]
      """  Date081  """  
      self.Date082:str = obj["Date082"]
      """  Date082  """  
      self.Date083:str = obj["Date083"]
      """  Date083  """  
      self.Date084:str = obj["Date084"]
      """  Date084  """  
      self.Date085:str = obj["Date085"]
      """  Date085  """  
      self.Date086:str = obj["Date086"]
      """  Date086  """  
      self.Date087:str = obj["Date087"]
      """  Date087  """  
      self.Date088:str = obj["Date088"]
      """  Date088  """  
      self.Date089:str = obj["Date089"]
      """  Date089  """  
      self.Date090:str = obj["Date090"]
      """  Date090  """  
      self.Date091:str = obj["Date091"]
      """  Date091  """  
      self.Date092:str = obj["Date092"]
      """  Date092  """  
      self.Date093:str = obj["Date093"]
      """  Date093  """  
      self.Date094:str = obj["Date094"]
      """  Date094  """  
      self.Date095:str = obj["Date095"]
      """  Date095  """  
      self.Date096:str = obj["Date096"]
      """  Date096  """  
      self.Date097:str = obj["Date097"]
      """  Date097  """  
      self.Date101:str = obj["Date101"]
      """  Date101  """  
      self.Date102:str = obj["Date102"]
      """  Date102  """  
      self.Date103:str = obj["Date103"]
      """  Date103  """  
      self.Date104:str = obj["Date104"]
      """  Date104  """  
      self.Date105:str = obj["Date105"]
      """  Date105  """  
      self.Date106:str = obj["Date106"]
      """  Date106  """  
      self.Date107:str = obj["Date107"]
      """  Date107  """  
      self.Date108:str = obj["Date108"]
      """  Date108  """  
      self.Date109:str = obj["Date109"]
      """  Date109  """  
      self.Date110:str = obj["Date110"]
      """  Date110  """  
      self.Date111:str = obj["Date111"]
      """  Date111  """  
      self.Date112:str = obj["Date112"]
      """  Date112  """  
      self.Date113:str = obj["Date113"]
      """  Date113  """  
      self.Date114:str = obj["Date114"]
      """  Date114  """  
      self.Date115:str = obj["Date115"]
      """  Date115  """  
      self.Date116:str = obj["Date116"]
      """  Date116  """  
      self.Date117:str = obj["Date117"]
      """  Date117  """  
      self.Date118:str = obj["Date118"]
      """  Date118  """  
      self.Date119:str = obj["Date119"]
      """  Date119  """  
      self.Date120:str = obj["Date120"]
      """  Date120  """  
      self.Date121:str = obj["Date121"]
      """  Date121  """  
      self.Date122:str = obj["Date122"]
      """  Date122  """  
      self.Date123:str = obj["Date123"]
      """  Date123  """  
      self.Date124:str = obj["Date124"]
      """  Date124  """  
      self.Date125:str = obj["Date125"]
      """  Date125  """  
      self.Date126:str = obj["Date126"]
      """  Date126  """  
      self.Date127:str = obj["Date127"]
      """  Date127  """  
      self.Date128:str = obj["Date128"]
      """  Date128  """  
      self.Date129:str = obj["Date129"]
      """  Date129  """  
      self.Date130:str = obj["Date130"]
      """  Date130  """  
      self.Date131:str = obj["Date131"]
      """  Date131  """  
      self.Date132:str = obj["Date132"]
      """  Date132  """  
      self.Date133:str = obj["Date133"]
      """  Date133  """  
      self.Date134:str = obj["Date134"]
      """  Date134  """  
      self.Date135:str = obj["Date135"]
      """  Date135  """  
      self.Date136:str = obj["Date136"]
      """  Date136  """  
      self.Date137:str = obj["Date137"]
      """  Date137  """  
      self.Date138:str = obj["Date138"]
      """  Date138  """  
      self.Date139:str = obj["Date139"]
      """  Date139  """  
      self.Date140:str = obj["Date140"]
      """  Date140  """  
      self.Date141:str = obj["Date141"]
      """  Date141  """  
      self.Date142:str = obj["Date142"]
      """  Date142  """  
      self.Date143:str = obj["Date143"]
      """  Date143  """  
      self.Date144:str = obj["Date144"]
      """  Date144  """  
      self.Date145:str = obj["Date145"]
      """  Date145  """  
      self.Date146:str = obj["Date146"]
      """  Date146  """  
      self.Date147:str = obj["Date147"]
      """  Date147  """  
      self.Date151:str = obj["Date151"]
      """  Date151  """  
      self.Date152:str = obj["Date152"]
      """  Date152  """  
      self.Date153:str = obj["Date153"]
      """  Date153  """  
      self.Date154:str = obj["Date154"]
      """  Date154  """  
      self.Date155:str = obj["Date155"]
      """  Date155  """  
      self.Date156:str = obj["Date156"]
      """  Date156  """  
      self.Date157:str = obj["Date157"]
      """  Date157  """  
      self.Date158:str = obj["Date158"]
      """  Date158  """  
      self.Date159:str = obj["Date159"]
      """  Date159  """  
      self.Date160:str = obj["Date160"]
      """  Date160  """  
      self.Date161:str = obj["Date161"]
      """  Date161  """  
      self.Date162:str = obj["Date162"]
      """  Date162  """  
      self.Date163:str = obj["Date163"]
      """  Date163  """  
      self.Date164:str = obj["Date164"]
      """  Date164  """  
      self.Date165:str = obj["Date165"]
      """  Date165  """  
      self.Date166:str = obj["Date166"]
      """  Date166  """  
      self.Date167:str = obj["Date167"]
      """  Date167  """  
      self.Date168:str = obj["Date168"]
      """  Date168  """  
      self.Date169:str = obj["Date169"]
      """  Date169  """  
      self.Date170:str = obj["Date170"]
      """  Date170  """  
      self.Date171:str = obj["Date171"]
      """  Date171  """  
      self.Date172:str = obj["Date172"]
      """  Date172  """  
      self.Date173:str = obj["Date173"]
      """  Date173  """  
      self.Date174:str = obj["Date174"]
      """  Date174  """  
      self.Date175:str = obj["Date175"]
      """  Date175  """  
      self.Date176:str = obj["Date176"]
      """  Date176  """  
      self.Date177:str = obj["Date177"]
      """  Date177  """  
      self.Date178:str = obj["Date178"]
      """  Date178  """  
      self.Date179:str = obj["Date179"]
      """  Date179  """  
      self.Date180:str = obj["Date180"]
      """  Date180  """  
      self.Date181:str = obj["Date181"]
      """  Date181  """  
      self.Date182:str = obj["Date182"]
      """  Date182  """  
      self.Date183:str = obj["Date183"]
      """  Date183  """  
      self.Date184:str = obj["Date184"]
      """  Date184  """  
      self.Date185:str = obj["Date185"]
      """  Date185  """  
      self.Date186:str = obj["Date186"]
      """  Date186  """  
      self.Date187:str = obj["Date187"]
      """  Date187  """  
      self.Date188:str = obj["Date188"]
      """  Date188  """  
      self.Date189:str = obj["Date189"]
      """  Date189  """  
      self.Date190:str = obj["Date190"]
      """  Date190  """  
      self.Date191:str = obj["Date191"]
      """  Date191  """  
      self.Date192:str = obj["Date192"]
      """  Date192  """  
      self.Date193:str = obj["Date193"]
      """  Date193  """  
      self.Date194:str = obj["Date194"]
      """  Date194  """  
      self.Date195:str = obj["Date195"]
      """  Date195  """  
      self.Date196:str = obj["Date196"]
      """  Date196  """  
      self.Date197:str = obj["Date197"]
      """  Date197  """  
      self.Date048:str = obj["Date048"]
      """  Date048  """  
      self.Date049:str = obj["Date049"]
      """  Date049  """  
      self.Date050:str = obj["Date050"]
      """  Date050  """  
      self.Date098:str = obj["Date098"]
      """  Date098  """  
      self.Date099:str = obj["Date099"]
      """  Date099  """  
      self.Date100:str = obj["Date100"]
      """  Date100  """  
      self.Date148:str = obj["Date148"]
      """  Date148  """  
      self.Date149:str = obj["Date149"]
      """  Date149  """  
      self.Date150:str = obj["Date150"]
      """  Date150  """  
      self.Date198:str = obj["Date198"]
      """  Date198  """  
      self.Date199:str = obj["Date199"]
      """  Date199  """  
      self.Date200:str = obj["Date200"]
      """  Date200  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to. Field not currently used.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record. For future use.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number inspected  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number Inspected  """  
      self.JobNum:str = obj["JobNum"]
      """  Contains the Job Number related to the job or non-conformance being inspected.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Contain the assembly sequence of the job being inspected  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Contains the operation sequence of the job operation being inspected.  """  
      self.NCMTranID:int = obj["NCMTranID"]
      """  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  Contains the inspection plan part number (configurator part number)  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  Contains the inspection plan revision number (configurator revision number)  """  
      self.SpecID:str = obj["SpecID"]
      """  Contains the specification ID that was used in the inspection plan.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Contains the specification revision number that was used in the inspection process.  """  
      self.RMANum:int = obj["RMANum"]
      """  Contains Return Material Authorization number if inspecting for an RMA  """  
      self.RMALine:int = obj["RMALine"]
      """  Contains Line number of the RMA if inspecting for an RMA.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Contains the PO Packing Slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """  Contains the PO Packing Slip line number.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Contains the VendorNum when inspected via Skip Lot processing  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Contains the serial number of the part inspected  """  
      self.LotNum:str = obj["LotNum"]
      """  Contains the lot number of the part inspected  """  
      self.Passed:bool = obj["Passed"]
      """  True if passed  """  
      self.FailedCmtText:str = obj["FailedCmtText"]
      """  Text describing why the inspection result failed  """  
      self.TestDataEntered:bool = obj["TestDataEntered"]
      """  True if the results were saved in product configuration  """  
      self.AuditRefNum:int = obj["AuditRefNum"]
      """  This is a unique reference number that is assigned by the system for each audit record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.AuditType:str = obj["AuditType"]
      """  Shows how the audit was created - Scheduled or Manual  """  
      self.AuditID:str = obj["AuditID"]
      """  User defined Audit ID  """  
      self.AuditRevNum:str = obj["AuditRevNum"]
      """  Supplier Audit Revision Number  """  
      self.Auditor:str = obj["Auditor"]
      """  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  """  
      self.AuditSchedDate:str = obj["AuditSchedDate"]
      self.AuditCreateDate:str = obj["AuditCreateDate"]
      """  Date the audit reference was created  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  """  
      self.AuditVendNum:int = obj["AuditVendNum"]
      """  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  """  
      self.AuditCompDate:str = obj["AuditCompDate"]
      """  Date the audit was completed  """  
      self.AuditStatus:str = obj["AuditStatus"]
      """  Planned, Scheduled, In Progress, Complete  """  
      self.AuditResult:str = obj["AuditResult"]
      """  Passed, Failed, Unspecified  """  
      self.AuditConNum:int = obj["AuditConNum"]
      """  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  """  
      self.AuditConRole:str = obj["AuditConRole"]
      """  Code that identifies the role of the audit contact.  """  
      self.AuditCost:int = obj["AuditCost"]
      """  This is the cost of performing the audit.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Description:str = obj["Description"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsNumAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsNumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Number001:int = obj["Number001"]
      """  Number001  """  
      self.Number002:int = obj["Number002"]
      """  Number002  """  
      self.Number003:int = obj["Number003"]
      """  Number003  """  
      self.Number004:int = obj["Number004"]
      """  Number004  """  
      self.Number005:int = obj["Number005"]
      """  Number005  """  
      self.Number006:int = obj["Number006"]
      """  Number006  """  
      self.Number007:int = obj["Number007"]
      """  Number007  """  
      self.Number008:int = obj["Number008"]
      """  Number008  """  
      self.Number009:int = obj["Number009"]
      """  Number009  """  
      self.Number010:int = obj["Number010"]
      """  Number010  """  
      self.Number011:int = obj["Number011"]
      """  Number011  """  
      self.Number012:int = obj["Number012"]
      """  Number012  """  
      self.Number013:int = obj["Number013"]
      """  Number013  """  
      self.Number014:int = obj["Number014"]
      """  Number014  """  
      self.Number015:int = obj["Number015"]
      """  Number015  """  
      self.Number016:int = obj["Number016"]
      """  Number016  """  
      self.Number017:int = obj["Number017"]
      """  Number017  """  
      self.Number018:int = obj["Number018"]
      """  Number018  """  
      self.Number019:int = obj["Number019"]
      """  Number019  """  
      self.Number020:int = obj["Number020"]
      """  Number020  """  
      self.Number021:int = obj["Number021"]
      """  Number021  """  
      self.Number022:int = obj["Number022"]
      """  Number022  """  
      self.Number023:int = obj["Number023"]
      """  Number023  """  
      self.Number024:int = obj["Number024"]
      """  Number024  """  
      self.Number025:int = obj["Number025"]
      """  Number025  """  
      self.Number026:int = obj["Number026"]
      """  Number026  """  
      self.Number027:int = obj["Number027"]
      """  Number027  """  
      self.Number028:int = obj["Number028"]
      """  Number028  """  
      self.Number029:int = obj["Number029"]
      """  Number029  """  
      self.Number030:int = obj["Number030"]
      """  Number030  """  
      self.Number031:int = obj["Number031"]
      """  Number031  """  
      self.Number032:int = obj["Number032"]
      """  Number032  """  
      self.Number033:int = obj["Number033"]
      """  Number033  """  
      self.Number034:int = obj["Number034"]
      """  Number034  """  
      self.Number035:int = obj["Number035"]
      """  Number035  """  
      self.Number036:int = obj["Number036"]
      """  Number036  """  
      self.Number037:int = obj["Number037"]
      """  Number037  """  
      self.Number038:int = obj["Number038"]
      """  Number038  """  
      self.Number039:int = obj["Number039"]
      """  Number039  """  
      self.Number040:int = obj["Number040"]
      """  Number040  """  
      self.Number041:int = obj["Number041"]
      """  Number041  """  
      self.Number042:int = obj["Number042"]
      """  Number042  """  
      self.Number043:int = obj["Number043"]
      """  Number043  """  
      self.Number044:int = obj["Number044"]
      """  Number044  """  
      self.Number045:int = obj["Number045"]
      """  Number045  """  
      self.Number046:int = obj["Number046"]
      """  Number046  """  
      self.Number047:int = obj["Number047"]
      """  Number047  """  
      self.Number048:int = obj["Number048"]
      """  Number048  """  
      self.Number049:int = obj["Number049"]
      """  Number049  """  
      self.Number050:int = obj["Number050"]
      """  Number050  """  
      self.Number051:int = obj["Number051"]
      """  Number051  """  
      self.Number052:int = obj["Number052"]
      """  Number052  """  
      self.Number053:int = obj["Number053"]
      """  Number053  """  
      self.Number054:int = obj["Number054"]
      """  Number054  """  
      self.Number055:int = obj["Number055"]
      """  Number055  """  
      self.Number056:int = obj["Number056"]
      """  Number056  """  
      self.Number057:int = obj["Number057"]
      """  Number057  """  
      self.Number058:int = obj["Number058"]
      """  Number058  """  
      self.Number059:int = obj["Number059"]
      """  Number059  """  
      self.Number060:int = obj["Number060"]
      """  Number060  """  
      self.Number061:int = obj["Number061"]
      """  Number061  """  
      self.Number062:int = obj["Number062"]
      """  Number062  """  
      self.Number063:int = obj["Number063"]
      """  Number063  """  
      self.Number064:int = obj["Number064"]
      """  Number064  """  
      self.Number065:int = obj["Number065"]
      """  Number065  """  
      self.Number066:int = obj["Number066"]
      """  Number066  """  
      self.Number067:int = obj["Number067"]
      """  Number067  """  
      self.Number068:int = obj["Number068"]
      """  Number068  """  
      self.Number069:int = obj["Number069"]
      """  Number069  """  
      self.Number070:int = obj["Number070"]
      """  Number070  """  
      self.Number071:int = obj["Number071"]
      """  Number071  """  
      self.Number072:int = obj["Number072"]
      """  Number072  """  
      self.Number073:int = obj["Number073"]
      """  Number073  """  
      self.Number074:int = obj["Number074"]
      """  Number074  """  
      self.Number075:int = obj["Number075"]
      """  Number075  """  
      self.Number076:int = obj["Number076"]
      """  Number076  """  
      self.Number077:int = obj["Number077"]
      """  Number077  """  
      self.Number078:int = obj["Number078"]
      """  Number078  """  
      self.Number079:int = obj["Number079"]
      """  Number079  """  
      self.Number080:int = obj["Number080"]
      """  Number080  """  
      self.Number081:int = obj["Number081"]
      """  Number081  """  
      self.Number082:int = obj["Number082"]
      """  Number082  """  
      self.Number083:int = obj["Number083"]
      """  Number083  """  
      self.Number084:int = obj["Number084"]
      """  Number084  """  
      self.Number085:int = obj["Number085"]
      """  Number085  """  
      self.Number086:int = obj["Number086"]
      """  Number086  """  
      self.Number087:int = obj["Number087"]
      """  Number087  """  
      self.Number088:int = obj["Number088"]
      """  Number088  """  
      self.Number089:int = obj["Number089"]
      """  Number089  """  
      self.Number090:int = obj["Number090"]
      """  Number090  """  
      self.Number091:int = obj["Number091"]
      """  Number091  """  
      self.Number092:int = obj["Number092"]
      """  Number092  """  
      self.Number093:int = obj["Number093"]
      """  Number093  """  
      self.Number094:int = obj["Number094"]
      """  Number094  """  
      self.Number095:int = obj["Number095"]
      """  Number095  """  
      self.Number096:int = obj["Number096"]
      """  Number096  """  
      self.Number097:int = obj["Number097"]
      """  Number097  """  
      self.Number098:int = obj["Number098"]
      """  Number098  """  
      self.Number099:int = obj["Number099"]
      """  Number099  """  
      self.Number100:int = obj["Number100"]
      """  Number100  """  
      self.Number101:int = obj["Number101"]
      """  Number101  """  
      self.Number102:int = obj["Number102"]
      """  Number102  """  
      self.Number103:int = obj["Number103"]
      """  Number103  """  
      self.Number104:int = obj["Number104"]
      """  Number104  """  
      self.Number105:int = obj["Number105"]
      """  Number105  """  
      self.Number106:int = obj["Number106"]
      """  Number106  """  
      self.Number107:int = obj["Number107"]
      """  Number107  """  
      self.Number108:int = obj["Number108"]
      """  Number108  """  
      self.Number109:int = obj["Number109"]
      """  Number109  """  
      self.Number110:int = obj["Number110"]
      """  Number110  """  
      self.Number111:int = obj["Number111"]
      """  Number111  """  
      self.Number112:int = obj["Number112"]
      """  Number112  """  
      self.Number113:int = obj["Number113"]
      """  Number113  """  
      self.Number114:int = obj["Number114"]
      """  Number114  """  
      self.Number115:int = obj["Number115"]
      """  Number115  """  
      self.Number116:int = obj["Number116"]
      """  Number116  """  
      self.Number117:int = obj["Number117"]
      """  Number117  """  
      self.Number118:int = obj["Number118"]
      """  Number118  """  
      self.Number119:int = obj["Number119"]
      """  Number119  """  
      self.Number120:int = obj["Number120"]
      """  Number120  """  
      self.Number121:int = obj["Number121"]
      """  Number121  """  
      self.Number122:int = obj["Number122"]
      """  Number122  """  
      self.Number123:int = obj["Number123"]
      """  Number123  """  
      self.Number124:int = obj["Number124"]
      """  Number124  """  
      self.Number125:int = obj["Number125"]
      """  Number125  """  
      self.Number126:int = obj["Number126"]
      """  Number126  """  
      self.Number127:int = obj["Number127"]
      """  Number127  """  
      self.Number128:int = obj["Number128"]
      """  Number128  """  
      self.Number129:int = obj["Number129"]
      """  Number129  """  
      self.Number130:int = obj["Number130"]
      """  Number130  """  
      self.Number131:int = obj["Number131"]
      """  Number131  """  
      self.Number132:int = obj["Number132"]
      """  Number132  """  
      self.Number133:int = obj["Number133"]
      """  Number133  """  
      self.Number134:int = obj["Number134"]
      """  Number134  """  
      self.Number135:int = obj["Number135"]
      """  Number135  """  
      self.Number136:int = obj["Number136"]
      """  Number136  """  
      self.Number137:int = obj["Number137"]
      """  Number137  """  
      self.Number138:int = obj["Number138"]
      """  Number138  """  
      self.Number139:int = obj["Number139"]
      """  Number139  """  
      self.Number140:int = obj["Number140"]
      """  Number140  """  
      self.Number141:int = obj["Number141"]
      """  Number141  """  
      self.Number142:int = obj["Number142"]
      """  Number142  """  
      self.Number143:int = obj["Number143"]
      """  Number143  """  
      self.Number144:int = obj["Number144"]
      """  Number144  """  
      self.Number145:int = obj["Number145"]
      """  Number145  """  
      self.Number146:int = obj["Number146"]
      """  Number146  """  
      self.Number147:int = obj["Number147"]
      """  Number147  """  
      self.Number148:int = obj["Number148"]
      """  Number148  """  
      self.Number149:int = obj["Number149"]
      """  Number149  """  
      self.Number150:int = obj["Number150"]
      """  Number150  """  
      self.Number151:int = obj["Number151"]
      """  Number151  """  
      self.Number152:int = obj["Number152"]
      """  Number152  """  
      self.Number153:int = obj["Number153"]
      """  Number153  """  
      self.Number154:int = obj["Number154"]
      """  Number154  """  
      self.Number155:int = obj["Number155"]
      """  Number155  """  
      self.Number156:int = obj["Number156"]
      """  Number156  """  
      self.Number157:int = obj["Number157"]
      """  Number157  """  
      self.Number158:int = obj["Number158"]
      """  Number158  """  
      self.Number159:int = obj["Number159"]
      """  Number159  """  
      self.Number160:int = obj["Number160"]
      """  Number160  """  
      self.Number161:int = obj["Number161"]
      """  Number161  """  
      self.Number162:int = obj["Number162"]
      """  Number162  """  
      self.Number163:int = obj["Number163"]
      """  Number163  """  
      self.Number164:int = obj["Number164"]
      """  Number164  """  
      self.Number165:int = obj["Number165"]
      """  Number165  """  
      self.Number166:int = obj["Number166"]
      """  Number166  """  
      self.Number167:int = obj["Number167"]
      """  Number167  """  
      self.Number168:int = obj["Number168"]
      """  Number168  """  
      self.Number169:int = obj["Number169"]
      """  Number169  """  
      self.Number170:int = obj["Number170"]
      """  Number170  """  
      self.Number171:int = obj["Number171"]
      """  Number171  """  
      self.Number172:int = obj["Number172"]
      """  Number172  """  
      self.Number173:int = obj["Number173"]
      """  Number173  """  
      self.Number174:int = obj["Number174"]
      """  Number174  """  
      self.Number175:int = obj["Number175"]
      """  Number175  """  
      self.Number176:int = obj["Number176"]
      """  Number176  """  
      self.Number177:int = obj["Number177"]
      """  Number177  """  
      self.Number178:int = obj["Number178"]
      """  Number178  """  
      self.Number179:int = obj["Number179"]
      """  Number179  """  
      self.Number180:int = obj["Number180"]
      """  Number180  """  
      self.Number181:int = obj["Number181"]
      """  Number181  """  
      self.Number182:int = obj["Number182"]
      """  Number182  """  
      self.Number183:int = obj["Number183"]
      """  Number183  """  
      self.Number184:int = obj["Number184"]
      """  Number184  """  
      self.Number185:int = obj["Number185"]
      """  Number185  """  
      self.Number186:int = obj["Number186"]
      """  Number186  """  
      self.Number187:int = obj["Number187"]
      """  Number187  """  
      self.Number188:int = obj["Number188"]
      """  Number188  """  
      self.Number189:int = obj["Number189"]
      """  Number189  """  
      self.Number190:int = obj["Number190"]
      """  Number190  """  
      self.Number191:int = obj["Number191"]
      """  Number191  """  
      self.Number192:int = obj["Number192"]
      """  Number192  """  
      self.Number193:int = obj["Number193"]
      """  Number193  """  
      self.Number194:int = obj["Number194"]
      """  Number194  """  
      self.Number195:int = obj["Number195"]
      """  Number195  """  
      self.Number196:int = obj["Number196"]
      """  Number196  """  
      self.Number197:int = obj["Number197"]
      """  Number197  """  
      self.Number198:int = obj["Number198"]
      """  Number198  """  
      self.Number199:int = obj["Number199"]
      """  Number199  """  
      self.Number200:int = obj["Number200"]
      """  Number200  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to. Field not currently used.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record. For future use.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number inspected  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number Inspected  """  
      self.JobNum:str = obj["JobNum"]
      """  Contains the Job Number related to the job or non-conformance being inspected.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Contain the assembly sequence of the job being inspected  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Contains the operation sequence of the job operation being inspected.  """  
      self.NCMTranID:int = obj["NCMTranID"]
      """  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  Contains the inspection plan part number (configurator part number)  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  Contains the inspection plan revision number (configurator revision number)  """  
      self.SpecID:str = obj["SpecID"]
      """  Contains the specification ID that was used in the inspection plan.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Contains the specification revision number that was used in the inspection process.  """  
      self.RMANum:int = obj["RMANum"]
      """  Contains Return Material Authorization number if inspecting for an RMA  """  
      self.RMALine:int = obj["RMALine"]
      """  Contains Line number of the RMA if inspecting for an RMA.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Contains the PO Packing Slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """  Contains the PO Packing Slip line number.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Contains the VendorNum when inspected via Skip Lot processing  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Contains the serial number of the part inspected  """  
      self.LotNum:str = obj["LotNum"]
      """  Contains the lot number of the part inspected  """  
      self.Passed:bool = obj["Passed"]
      """  True if passed  """  
      self.FailedCmtText:str = obj["FailedCmtText"]
      """  Text describing why the inspection result failed  """  
      self.TestDataEntered:bool = obj["TestDataEntered"]
      """  True if the results were saved in product configuration  """  
      self.AuditRefNum:int = obj["AuditRefNum"]
      """  This is a unique reference number that is assigned by the system for each audit record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.AuditType:str = obj["AuditType"]
      """  Shows how the audit was created - Scheduled or Manual  """  
      self.AuditID:str = obj["AuditID"]
      """  User defined Audit ID  """  
      self.AuditRevNum:str = obj["AuditRevNum"]
      """  Supplier Audit Revision Number  """  
      self.Auditor:str = obj["Auditor"]
      """  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  """  
      self.AuditSchedDate:str = obj["AuditSchedDate"]
      self.AuditCreateDate:str = obj["AuditCreateDate"]
      """  Date the audit reference was created  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  """  
      self.AuditVendNum:int = obj["AuditVendNum"]
      """  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  """  
      self.AuditCompDate:str = obj["AuditCompDate"]
      """  Date the audit was completed  """  
      self.AuditStatus:str = obj["AuditStatus"]
      """  Planned, Scheduled, In Progress, Complete  """  
      self.AuditResult:str = obj["AuditResult"]
      """  Passed, Failed, Unspecified  """  
      self.AuditConNum:int = obj["AuditConNum"]
      """  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  """  
      self.AuditConRole:str = obj["AuditConRole"]
      """  Code that identifies the role of the audit contact.  """  
      self.AuditCost:int = obj["AuditCost"]
      """  This is the cost of performing the audit.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsShortCharAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsShortCharRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.ShortChar001:str = obj["ShortChar001"]
      """  ShortChar001  """  
      self.ShortChar002:str = obj["ShortChar002"]
      """  ShortChar002  """  
      self.ShortChar003:str = obj["ShortChar003"]
      """  ShortChar003  """  
      self.ShortChar004:str = obj["ShortChar004"]
      """  ShortChar004  """  
      self.ShortChar005:str = obj["ShortChar005"]
      """  ShortChar005  """  
      self.ShortChar006:str = obj["ShortChar006"]
      """  ShortChar006  """  
      self.ShortChar007:str = obj["ShortChar007"]
      """  ShortChar007  """  
      self.ShortChar008:str = obj["ShortChar008"]
      """  ShortChar008  """  
      self.ShortChar009:str = obj["ShortChar009"]
      """  ShortChar009  """  
      self.ShortChar010:str = obj["ShortChar010"]
      """  ShortChar010  """  
      self.ShortChar011:str = obj["ShortChar011"]
      """  ShortChar011  """  
      self.ShortChar012:str = obj["ShortChar012"]
      """  ShortChar012  """  
      self.ShortChar013:str = obj["ShortChar013"]
      """  ShortChar013  """  
      self.ShortChar014:str = obj["ShortChar014"]
      """  ShortChar014  """  
      self.ShortChar015:str = obj["ShortChar015"]
      """  ShortChar015  """  
      self.ShortChar016:str = obj["ShortChar016"]
      """  ShortChar016  """  
      self.ShortChar017:str = obj["ShortChar017"]
      """  ShortChar017  """  
      self.ShortChar018:str = obj["ShortChar018"]
      """  ShortChar018  """  
      self.ShortChar019:str = obj["ShortChar019"]
      """  ShortChar019  """  
      self.ShortChar020:str = obj["ShortChar020"]
      """  ShortChar020  """  
      self.ShortChar021:str = obj["ShortChar021"]
      """  ShortChar021  """  
      self.ShortChar022:str = obj["ShortChar022"]
      """  ShortChar022  """  
      self.ShortChar023:str = obj["ShortChar023"]
      """  ShortChar023  """  
      self.ShortChar024:str = obj["ShortChar024"]
      """  ShortChar024  """  
      self.ShortChar025:str = obj["ShortChar025"]
      """  ShortChar025  """  
      self.ShortChar026:str = obj["ShortChar026"]
      """  ShortChar026  """  
      self.ShortChar027:str = obj["ShortChar027"]
      """  ShortChar027  """  
      self.ShortChar028:str = obj["ShortChar028"]
      """  ShortChar028  """  
      self.ShortChar029:str = obj["ShortChar029"]
      """  ShortChar029  """  
      self.ShortChar030:str = obj["ShortChar030"]
      """  ShortChar030  """  
      self.ShortChar031:str = obj["ShortChar031"]
      """  ShortChar031  """  
      self.ShortChar032:str = obj["ShortChar032"]
      """  ShortChar032  """  
      self.ShortChar033:str = obj["ShortChar033"]
      """  ShortChar033  """  
      self.ShortChar034:str = obj["ShortChar034"]
      """  ShortChar034  """  
      self.ShortChar035:str = obj["ShortChar035"]
      """  ShortChar035  """  
      self.ShortChar036:str = obj["ShortChar036"]
      """  ShortChar036  """  
      self.ShortChar037:str = obj["ShortChar037"]
      """  ShortChar037  """  
      self.ShortChar038:str = obj["ShortChar038"]
      """  ShortChar038  """  
      self.ShortChar039:str = obj["ShortChar039"]
      """  ShortChar039  """  
      self.ShortChar040:str = obj["ShortChar040"]
      """  ShortChar040  """  
      self.ShortChar041:str = obj["ShortChar041"]
      """  ShortChar041  """  
      self.ShortChar042:str = obj["ShortChar042"]
      """  ShortChar042  """  
      self.ShortChar043:str = obj["ShortChar043"]
      """  ShortChar043  """  
      self.ShortChar044:str = obj["ShortChar044"]
      """  ShortChar044  """  
      self.ShortChar045:str = obj["ShortChar045"]
      """  ShortChar045  """  
      self.ShortChar046:str = obj["ShortChar046"]
      """  ShortChar046  """  
      self.ShortChar047:str = obj["ShortChar047"]
      """  ShortChar047  """  
      self.ShortChar048:str = obj["ShortChar048"]
      """  ShortChar048  """  
      self.ShortChar049:str = obj["ShortChar049"]
      """  ShortChar049  """  
      self.ShortChar050:str = obj["ShortChar050"]
      """  ShortChar050  """  
      self.ShortChar051:str = obj["ShortChar051"]
      """  ShortChar051  """  
      self.ShortChar052:str = obj["ShortChar052"]
      """  ShortChar052  """  
      self.ShortChar053:str = obj["ShortChar053"]
      """  ShortChar053  """  
      self.ShortChar054:str = obj["ShortChar054"]
      """  ShortChar054  """  
      self.ShortChar055:str = obj["ShortChar055"]
      """  ShortChar055  """  
      self.ShortChar056:str = obj["ShortChar056"]
      """  ShortChar056  """  
      self.ShortChar057:str = obj["ShortChar057"]
      """  ShortChar057  """  
      self.ShortChar058:str = obj["ShortChar058"]
      """  ShortChar058  """  
      self.ShortChar059:str = obj["ShortChar059"]
      """  ShortChar059  """  
      self.ShortChar060:str = obj["ShortChar060"]
      """  ShortChar060  """  
      self.ShortChar061:str = obj["ShortChar061"]
      """  ShortChar061  """  
      self.ShortChar062:str = obj["ShortChar062"]
      """  ShortChar062  """  
      self.ShortChar063:str = obj["ShortChar063"]
      """  ShortChar063  """  
      self.ShortChar064:str = obj["ShortChar064"]
      """  ShortChar064  """  
      self.ShortChar065:str = obj["ShortChar065"]
      """  ShortChar065  """  
      self.ShortChar066:str = obj["ShortChar066"]
      """  ShortChar066  """  
      self.ShortChar067:str = obj["ShortChar067"]
      """  ShortChar067  """  
      self.ShortChar068:str = obj["ShortChar068"]
      """  ShortChar068  """  
      self.ShortChar069:str = obj["ShortChar069"]
      """  ShortChar069  """  
      self.ShortChar070:str = obj["ShortChar070"]
      """  ShortChar070  """  
      self.ShortChar071:str = obj["ShortChar071"]
      """  ShortChar071  """  
      self.ShortChar072:str = obj["ShortChar072"]
      """  ShortChar072  """  
      self.ShortChar073:str = obj["ShortChar073"]
      """  ShortChar073  """  
      self.ShortChar074:str = obj["ShortChar074"]
      """  ShortChar074  """  
      self.ShortChar075:str = obj["ShortChar075"]
      """  ShortChar075  """  
      self.ShortChar076:str = obj["ShortChar076"]
      """  ShortChar076  """  
      self.ShortChar077:str = obj["ShortChar077"]
      """  ShortChar077  """  
      self.ShortChar078:str = obj["ShortChar078"]
      """  ShortChar078  """  
      self.ShortChar079:str = obj["ShortChar079"]
      """  ShortChar079  """  
      self.ShortChar080:str = obj["ShortChar080"]
      """  ShortChar080  """  
      self.ShortChar081:str = obj["ShortChar081"]
      """  ShortChar081  """  
      self.ShortChar082:str = obj["ShortChar082"]
      """  ShortChar082  """  
      self.ShortChar083:str = obj["ShortChar083"]
      """  ShortChar083  """  
      self.ShortChar084:str = obj["ShortChar084"]
      """  ShortChar084  """  
      self.ShortChar085:str = obj["ShortChar085"]
      """  ShortChar085  """  
      self.ShortChar086:str = obj["ShortChar086"]
      """  ShortChar086  """  
      self.ShortChar087:str = obj["ShortChar087"]
      """  ShortChar087  """  
      self.ShortChar088:str = obj["ShortChar088"]
      """  ShortChar088  """  
      self.ShortChar089:str = obj["ShortChar089"]
      """  ShortChar089  """  
      self.ShortChar090:str = obj["ShortChar090"]
      """  ShortChar090  """  
      self.ShortChar091:str = obj["ShortChar091"]
      """  ShortChar091  """  
      self.ShortChar092:str = obj["ShortChar092"]
      """  ShortChar092  """  
      self.ShortChar093:str = obj["ShortChar093"]
      """  ShortChar093  """  
      self.ShortChar094:str = obj["ShortChar094"]
      """  ShortChar094  """  
      self.ShortChar095:str = obj["ShortChar095"]
      """  ShortChar095  """  
      self.ShortChar096:str = obj["ShortChar096"]
      """  ShortChar096  """  
      self.ShortChar097:str = obj["ShortChar097"]
      """  ShortChar097  """  
      self.ShortChar098:str = obj["ShortChar098"]
      """  ShortChar098  """  
      self.ShortChar099:str = obj["ShortChar099"]
      """  ShortChar099  """  
      self.ShortChar100:str = obj["ShortChar100"]
      """  ShortChar100  """  
      self.ShortChar101:str = obj["ShortChar101"]
      """  ShortChar101  """  
      self.ShortChar102:str = obj["ShortChar102"]
      """  ShortChar102  """  
      self.ShortChar103:str = obj["ShortChar103"]
      """  ShortChar103  """  
      self.ShortChar104:str = obj["ShortChar104"]
      """  ShortChar104  """  
      self.ShortChar105:str = obj["ShortChar105"]
      """  ShortChar105  """  
      self.ShortChar106:str = obj["ShortChar106"]
      """  ShortChar106  """  
      self.ShortChar107:str = obj["ShortChar107"]
      """  ShortChar107  """  
      self.ShortChar108:str = obj["ShortChar108"]
      """  ShortChar108  """  
      self.ShortChar109:str = obj["ShortChar109"]
      """  ShortChar109  """  
      self.ShortChar110:str = obj["ShortChar110"]
      """  ShortChar110  """  
      self.ShortChar111:str = obj["ShortChar111"]
      """  ShortChar111  """  
      self.ShortChar112:str = obj["ShortChar112"]
      """  ShortChar112  """  
      self.ShortChar113:str = obj["ShortChar113"]
      """  ShortChar113  """  
      self.ShortChar114:str = obj["ShortChar114"]
      """  ShortChar114  """  
      self.ShortChar115:str = obj["ShortChar115"]
      """  ShortChar115  """  
      self.ShortChar116:str = obj["ShortChar116"]
      """  ShortChar116  """  
      self.ShortChar117:str = obj["ShortChar117"]
      """  ShortChar117  """  
      self.ShortChar118:str = obj["ShortChar118"]
      """  ShortChar118  """  
      self.ShortChar119:str = obj["ShortChar119"]
      """  ShortChar119  """  
      self.ShortChar120:str = obj["ShortChar120"]
      """  ShortChar120  """  
      self.ShortChar121:str = obj["ShortChar121"]
      """  ShortChar121  """  
      self.ShortChar122:str = obj["ShortChar122"]
      """  ShortChar122  """  
      self.ShortChar123:str = obj["ShortChar123"]
      """  ShortChar123  """  
      self.ShortChar124:str = obj["ShortChar124"]
      """  ShortChar124  """  
      self.ShortChar125:str = obj["ShortChar125"]
      """  ShortChar125  """  
      self.ShortChar126:str = obj["ShortChar126"]
      """  ShortChar126  """  
      self.ShortChar127:str = obj["ShortChar127"]
      """  ShortChar127  """  
      self.ShortChar128:str = obj["ShortChar128"]
      """  ShortChar128  """  
      self.ShortChar129:str = obj["ShortChar129"]
      """  ShortChar129  """  
      self.ShortChar130:str = obj["ShortChar130"]
      """  ShortChar130  """  
      self.ShortChar131:str = obj["ShortChar131"]
      """  ShortChar131  """  
      self.ShortChar132:str = obj["ShortChar132"]
      """  ShortChar132  """  
      self.ShortChar133:str = obj["ShortChar133"]
      """  ShortChar133  """  
      self.ShortChar134:str = obj["ShortChar134"]
      """  ShortChar134  """  
      self.ShortChar135:str = obj["ShortChar135"]
      """  ShortChar135  """  
      self.ShortChar136:str = obj["ShortChar136"]
      """  ShortChar136  """  
      self.ShortChar137:str = obj["ShortChar137"]
      """  ShortChar137  """  
      self.ShortChar138:str = obj["ShortChar138"]
      """  ShortChar138  """  
      self.ShortChar139:str = obj["ShortChar139"]
      """  ShortChar139  """  
      self.ShortChar140:str = obj["ShortChar140"]
      """  ShortChar140  """  
      self.ShortChar141:str = obj["ShortChar141"]
      """  ShortChar141  """  
      self.ShortChar142:str = obj["ShortChar142"]
      """  ShortChar142  """  
      self.ShortChar143:str = obj["ShortChar143"]
      """  ShortChar143  """  
      self.ShortChar144:str = obj["ShortChar144"]
      """  ShortChar144  """  
      self.ShortChar145:str = obj["ShortChar145"]
      """  ShortChar145  """  
      self.ShortChar146:str = obj["ShortChar146"]
      """  ShortChar146  """  
      self.ShortChar147:str = obj["ShortChar147"]
      """  ShortChar147  """  
      self.ShortChar148:str = obj["ShortChar148"]
      """  ShortChar148  """  
      self.ShortChar149:str = obj["ShortChar149"]
      """  ShortChar149  """  
      self.ShortChar150:str = obj["ShortChar150"]
      """  ShortChar150  """  
      self.ShortChar151:str = obj["ShortChar151"]
      """  ShortChar151  """  
      self.ShortChar152:str = obj["ShortChar152"]
      """  ShortChar152  """  
      self.ShortChar153:str = obj["ShortChar153"]
      """  ShortChar153  """  
      self.ShortChar154:str = obj["ShortChar154"]
      """  ShortChar154  """  
      self.ShortChar155:str = obj["ShortChar155"]
      """  ShortChar155  """  
      self.ShortChar156:str = obj["ShortChar156"]
      """  ShortChar156  """  
      self.ShortChar157:str = obj["ShortChar157"]
      """  ShortChar157  """  
      self.ShortChar158:str = obj["ShortChar158"]
      """  ShortChar158  """  
      self.ShortChar159:str = obj["ShortChar159"]
      """  ShortChar159  """  
      self.ShortChar160:str = obj["ShortChar160"]
      """  ShortChar160  """  
      self.ShortChar161:str = obj["ShortChar161"]
      """  ShortChar161  """  
      self.ShortChar162:str = obj["ShortChar162"]
      """  ShortChar162  """  
      self.ShortChar163:str = obj["ShortChar163"]
      """  ShortChar163  """  
      self.ShortChar164:str = obj["ShortChar164"]
      """  ShortChar164  """  
      self.ShortChar165:str = obj["ShortChar165"]
      """  ShortChar165  """  
      self.ShortChar166:str = obj["ShortChar166"]
      """  ShortChar166  """  
      self.ShortChar167:str = obj["ShortChar167"]
      """  ShortChar167  """  
      self.ShortChar168:str = obj["ShortChar168"]
      """  ShortChar168  """  
      self.ShortChar169:str = obj["ShortChar169"]
      """  ShortChar169  """  
      self.ShortChar170:str = obj["ShortChar170"]
      """  ShortChar170  """  
      self.ShortChar171:str = obj["ShortChar171"]
      """  ShortChar171  """  
      self.ShortChar172:str = obj["ShortChar172"]
      """  ShortChar172  """  
      self.ShortChar173:str = obj["ShortChar173"]
      """  ShortChar173  """  
      self.ShortChar174:str = obj["ShortChar174"]
      """  ShortChar174  """  
      self.ShortChar175:str = obj["ShortChar175"]
      """  ShortChar175  """  
      self.ShortChar176:str = obj["ShortChar176"]
      """  ShortChar176  """  
      self.ShortChar177:str = obj["ShortChar177"]
      """  ShortChar177  """  
      self.ShortChar178:str = obj["ShortChar178"]
      """  ShortChar178  """  
      self.ShortChar179:str = obj["ShortChar179"]
      """  ShortChar179  """  
      self.ShortChar180:str = obj["ShortChar180"]
      """  ShortChar180  """  
      self.ShortChar181:str = obj["ShortChar181"]
      """  ShortChar181  """  
      self.ShortChar182:str = obj["ShortChar182"]
      """  ShortChar182  """  
      self.ShortChar183:str = obj["ShortChar183"]
      """  ShortChar183  """  
      self.ShortChar184:str = obj["ShortChar184"]
      """  ShortChar184  """  
      self.ShortChar185:str = obj["ShortChar185"]
      """  ShortChar185  """  
      self.ShortChar186:str = obj["ShortChar186"]
      """  ShortChar186  """  
      self.ShortChar187:str = obj["ShortChar187"]
      """  ShortChar187  """  
      self.ShortChar188:str = obj["ShortChar188"]
      """  ShortChar188  """  
      self.ShortChar189:str = obj["ShortChar189"]
      """  ShortChar189  """  
      self.ShortChar190:str = obj["ShortChar190"]
      """  ShortChar190  """  
      self.ShortChar191:str = obj["ShortChar191"]
      """  ShortChar191  """  
      self.ShortChar192:str = obj["ShortChar192"]
      """  ShortChar192  """  
      self.ShortChar193:str = obj["ShortChar193"]
      """  ShortChar193  """  
      self.ShortChar194:str = obj["ShortChar194"]
      """  ShortChar194  """  
      self.ShortChar195:str = obj["ShortChar195"]
      """  ShortChar195  """  
      self.ShortChar196:str = obj["ShortChar196"]
      """  ShortChar196  """  
      self.ShortChar197:str = obj["ShortChar197"]
      """  ShortChar197  """  
      self.ShortChar198:str = obj["ShortChar198"]
      """  ShortChar198  """  
      self.ShortChar199:str = obj["ShortChar199"]
      """  ShortChar199  """  
      self.ShortChar200:str = obj["ShortChar200"]
      """  ShortChar200  """  
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
class ClickToolRetrieveValues_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class ClickToolRetrieveValues_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      self.dynamicMetadataDS:list[Erp_Tablesets_DynamicMetadataTableset] = obj["dynamicMetadataDS"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
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

class Erp_Tablesets_InspDataParamRow:
   def __init__(self, obj):
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      self.SpecID:str = obj["SpecID"]
      self.SpecRevNum:str = obj["SpecRevNum"]
      self.InspPlanDesc:str = obj["InspPlanDesc"]
      self.SpecDesc:str = obj["SpecDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PartDesc:str = obj["PartDesc"]
      self.NCMTranID:int = obj["NCMTranID"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.InspectDate:str = obj["InspectDate"]
      self.PackSlip:str = obj["PackSlip"]
      self.PackLine:int = obj["PackLine"]
      self.VendorNum:int = obj["VendorNum"]
      self.VendorName:str = obj["VendorName"]
      self.SeqNum:int = obj["SeqNum"]
      self.InspType:str = obj["InspType"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.VendorID:str = obj["VendorID"]
      self.DataEntered:bool = obj["DataEntered"]
      self.PartOnlyDataExists:bool = obj["PartOnlyDataExists"]
      self.AssetID:str = obj["AssetID"]
      """  Asset ID  """  
      self.EquipID:str = obj["EquipID"]
      """  Equipment ID  """  
      self.ResourceSelectID:str = obj["ResourceSelectID"]
      """  Resource ID  """  
      self.InspTypeDesc:str = obj["InspTypeDesc"]
      """  Description for Resorce, Asset or Qqupment based on the valuse ot InspType  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspDataParamTableset:
   def __init__(self, obj):
      self.InspDataParam:list[Erp_Tablesets_InspDataParamRow] = obj["InspDataParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InspDataTrackerTableset:
   def __init__(self, obj):
      self.InspResults:list[Erp_Tablesets_InspResultsRow] = obj["InspResults"]
      self.InspResultsAttch:list[Erp_Tablesets_InspResultsAttchRow] = obj["InspResultsAttch"]
      self.InspResultsChar:list[Erp_Tablesets_InspResultsCharRow] = obj["InspResultsChar"]
      self.InspResultsCharAttch:list[Erp_Tablesets_InspResultsCharAttchRow] = obj["InspResultsCharAttch"]
      self.InspResultsCheckBox:list[Erp_Tablesets_InspResultsCheckBoxRow] = obj["InspResultsCheckBox"]
      self.InspResultsCheckBoxAttch:list[Erp_Tablesets_InspResultsCheckBoxAttchRow] = obj["InspResultsCheckBoxAttch"]
      self.InspResultsDate:list[Erp_Tablesets_InspResultsDateRow] = obj["InspResultsDate"]
      self.InspResultsDateAttch:list[Erp_Tablesets_InspResultsDateAttchRow] = obj["InspResultsDateAttch"]
      self.InspResultsNum:list[Erp_Tablesets_InspResultsNumRow] = obj["InspResultsNum"]
      self.InspResultsNumAttch:list[Erp_Tablesets_InspResultsNumAttchRow] = obj["InspResultsNumAttch"]
      self.InspResultsShortChar:list[Erp_Tablesets_InspResultsShortCharRow] = obj["InspResultsShortChar"]
      self.InspResultsShortCharAttch:list[Erp_Tablesets_InspResultsShortCharAttchRow] = obj["InspResultsShortCharAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InspDisplayColumnsRow:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      self.AttributeID:str = obj["AttributeID"]
      self.ColumnFormat:str = obj["ColumnFormat"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspDisplayColumnsTableset:
   def __init__(self, obj):
      self.InspDisplayColumns:list[Erp_Tablesets_InspDisplayColumnsRow] = obj["InspDisplayColumns"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InspResultsAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsCharAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsCharRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Character001:str = obj["Character001"]
      """  Character001  """  
      self.Character002:str = obj["Character002"]
      """  Character002  """  
      self.Character003:str = obj["Character003"]
      """  Character003  """  
      self.Character004:str = obj["Character004"]
      """  Character004  """  
      self.Character005:str = obj["Character005"]
      """  Character005  """  
      self.Character006:str = obj["Character006"]
      """  Character006  """  
      self.Character007:str = obj["Character007"]
      """  Character007  """  
      self.Character008:str = obj["Character008"]
      """  Character008  """  
      self.Character009:str = obj["Character009"]
      """  Character009  """  
      self.Character010:str = obj["Character010"]
      """  Character010  """  
      self.Character011:str = obj["Character011"]
      """  Character011  """  
      self.Character012:str = obj["Character012"]
      """  Character012  """  
      self.Character013:str = obj["Character013"]
      """  Character013  """  
      self.Character014:str = obj["Character014"]
      """  Character014  """  
      self.Character015:str = obj["Character015"]
      """  Character015  """  
      self.Character016:str = obj["Character016"]
      """  Character016  """  
      self.Character017:str = obj["Character017"]
      """  Character017  """  
      self.Character018:str = obj["Character018"]
      """  Character018  """  
      self.Character019:str = obj["Character019"]
      """  Character019  """  
      self.Character020:str = obj["Character020"]
      """  Character020  """  
      self.Character021:str = obj["Character021"]
      """  Character021  """  
      self.Character022:str = obj["Character022"]
      """  Character022  """  
      self.Character023:str = obj["Character023"]
      """  Character023  """  
      self.Character024:str = obj["Character024"]
      """  Character024  """  
      self.Character025:str = obj["Character025"]
      """  Character025  """  
      self.Character026:str = obj["Character026"]
      """  Character026  """  
      self.Character027:str = obj["Character027"]
      """  Character027  """  
      self.Character028:str = obj["Character028"]
      """  Character028  """  
      self.Character029:str = obj["Character029"]
      """  Character029  """  
      self.Character030:str = obj["Character030"]
      """  Character030  """  
      self.Character031:str = obj["Character031"]
      """  Character031  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsCheckBoxAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsCheckBoxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.CheckBox001:bool = obj["CheckBox001"]
      """  CheckBox001  """  
      self.CheckBox002:bool = obj["CheckBox002"]
      """  CheckBox002  """  
      self.CheckBox003:bool = obj["CheckBox003"]
      """  CheckBox003  """  
      self.CheckBox004:bool = obj["CheckBox004"]
      """  CheckBox004  """  
      self.CheckBox005:bool = obj["CheckBox005"]
      """  CheckBox005  """  
      self.CheckBox006:bool = obj["CheckBox006"]
      """  CheckBox006  """  
      self.CheckBox007:bool = obj["CheckBox007"]
      """  CheckBox007  """  
      self.CheckBox008:bool = obj["CheckBox008"]
      """  CheckBox008  """  
      self.CheckBox009:bool = obj["CheckBox009"]
      """  CheckBox009  """  
      self.CheckBox010:bool = obj["CheckBox010"]
      """  CheckBox010  """  
      self.CheckBox011:bool = obj["CheckBox011"]
      """  CheckBox011  """  
      self.CheckBox012:bool = obj["CheckBox012"]
      """  CheckBox012  """  
      self.CheckBox013:bool = obj["CheckBox013"]
      """  CheckBox013  """  
      self.CheckBox014:bool = obj["CheckBox014"]
      """  CheckBox014  """  
      self.CheckBox015:bool = obj["CheckBox015"]
      """  CheckBox015  """  
      self.CheckBox016:bool = obj["CheckBox016"]
      """  CheckBox016  """  
      self.CheckBox017:bool = obj["CheckBox017"]
      """  CheckBox017  """  
      self.CheckBox018:bool = obj["CheckBox018"]
      """  CheckBox018  """  
      self.CheckBox019:bool = obj["CheckBox019"]
      """  CheckBox019  """  
      self.CheckBox020:bool = obj["CheckBox020"]
      """  CheckBox020  """  
      self.CheckBox021:bool = obj["CheckBox021"]
      """  CheckBox021  """  
      self.CheckBox022:bool = obj["CheckBox022"]
      """  CheckBox022  """  
      self.CheckBox023:bool = obj["CheckBox023"]
      """  CheckBox023  """  
      self.CheckBox024:bool = obj["CheckBox024"]
      """  CheckBox024  """  
      self.CheckBox025:bool = obj["CheckBox025"]
      """  CheckBox025  """  
      self.CheckBox026:bool = obj["CheckBox026"]
      """  CheckBox026  """  
      self.CheckBox027:bool = obj["CheckBox027"]
      """  CheckBox027  """  
      self.CheckBox028:bool = obj["CheckBox028"]
      """  CheckBox028  """  
      self.CheckBox029:bool = obj["CheckBox029"]
      """  CheckBox029  """  
      self.CheckBox030:bool = obj["CheckBox030"]
      """  CheckBox030  """  
      self.CheckBox031:bool = obj["CheckBox031"]
      """  CheckBox031  """  
      self.CheckBox032:bool = obj["CheckBox032"]
      """  CheckBox032  """  
      self.CheckBox033:bool = obj["CheckBox033"]
      """  CheckBox033  """  
      self.CheckBox034:bool = obj["CheckBox034"]
      """  CheckBox034  """  
      self.CheckBox035:bool = obj["CheckBox035"]
      """  CheckBox035  """  
      self.CheckBox036:bool = obj["CheckBox036"]
      """  CheckBox036  """  
      self.CheckBox037:bool = obj["CheckBox037"]
      """  CheckBox037  """  
      self.CheckBox038:bool = obj["CheckBox038"]
      """  CheckBox038  """  
      self.CheckBox039:bool = obj["CheckBox039"]
      """  CheckBox039  """  
      self.CheckBox040:bool = obj["CheckBox040"]
      """  CheckBox040  """  
      self.CheckBox041:bool = obj["CheckBox041"]
      """  CheckBox041  """  
      self.CheckBox042:bool = obj["CheckBox042"]
      """  CheckBox042  """  
      self.CheckBox043:bool = obj["CheckBox043"]
      """  CheckBox043  """  
      self.CheckBox044:bool = obj["CheckBox044"]
      """  CheckBox044  """  
      self.CheckBox045:bool = obj["CheckBox045"]
      """  CheckBox045  """  
      self.CheckBox046:bool = obj["CheckBox046"]
      """  CheckBox046  """  
      self.CheckBox047:bool = obj["CheckBox047"]
      """  CheckBox047  """  
      self.CheckBox048:bool = obj["CheckBox048"]
      """  CheckBox048  """  
      self.CheckBox049:bool = obj["CheckBox049"]
      """  CheckBox049  """  
      self.CheckBox050:bool = obj["CheckBox050"]
      """  CheckBox050  """  
      self.CheckBox051:bool = obj["CheckBox051"]
      """  CheckBox051  """  
      self.CheckBox052:bool = obj["CheckBox052"]
      """  CheckBox052  """  
      self.CheckBox053:bool = obj["CheckBox053"]
      """  CheckBox053  """  
      self.CheckBox054:bool = obj["CheckBox054"]
      """  CheckBox054  """  
      self.CheckBox055:bool = obj["CheckBox055"]
      """  CheckBox055  """  
      self.CheckBox056:bool = obj["CheckBox056"]
      """  CheckBox056  """  
      self.CheckBox057:bool = obj["CheckBox057"]
      """  CheckBox057  """  
      self.CheckBox058:bool = obj["CheckBox058"]
      """  CheckBox058  """  
      self.CheckBox059:bool = obj["CheckBox059"]
      """  CheckBox059  """  
      self.CheckBox060:bool = obj["CheckBox060"]
      """  CheckBox060  """  
      self.CheckBox061:bool = obj["CheckBox061"]
      """  CheckBox061  """  
      self.CheckBox062:bool = obj["CheckBox062"]
      """  CheckBox062  """  
      self.CheckBox063:bool = obj["CheckBox063"]
      """  CheckBox063  """  
      self.CheckBox064:bool = obj["CheckBox064"]
      """  CheckBox064  """  
      self.CheckBox065:bool = obj["CheckBox065"]
      """  CheckBox065  """  
      self.CheckBox066:bool = obj["CheckBox066"]
      """  CheckBox066  """  
      self.CheckBox067:bool = obj["CheckBox067"]
      """  CheckBox067  """  
      self.CheckBox068:bool = obj["CheckBox068"]
      """  CheckBox068  """  
      self.CheckBox069:bool = obj["CheckBox069"]
      """  CheckBox069  """  
      self.CheckBox070:bool = obj["CheckBox070"]
      """  CheckBox070  """  
      self.CheckBox071:bool = obj["CheckBox071"]
      """  CheckBox071  """  
      self.CheckBox072:bool = obj["CheckBox072"]
      """  CheckBox072  """  
      self.CheckBox073:bool = obj["CheckBox073"]
      """  CheckBox073  """  
      self.CheckBox074:bool = obj["CheckBox074"]
      """  CheckBox074  """  
      self.CheckBox075:bool = obj["CheckBox075"]
      """  CheckBox075  """  
      self.CheckBox076:bool = obj["CheckBox076"]
      """  CheckBox076  """  
      self.CheckBox077:bool = obj["CheckBox077"]
      """  CheckBox077  """  
      self.CheckBox078:bool = obj["CheckBox078"]
      """  CheckBox078  """  
      self.CheckBox079:bool = obj["CheckBox079"]
      """  CheckBox079  """  
      self.CheckBox080:bool = obj["CheckBox080"]
      """  CheckBox080  """  
      self.CheckBox081:bool = obj["CheckBox081"]
      """  CheckBox081  """  
      self.CheckBox082:bool = obj["CheckBox082"]
      """  CheckBox082  """  
      self.CheckBox083:bool = obj["CheckBox083"]
      """  CheckBox083  """  
      self.CheckBox084:bool = obj["CheckBox084"]
      """  CheckBox084  """  
      self.CheckBox085:bool = obj["CheckBox085"]
      """  CheckBox085  """  
      self.CheckBox086:bool = obj["CheckBox086"]
      """  CheckBox086  """  
      self.CheckBox087:bool = obj["CheckBox087"]
      """  CheckBox087  """  
      self.CheckBox088:bool = obj["CheckBox088"]
      """  CheckBox088  """  
      self.CheckBox089:bool = obj["CheckBox089"]
      """  CheckBox089  """  
      self.CheckBox090:bool = obj["CheckBox090"]
      """  CheckBox090  """  
      self.CheckBox091:bool = obj["CheckBox091"]
      """  CheckBox091  """  
      self.CheckBox092:bool = obj["CheckBox092"]
      """  CheckBox092  """  
      self.CheckBox093:bool = obj["CheckBox093"]
      """  CheckBox093  """  
      self.CheckBox094:bool = obj["CheckBox094"]
      """  CheckBox094  """  
      self.CheckBox095:bool = obj["CheckBox095"]
      """  CheckBox095  """  
      self.CheckBox096:bool = obj["CheckBox096"]
      """  CheckBox096  """  
      self.CheckBox097:bool = obj["CheckBox097"]
      """  CheckBox097  """  
      self.CheckBox098:bool = obj["CheckBox098"]
      """  CheckBox098  """  
      self.CheckBox099:bool = obj["CheckBox099"]
      """  CheckBox099  """  
      self.CheckBox100:bool = obj["CheckBox100"]
      """  CheckBox100  """  
      self.CheckBox101:bool = obj["CheckBox101"]
      """  CheckBox101  """  
      self.CheckBox102:bool = obj["CheckBox102"]
      """  CheckBox102  """  
      self.CheckBox103:bool = obj["CheckBox103"]
      """  CheckBox103  """  
      self.CheckBox104:bool = obj["CheckBox104"]
      """  CheckBox104  """  
      self.CheckBox105:bool = obj["CheckBox105"]
      """  CheckBox105  """  
      self.CheckBox106:bool = obj["CheckBox106"]
      """  CheckBox106  """  
      self.CheckBox107:bool = obj["CheckBox107"]
      """  CheckBox107  """  
      self.CheckBox108:bool = obj["CheckBox108"]
      """  CheckBox108  """  
      self.CheckBox109:bool = obj["CheckBox109"]
      """  CheckBox109  """  
      self.CheckBox110:bool = obj["CheckBox110"]
      """  CheckBox110  """  
      self.CheckBox111:bool = obj["CheckBox111"]
      """  CheckBox111  """  
      self.CheckBox112:bool = obj["CheckBox112"]
      """  CheckBox112  """  
      self.CheckBox113:bool = obj["CheckBox113"]
      """  CheckBox113  """  
      self.CheckBox114:bool = obj["CheckBox114"]
      """  CheckBox114  """  
      self.CheckBox115:bool = obj["CheckBox115"]
      """  CheckBox115  """  
      self.CheckBox116:bool = obj["CheckBox116"]
      """  CheckBox116  """  
      self.CheckBox117:bool = obj["CheckBox117"]
      """  CheckBox117  """  
      self.CheckBox118:bool = obj["CheckBox118"]
      """  CheckBox118  """  
      self.CheckBox119:bool = obj["CheckBox119"]
      """  CheckBox119  """  
      self.CheckBox120:bool = obj["CheckBox120"]
      """  CheckBox120  """  
      self.CheckBox121:bool = obj["CheckBox121"]
      """  CheckBox121  """  
      self.CheckBox122:bool = obj["CheckBox122"]
      """  CheckBox122  """  
      self.CheckBox123:bool = obj["CheckBox123"]
      """  CheckBox123  """  
      self.CheckBox124:bool = obj["CheckBox124"]
      """  CheckBox124  """  
      self.CheckBox125:bool = obj["CheckBox125"]
      """  CheckBox125  """  
      self.CheckBox126:bool = obj["CheckBox126"]
      """  CheckBox126  """  
      self.CheckBox127:bool = obj["CheckBox127"]
      """  CheckBox127  """  
      self.CheckBox128:bool = obj["CheckBox128"]
      """  CheckBox128  """  
      self.CheckBox129:bool = obj["CheckBox129"]
      """  CheckBox129  """  
      self.CheckBox130:bool = obj["CheckBox130"]
      """  CheckBox130  """  
      self.CheckBox131:bool = obj["CheckBox131"]
      """  CheckBox131  """  
      self.CheckBox132:bool = obj["CheckBox132"]
      """  CheckBox132  """  
      self.CheckBox133:bool = obj["CheckBox133"]
      """  CheckBox133  """  
      self.CheckBox134:bool = obj["CheckBox134"]
      """  CheckBox134  """  
      self.CheckBox135:bool = obj["CheckBox135"]
      """  CheckBox135  """  
      self.CheckBox136:bool = obj["CheckBox136"]
      """  CheckBox136  """  
      self.CheckBox137:bool = obj["CheckBox137"]
      """  CheckBox137  """  
      self.CheckBox138:bool = obj["CheckBox138"]
      """  CheckBox138  """  
      self.CheckBox139:bool = obj["CheckBox139"]
      """  CheckBox139  """  
      self.CheckBox140:bool = obj["CheckBox140"]
      """  CheckBox140  """  
      self.CheckBox141:bool = obj["CheckBox141"]
      """  CheckBox141  """  
      self.CheckBox142:bool = obj["CheckBox142"]
      """  CheckBox142  """  
      self.CheckBox143:bool = obj["CheckBox143"]
      """  CheckBox143  """  
      self.CheckBox144:bool = obj["CheckBox144"]
      """  CheckBox144  """  
      self.CheckBox145:bool = obj["CheckBox145"]
      """  CheckBox145  """  
      self.CheckBox146:bool = obj["CheckBox146"]
      """  CheckBox146  """  
      self.CheckBox147:bool = obj["CheckBox147"]
      """  CheckBox147  """  
      self.CheckBox148:bool = obj["CheckBox148"]
      """  CheckBox148  """  
      self.CheckBox149:bool = obj["CheckBox149"]
      """  CheckBox149  """  
      self.CheckBox150:bool = obj["CheckBox150"]
      """  CheckBox150  """  
      self.CheckBox151:bool = obj["CheckBox151"]
      """  CheckBox151  """  
      self.CheckBox152:bool = obj["CheckBox152"]
      """  CheckBox152  """  
      self.CheckBox153:bool = obj["CheckBox153"]
      """  CheckBox153  """  
      self.CheckBox154:bool = obj["CheckBox154"]
      """  CheckBox154  """  
      self.CheckBox155:bool = obj["CheckBox155"]
      """  CheckBox155  """  
      self.CheckBox156:bool = obj["CheckBox156"]
      """  CheckBox156  """  
      self.CheckBox157:bool = obj["CheckBox157"]
      """  CheckBox157  """  
      self.CheckBox158:bool = obj["CheckBox158"]
      """  CheckBox158  """  
      self.CheckBox159:bool = obj["CheckBox159"]
      """  CheckBox159  """  
      self.CheckBox160:bool = obj["CheckBox160"]
      """  CheckBox160  """  
      self.CheckBox161:bool = obj["CheckBox161"]
      """  CheckBox161  """  
      self.CheckBox162:bool = obj["CheckBox162"]
      """  CheckBox162  """  
      self.CheckBox163:bool = obj["CheckBox163"]
      """  CheckBox163  """  
      self.CheckBox164:bool = obj["CheckBox164"]
      """  CheckBox164  """  
      self.CheckBox165:bool = obj["CheckBox165"]
      """  CheckBox165  """  
      self.CheckBox166:bool = obj["CheckBox166"]
      """  CheckBox166  """  
      self.CheckBox167:bool = obj["CheckBox167"]
      """  CheckBox167  """  
      self.CheckBox168:bool = obj["CheckBox168"]
      """  CheckBox168  """  
      self.CheckBox169:bool = obj["CheckBox169"]
      """  CheckBox169  """  
      self.CheckBox170:bool = obj["CheckBox170"]
      """  CheckBox170  """  
      self.CheckBox171:bool = obj["CheckBox171"]
      """  CheckBox171  """  
      self.CheckBox172:bool = obj["CheckBox172"]
      """  CheckBox172  """  
      self.CheckBox173:bool = obj["CheckBox173"]
      """  CheckBox173  """  
      self.CheckBox174:bool = obj["CheckBox174"]
      """  CheckBox174  """  
      self.CheckBox175:bool = obj["CheckBox175"]
      """  CheckBox175  """  
      self.CheckBox176:bool = obj["CheckBox176"]
      """  CheckBox176  """  
      self.CheckBox177:bool = obj["CheckBox177"]
      """  CheckBox177  """  
      self.CheckBox178:bool = obj["CheckBox178"]
      """  CheckBox178  """  
      self.CheckBox179:bool = obj["CheckBox179"]
      """  CheckBox179  """  
      self.CheckBox180:bool = obj["CheckBox180"]
      """  CheckBox180  """  
      self.CheckBox181:bool = obj["CheckBox181"]
      """  CheckBox181  """  
      self.CheckBox182:bool = obj["CheckBox182"]
      """  CheckBox182  """  
      self.CheckBox183:bool = obj["CheckBox183"]
      """  CheckBox183  """  
      self.CheckBox184:bool = obj["CheckBox184"]
      """  CheckBox184  """  
      self.CheckBox185:bool = obj["CheckBox185"]
      """  CheckBox185  """  
      self.CheckBox186:bool = obj["CheckBox186"]
      """  CheckBox186  """  
      self.CheckBox187:bool = obj["CheckBox187"]
      """  CheckBox187  """  
      self.CheckBox188:bool = obj["CheckBox188"]
      """  CheckBox188  """  
      self.CheckBox189:bool = obj["CheckBox189"]
      """  CheckBox189  """  
      self.CheckBox190:bool = obj["CheckBox190"]
      """  CheckBox190  """  
      self.CheckBox191:bool = obj["CheckBox191"]
      """  CheckBox191  """  
      self.CheckBox192:bool = obj["CheckBox192"]
      """  CheckBox192  """  
      self.CheckBox193:bool = obj["CheckBox193"]
      """  CheckBox193  """  
      self.CheckBox194:bool = obj["CheckBox194"]
      """  CheckBox194  """  
      self.CheckBox195:bool = obj["CheckBox195"]
      """  CheckBox195  """  
      self.CheckBox196:bool = obj["CheckBox196"]
      """  CheckBox196  """  
      self.CheckBox197:bool = obj["CheckBox197"]
      """  CheckBox197  """  
      self.CheckBox198:bool = obj["CheckBox198"]
      """  CheckBox198  """  
      self.CheckBox199:bool = obj["CheckBox199"]
      """  CheckBox199  """  
      self.CheckBox200:bool = obj["CheckBox200"]
      """  CheckBox200  """  
      self.CheckBox201:bool = obj["CheckBox201"]
      """  CheckBox201  """  
      self.CheckBox202:bool = obj["CheckBox202"]
      """  CheckBox202  """  
      self.CheckBox203:bool = obj["CheckBox203"]
      """  CheckBox203  """  
      self.CheckBox204:bool = obj["CheckBox204"]
      """  CheckBox204  """  
      self.CheckBox205:bool = obj["CheckBox205"]
      """  CheckBox205  """  
      self.CheckBox206:bool = obj["CheckBox206"]
      """  CheckBox206  """  
      self.CheckBox207:bool = obj["CheckBox207"]
      """  CheckBox207  """  
      self.CheckBox208:bool = obj["CheckBox208"]
      """  CheckBox208  """  
      self.CheckBox209:bool = obj["CheckBox209"]
      """  CheckBox209  """  
      self.CheckBox210:bool = obj["CheckBox210"]
      """  CheckBox210  """  
      self.CheckBox211:bool = obj["CheckBox211"]
      """  CheckBox211  """  
      self.CheckBox212:bool = obj["CheckBox212"]
      """  CheckBox212  """  
      self.CheckBox213:bool = obj["CheckBox213"]
      """  CheckBox213  """  
      self.CheckBox214:bool = obj["CheckBox214"]
      """  CheckBox214  """  
      self.CheckBox215:bool = obj["CheckBox215"]
      """  CheckBox215  """  
      self.CheckBox216:bool = obj["CheckBox216"]
      """  CheckBox216  """  
      self.CheckBox217:bool = obj["CheckBox217"]
      """  CheckBox217  """  
      self.CheckBox218:bool = obj["CheckBox218"]
      """  CheckBox218  """  
      self.CheckBox219:bool = obj["CheckBox219"]
      """  CheckBox219  """  
      self.CheckBox220:bool = obj["CheckBox220"]
      """  CheckBox220  """  
      self.CheckBox221:bool = obj["CheckBox221"]
      """  CheckBox221  """  
      self.CheckBox222:bool = obj["CheckBox222"]
      """  CheckBox222  """  
      self.CheckBox223:bool = obj["CheckBox223"]
      """  CheckBox223  """  
      self.CheckBox224:bool = obj["CheckBox224"]
      """  CheckBox224  """  
      self.CheckBox225:bool = obj["CheckBox225"]
      """  CheckBox225  """  
      self.CheckBox226:bool = obj["CheckBox226"]
      """  CheckBox226  """  
      self.CheckBox227:bool = obj["CheckBox227"]
      """  CheckBox227  """  
      self.CheckBox228:bool = obj["CheckBox228"]
      """  CheckBox228  """  
      self.CheckBox229:bool = obj["CheckBox229"]
      """  CheckBox229  """  
      self.CheckBox230:bool = obj["CheckBox230"]
      """  CheckBox230  """  
      self.CheckBox231:bool = obj["CheckBox231"]
      """  CheckBox231  """  
      self.CheckBox232:bool = obj["CheckBox232"]
      """  CheckBox232  """  
      self.CheckBox233:bool = obj["CheckBox233"]
      """  CheckBox233  """  
      self.CheckBox234:bool = obj["CheckBox234"]
      """  CheckBox234  """  
      self.CheckBox235:bool = obj["CheckBox235"]
      """  CheckBox235  """  
      self.CheckBox236:bool = obj["CheckBox236"]
      """  CheckBox236  """  
      self.CheckBox237:bool = obj["CheckBox237"]
      """  CheckBox237  """  
      self.CheckBox238:bool = obj["CheckBox238"]
      """  CheckBox238  """  
      self.CheckBox239:bool = obj["CheckBox239"]
      """  CheckBox239  """  
      self.CheckBox240:bool = obj["CheckBox240"]
      """  CheckBox240  """  
      self.CheckBox241:bool = obj["CheckBox241"]
      """  CheckBox241  """  
      self.CheckBox242:bool = obj["CheckBox242"]
      """  CheckBox242  """  
      self.CheckBox243:bool = obj["CheckBox243"]
      """  CheckBox243  """  
      self.CheckBox244:bool = obj["CheckBox244"]
      """  CheckBox244  """  
      self.CheckBox245:bool = obj["CheckBox245"]
      """  CheckBox245  """  
      self.CheckBox246:bool = obj["CheckBox246"]
      """  CheckBox246  """  
      self.CheckBox247:bool = obj["CheckBox247"]
      """  CheckBox247  """  
      self.CheckBox248:bool = obj["CheckBox248"]
      """  CheckBox248  """  
      self.CheckBox249:bool = obj["CheckBox249"]
      """  CheckBox249  """  
      self.CheckBox250:bool = obj["CheckBox250"]
      """  CheckBox250  """  
      self.CheckBox251:bool = obj["CheckBox251"]
      """  CheckBox251  """  
      self.CheckBox252:bool = obj["CheckBox252"]
      """  CheckBox252  """  
      self.CheckBox253:bool = obj["CheckBox253"]
      """  CheckBox253  """  
      self.CheckBox254:bool = obj["CheckBox254"]
      """  CheckBox254  """  
      self.CheckBox255:bool = obj["CheckBox255"]
      """  CheckBox255  """  
      self.CheckBox256:bool = obj["CheckBox256"]
      """  CheckBox256  """  
      self.CheckBox257:bool = obj["CheckBox257"]
      """  CheckBox257  """  
      self.CheckBox258:bool = obj["CheckBox258"]
      """  CheckBox258  """  
      self.CheckBox259:bool = obj["CheckBox259"]
      """  CheckBox259  """  
      self.CheckBox260:bool = obj["CheckBox260"]
      """  CheckBox260  """  
      self.CheckBox261:bool = obj["CheckBox261"]
      """  CheckBox261  """  
      self.CheckBox262:bool = obj["CheckBox262"]
      """  CheckBox262  """  
      self.CheckBox263:bool = obj["CheckBox263"]
      """  CheckBox263  """  
      self.CheckBox264:bool = obj["CheckBox264"]
      """  CheckBox264  """  
      self.CheckBox265:bool = obj["CheckBox265"]
      """  CheckBox265  """  
      self.CheckBox266:bool = obj["CheckBox266"]
      """  CheckBox266  """  
      self.CheckBox267:bool = obj["CheckBox267"]
      """  CheckBox267  """  
      self.CheckBox268:bool = obj["CheckBox268"]
      """  CheckBox268  """  
      self.CheckBox269:bool = obj["CheckBox269"]
      """  CheckBox269  """  
      self.CheckBox270:bool = obj["CheckBox270"]
      """  CheckBox270  """  
      self.CheckBox271:bool = obj["CheckBox271"]
      """  CheckBox271  """  
      self.CheckBox272:bool = obj["CheckBox272"]
      """  CheckBox272  """  
      self.CheckBox273:bool = obj["CheckBox273"]
      """  CheckBox273  """  
      self.CheckBox274:bool = obj["CheckBox274"]
      """  CheckBox274  """  
      self.CheckBox275:bool = obj["CheckBox275"]
      """  CheckBox275  """  
      self.CheckBox276:bool = obj["CheckBox276"]
      """  CheckBox276  """  
      self.CheckBox277:bool = obj["CheckBox277"]
      """  CheckBox277  """  
      self.CheckBox278:bool = obj["CheckBox278"]
      """  CheckBox278  """  
      self.CheckBox279:bool = obj["CheckBox279"]
      """  CheckBox279  """  
      self.CheckBox280:bool = obj["CheckBox280"]
      """  CheckBox280  """  
      self.CheckBox281:bool = obj["CheckBox281"]
      """  CheckBox281  """  
      self.CheckBox282:bool = obj["CheckBox282"]
      """  CheckBox282  """  
      self.CheckBox283:bool = obj["CheckBox283"]
      """  CheckBox283  """  
      self.CheckBox284:bool = obj["CheckBox284"]
      """  CheckBox284  """  
      self.CheckBox285:bool = obj["CheckBox285"]
      """  CheckBox285  """  
      self.CheckBox286:bool = obj["CheckBox286"]
      """  CheckBox286  """  
      self.CheckBox287:bool = obj["CheckBox287"]
      """  CheckBox287  """  
      self.CheckBox288:bool = obj["CheckBox288"]
      """  CheckBox288  """  
      self.CheckBox289:bool = obj["CheckBox289"]
      """  CheckBox289  """  
      self.CheckBox290:bool = obj["CheckBox290"]
      """  CheckBox290  """  
      self.CheckBox291:bool = obj["CheckBox291"]
      """  CheckBox291  """  
      self.CheckBox292:bool = obj["CheckBox292"]
      """  CheckBox292  """  
      self.CheckBox293:bool = obj["CheckBox293"]
      """  CheckBox293  """  
      self.CheckBox294:bool = obj["CheckBox294"]
      """  CheckBox294  """  
      self.CheckBox295:bool = obj["CheckBox295"]
      """  CheckBox295  """  
      self.CheckBox296:bool = obj["CheckBox296"]
      """  CheckBox296  """  
      self.CheckBox297:bool = obj["CheckBox297"]
      """  CheckBox297  """  
      self.CheckBox298:bool = obj["CheckBox298"]
      """  CheckBox298  """  
      self.CheckBox299:bool = obj["CheckBox299"]
      """  CheckBox299  """  
      self.CheckBox300:bool = obj["CheckBox300"]
      """  CheckBox300  """  
      self.CheckBox301:bool = obj["CheckBox301"]
      """  CheckBox301  """  
      self.CheckBox302:bool = obj["CheckBox302"]
      """  CheckBox302  """  
      self.CheckBox303:bool = obj["CheckBox303"]
      """  CheckBox303  """  
      self.CheckBox304:bool = obj["CheckBox304"]
      """  CheckBox304  """  
      self.CheckBox305:bool = obj["CheckBox305"]
      """  CheckBox305  """  
      self.CheckBox306:bool = obj["CheckBox306"]
      """  CheckBox306  """  
      self.CheckBox307:bool = obj["CheckBox307"]
      """  CheckBox307  """  
      self.CheckBox308:bool = obj["CheckBox308"]
      """  CheckBox308  """  
      self.CheckBox309:bool = obj["CheckBox309"]
      """  CheckBox309  """  
      self.CheckBox310:bool = obj["CheckBox310"]
      """  CheckBox310  """  
      self.CheckBox311:bool = obj["CheckBox311"]
      """  CheckBox311  """  
      self.CheckBox312:bool = obj["CheckBox312"]
      """  CheckBox312  """  
      self.CheckBox313:bool = obj["CheckBox313"]
      """  CheckBox313  """  
      self.CheckBox314:bool = obj["CheckBox314"]
      """  CheckBox314  """  
      self.CheckBox315:bool = obj["CheckBox315"]
      """  CheckBox315  """  
      self.CheckBox316:bool = obj["CheckBox316"]
      """  CheckBox316  """  
      self.CheckBox317:bool = obj["CheckBox317"]
      """  CheckBox317  """  
      self.CheckBox318:bool = obj["CheckBox318"]
      """  CheckBox318  """  
      self.CheckBox319:bool = obj["CheckBox319"]
      """  CheckBox319  """  
      self.CheckBox320:bool = obj["CheckBox320"]
      """  CheckBox320  """  
      self.CheckBox321:bool = obj["CheckBox321"]
      """  CheckBox321  """  
      self.CheckBox322:bool = obj["CheckBox322"]
      """  CheckBox322  """  
      self.CheckBox323:bool = obj["CheckBox323"]
      """  CheckBox323  """  
      self.CheckBox324:bool = obj["CheckBox324"]
      """  CheckBox324  """  
      self.CheckBox325:bool = obj["CheckBox325"]
      """  CheckBox325  """  
      self.CheckBox326:bool = obj["CheckBox326"]
      """  CheckBox326  """  
      self.CheckBox327:bool = obj["CheckBox327"]
      """  CheckBox327  """  
      self.CheckBox328:bool = obj["CheckBox328"]
      """  CheckBox328  """  
      self.CheckBox329:bool = obj["CheckBox329"]
      """  CheckBox329  """  
      self.CheckBox330:bool = obj["CheckBox330"]
      """  CheckBox330  """  
      self.CheckBox331:bool = obj["CheckBox331"]
      """  CheckBox331  """  
      self.CheckBox332:bool = obj["CheckBox332"]
      """  CheckBox332  """  
      self.CheckBox333:bool = obj["CheckBox333"]
      """  CheckBox333  """  
      self.CheckBox334:bool = obj["CheckBox334"]
      """  CheckBox334  """  
      self.CheckBox335:bool = obj["CheckBox335"]
      """  CheckBox335  """  
      self.CheckBox336:bool = obj["CheckBox336"]
      """  CheckBox336  """  
      self.CheckBox337:bool = obj["CheckBox337"]
      """  CheckBox337  """  
      self.CheckBox338:bool = obj["CheckBox338"]
      """  CheckBox338  """  
      self.CheckBox339:bool = obj["CheckBox339"]
      """  CheckBox339  """  
      self.CheckBox340:bool = obj["CheckBox340"]
      """  CheckBox340  """  
      self.CheckBox341:bool = obj["CheckBox341"]
      """  CheckBox341  """  
      self.CheckBox342:bool = obj["CheckBox342"]
      """  CheckBox342  """  
      self.CheckBox343:bool = obj["CheckBox343"]
      """  CheckBox343  """  
      self.CheckBox344:bool = obj["CheckBox344"]
      """  CheckBox344  """  
      self.CheckBox345:bool = obj["CheckBox345"]
      """  CheckBox345  """  
      self.CheckBox346:bool = obj["CheckBox346"]
      """  CheckBox346  """  
      self.CheckBox347:bool = obj["CheckBox347"]
      """  CheckBox347  """  
      self.CheckBox348:bool = obj["CheckBox348"]
      """  CheckBox348  """  
      self.CheckBox349:bool = obj["CheckBox349"]
      """  CheckBox349  """  
      self.CheckBox350:bool = obj["CheckBox350"]
      """  CheckBox350  """  
      self.CheckBox351:bool = obj["CheckBox351"]
      """  CheckBox351  """  
      self.CheckBox352:bool = obj["CheckBox352"]
      """  CheckBox352  """  
      self.CheckBox353:bool = obj["CheckBox353"]
      """  CheckBox353  """  
      self.CheckBox354:bool = obj["CheckBox354"]
      """  CheckBox354  """  
      self.CheckBox355:bool = obj["CheckBox355"]
      """  CheckBox355  """  
      self.CheckBox356:bool = obj["CheckBox356"]
      """  CheckBox356  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsDateAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsDateRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Date001:str = obj["Date001"]
      """  Date001  """  
      self.Date002:str = obj["Date002"]
      """  Date002  """  
      self.Date003:str = obj["Date003"]
      """  Date003  """  
      self.Date004:str = obj["Date004"]
      """  Date004  """  
      self.Date005:str = obj["Date005"]
      """  Date005  """  
      self.Date006:str = obj["Date006"]
      """  Date006  """  
      self.Date007:str = obj["Date007"]
      """  Date007  """  
      self.Date008:str = obj["Date008"]
      """  Date008  """  
      self.Date009:str = obj["Date009"]
      """  Date009  """  
      self.Date010:str = obj["Date010"]
      """  Date010  """  
      self.Date011:str = obj["Date011"]
      """  Date011  """  
      self.Date012:str = obj["Date012"]
      """  Date012  """  
      self.Date013:str = obj["Date013"]
      """  Date013  """  
      self.Date014:str = obj["Date014"]
      """  Date014  """  
      self.Date015:str = obj["Date015"]
      """  Date015  """  
      self.Date016:str = obj["Date016"]
      """  Date016  """  
      self.Date017:str = obj["Date017"]
      """  Date017  """  
      self.Date018:str = obj["Date018"]
      """  Date018  """  
      self.Date019:str = obj["Date019"]
      """  Date019  """  
      self.Date020:str = obj["Date020"]
      """  Date020  """  
      self.Date021:str = obj["Date021"]
      """  Date021  """  
      self.Date022:str = obj["Date022"]
      """  Date022  """  
      self.Date023:str = obj["Date023"]
      """  Date023  """  
      self.Date024:str = obj["Date024"]
      """  Date024  """  
      self.Date025:str = obj["Date025"]
      """  Date025  """  
      self.Date026:str = obj["Date026"]
      """  Date026  """  
      self.Date027:str = obj["Date027"]
      """  Date027  """  
      self.Date028:str = obj["Date028"]
      """  Date028  """  
      self.Date029:str = obj["Date029"]
      """  Date029  """  
      self.Date030:str = obj["Date030"]
      """  Date030  """  
      self.Date031:str = obj["Date031"]
      """  Date031  """  
      self.Date032:str = obj["Date032"]
      """  Date032  """  
      self.Date033:str = obj["Date033"]
      """  Date033  """  
      self.Date034:str = obj["Date034"]
      """  Date034  """  
      self.Date035:str = obj["Date035"]
      """  Date035  """  
      self.Date036:str = obj["Date036"]
      """  Date036  """  
      self.Date037:str = obj["Date037"]
      """  Date037  """  
      self.Date038:str = obj["Date038"]
      """  Date038  """  
      self.Date039:str = obj["Date039"]
      """  Date039  """  
      self.Date040:str = obj["Date040"]
      """  Date040  """  
      self.Date041:str = obj["Date041"]
      """  Date041  """  
      self.Date042:str = obj["Date042"]
      """  Date042  """  
      self.Date043:str = obj["Date043"]
      """  Date043  """  
      self.Date044:str = obj["Date044"]
      """  Date044  """  
      self.Date045:str = obj["Date045"]
      """  Date045  """  
      self.Date046:str = obj["Date046"]
      """  Date046  """  
      self.Date047:str = obj["Date047"]
      """  Date047  """  
      self.Date051:str = obj["Date051"]
      """  Date051  """  
      self.Date052:str = obj["Date052"]
      """  Date052  """  
      self.Date053:str = obj["Date053"]
      """  Date053  """  
      self.Date054:str = obj["Date054"]
      """  Date054  """  
      self.Date055:str = obj["Date055"]
      """  Date055  """  
      self.Date056:str = obj["Date056"]
      """  Date056  """  
      self.Date057:str = obj["Date057"]
      """  Date057  """  
      self.Date058:str = obj["Date058"]
      """  Date058  """  
      self.Date059:str = obj["Date059"]
      """  Date059  """  
      self.Date060:str = obj["Date060"]
      """  Date060  """  
      self.Date061:str = obj["Date061"]
      """  Date061  """  
      self.Date062:str = obj["Date062"]
      """  Date062  """  
      self.Date063:str = obj["Date063"]
      """  Date063  """  
      self.Date064:str = obj["Date064"]
      """  Date064  """  
      self.Date065:str = obj["Date065"]
      """  Date065  """  
      self.Date066:str = obj["Date066"]
      """  Date066  """  
      self.Date067:str = obj["Date067"]
      """  Date067  """  
      self.Date068:str = obj["Date068"]
      """  Date068  """  
      self.Date069:str = obj["Date069"]
      """  Date069  """  
      self.Date070:str = obj["Date070"]
      """  Date070  """  
      self.Date071:str = obj["Date071"]
      """  Date071  """  
      self.Date072:str = obj["Date072"]
      """  Date072  """  
      self.Date073:str = obj["Date073"]
      """  Date073  """  
      self.Date074:str = obj["Date074"]
      """  Date074  """  
      self.Date075:str = obj["Date075"]
      """  Date075  """  
      self.Date076:str = obj["Date076"]
      """  Date076  """  
      self.Date077:str = obj["Date077"]
      """  Date077  """  
      self.Date078:str = obj["Date078"]
      """  Date078  """  
      self.Date079:str = obj["Date079"]
      """  Date079  """  
      self.Date080:str = obj["Date080"]
      """  Date080  """  
      self.Date081:str = obj["Date081"]
      """  Date081  """  
      self.Date082:str = obj["Date082"]
      """  Date082  """  
      self.Date083:str = obj["Date083"]
      """  Date083  """  
      self.Date084:str = obj["Date084"]
      """  Date084  """  
      self.Date085:str = obj["Date085"]
      """  Date085  """  
      self.Date086:str = obj["Date086"]
      """  Date086  """  
      self.Date087:str = obj["Date087"]
      """  Date087  """  
      self.Date088:str = obj["Date088"]
      """  Date088  """  
      self.Date089:str = obj["Date089"]
      """  Date089  """  
      self.Date090:str = obj["Date090"]
      """  Date090  """  
      self.Date091:str = obj["Date091"]
      """  Date091  """  
      self.Date092:str = obj["Date092"]
      """  Date092  """  
      self.Date093:str = obj["Date093"]
      """  Date093  """  
      self.Date094:str = obj["Date094"]
      """  Date094  """  
      self.Date095:str = obj["Date095"]
      """  Date095  """  
      self.Date096:str = obj["Date096"]
      """  Date096  """  
      self.Date097:str = obj["Date097"]
      """  Date097  """  
      self.Date101:str = obj["Date101"]
      """  Date101  """  
      self.Date102:str = obj["Date102"]
      """  Date102  """  
      self.Date103:str = obj["Date103"]
      """  Date103  """  
      self.Date104:str = obj["Date104"]
      """  Date104  """  
      self.Date105:str = obj["Date105"]
      """  Date105  """  
      self.Date106:str = obj["Date106"]
      """  Date106  """  
      self.Date107:str = obj["Date107"]
      """  Date107  """  
      self.Date108:str = obj["Date108"]
      """  Date108  """  
      self.Date109:str = obj["Date109"]
      """  Date109  """  
      self.Date110:str = obj["Date110"]
      """  Date110  """  
      self.Date111:str = obj["Date111"]
      """  Date111  """  
      self.Date112:str = obj["Date112"]
      """  Date112  """  
      self.Date113:str = obj["Date113"]
      """  Date113  """  
      self.Date114:str = obj["Date114"]
      """  Date114  """  
      self.Date115:str = obj["Date115"]
      """  Date115  """  
      self.Date116:str = obj["Date116"]
      """  Date116  """  
      self.Date117:str = obj["Date117"]
      """  Date117  """  
      self.Date118:str = obj["Date118"]
      """  Date118  """  
      self.Date119:str = obj["Date119"]
      """  Date119  """  
      self.Date120:str = obj["Date120"]
      """  Date120  """  
      self.Date121:str = obj["Date121"]
      """  Date121  """  
      self.Date122:str = obj["Date122"]
      """  Date122  """  
      self.Date123:str = obj["Date123"]
      """  Date123  """  
      self.Date124:str = obj["Date124"]
      """  Date124  """  
      self.Date125:str = obj["Date125"]
      """  Date125  """  
      self.Date126:str = obj["Date126"]
      """  Date126  """  
      self.Date127:str = obj["Date127"]
      """  Date127  """  
      self.Date128:str = obj["Date128"]
      """  Date128  """  
      self.Date129:str = obj["Date129"]
      """  Date129  """  
      self.Date130:str = obj["Date130"]
      """  Date130  """  
      self.Date131:str = obj["Date131"]
      """  Date131  """  
      self.Date132:str = obj["Date132"]
      """  Date132  """  
      self.Date133:str = obj["Date133"]
      """  Date133  """  
      self.Date134:str = obj["Date134"]
      """  Date134  """  
      self.Date135:str = obj["Date135"]
      """  Date135  """  
      self.Date136:str = obj["Date136"]
      """  Date136  """  
      self.Date137:str = obj["Date137"]
      """  Date137  """  
      self.Date138:str = obj["Date138"]
      """  Date138  """  
      self.Date139:str = obj["Date139"]
      """  Date139  """  
      self.Date140:str = obj["Date140"]
      """  Date140  """  
      self.Date141:str = obj["Date141"]
      """  Date141  """  
      self.Date142:str = obj["Date142"]
      """  Date142  """  
      self.Date143:str = obj["Date143"]
      """  Date143  """  
      self.Date144:str = obj["Date144"]
      """  Date144  """  
      self.Date145:str = obj["Date145"]
      """  Date145  """  
      self.Date146:str = obj["Date146"]
      """  Date146  """  
      self.Date147:str = obj["Date147"]
      """  Date147  """  
      self.Date151:str = obj["Date151"]
      """  Date151  """  
      self.Date152:str = obj["Date152"]
      """  Date152  """  
      self.Date153:str = obj["Date153"]
      """  Date153  """  
      self.Date154:str = obj["Date154"]
      """  Date154  """  
      self.Date155:str = obj["Date155"]
      """  Date155  """  
      self.Date156:str = obj["Date156"]
      """  Date156  """  
      self.Date157:str = obj["Date157"]
      """  Date157  """  
      self.Date158:str = obj["Date158"]
      """  Date158  """  
      self.Date159:str = obj["Date159"]
      """  Date159  """  
      self.Date160:str = obj["Date160"]
      """  Date160  """  
      self.Date161:str = obj["Date161"]
      """  Date161  """  
      self.Date162:str = obj["Date162"]
      """  Date162  """  
      self.Date163:str = obj["Date163"]
      """  Date163  """  
      self.Date164:str = obj["Date164"]
      """  Date164  """  
      self.Date165:str = obj["Date165"]
      """  Date165  """  
      self.Date166:str = obj["Date166"]
      """  Date166  """  
      self.Date167:str = obj["Date167"]
      """  Date167  """  
      self.Date168:str = obj["Date168"]
      """  Date168  """  
      self.Date169:str = obj["Date169"]
      """  Date169  """  
      self.Date170:str = obj["Date170"]
      """  Date170  """  
      self.Date171:str = obj["Date171"]
      """  Date171  """  
      self.Date172:str = obj["Date172"]
      """  Date172  """  
      self.Date173:str = obj["Date173"]
      """  Date173  """  
      self.Date174:str = obj["Date174"]
      """  Date174  """  
      self.Date175:str = obj["Date175"]
      """  Date175  """  
      self.Date176:str = obj["Date176"]
      """  Date176  """  
      self.Date177:str = obj["Date177"]
      """  Date177  """  
      self.Date178:str = obj["Date178"]
      """  Date178  """  
      self.Date179:str = obj["Date179"]
      """  Date179  """  
      self.Date180:str = obj["Date180"]
      """  Date180  """  
      self.Date181:str = obj["Date181"]
      """  Date181  """  
      self.Date182:str = obj["Date182"]
      """  Date182  """  
      self.Date183:str = obj["Date183"]
      """  Date183  """  
      self.Date184:str = obj["Date184"]
      """  Date184  """  
      self.Date185:str = obj["Date185"]
      """  Date185  """  
      self.Date186:str = obj["Date186"]
      """  Date186  """  
      self.Date187:str = obj["Date187"]
      """  Date187  """  
      self.Date188:str = obj["Date188"]
      """  Date188  """  
      self.Date189:str = obj["Date189"]
      """  Date189  """  
      self.Date190:str = obj["Date190"]
      """  Date190  """  
      self.Date191:str = obj["Date191"]
      """  Date191  """  
      self.Date192:str = obj["Date192"]
      """  Date192  """  
      self.Date193:str = obj["Date193"]
      """  Date193  """  
      self.Date194:str = obj["Date194"]
      """  Date194  """  
      self.Date195:str = obj["Date195"]
      """  Date195  """  
      self.Date196:str = obj["Date196"]
      """  Date196  """  
      self.Date197:str = obj["Date197"]
      """  Date197  """  
      self.Date048:str = obj["Date048"]
      """  Date048  """  
      self.Date049:str = obj["Date049"]
      """  Date049  """  
      self.Date050:str = obj["Date050"]
      """  Date050  """  
      self.Date098:str = obj["Date098"]
      """  Date098  """  
      self.Date099:str = obj["Date099"]
      """  Date099  """  
      self.Date100:str = obj["Date100"]
      """  Date100  """  
      self.Date148:str = obj["Date148"]
      """  Date148  """  
      self.Date149:str = obj["Date149"]
      """  Date149  """  
      self.Date150:str = obj["Date150"]
      """  Date150  """  
      self.Date198:str = obj["Date198"]
      """  Date198  """  
      self.Date199:str = obj["Date199"]
      """  Date199  """  
      self.Date200:str = obj["Date200"]
      """  Date200  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to. Field not currently used.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record. For future use.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number inspected  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number Inspected  """  
      self.JobNum:str = obj["JobNum"]
      """  Contains the Job Number related to the job or non-conformance being inspected.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Contain the assembly sequence of the job being inspected  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Contains the operation sequence of the job operation being inspected.  """  
      self.NCMTranID:int = obj["NCMTranID"]
      """  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  Contains the inspection plan part number (configurator part number)  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  Contains the inspection plan revision number (configurator revision number)  """  
      self.SpecID:str = obj["SpecID"]
      """  Contains the specification ID that was used in the inspection plan.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Contains the specification revision number that was used in the inspection process.  """  
      self.RMANum:int = obj["RMANum"]
      """  Contains Return Material Authorization number if inspecting for an RMA  """  
      self.RMALine:int = obj["RMALine"]
      """  Contains Line number of the RMA if inspecting for an RMA.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Contains the PO Packing Slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """  Contains the PO Packing Slip line number.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Contains the VendorNum when inspected via Skip Lot processing  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Contains the serial number of the part inspected  """  
      self.LotNum:str = obj["LotNum"]
      """  Contains the lot number of the part inspected  """  
      self.Passed:bool = obj["Passed"]
      """  True if passed  """  
      self.FailedCmtText:str = obj["FailedCmtText"]
      """  Text describing why the inspection result failed  """  
      self.TestDataEntered:bool = obj["TestDataEntered"]
      """  True if the results were saved in product configuration  """  
      self.AuditRefNum:int = obj["AuditRefNum"]
      """  This is a unique reference number that is assigned by the system for each audit record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.AuditType:str = obj["AuditType"]
      """  Shows how the audit was created - Scheduled or Manual  """  
      self.AuditID:str = obj["AuditID"]
      """  User defined Audit ID  """  
      self.AuditRevNum:str = obj["AuditRevNum"]
      """  Supplier Audit Revision Number  """  
      self.Auditor:str = obj["Auditor"]
      """  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  """  
      self.AuditSchedDate:str = obj["AuditSchedDate"]
      self.AuditCreateDate:str = obj["AuditCreateDate"]
      """  Date the audit reference was created  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  """  
      self.AuditVendNum:int = obj["AuditVendNum"]
      """  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  """  
      self.AuditCompDate:str = obj["AuditCompDate"]
      """  Date the audit was completed  """  
      self.AuditStatus:str = obj["AuditStatus"]
      """  Planned, Scheduled, In Progress, Complete  """  
      self.AuditResult:str = obj["AuditResult"]
      """  Passed, Failed, Unspecified  """  
      self.AuditConNum:int = obj["AuditConNum"]
      """  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  """  
      self.AuditConRole:str = obj["AuditConRole"]
      """  Code that identifies the role of the audit contact.  """  
      self.AuditCost:int = obj["AuditCost"]
      """  This is the cost of performing the audit.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Description:str = obj["Description"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsListTableset:
   def __init__(self, obj):
      self.InspResultsList:list[Erp_Tablesets_InspResultsListRow] = obj["InspResultsList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_InspResultsNumAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsNumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Number001:int = obj["Number001"]
      """  Number001  """  
      self.Number002:int = obj["Number002"]
      """  Number002  """  
      self.Number003:int = obj["Number003"]
      """  Number003  """  
      self.Number004:int = obj["Number004"]
      """  Number004  """  
      self.Number005:int = obj["Number005"]
      """  Number005  """  
      self.Number006:int = obj["Number006"]
      """  Number006  """  
      self.Number007:int = obj["Number007"]
      """  Number007  """  
      self.Number008:int = obj["Number008"]
      """  Number008  """  
      self.Number009:int = obj["Number009"]
      """  Number009  """  
      self.Number010:int = obj["Number010"]
      """  Number010  """  
      self.Number011:int = obj["Number011"]
      """  Number011  """  
      self.Number012:int = obj["Number012"]
      """  Number012  """  
      self.Number013:int = obj["Number013"]
      """  Number013  """  
      self.Number014:int = obj["Number014"]
      """  Number014  """  
      self.Number015:int = obj["Number015"]
      """  Number015  """  
      self.Number016:int = obj["Number016"]
      """  Number016  """  
      self.Number017:int = obj["Number017"]
      """  Number017  """  
      self.Number018:int = obj["Number018"]
      """  Number018  """  
      self.Number019:int = obj["Number019"]
      """  Number019  """  
      self.Number020:int = obj["Number020"]
      """  Number020  """  
      self.Number021:int = obj["Number021"]
      """  Number021  """  
      self.Number022:int = obj["Number022"]
      """  Number022  """  
      self.Number023:int = obj["Number023"]
      """  Number023  """  
      self.Number024:int = obj["Number024"]
      """  Number024  """  
      self.Number025:int = obj["Number025"]
      """  Number025  """  
      self.Number026:int = obj["Number026"]
      """  Number026  """  
      self.Number027:int = obj["Number027"]
      """  Number027  """  
      self.Number028:int = obj["Number028"]
      """  Number028  """  
      self.Number029:int = obj["Number029"]
      """  Number029  """  
      self.Number030:int = obj["Number030"]
      """  Number030  """  
      self.Number031:int = obj["Number031"]
      """  Number031  """  
      self.Number032:int = obj["Number032"]
      """  Number032  """  
      self.Number033:int = obj["Number033"]
      """  Number033  """  
      self.Number034:int = obj["Number034"]
      """  Number034  """  
      self.Number035:int = obj["Number035"]
      """  Number035  """  
      self.Number036:int = obj["Number036"]
      """  Number036  """  
      self.Number037:int = obj["Number037"]
      """  Number037  """  
      self.Number038:int = obj["Number038"]
      """  Number038  """  
      self.Number039:int = obj["Number039"]
      """  Number039  """  
      self.Number040:int = obj["Number040"]
      """  Number040  """  
      self.Number041:int = obj["Number041"]
      """  Number041  """  
      self.Number042:int = obj["Number042"]
      """  Number042  """  
      self.Number043:int = obj["Number043"]
      """  Number043  """  
      self.Number044:int = obj["Number044"]
      """  Number044  """  
      self.Number045:int = obj["Number045"]
      """  Number045  """  
      self.Number046:int = obj["Number046"]
      """  Number046  """  
      self.Number047:int = obj["Number047"]
      """  Number047  """  
      self.Number048:int = obj["Number048"]
      """  Number048  """  
      self.Number049:int = obj["Number049"]
      """  Number049  """  
      self.Number050:int = obj["Number050"]
      """  Number050  """  
      self.Number051:int = obj["Number051"]
      """  Number051  """  
      self.Number052:int = obj["Number052"]
      """  Number052  """  
      self.Number053:int = obj["Number053"]
      """  Number053  """  
      self.Number054:int = obj["Number054"]
      """  Number054  """  
      self.Number055:int = obj["Number055"]
      """  Number055  """  
      self.Number056:int = obj["Number056"]
      """  Number056  """  
      self.Number057:int = obj["Number057"]
      """  Number057  """  
      self.Number058:int = obj["Number058"]
      """  Number058  """  
      self.Number059:int = obj["Number059"]
      """  Number059  """  
      self.Number060:int = obj["Number060"]
      """  Number060  """  
      self.Number061:int = obj["Number061"]
      """  Number061  """  
      self.Number062:int = obj["Number062"]
      """  Number062  """  
      self.Number063:int = obj["Number063"]
      """  Number063  """  
      self.Number064:int = obj["Number064"]
      """  Number064  """  
      self.Number065:int = obj["Number065"]
      """  Number065  """  
      self.Number066:int = obj["Number066"]
      """  Number066  """  
      self.Number067:int = obj["Number067"]
      """  Number067  """  
      self.Number068:int = obj["Number068"]
      """  Number068  """  
      self.Number069:int = obj["Number069"]
      """  Number069  """  
      self.Number070:int = obj["Number070"]
      """  Number070  """  
      self.Number071:int = obj["Number071"]
      """  Number071  """  
      self.Number072:int = obj["Number072"]
      """  Number072  """  
      self.Number073:int = obj["Number073"]
      """  Number073  """  
      self.Number074:int = obj["Number074"]
      """  Number074  """  
      self.Number075:int = obj["Number075"]
      """  Number075  """  
      self.Number076:int = obj["Number076"]
      """  Number076  """  
      self.Number077:int = obj["Number077"]
      """  Number077  """  
      self.Number078:int = obj["Number078"]
      """  Number078  """  
      self.Number079:int = obj["Number079"]
      """  Number079  """  
      self.Number080:int = obj["Number080"]
      """  Number080  """  
      self.Number081:int = obj["Number081"]
      """  Number081  """  
      self.Number082:int = obj["Number082"]
      """  Number082  """  
      self.Number083:int = obj["Number083"]
      """  Number083  """  
      self.Number084:int = obj["Number084"]
      """  Number084  """  
      self.Number085:int = obj["Number085"]
      """  Number085  """  
      self.Number086:int = obj["Number086"]
      """  Number086  """  
      self.Number087:int = obj["Number087"]
      """  Number087  """  
      self.Number088:int = obj["Number088"]
      """  Number088  """  
      self.Number089:int = obj["Number089"]
      """  Number089  """  
      self.Number090:int = obj["Number090"]
      """  Number090  """  
      self.Number091:int = obj["Number091"]
      """  Number091  """  
      self.Number092:int = obj["Number092"]
      """  Number092  """  
      self.Number093:int = obj["Number093"]
      """  Number093  """  
      self.Number094:int = obj["Number094"]
      """  Number094  """  
      self.Number095:int = obj["Number095"]
      """  Number095  """  
      self.Number096:int = obj["Number096"]
      """  Number096  """  
      self.Number097:int = obj["Number097"]
      """  Number097  """  
      self.Number098:int = obj["Number098"]
      """  Number098  """  
      self.Number099:int = obj["Number099"]
      """  Number099  """  
      self.Number100:int = obj["Number100"]
      """  Number100  """  
      self.Number101:int = obj["Number101"]
      """  Number101  """  
      self.Number102:int = obj["Number102"]
      """  Number102  """  
      self.Number103:int = obj["Number103"]
      """  Number103  """  
      self.Number104:int = obj["Number104"]
      """  Number104  """  
      self.Number105:int = obj["Number105"]
      """  Number105  """  
      self.Number106:int = obj["Number106"]
      """  Number106  """  
      self.Number107:int = obj["Number107"]
      """  Number107  """  
      self.Number108:int = obj["Number108"]
      """  Number108  """  
      self.Number109:int = obj["Number109"]
      """  Number109  """  
      self.Number110:int = obj["Number110"]
      """  Number110  """  
      self.Number111:int = obj["Number111"]
      """  Number111  """  
      self.Number112:int = obj["Number112"]
      """  Number112  """  
      self.Number113:int = obj["Number113"]
      """  Number113  """  
      self.Number114:int = obj["Number114"]
      """  Number114  """  
      self.Number115:int = obj["Number115"]
      """  Number115  """  
      self.Number116:int = obj["Number116"]
      """  Number116  """  
      self.Number117:int = obj["Number117"]
      """  Number117  """  
      self.Number118:int = obj["Number118"]
      """  Number118  """  
      self.Number119:int = obj["Number119"]
      """  Number119  """  
      self.Number120:int = obj["Number120"]
      """  Number120  """  
      self.Number121:int = obj["Number121"]
      """  Number121  """  
      self.Number122:int = obj["Number122"]
      """  Number122  """  
      self.Number123:int = obj["Number123"]
      """  Number123  """  
      self.Number124:int = obj["Number124"]
      """  Number124  """  
      self.Number125:int = obj["Number125"]
      """  Number125  """  
      self.Number126:int = obj["Number126"]
      """  Number126  """  
      self.Number127:int = obj["Number127"]
      """  Number127  """  
      self.Number128:int = obj["Number128"]
      """  Number128  """  
      self.Number129:int = obj["Number129"]
      """  Number129  """  
      self.Number130:int = obj["Number130"]
      """  Number130  """  
      self.Number131:int = obj["Number131"]
      """  Number131  """  
      self.Number132:int = obj["Number132"]
      """  Number132  """  
      self.Number133:int = obj["Number133"]
      """  Number133  """  
      self.Number134:int = obj["Number134"]
      """  Number134  """  
      self.Number135:int = obj["Number135"]
      """  Number135  """  
      self.Number136:int = obj["Number136"]
      """  Number136  """  
      self.Number137:int = obj["Number137"]
      """  Number137  """  
      self.Number138:int = obj["Number138"]
      """  Number138  """  
      self.Number139:int = obj["Number139"]
      """  Number139  """  
      self.Number140:int = obj["Number140"]
      """  Number140  """  
      self.Number141:int = obj["Number141"]
      """  Number141  """  
      self.Number142:int = obj["Number142"]
      """  Number142  """  
      self.Number143:int = obj["Number143"]
      """  Number143  """  
      self.Number144:int = obj["Number144"]
      """  Number144  """  
      self.Number145:int = obj["Number145"]
      """  Number145  """  
      self.Number146:int = obj["Number146"]
      """  Number146  """  
      self.Number147:int = obj["Number147"]
      """  Number147  """  
      self.Number148:int = obj["Number148"]
      """  Number148  """  
      self.Number149:int = obj["Number149"]
      """  Number149  """  
      self.Number150:int = obj["Number150"]
      """  Number150  """  
      self.Number151:int = obj["Number151"]
      """  Number151  """  
      self.Number152:int = obj["Number152"]
      """  Number152  """  
      self.Number153:int = obj["Number153"]
      """  Number153  """  
      self.Number154:int = obj["Number154"]
      """  Number154  """  
      self.Number155:int = obj["Number155"]
      """  Number155  """  
      self.Number156:int = obj["Number156"]
      """  Number156  """  
      self.Number157:int = obj["Number157"]
      """  Number157  """  
      self.Number158:int = obj["Number158"]
      """  Number158  """  
      self.Number159:int = obj["Number159"]
      """  Number159  """  
      self.Number160:int = obj["Number160"]
      """  Number160  """  
      self.Number161:int = obj["Number161"]
      """  Number161  """  
      self.Number162:int = obj["Number162"]
      """  Number162  """  
      self.Number163:int = obj["Number163"]
      """  Number163  """  
      self.Number164:int = obj["Number164"]
      """  Number164  """  
      self.Number165:int = obj["Number165"]
      """  Number165  """  
      self.Number166:int = obj["Number166"]
      """  Number166  """  
      self.Number167:int = obj["Number167"]
      """  Number167  """  
      self.Number168:int = obj["Number168"]
      """  Number168  """  
      self.Number169:int = obj["Number169"]
      """  Number169  """  
      self.Number170:int = obj["Number170"]
      """  Number170  """  
      self.Number171:int = obj["Number171"]
      """  Number171  """  
      self.Number172:int = obj["Number172"]
      """  Number172  """  
      self.Number173:int = obj["Number173"]
      """  Number173  """  
      self.Number174:int = obj["Number174"]
      """  Number174  """  
      self.Number175:int = obj["Number175"]
      """  Number175  """  
      self.Number176:int = obj["Number176"]
      """  Number176  """  
      self.Number177:int = obj["Number177"]
      """  Number177  """  
      self.Number178:int = obj["Number178"]
      """  Number178  """  
      self.Number179:int = obj["Number179"]
      """  Number179  """  
      self.Number180:int = obj["Number180"]
      """  Number180  """  
      self.Number181:int = obj["Number181"]
      """  Number181  """  
      self.Number182:int = obj["Number182"]
      """  Number182  """  
      self.Number183:int = obj["Number183"]
      """  Number183  """  
      self.Number184:int = obj["Number184"]
      """  Number184  """  
      self.Number185:int = obj["Number185"]
      """  Number185  """  
      self.Number186:int = obj["Number186"]
      """  Number186  """  
      self.Number187:int = obj["Number187"]
      """  Number187  """  
      self.Number188:int = obj["Number188"]
      """  Number188  """  
      self.Number189:int = obj["Number189"]
      """  Number189  """  
      self.Number190:int = obj["Number190"]
      """  Number190  """  
      self.Number191:int = obj["Number191"]
      """  Number191  """  
      self.Number192:int = obj["Number192"]
      """  Number192  """  
      self.Number193:int = obj["Number193"]
      """  Number193  """  
      self.Number194:int = obj["Number194"]
      """  Number194  """  
      self.Number195:int = obj["Number195"]
      """  Number195  """  
      self.Number196:int = obj["Number196"]
      """  Number196  """  
      self.Number197:int = obj["Number197"]
      """  Number197  """  
      self.Number198:int = obj["Number198"]
      """  Number198  """  
      self.Number199:int = obj["Number199"]
      """  Number199  """  
      self.Number200:int = obj["Number200"]
      """  Number200  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type.  Valid plan type values - I (Inspection Plan),  C (Calibration Plan).  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to. Field not currently used.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record. Depending on the context in which the inspection was done: for RMA, it would be the RMANum; for Receipts it would be the PackSlip; for FirstArt it would be the JobNum; for Materials, it would be the LaborHedSeq; for Inventory it would be the NCMTranID; JobNum or PartNum when no more information.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the primary key to the related record. The usage of this field is dependent on the type of record.  For example:  for a RMA, it would be the RMALine; for a Receipt it would be the PackLine; for FirstArt it would be the AssemblySeq; for Materials, it would be the LaborDtlSeq; in other cases would be the AssemblySeq or the RevisionNum of a PartNum.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the primary key to the related record. The usage of this field is dependent on the type of record referenced. The usage of this field is dependent on the type of record referenced. For example: for a RMA, it would be the RMAReceipt; for a Receipt it would be the VendorNum; for FirstArt it would be the OprSeq; in other cases it would be the OprSeq.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  For Example: for a RMA it would be the RMADisp.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record. For future use.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number inspected  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number Inspected  """  
      self.JobNum:str = obj["JobNum"]
      """  Contains the Job Number related to the job or non-conformance being inspected.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Contain the assembly sequence of the job being inspected  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Contains the operation sequence of the job operation being inspected.  """  
      self.NCMTranID:int = obj["NCMTranID"]
      """  Contains the Non-Conformance (NonConf) TranID if inspecting Non-Conformance  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  Contains the inspection plan part number (configurator part number)  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  Contains the inspection plan revision number (configurator revision number)  """  
      self.SpecID:str = obj["SpecID"]
      """  Contains the specification ID that was used in the inspection plan.  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  Contains the specification revision number that was used in the inspection process.  """  
      self.RMANum:int = obj["RMANum"]
      """  Contains Return Material Authorization number if inspecting for an RMA  """  
      self.RMALine:int = obj["RMALine"]
      """  Contains Line number of the RMA if inspecting for an RMA.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Contain the ResourceGrpID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Contain the ResourceID when inspected via Fixed Asset Calibration or Preventative Maintenance Calibration  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Contains the PO Packing Slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """  Contains the PO Packing Slip line number.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Contains the VendorNum when inspected via Skip Lot processing  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Contains the serial number of the part inspected  """  
      self.LotNum:str = obj["LotNum"]
      """  Contains the lot number of the part inspected  """  
      self.Passed:bool = obj["Passed"]
      """  True if passed  """  
      self.FailedCmtText:str = obj["FailedCmtText"]
      """  Text describing why the inspection result failed  """  
      self.TestDataEntered:bool = obj["TestDataEntered"]
      """  True if the results were saved in product configuration  """  
      self.AuditRefNum:int = obj["AuditRefNum"]
      """  This is a unique reference number that is assigned by the system for each audit record.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.AuditType:str = obj["AuditType"]
      """  Shows how the audit was created - Scheduled or Manual  """  
      self.AuditID:str = obj["AuditID"]
      """  User defined Audit ID  """  
      self.AuditRevNum:str = obj["AuditRevNum"]
      """  Supplier Audit Revision Number  """  
      self.Auditor:str = obj["Auditor"]
      """  Auditor.  Valid auditor values - E (Employee),  R (Role), S (Supplier)  """  
      self.AuditSchedDate:str = obj["AuditSchedDate"]
      self.AuditCreateDate:str = obj["AuditCreateDate"]
      """  Date the audit reference was created  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  If an employee code is entered, it must be valid in the EmpBasic table.  """  
      self.AuditVendNum:int = obj["AuditVendNum"]
      """  Auditor Supplier Number.  If a supplier number is entered, it must be valid in the Vendor table.  """  
      self.AuditCompDate:str = obj["AuditCompDate"]
      """  Date the audit was completed  """  
      self.AuditStatus:str = obj["AuditStatus"]
      """  Planned, Scheduled, In Progress, Complete  """  
      self.AuditResult:str = obj["AuditResult"]
      """  Passed, Failed, Unspecified  """  
      self.AuditConNum:int = obj["AuditConNum"]
      """  Supplier Contact number.  If entered, it must be valid in the VendCnt record.  """  
      self.AuditConRole:str = obj["AuditConRole"]
      """  Code that identifies the role of the audit contact.  """  
      self.AuditCost:int = obj["AuditCost"]
      """  This is the cost of performing the audit.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.Description:str = obj["Description"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InspResultsShortCharAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.InspPlanType:str = obj["InspPlanType"]
      self.File:str = obj["File"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.SampleNumber:int = obj["SampleNumber"]
      self.InspectDate:str = obj["InspectDate"]
      self.InspectTime:int = obj["InspectTime"]
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

class Erp_Tablesets_InspResultsShortCharRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.InspPlanType:str = obj["InspPlanType"]
      """  Inspection Plan Type - Inspection, Audit, or Survey  """  
      self.File:str = obj["File"]
      """  The name of the table that this record pertains to.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the primary key to the record.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the primary key to the related record.
For example: For a "OrderDtl"   this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependant on the type of record.  For example "Part" references do not use this field while PartRev  would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the primary key to the related record.
For example: For a "OrderRel"   this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependant on the type of record referenced.  """  
      self.Key4:str = obj["Key4"]
      """  4th component of the primary key to the related record.  """  
      self.Key5:str = obj["Key5"]
      """  5th component of the primary key to the related record.  """  
      self.SampleNumber:int = obj["SampleNumber"]
      """  A sequential number up to the total in the Inspection Quantity field.  """  
      self.InspectDate:str = obj["InspectDate"]
      """  Date the inspection data was saved  """  
      self.InspectTime:int = obj["InspectTime"]
      """  System time (seconds since midnight) of when the inspection data was saved  """  
      self.ShortChar001:str = obj["ShortChar001"]
      """  ShortChar001  """  
      self.ShortChar002:str = obj["ShortChar002"]
      """  ShortChar002  """  
      self.ShortChar003:str = obj["ShortChar003"]
      """  ShortChar003  """  
      self.ShortChar004:str = obj["ShortChar004"]
      """  ShortChar004  """  
      self.ShortChar005:str = obj["ShortChar005"]
      """  ShortChar005  """  
      self.ShortChar006:str = obj["ShortChar006"]
      """  ShortChar006  """  
      self.ShortChar007:str = obj["ShortChar007"]
      """  ShortChar007  """  
      self.ShortChar008:str = obj["ShortChar008"]
      """  ShortChar008  """  
      self.ShortChar009:str = obj["ShortChar009"]
      """  ShortChar009  """  
      self.ShortChar010:str = obj["ShortChar010"]
      """  ShortChar010  """  
      self.ShortChar011:str = obj["ShortChar011"]
      """  ShortChar011  """  
      self.ShortChar012:str = obj["ShortChar012"]
      """  ShortChar012  """  
      self.ShortChar013:str = obj["ShortChar013"]
      """  ShortChar013  """  
      self.ShortChar014:str = obj["ShortChar014"]
      """  ShortChar014  """  
      self.ShortChar015:str = obj["ShortChar015"]
      """  ShortChar015  """  
      self.ShortChar016:str = obj["ShortChar016"]
      """  ShortChar016  """  
      self.ShortChar017:str = obj["ShortChar017"]
      """  ShortChar017  """  
      self.ShortChar018:str = obj["ShortChar018"]
      """  ShortChar018  """  
      self.ShortChar019:str = obj["ShortChar019"]
      """  ShortChar019  """  
      self.ShortChar020:str = obj["ShortChar020"]
      """  ShortChar020  """  
      self.ShortChar021:str = obj["ShortChar021"]
      """  ShortChar021  """  
      self.ShortChar022:str = obj["ShortChar022"]
      """  ShortChar022  """  
      self.ShortChar023:str = obj["ShortChar023"]
      """  ShortChar023  """  
      self.ShortChar024:str = obj["ShortChar024"]
      """  ShortChar024  """  
      self.ShortChar025:str = obj["ShortChar025"]
      """  ShortChar025  """  
      self.ShortChar026:str = obj["ShortChar026"]
      """  ShortChar026  """  
      self.ShortChar027:str = obj["ShortChar027"]
      """  ShortChar027  """  
      self.ShortChar028:str = obj["ShortChar028"]
      """  ShortChar028  """  
      self.ShortChar029:str = obj["ShortChar029"]
      """  ShortChar029  """  
      self.ShortChar030:str = obj["ShortChar030"]
      """  ShortChar030  """  
      self.ShortChar031:str = obj["ShortChar031"]
      """  ShortChar031  """  
      self.ShortChar032:str = obj["ShortChar032"]
      """  ShortChar032  """  
      self.ShortChar033:str = obj["ShortChar033"]
      """  ShortChar033  """  
      self.ShortChar034:str = obj["ShortChar034"]
      """  ShortChar034  """  
      self.ShortChar035:str = obj["ShortChar035"]
      """  ShortChar035  """  
      self.ShortChar036:str = obj["ShortChar036"]
      """  ShortChar036  """  
      self.ShortChar037:str = obj["ShortChar037"]
      """  ShortChar037  """  
      self.ShortChar038:str = obj["ShortChar038"]
      """  ShortChar038  """  
      self.ShortChar039:str = obj["ShortChar039"]
      """  ShortChar039  """  
      self.ShortChar040:str = obj["ShortChar040"]
      """  ShortChar040  """  
      self.ShortChar041:str = obj["ShortChar041"]
      """  ShortChar041  """  
      self.ShortChar042:str = obj["ShortChar042"]
      """  ShortChar042  """  
      self.ShortChar043:str = obj["ShortChar043"]
      """  ShortChar043  """  
      self.ShortChar044:str = obj["ShortChar044"]
      """  ShortChar044  """  
      self.ShortChar045:str = obj["ShortChar045"]
      """  ShortChar045  """  
      self.ShortChar046:str = obj["ShortChar046"]
      """  ShortChar046  """  
      self.ShortChar047:str = obj["ShortChar047"]
      """  ShortChar047  """  
      self.ShortChar048:str = obj["ShortChar048"]
      """  ShortChar048  """  
      self.ShortChar049:str = obj["ShortChar049"]
      """  ShortChar049  """  
      self.ShortChar050:str = obj["ShortChar050"]
      """  ShortChar050  """  
      self.ShortChar051:str = obj["ShortChar051"]
      """  ShortChar051  """  
      self.ShortChar052:str = obj["ShortChar052"]
      """  ShortChar052  """  
      self.ShortChar053:str = obj["ShortChar053"]
      """  ShortChar053  """  
      self.ShortChar054:str = obj["ShortChar054"]
      """  ShortChar054  """  
      self.ShortChar055:str = obj["ShortChar055"]
      """  ShortChar055  """  
      self.ShortChar056:str = obj["ShortChar056"]
      """  ShortChar056  """  
      self.ShortChar057:str = obj["ShortChar057"]
      """  ShortChar057  """  
      self.ShortChar058:str = obj["ShortChar058"]
      """  ShortChar058  """  
      self.ShortChar059:str = obj["ShortChar059"]
      """  ShortChar059  """  
      self.ShortChar060:str = obj["ShortChar060"]
      """  ShortChar060  """  
      self.ShortChar061:str = obj["ShortChar061"]
      """  ShortChar061  """  
      self.ShortChar062:str = obj["ShortChar062"]
      """  ShortChar062  """  
      self.ShortChar063:str = obj["ShortChar063"]
      """  ShortChar063  """  
      self.ShortChar064:str = obj["ShortChar064"]
      """  ShortChar064  """  
      self.ShortChar065:str = obj["ShortChar065"]
      """  ShortChar065  """  
      self.ShortChar066:str = obj["ShortChar066"]
      """  ShortChar066  """  
      self.ShortChar067:str = obj["ShortChar067"]
      """  ShortChar067  """  
      self.ShortChar068:str = obj["ShortChar068"]
      """  ShortChar068  """  
      self.ShortChar069:str = obj["ShortChar069"]
      """  ShortChar069  """  
      self.ShortChar070:str = obj["ShortChar070"]
      """  ShortChar070  """  
      self.ShortChar071:str = obj["ShortChar071"]
      """  ShortChar071  """  
      self.ShortChar072:str = obj["ShortChar072"]
      """  ShortChar072  """  
      self.ShortChar073:str = obj["ShortChar073"]
      """  ShortChar073  """  
      self.ShortChar074:str = obj["ShortChar074"]
      """  ShortChar074  """  
      self.ShortChar075:str = obj["ShortChar075"]
      """  ShortChar075  """  
      self.ShortChar076:str = obj["ShortChar076"]
      """  ShortChar076  """  
      self.ShortChar077:str = obj["ShortChar077"]
      """  ShortChar077  """  
      self.ShortChar078:str = obj["ShortChar078"]
      """  ShortChar078  """  
      self.ShortChar079:str = obj["ShortChar079"]
      """  ShortChar079  """  
      self.ShortChar080:str = obj["ShortChar080"]
      """  ShortChar080  """  
      self.ShortChar081:str = obj["ShortChar081"]
      """  ShortChar081  """  
      self.ShortChar082:str = obj["ShortChar082"]
      """  ShortChar082  """  
      self.ShortChar083:str = obj["ShortChar083"]
      """  ShortChar083  """  
      self.ShortChar084:str = obj["ShortChar084"]
      """  ShortChar084  """  
      self.ShortChar085:str = obj["ShortChar085"]
      """  ShortChar085  """  
      self.ShortChar086:str = obj["ShortChar086"]
      """  ShortChar086  """  
      self.ShortChar087:str = obj["ShortChar087"]
      """  ShortChar087  """  
      self.ShortChar088:str = obj["ShortChar088"]
      """  ShortChar088  """  
      self.ShortChar089:str = obj["ShortChar089"]
      """  ShortChar089  """  
      self.ShortChar090:str = obj["ShortChar090"]
      """  ShortChar090  """  
      self.ShortChar091:str = obj["ShortChar091"]
      """  ShortChar091  """  
      self.ShortChar092:str = obj["ShortChar092"]
      """  ShortChar092  """  
      self.ShortChar093:str = obj["ShortChar093"]
      """  ShortChar093  """  
      self.ShortChar094:str = obj["ShortChar094"]
      """  ShortChar094  """  
      self.ShortChar095:str = obj["ShortChar095"]
      """  ShortChar095  """  
      self.ShortChar096:str = obj["ShortChar096"]
      """  ShortChar096  """  
      self.ShortChar097:str = obj["ShortChar097"]
      """  ShortChar097  """  
      self.ShortChar098:str = obj["ShortChar098"]
      """  ShortChar098  """  
      self.ShortChar099:str = obj["ShortChar099"]
      """  ShortChar099  """  
      self.ShortChar100:str = obj["ShortChar100"]
      """  ShortChar100  """  
      self.ShortChar101:str = obj["ShortChar101"]
      """  ShortChar101  """  
      self.ShortChar102:str = obj["ShortChar102"]
      """  ShortChar102  """  
      self.ShortChar103:str = obj["ShortChar103"]
      """  ShortChar103  """  
      self.ShortChar104:str = obj["ShortChar104"]
      """  ShortChar104  """  
      self.ShortChar105:str = obj["ShortChar105"]
      """  ShortChar105  """  
      self.ShortChar106:str = obj["ShortChar106"]
      """  ShortChar106  """  
      self.ShortChar107:str = obj["ShortChar107"]
      """  ShortChar107  """  
      self.ShortChar108:str = obj["ShortChar108"]
      """  ShortChar108  """  
      self.ShortChar109:str = obj["ShortChar109"]
      """  ShortChar109  """  
      self.ShortChar110:str = obj["ShortChar110"]
      """  ShortChar110  """  
      self.ShortChar111:str = obj["ShortChar111"]
      """  ShortChar111  """  
      self.ShortChar112:str = obj["ShortChar112"]
      """  ShortChar112  """  
      self.ShortChar113:str = obj["ShortChar113"]
      """  ShortChar113  """  
      self.ShortChar114:str = obj["ShortChar114"]
      """  ShortChar114  """  
      self.ShortChar115:str = obj["ShortChar115"]
      """  ShortChar115  """  
      self.ShortChar116:str = obj["ShortChar116"]
      """  ShortChar116  """  
      self.ShortChar117:str = obj["ShortChar117"]
      """  ShortChar117  """  
      self.ShortChar118:str = obj["ShortChar118"]
      """  ShortChar118  """  
      self.ShortChar119:str = obj["ShortChar119"]
      """  ShortChar119  """  
      self.ShortChar120:str = obj["ShortChar120"]
      """  ShortChar120  """  
      self.ShortChar121:str = obj["ShortChar121"]
      """  ShortChar121  """  
      self.ShortChar122:str = obj["ShortChar122"]
      """  ShortChar122  """  
      self.ShortChar123:str = obj["ShortChar123"]
      """  ShortChar123  """  
      self.ShortChar124:str = obj["ShortChar124"]
      """  ShortChar124  """  
      self.ShortChar125:str = obj["ShortChar125"]
      """  ShortChar125  """  
      self.ShortChar126:str = obj["ShortChar126"]
      """  ShortChar126  """  
      self.ShortChar127:str = obj["ShortChar127"]
      """  ShortChar127  """  
      self.ShortChar128:str = obj["ShortChar128"]
      """  ShortChar128  """  
      self.ShortChar129:str = obj["ShortChar129"]
      """  ShortChar129  """  
      self.ShortChar130:str = obj["ShortChar130"]
      """  ShortChar130  """  
      self.ShortChar131:str = obj["ShortChar131"]
      """  ShortChar131  """  
      self.ShortChar132:str = obj["ShortChar132"]
      """  ShortChar132  """  
      self.ShortChar133:str = obj["ShortChar133"]
      """  ShortChar133  """  
      self.ShortChar134:str = obj["ShortChar134"]
      """  ShortChar134  """  
      self.ShortChar135:str = obj["ShortChar135"]
      """  ShortChar135  """  
      self.ShortChar136:str = obj["ShortChar136"]
      """  ShortChar136  """  
      self.ShortChar137:str = obj["ShortChar137"]
      """  ShortChar137  """  
      self.ShortChar138:str = obj["ShortChar138"]
      """  ShortChar138  """  
      self.ShortChar139:str = obj["ShortChar139"]
      """  ShortChar139  """  
      self.ShortChar140:str = obj["ShortChar140"]
      """  ShortChar140  """  
      self.ShortChar141:str = obj["ShortChar141"]
      """  ShortChar141  """  
      self.ShortChar142:str = obj["ShortChar142"]
      """  ShortChar142  """  
      self.ShortChar143:str = obj["ShortChar143"]
      """  ShortChar143  """  
      self.ShortChar144:str = obj["ShortChar144"]
      """  ShortChar144  """  
      self.ShortChar145:str = obj["ShortChar145"]
      """  ShortChar145  """  
      self.ShortChar146:str = obj["ShortChar146"]
      """  ShortChar146  """  
      self.ShortChar147:str = obj["ShortChar147"]
      """  ShortChar147  """  
      self.ShortChar148:str = obj["ShortChar148"]
      """  ShortChar148  """  
      self.ShortChar149:str = obj["ShortChar149"]
      """  ShortChar149  """  
      self.ShortChar150:str = obj["ShortChar150"]
      """  ShortChar150  """  
      self.ShortChar151:str = obj["ShortChar151"]
      """  ShortChar151  """  
      self.ShortChar152:str = obj["ShortChar152"]
      """  ShortChar152  """  
      self.ShortChar153:str = obj["ShortChar153"]
      """  ShortChar153  """  
      self.ShortChar154:str = obj["ShortChar154"]
      """  ShortChar154  """  
      self.ShortChar155:str = obj["ShortChar155"]
      """  ShortChar155  """  
      self.ShortChar156:str = obj["ShortChar156"]
      """  ShortChar156  """  
      self.ShortChar157:str = obj["ShortChar157"]
      """  ShortChar157  """  
      self.ShortChar158:str = obj["ShortChar158"]
      """  ShortChar158  """  
      self.ShortChar159:str = obj["ShortChar159"]
      """  ShortChar159  """  
      self.ShortChar160:str = obj["ShortChar160"]
      """  ShortChar160  """  
      self.ShortChar161:str = obj["ShortChar161"]
      """  ShortChar161  """  
      self.ShortChar162:str = obj["ShortChar162"]
      """  ShortChar162  """  
      self.ShortChar163:str = obj["ShortChar163"]
      """  ShortChar163  """  
      self.ShortChar164:str = obj["ShortChar164"]
      """  ShortChar164  """  
      self.ShortChar165:str = obj["ShortChar165"]
      """  ShortChar165  """  
      self.ShortChar166:str = obj["ShortChar166"]
      """  ShortChar166  """  
      self.ShortChar167:str = obj["ShortChar167"]
      """  ShortChar167  """  
      self.ShortChar168:str = obj["ShortChar168"]
      """  ShortChar168  """  
      self.ShortChar169:str = obj["ShortChar169"]
      """  ShortChar169  """  
      self.ShortChar170:str = obj["ShortChar170"]
      """  ShortChar170  """  
      self.ShortChar171:str = obj["ShortChar171"]
      """  ShortChar171  """  
      self.ShortChar172:str = obj["ShortChar172"]
      """  ShortChar172  """  
      self.ShortChar173:str = obj["ShortChar173"]
      """  ShortChar173  """  
      self.ShortChar174:str = obj["ShortChar174"]
      """  ShortChar174  """  
      self.ShortChar175:str = obj["ShortChar175"]
      """  ShortChar175  """  
      self.ShortChar176:str = obj["ShortChar176"]
      """  ShortChar176  """  
      self.ShortChar177:str = obj["ShortChar177"]
      """  ShortChar177  """  
      self.ShortChar178:str = obj["ShortChar178"]
      """  ShortChar178  """  
      self.ShortChar179:str = obj["ShortChar179"]
      """  ShortChar179  """  
      self.ShortChar180:str = obj["ShortChar180"]
      """  ShortChar180  """  
      self.ShortChar181:str = obj["ShortChar181"]
      """  ShortChar181  """  
      self.ShortChar182:str = obj["ShortChar182"]
      """  ShortChar182  """  
      self.ShortChar183:str = obj["ShortChar183"]
      """  ShortChar183  """  
      self.ShortChar184:str = obj["ShortChar184"]
      """  ShortChar184  """  
      self.ShortChar185:str = obj["ShortChar185"]
      """  ShortChar185  """  
      self.ShortChar186:str = obj["ShortChar186"]
      """  ShortChar186  """  
      self.ShortChar187:str = obj["ShortChar187"]
      """  ShortChar187  """  
      self.ShortChar188:str = obj["ShortChar188"]
      """  ShortChar188  """  
      self.ShortChar189:str = obj["ShortChar189"]
      """  ShortChar189  """  
      self.ShortChar190:str = obj["ShortChar190"]
      """  ShortChar190  """  
      self.ShortChar191:str = obj["ShortChar191"]
      """  ShortChar191  """  
      self.ShortChar192:str = obj["ShortChar192"]
      """  ShortChar192  """  
      self.ShortChar193:str = obj["ShortChar193"]
      """  ShortChar193  """  
      self.ShortChar194:str = obj["ShortChar194"]
      """  ShortChar194  """  
      self.ShortChar195:str = obj["ShortChar195"]
      """  ShortChar195  """  
      self.ShortChar196:str = obj["ShortChar196"]
      """  ShortChar196  """  
      self.ShortChar197:str = obj["ShortChar197"]
      """  ShortChar197  """  
      self.ShortChar198:str = obj["ShortChar198"]
      """  ShortChar198  """  
      self.ShortChar199:str = obj["ShortChar199"]
      """  ShortChar199  """  
      self.ShortChar200:str = obj["ShortChar200"]
      """  ShortChar200  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtInspDataTrackerTableset:
   def __init__(self, obj):
      self.InspResults:list[Erp_Tablesets_InspResultsRow] = obj["InspResults"]
      self.InspResultsAttch:list[Erp_Tablesets_InspResultsAttchRow] = obj["InspResultsAttch"]
      self.InspResultsChar:list[Erp_Tablesets_InspResultsCharRow] = obj["InspResultsChar"]
      self.InspResultsCharAttch:list[Erp_Tablesets_InspResultsCharAttchRow] = obj["InspResultsCharAttch"]
      self.InspResultsCheckBox:list[Erp_Tablesets_InspResultsCheckBoxRow] = obj["InspResultsCheckBox"]
      self.InspResultsCheckBoxAttch:list[Erp_Tablesets_InspResultsCheckBoxAttchRow] = obj["InspResultsCheckBoxAttch"]
      self.InspResultsDate:list[Erp_Tablesets_InspResultsDateRow] = obj["InspResultsDate"]
      self.InspResultsDateAttch:list[Erp_Tablesets_InspResultsDateAttchRow] = obj["InspResultsDateAttch"]
      self.InspResultsNum:list[Erp_Tablesets_InspResultsNumRow] = obj["InspResultsNum"]
      self.InspResultsNumAttch:list[Erp_Tablesets_InspResultsNumAttchRow] = obj["InspResultsNumAttch"]
      self.InspResultsShortChar:list[Erp_Tablesets_InspResultsShortCharRow] = obj["InspResultsShortChar"]
      self.InspResultsShortCharAttch:list[Erp_Tablesets_InspResultsShortCharAttchRow] = obj["InspResultsShortCharAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspDataTrackerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_InspDataTrackerTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_InspDataTrackerTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrentPlanRev_input:
   """ Required : 
   ipInspPlan
   """  
   def __init__(self, obj):
      self.ipInspPlan:str = obj["ipInspPlan"]
      pass

class GetCurrentPlanRev_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetCurrentSpecRev_input:
   """ Required : 
   ipSpecID
   """  
   def __init__(self, obj):
      self.ipSpecID:str = obj["ipSpecID"]
      pass

class GetCurrentSpecRev_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDisplayColumns_input:
   """ Required : 
   inSpecID
   inSpecRevNum
   inInspPlanPartNum
   inInspPlanRevNum
   """  
   def __init__(self, obj):
      self.inSpecID:str = obj["inSpecID"]
      """  The specification ID  """  
      self.inSpecRevNum:str = obj["inSpecRevNum"]
      """  The specification revision number  """  
      self.inInspPlanPartNum:str = obj["inInspPlanPartNum"]
      """  The inspection plan part number  """  
      self.inInspPlanRevNum:str = obj["inInspPlanRevNum"]
      """  The inspection plan revision number  """  
      pass

class GetDisplayColumns_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspDisplayColumnsTableset] = obj["returnObj"]
      pass

class GetInspDataParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspDataParamTableset] = obj["returnObj"]
      pass

class GetInspPlanRevs_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class GetInspPlanRevs_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_InspResultsListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewInspResultsAttch_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetNewInspResultsAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsCharAttch_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetNewInspResultsCharAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsChar_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      pass

class GetNewInspResultsChar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsCheckBoxAttch_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetNewInspResultsCheckBoxAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsCheckBox_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      pass

class GetNewInspResultsCheckBox_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsDateAttch_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetNewInspResultsDateAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsDate_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      pass

class GetNewInspResultsDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsNumAttch_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetNewInspResultsNumAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsNum_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      pass

class GetNewInspResultsNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsShortCharAttch_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   inspectTime
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      self.inspectTime:int = obj["inspectTime"]
      pass

class GetNewInspResultsShortCharAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResultsShortChar_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      pass

class GetNewInspResultsShortChar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewInspResults_input:
   """ Required : 
   ds
   inspPlanType
   file
   key1
   key2
   key3
   key4
   key5
   sampleNumber
   inspectDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      self.inspPlanType:str = obj["inspPlanType"]
      self.file:str = obj["file"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.sampleNumber:int = obj["sampleNumber"]
      self.inspectDate:str = obj["inspectDate"]
      pass

class GetNewInspResults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseInspResults
   whereClauseInspResultsAttch
   whereClauseInspResultsChar
   whereClauseInspResultsCharAttch
   whereClauseInspResultsCheckBox
   whereClauseInspResultsCheckBoxAttch
   whereClauseInspResultsDate
   whereClauseInspResultsDateAttch
   whereClauseInspResultsNum
   whereClauseInspResultsNumAttch
   whereClauseInspResultsShortChar
   whereClauseInspResultsShortCharAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseInspResults:str = obj["whereClauseInspResults"]
      self.whereClauseInspResultsAttch:str = obj["whereClauseInspResultsAttch"]
      self.whereClauseInspResultsChar:str = obj["whereClauseInspResultsChar"]
      self.whereClauseInspResultsCharAttch:str = obj["whereClauseInspResultsCharAttch"]
      self.whereClauseInspResultsCheckBox:str = obj["whereClauseInspResultsCheckBox"]
      self.whereClauseInspResultsCheckBoxAttch:str = obj["whereClauseInspResultsCheckBoxAttch"]
      self.whereClauseInspResultsDate:str = obj["whereClauseInspResultsDate"]
      self.whereClauseInspResultsDateAttch:str = obj["whereClauseInspResultsDateAttch"]
      self.whereClauseInspResultsNum:str = obj["whereClauseInspResultsNum"]
      self.whereClauseInspResultsNumAttch:str = obj["whereClauseInspResultsNumAttch"]
      self.whereClauseInspResultsShortChar:str = obj["whereClauseInspResultsShortChar"]
      self.whereClauseInspResultsShortCharAttch:str = obj["whereClauseInspResultsShortCharAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspDataTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSpecRevs_input:
   """ Required : 
   ipSpecID
   """  
   def __init__(self, obj):
      self.ipSpecID:str = obj["ipSpecID"]
      pass

class GetSpecRevs_output:
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

class OnChangeInspPlanPartNum_input:
   """ Required : 
   pcProposedInspPlanNum
   ds
   """  
   def __init__(self, obj):
      self.pcProposedInspPlanNum:str = obj["pcProposedInspPlanNum"]
      """  The new proposed Inspection Plan Number  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeInspPlanPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeInspType_input:
   """ Required : 
   pcProposedInspType
   ds
   """  
   def __init__(self, obj):
      self.pcProposedInspType:str = obj["pcProposedInspType"]
      """  The new proposed inspection type value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeInspType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobAsm_input:
   """ Required : 
   piProposedAssemblySeq
   ds
   """  
   def __init__(self, obj):
      self.piProposedAssemblySeq:int = obj["piProposedAssemblySeq"]
      """  The new proposed Job Assembly value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeJobAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   pcProposedJobNum
   ds
   """  
   def __init__(self, obj):
      self.pcProposedJobNum:str = obj["pcProposedJobNum"]
      """  The new proposed JobNum value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobOpr_input:
   """ Required : 
   piProposedOprSeq
   ds
   """  
   def __init__(self, obj):
      self.piProposedOprSeq:int = obj["piProposedOprSeq"]
      """  The new proposed Job Operation Sequence value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeJobOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeNCMID_input:
   """ Required : 
   pcProposedNCMTranID
   ds
   """  
   def __init__(self, obj):
      self.pcProposedNCMTranID:int = obj["pcProposedNCMTranID"]
      """  The new proposed NCMTranID value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeNCMID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePackSlip_input:
   """ Required : 
   piProposedPackSlip
   ds
   """  
   def __init__(self, obj):
      self.piProposedPackSlip:str = obj["piProposedPackSlip"]
      """  The new proposed PackSlip value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangePackSlip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   piProposedPartNum
   ds
   """  
   def __init__(self, obj):
      self.piProposedPartNum:str = obj["piProposedPartNum"]
      """  The new proposed PartNum value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSpecID_input:
   """ Required : 
   pcProposedSpecID
   ds
   """  
   def __init__(self, obj):
      self.pcProposedSpecID:str = obj["pcProposedSpecID"]
      """  The new proposed Inspection Plan Number  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeSpecID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeVendorID_input:
   """ Required : 
   pcProposedVendorID
   ds
   """  
   def __init__(self, obj):
      self.pcProposedVendorID:str = obj["pcProposedVendorID"]
      """  The new proposed Vendor ID  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class OnChangeVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PackLineChanged_input:
   """ Required : 
   packSlip
   proposedPackLine
   vendorNum
   ds
   """  
   def __init__(self, obj):
      self.packSlip:str = obj["packSlip"]
      self.proposedPackLine:int = obj["proposedPackLine"]
      self.vendorNum:int = obj["vendorNum"]
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class PackLineChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PackSlipChanged_input:
   """ Required : 
   piProposedPackSlip
   ds
   """  
   def __init__(self, obj):
      self.piProposedPackSlip:str = obj["piProposedPackSlip"]
      """  The new proposed PackSlip value  """  
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class PackSlipChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RetrieveValues_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

class RetrieveValues_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InspDataTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataParamTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtInspDataTrackerTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtInspDataTrackerTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InspDataTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

