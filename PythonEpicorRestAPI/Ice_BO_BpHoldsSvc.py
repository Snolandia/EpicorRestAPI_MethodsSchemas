import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.BpHoldsSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BpHolds(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BpHolds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpHolds
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpHoldTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds",headers=creds) as resp:
           return await resp.json()

async def post_BpHolds(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpHolds
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpHoldTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpHoldTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BpHolds_Company_HoldTypeID(Company, HoldTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpHold item
   Description: Calls GetByID to retrieve the BpHold item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpHold
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpHoldTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BpHolds_Company_HoldTypeID(Company, HoldTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BpHold for the service
   Description: Calls UpdateExt to update BpHold. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpHold
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpHoldTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BpHolds_Company_HoldTypeID(Company, HoldTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BpHold item
   Description: Call UpdateExt to delete BpHold item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpHold
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpHolds_Company_HoldTypeID_BpHoldAttachHists(Company, HoldTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BpHoldAttachHists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BpHoldAttachHists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpHoldAttachHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")/BpHoldAttachHists",headers=creds) as resp:
           return await resp.json()

async def get_BpHolds_Company_HoldTypeID_BpHoldAttachHists_Company_HoldTypeID_HoldHistoryID(Company, HoldTypeID, HoldHistoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpHoldAttachHist item
   Description: Calls GetByID to retrieve the BpHoldAttachHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpHoldAttachHist1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldHistoryID: Desc: HoldHistoryID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpHoldAttachHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")/BpHoldAttachHists(" + Company + "," + HoldTypeID + "," + HoldHistoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpHolds_Company_HoldTypeID_BpHoldAttachments(Company, HoldTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BpHoldAttachments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BpHoldAttachments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpHoldAttachmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")/BpHoldAttachments",headers=creds) as resp:
           return await resp.json()

async def get_BpHolds_Company_HoldTypeID_BpHoldAttachments_Company_HoldTypeID_HoldAttachID(Company, HoldTypeID, HoldAttachID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpHoldAttachment item
   Description: Calls GetByID to retrieve the BpHoldAttachment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpHoldAttachment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldAttachID: Desc: HoldAttachID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpHoldAttachmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHolds(" + Company + "," + HoldTypeID + ")/BpHoldAttachments(" + Company + "," + HoldTypeID + "," + HoldAttachID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpHoldAttachHists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BpHoldAttachHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpHoldAttachHists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpHoldAttachHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachHists",headers=creds) as resp:
           return await resp.json()

async def post_BpHoldAttachHists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpHoldAttachHists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpHoldAttachHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpHoldAttachHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachHists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BpHoldAttachHists_Company_HoldTypeID_HoldHistoryID(Company, HoldTypeID, HoldHistoryID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpHoldAttachHist item
   Description: Calls GetByID to retrieve the BpHoldAttachHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpHoldAttachHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldHistoryID: Desc: HoldHistoryID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpHoldAttachHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachHists(" + Company + "," + HoldTypeID + "," + HoldHistoryID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BpHoldAttachHists_Company_HoldTypeID_HoldHistoryID(Company, HoldTypeID, HoldHistoryID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BpHoldAttachHist for the service
   Description: Calls UpdateExt to update BpHoldAttachHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpHoldAttachHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldHistoryID: Desc: HoldHistoryID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpHoldAttachHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachHists(" + Company + "," + HoldTypeID + "," + HoldHistoryID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BpHoldAttachHists_Company_HoldTypeID_HoldHistoryID(Company, HoldTypeID, HoldHistoryID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BpHoldAttachHist item
   Description: Call UpdateExt to delete BpHoldAttachHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpHoldAttachHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldHistoryID: Desc: HoldHistoryID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachHists(" + Company + "," + HoldTypeID + "," + HoldHistoryID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BpHoldAttachments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BpHoldAttachments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BpHoldAttachments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpHoldAttachmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachments",headers=creds) as resp:
           return await resp.json()

async def post_BpHoldAttachments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BpHoldAttachments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.BpHoldAttachmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.BpHoldAttachmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BpHoldAttachments_Company_HoldTypeID_HoldAttachID(Company, HoldTypeID, HoldAttachID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BpHoldAttachment item
   Description: Calls GetByID to retrieve the BpHoldAttachment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BpHoldAttachment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldAttachID: Desc: HoldAttachID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.BpHoldAttachmentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachments(" + Company + "," + HoldTypeID + "," + HoldAttachID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BpHoldAttachments_Company_HoldTypeID_HoldAttachID(Company, HoldTypeID, HoldAttachID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BpHoldAttachment for the service
   Description: Calls UpdateExt to update BpHoldAttachment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BpHoldAttachment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldAttachID: Desc: HoldAttachID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.BpHoldAttachmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachments(" + Company + "," + HoldTypeID + "," + HoldAttachID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BpHoldAttachments_Company_HoldTypeID_HoldAttachID(Company, HoldTypeID, HoldAttachID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BpHoldAttachment item
   Description: Call UpdateExt to delete BpHoldAttachment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BpHoldAttachment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param HoldTypeID: Desc: HoldTypeID   Required: True   Allow empty value : True
      :param HoldAttachID: Desc: HoldAttachID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/BpHoldAttachments(" + Company + "," + HoldTypeID + "," + HoldAttachID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.BpHoldTypeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBpHoldType, whereClauseBpHoldAttachHist, whereClauseBpHoldAttachment, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseBpHoldType=" + whereClauseBpHoldType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBpHoldAttachHist=" + whereClauseBpHoldAttachHist
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBpHoldAttachment=" + whereClauseBpHoldAttachment
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(holdTypeID, epicorHeaders = None):
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
   params += "holdTypeID=" + holdTypeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpHoldType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpHoldType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpHoldType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpHoldType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpHoldType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpHoldAttachHist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpHoldAttachHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpHoldAttachHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpHoldAttachHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpHoldAttachHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBpHoldAttachment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBpHoldAttachment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBpHoldAttachment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBpHoldAttachment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBpHoldAttachment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.BpHoldsSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpHoldAttachHistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpHoldAttachHistRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpHoldAttachmentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpHoldAttachmentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpHoldTypeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpHoldTypeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_BpHoldTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_BpHoldTypeRow] = obj["value"]
      pass

class Ice_Tablesets_BpHoldAttachHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.HoldHistoryID:int = obj["HoldHistoryID"]
      """  Unique ID of the archived hold attachment  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  user, created the hold attachment  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.RemoveUserID:str = obj["RemoveUserID"]
      """  user, removed the hold attachment  """  
      self.RemovedOn:str = obj["RemovedOn"]
      """  RemovedOn  """  
      self.HoldSysRowID:str = obj["HoldSysRowID"]
      """  HoldSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpHoldAttachmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.HoldAttachID:int = obj["HoldAttachID"]
      """  Unique ID of the hold attachment  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  user, created the hold attachment  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.HoldSysRowID:str = obj["HoldSysRowID"]
      """  HoldSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpHoldTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.SystemCode:str = obj["SystemCode"]
      """  Code that identifies the system (ex. ICE)  """  
      self.ClassName:str = obj["ClassName"]
      """  Hold Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Hold Namespace  """  
      self.DataTableID:str = obj["DataTableID"]
      """  Data Table  """  
      self.Description:str = obj["Description"]
      """  Hold Description  """  
      self.HistoryLength:int = obj["HistoryLength"]
      """  Defines how many holds are stored in history  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpHoldTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.SystemCode:str = obj["SystemCode"]
      """  Code that identifies the system (ex. ICE)  """  
      self.ClassName:str = obj["ClassName"]
      """  Hold Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Hold Namespace  """  
      self.DataTableID:str = obj["DataTableID"]
      """  Data Table  """  
      self.Description:str = obj["Description"]
      """  Hold Description  """  
      self.HistoryLength:int = obj["HistoryLength"]
      """  Defines how many holds are stored in history  """  
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




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   holdTypeID
   """  
   def __init__(self, obj):
      self.holdTypeID:str = obj["holdTypeID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   holdTypeID
   """  
   def __init__(self, obj):
      self.holdTypeID:str = obj["holdTypeID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpHoldsTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BpHoldsTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BpHoldsTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_BpHoldTypeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBpHoldAttachHist_input:
   """ Required : 
   ds
   holdTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      self.holdTypeID:str = obj["holdTypeID"]
      pass

class GetNewBpHoldAttachHist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBpHoldAttachment_input:
   """ Required : 
   ds
   holdTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      self.holdTypeID:str = obj["holdTypeID"]
      pass

class GetNewBpHoldAttachment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBpHoldType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      pass

class GetNewBpHoldType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBpHoldType
   whereClauseBpHoldAttachHist
   whereClauseBpHoldAttachment
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBpHoldType:str = obj["whereClauseBpHoldType"]
      self.whereClauseBpHoldAttachHist:str = obj["whereClauseBpHoldAttachHist"]
      self.whereClauseBpHoldAttachment:str = obj["whereClauseBpHoldAttachment"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_BpHoldsTableset] = obj["returnObj"]
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

class Ice_Tablesets_BpHoldAttachHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.HoldHistoryID:int = obj["HoldHistoryID"]
      """  Unique ID of the archived hold attachment  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  user, created the hold attachment  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.RemoveUserID:str = obj["RemoveUserID"]
      """  user, removed the hold attachment  """  
      self.RemovedOn:str = obj["RemovedOn"]
      """  RemovedOn  """  
      self.HoldSysRowID:str = obj["HoldSysRowID"]
      """  HoldSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpHoldAttachmentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.HoldAttachID:int = obj["HoldAttachID"]
      """  Unique ID of the hold attachment  """  
      self.CreateUserID:str = obj["CreateUserID"]
      """  user, created the hold attachment  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.HoldSysRowID:str = obj["HoldSysRowID"]
      """  HoldSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpHoldTypeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.SystemCode:str = obj["SystemCode"]
      """  Code that identifies the system (ex. ICE)  """  
      self.ClassName:str = obj["ClassName"]
      """  Hold Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Hold Namespace  """  
      self.DataTableID:str = obj["DataTableID"]
      """  Data Table  """  
      self.Description:str = obj["Description"]
      """  Hold Description  """  
      self.HistoryLength:int = obj["HistoryLength"]
      """  Defines how many holds are stored in history  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_BpHoldTypeListTableset:
   def __init__(self, obj):
      self.BpHoldTypeList:list[Ice_Tablesets_BpHoldTypeListRow] = obj["BpHoldTypeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_BpHoldTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.HoldTypeID:str = obj["HoldTypeID"]
      """  Unique ID of the hold type  """  
      self.SystemCode:str = obj["SystemCode"]
      """  Code that identifies the system (ex. ICE)  """  
      self.ClassName:str = obj["ClassName"]
      """  Hold Class Name  """  
      self.ObjectNS:str = obj["ObjectNS"]
      """  Hold Namespace  """  
      self.DataTableID:str = obj["DataTableID"]
      """  Data Table  """  
      self.Description:str = obj["Description"]
      """  Hold Description  """  
      self.HistoryLength:int = obj["HistoryLength"]
      """  Defines how many holds are stored in history  """  
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

class Ice_Tablesets_BpHoldsTableset:
   def __init__(self, obj):
      self.BpHoldType:list[Ice_Tablesets_BpHoldTypeRow] = obj["BpHoldType"]
      self.BpHoldAttachHist:list[Ice_Tablesets_BpHoldAttachHistRow] = obj["BpHoldAttachHist"]
      self.BpHoldAttachment:list[Ice_Tablesets_BpHoldAttachmentRow] = obj["BpHoldAttachment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtBpHoldsTableset:
   def __init__(self, obj):
      self.BpHoldType:list[Ice_Tablesets_BpHoldTypeRow] = obj["BpHoldType"]
      self.BpHoldAttachHist:list[Ice_Tablesets_BpHoldAttachHistRow] = obj["BpHoldAttachHist"]
      self.BpHoldAttachment:list[Ice_Tablesets_BpHoldAttachmentRow] = obj["BpHoldAttachment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBpHoldsTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtBpHoldsTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_BpHoldsTableset] = obj["ds"]
      pass

      """  output parameters  """  

