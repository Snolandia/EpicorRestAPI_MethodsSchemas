import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.SysActivityTrackerSvc
# Description: Activity Tracking Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SysActivityTrackers(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysActivityTrackers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysActivityTrackers
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysActivityTrackerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers",headers=creds) as resp:
           return await resp.json()

async def post_SysActivityTrackers(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysActivityTrackers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysActivityTrackerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysActivityTrackerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysActivityTrackers_Company_ActivityType_ActivityID(Company, ActivityType, ActivityID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysActivityTracker item
   Description: Calls GetByID to retrieve the SysActivityTracker item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysActivityTracker
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActivityType: Desc: ActivityType   Required: True
      :param ActivityID: Desc: ActivityID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysActivityTrackerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers(" + Company + "," + ActivityType + "," + ActivityID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysActivityTrackers_Company_ActivityType_ActivityID(Company, ActivityType, ActivityID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysActivityTracker for the service
   Description: Calls UpdateExt to update SysActivityTracker. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysActivityTracker
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActivityType: Desc: ActivityType   Required: True
      :param ActivityID: Desc: ActivityID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysActivityTrackerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers(" + Company + "," + ActivityType + "," + ActivityID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysActivityTrackers_Company_ActivityType_ActivityID(Company, ActivityType, ActivityID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysActivityTracker item
   Description: Call UpdateExt to delete SysActivityTracker item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysActivityTracker
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActivityType: Desc: ActivityType   Required: True
      :param ActivityID: Desc: ActivityID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers(" + Company + "," + ActivityType + "," + ActivityID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysActivityTrackers_Company_ActivityType_ActivityID_SysActivities(Company, ActivityType, ActivityID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysActivities items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysActivities1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActivityType: Desc: ActivityType   Required: True
      :param ActivityID: Desc: ActivityID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysActivityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers(" + Company + "," + ActivityType + "," + ActivityID + ")/SysActivities",headers=creds) as resp:
           return await resp.json()

async def get_SysActivityTrackers_Company_ActivityType_ActivityID_SysActivities_ActivitySeq(Company, ActivityType, ActivityID, ActivitySeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysActivity item
   Description: Calls GetByID to retrieve the SysActivity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysActivity1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ActivityType: Desc: ActivityType   Required: True
      :param ActivityID: Desc: ActivityID   Required: True   Allow empty value : True
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysActivityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityTrackers(" + Company + "," + ActivityType + "," + ActivityID + ")/SysActivities(" + ActivitySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysActivities(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysActivities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysActivities
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysActivityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities",headers=creds) as resp:
           return await resp.json()

async def post_SysActivities(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysActivities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysActivityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysActivityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysActivities_ActivitySeq(ActivitySeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysActivity item
   Description: Calls GetByID to retrieve the SysActivity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysActivity
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysActivityRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities(" + ActivitySeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysActivities_ActivitySeq(ActivitySeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysActivity for the service
   Description: Calls UpdateExt to update SysActivity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysActivity
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysActivityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities(" + ActivitySeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysActivities_ActivitySeq(ActivitySeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysActivity item
   Description: Call UpdateExt to delete SysActivity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysActivity
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities(" + ActivitySeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysActivities_ActivitySeq_SysActivityDetails(ActivitySeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SysActivityDetails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SysActivityDetails1
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysActivityDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities(" + ActivitySeq + ")/SysActivityDetails",headers=creds) as resp:
           return await resp.json()

async def get_SysActivities_ActivitySeq_SysActivityDetails_ActivitySeq_CreatedOn(ActivitySeq, CreatedOn, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysActivityDetail item
   Description: Calls GetByID to retrieve the SysActivityDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysActivityDetail1
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysActivityDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivities(" + ActivitySeq + ")/SysActivityDetails(" + ActivitySeq + "," + CreatedOn + ")",headers=creds) as resp:
           return await resp.json()

async def get_SysActivityDetails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SysActivityDetails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SysActivityDetails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysActivityDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityDetails",headers=creds) as resp:
           return await resp.json()

async def post_SysActivityDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SysActivityDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysActivityDetailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysActivityDetailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityDetails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SysActivityDetails_ActivitySeq_CreatedOn(ActivitySeq, CreatedOn, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SysActivityDetail item
   Description: Calls GetByID to retrieve the SysActivityDetail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SysActivityDetail
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysActivityDetailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityDetails(" + ActivitySeq + "," + CreatedOn + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SysActivityDetails_ActivitySeq_CreatedOn(ActivitySeq, CreatedOn, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SysActivityDetail for the service
   Description: Calls UpdateExt to update SysActivityDetail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SysActivityDetail
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysActivityDetailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityDetails(" + ActivitySeq + "," + CreatedOn + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SysActivityDetails_ActivitySeq_CreatedOn(ActivitySeq, CreatedOn, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SysActivityDetail item
   Description: Call UpdateExt to delete SysActivityDetail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SysActivityDetail
      :param ActivitySeq: Desc: ActivitySeq   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/SysActivityDetails(" + ActivitySeq + "," + CreatedOn + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysActivityTrackerListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysActivityTracker, whereClauseSysActivity, whereClauseSysActivityDetail, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSysActivityTracker=" + whereClauseSysActivityTracker
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysActivity=" + whereClauseSysActivity
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSysActivityDetail=" + whereClauseSysActivityDetail
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(activityType, activityID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "activityType=" + activityType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "activityID=" + activityID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSysActivityTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSysActivityTypeList
   Description: Returns the SysActivityTypeList for the current company and global company.
   OperationID: GetSysActivityTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSysActivityTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_DeleteActivityDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteActivityDetail
   Description: Deletes the detail rows.
   OperationID: DeleteActivityDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteActivityDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteActivityDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteActivity
   Description: Deletes the Activity row and child detail rows.
   OperationID: DeleteActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TrackActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TrackActivity
   Description: Allows tracking of an activity.
   OperationID: TrackActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TrackActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TrackActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysActivityTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysActivityTracker
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysActivityTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysActivityTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysActivityTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysActivity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysActivityDetail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysActivityDetail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysActivityDetail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysActivityDetail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysActivityDetail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.SysActivityTrackerSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysActivityDetailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysActivityDetailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysActivityRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysActivityRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysActivityTrackerListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysActivityTrackerListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysActivityTrackerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysActivityTrackerRow] = obj["value"]
      pass

class Ice_Tablesets_SysActivityDetailRow:
   def __init__(self, obj):
      self.ActivitySeq:int = obj["ActivitySeq"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.Company:str = obj["Company"]
      self.ActivityType:int = obj["ActivityType"]
      self.ActivityID:str = obj["ActivityID"]
      self.UserID:str = obj["UserID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysActivityRow:
   def __init__(self, obj):
      self.ActivitySeq:int = obj["ActivitySeq"]
      self.Company:str = obj["Company"]
      self.ActivityType:int = obj["ActivityType"]
      self.ActivityID:str = obj["ActivityID"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.Key6:str = obj["Key6"]
      self.Key7:str = obj["Key7"]
      self.Key8:str = obj["Key8"]
      self.Key9:str = obj["Key9"]
      self.Key10:str = obj["Key10"]
      self.ActivityCount:int = obj["ActivityCount"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.Description:str = obj["Description"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysActivityTrackerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ActivityType:int = obj["ActivityType"]
      """  ActivityType  """  
      self.ActivityID:str = obj["ActivityID"]
      """  ActivityID  """  
      self.ActivityDesc:str = obj["ActivityDesc"]
      """  ActivityDesc  """  
      self.Frequency:int = obj["Frequency"]
      """  Frequency  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.RetentionDurationDays:int = obj["RetentionDurationDays"]
      """  RetentionDurationDays  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled  """  
      self.LogDetail:bool = obj["LogDetail"]
      """  LogDetail  """  
      self.ActivityRetentionDays:int = obj["ActivityRetentionDays"]
      """  ActivityRetentionDays  """  
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

class Ice_Tablesets_SysActivityTrackerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ActivityType:int = obj["ActivityType"]
      """  ActivityType  """  
      self.ActivityID:str = obj["ActivityID"]
      """  ActivityID  """  
      self.ActivityDesc:str = obj["ActivityDesc"]
      """  ActivityDesc  """  
      self.Frequency:int = obj["Frequency"]
      """  Frequency  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.RetentionDurationDays:int = obj["RetentionDurationDays"]
      """  RetentionDurationDays  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled  """  
      self.LogDetail:bool = obj["LogDetail"]
      """  LogDetail  """  
      self.ActivityRetentionDays:int = obj["ActivityRetentionDays"]
      """  ActivityRetentionDays  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteActivityDetail_input:
   """ Required : 
   activityType
   activityID
   activitySeq
   """  
   def __init__(self, obj):
      self.activityType:int = obj["activityType"]
      """  The activity type.  """  
      self.activityID:str = obj["activityID"]
      """  The activity ID.  """  
      self.activitySeq:int = obj["activitySeq"]
      """  The activity sequence.  """  
      pass

class DeleteActivityDetail_output:
   def __init__(self, obj):
      pass

class DeleteActivity_input:
   """ Required : 
   activityType
   activityID
   activitySeq
   """  
   def __init__(self, obj):
      self.activityType:int = obj["activityType"]
      """  The activity type.  """  
      self.activityID:str = obj["activityID"]
      """  The activity ID.  """  
      self.activitySeq:int = obj["activitySeq"]
      """  The activity sequence.  """  
      pass

class DeleteActivity_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   activityType
   activityID
   """  
   def __init__(self, obj):
      self.activityType:int = obj["activityType"]
      self.activityID:str = obj["activityID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   activityType
   activityID
   """  
   def __init__(self, obj):
      self.activityType:int = obj["activityType"]
      self.activityID:str = obj["activityID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_SysActivityTrackerListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSysActivityDetail_input:
   """ Required : 
   ds
   activitySeq
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      self.activitySeq:int = obj["activitySeq"]
      pass

class GetNewSysActivityDetail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysActivityTracker_input:
   """ Required : 
   ds
   activityType
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      self.activityType:int = obj["activityType"]
      pass

class GetNewSysActivityTracker_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSysActivity_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      pass

class GetNewSysActivity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSysActivityTracker
   whereClauseSysActivity
   whereClauseSysActivityDetail
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysActivityTracker:str = obj["whereClauseSysActivityTracker"]
      self.whereClauseSysActivity:str = obj["whereClauseSysActivity"]
      self.whereClauseSysActivityDetail:str = obj["whereClauseSysActivityDetail"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSysActivityTypeList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_SysActivityTypeTableset] = obj["returnObj"]
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

class Ice_Tablesets_SysActivityDetailRow:
   def __init__(self, obj):
      self.ActivitySeq:int = obj["ActivitySeq"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.Company:str = obj["Company"]
      self.ActivityType:int = obj["ActivityType"]
      self.ActivityID:str = obj["ActivityID"]
      self.UserID:str = obj["UserID"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysActivityRow:
   def __init__(self, obj):
      self.ActivitySeq:int = obj["ActivitySeq"]
      self.Company:str = obj["Company"]
      self.ActivityType:int = obj["ActivityType"]
      self.ActivityID:str = obj["ActivityID"]
      self.Key1:str = obj["Key1"]
      self.Key2:str = obj["Key2"]
      self.Key3:str = obj["Key3"]
      self.Key4:str = obj["Key4"]
      self.Key5:str = obj["Key5"]
      self.Key6:str = obj["Key6"]
      self.Key7:str = obj["Key7"]
      self.Key8:str = obj["Key8"]
      self.Key9:str = obj["Key9"]
      self.Key10:str = obj["Key10"]
      self.ActivityCount:int = obj["ActivityCount"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.LastUpdated:str = obj["LastUpdated"]
      self.Description:str = obj["Description"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysActivityTrackerListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ActivityType:int = obj["ActivityType"]
      """  ActivityType  """  
      self.ActivityID:str = obj["ActivityID"]
      """  ActivityID  """  
      self.ActivityDesc:str = obj["ActivityDesc"]
      """  ActivityDesc  """  
      self.Frequency:int = obj["Frequency"]
      """  Frequency  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.RetentionDurationDays:int = obj["RetentionDurationDays"]
      """  RetentionDurationDays  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled  """  
      self.LogDetail:bool = obj["LogDetail"]
      """  LogDetail  """  
      self.ActivityRetentionDays:int = obj["ActivityRetentionDays"]
      """  ActivityRetentionDays  """  
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

class Ice_Tablesets_SysActivityTrackerListTableset:
   def __init__(self, obj):
      self.SysActivityTrackerList:list[Ice_Tablesets_SysActivityTrackerListRow] = obj["SysActivityTrackerList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysActivityTrackerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ActivityType:int = obj["ActivityType"]
      """  ActivityType  """  
      self.ActivityID:str = obj["ActivityID"]
      """  ActivityID  """  
      self.ActivityDesc:str = obj["ActivityDesc"]
      """  ActivityDesc  """  
      self.Frequency:int = obj["Frequency"]
      """  Frequency  """  
      self.CompanyVisibility:int = obj["CompanyVisibility"]
      """  CompanyVisibility  """  
      self.RetentionDurationDays:int = obj["RetentionDurationDays"]
      """  RetentionDurationDays  """  
      self.Enabled:bool = obj["Enabled"]
      """  Enabled  """  
      self.LogDetail:bool = obj["LogDetail"]
      """  LogDetail  """  
      self.ActivityRetentionDays:int = obj["ActivityRetentionDays"]
      """  ActivityRetentionDays  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  SystemFlag  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllCompanies:bool = obj["AllCompanies"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysActivityTrackerTableset:
   def __init__(self, obj):
      self.SysActivityTracker:list[Ice_Tablesets_SysActivityTrackerRow] = obj["SysActivityTracker"]
      self.SysActivity:list[Ice_Tablesets_SysActivityRow] = obj["SysActivity"]
      self.SysActivityDetail:list[Ice_Tablesets_SysActivityDetailRow] = obj["SysActivityDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysActivityTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ActivityType:int = obj["ActivityType"]
      self.Description:str = obj["Description"]
      self.SystemFlag:bool = obj["SystemFlag"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysActivityTypeTableset:
   def __init__(self, obj):
      self.SysActivityType:list[Ice_Tablesets_SysActivityTypeRow] = obj["SysActivityType"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtSysActivityTrackerTableset:
   def __init__(self, obj):
      self.SysActivityTracker:list[Ice_Tablesets_SysActivityTrackerRow] = obj["SysActivityTracker"]
      self.SysActivity:list[Ice_Tablesets_SysActivityRow] = obj["SysActivity"]
      self.SysActivityDetail:list[Ice_Tablesets_SysActivityDetailRow] = obj["SysActivityDetail"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class TrackActivity_input:
   """ Required : 
   activityType
   recordKeys
   description
   """  
   def __init__(self, obj):
      self.activityType:int = obj["activityType"]
      """  Must be a valid ActivityType.  """  
      self.recordKeys:str = obj["recordKeys"]
      """  Array of key values to use.  Up to 10 allowed.  """  
      self.description:str = obj["description"]
      """  A freeform description of the event you are tracking.  """  
      pass

class TrackActivity_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysActivityTrackerTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtSysActivityTrackerTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_SysActivityTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

