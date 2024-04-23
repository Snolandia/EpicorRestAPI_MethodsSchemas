import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PurAgentSvc
# Description: Purchasing Agent
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PurAgents(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurAgents items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurAgents
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurAgentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents",headers=creds) as resp:
           return await resp.json()

async def post_PurAgents(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurAgents
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurAgentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurAgentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurAgents_Company_BuyerID(Company, BuyerID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurAgent item
   Description: Calls GetByID to retrieve the PurAgent item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurAgent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurAgentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurAgents_Company_BuyerID(Company, BuyerID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurAgent for the service
   Description: Calls UpdateExt to update PurAgent. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurAgent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurAgentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurAgents_Company_BuyerID(Company, BuyerID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurAgent item
   Description: Call UpdateExt to delete PurAgent item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurAgent
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurAgents_Company_BuyerID_PurAuths(Company, BuyerID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurAuths items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurAuths1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")/PurAuths",headers=creds) as resp:
           return await resp.json()

async def get_PurAgents_Company_BuyerID_PurAuths_Company_BuyerID_DcdUserID(Company, BuyerID, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurAuth item
   Description: Calls GetByID to retrieve the PurAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurAuth1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")/PurAuths(" + Company + "," + BuyerID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurAgents_Company_BuyerID_PurAgentAttches(Company, BuyerID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurAgentAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurAgentAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurAgentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")/PurAgentAttches",headers=creds) as resp:
           return await resp.json()

async def get_PurAgents_Company_BuyerID_PurAgentAttches_Company_BuyerID_DrawingSeq(Company, BuyerID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurAgentAttch item
   Description: Calls GetByID to retrieve the PurAgentAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurAgentAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurAgentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgents(" + Company + "," + BuyerID + ")/PurAgentAttches(" + Company + "," + BuyerID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurAuths(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurAuths items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurAuths
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAuths",headers=creds) as resp:
           return await resp.json()

async def post_PurAuths(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurAuths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurAuthRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurAuthRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAuths", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurAuths_Company_BuyerID_DcdUserID(Company, BuyerID, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurAuth item
   Description: Calls GetByID to retrieve the PurAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAuths(" + Company + "," + BuyerID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurAuths_Company_BuyerID_DcdUserID(Company, BuyerID, DcdUserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurAuth for the service
   Description: Calls UpdateExt to update PurAuth. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurAuthRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAuths(" + Company + "," + BuyerID + "," + DcdUserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurAuths_Company_BuyerID_DcdUserID(Company, BuyerID, DcdUserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurAuth item
   Description: Call UpdateExt to delete PurAuth item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAuths(" + Company + "," + BuyerID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurAgentAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurAgentAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurAgentAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurAgentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgentAttches",headers=creds) as resp:
           return await resp.json()

async def post_PurAgentAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurAgentAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurAgentAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurAgentAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgentAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurAgentAttches_Company_BuyerID_DrawingSeq(Company, BuyerID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurAgentAttch item
   Description: Calls GetByID to retrieve the PurAgentAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurAgentAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurAgentAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgentAttches(" + Company + "," + BuyerID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurAgentAttches_Company_BuyerID_DrawingSeq(Company, BuyerID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurAgentAttch for the service
   Description: Calls UpdateExt to update PurAgentAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurAgentAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurAgentAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgentAttches(" + Company + "," + BuyerID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurAgentAttches_Company_BuyerID_DrawingSeq(Company, BuyerID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurAgentAttch item
   Description: Call UpdateExt to delete PurAgentAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurAgentAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BuyerID: Desc: BuyerID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/PurAgentAttches(" + Company + "," + BuyerID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurAgentListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePurAgent, whereClausePurAgentAttch, whereClausePurAuth, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePurAgent=" + whereClausePurAgent
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurAgentAttch=" + whereClausePurAgentAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurAuth=" + whereClausePurAuth
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(buyerID, epicorHeaders = None):
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
   params += "buyerID=" + buyerID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConData
   Description: Gets the person contact information.
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedofAuthUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedofAuthUser
   Description: Set the EnableDefaultBuyer flag
   OperationID: OnChangedofAuthUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedofAuthUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedofAuthUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIsPrimaryUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIsPrimaryUser
   Description: Set the EnableDefaultBuyer flag to no on all PurAuth records except for
the one that meets the parameters passed in as it is the primary user.
   OperationID: OnChangeIsPrimaryUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIsPrimaryUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIsPrimaryUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListCustom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListCustom
   Description: This overload of GetList adds Buyers which are authorized for current user.
   OperationID: GetListCustom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListCustom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListCustom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurAgent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurAgent
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurAgentAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurAgentAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurAgentAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurAgentAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurAgentAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurAuth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurAuth
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurAuth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurAuth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurAuth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurAgentSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurAgentAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurAgentAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurAgentListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurAgentListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurAgentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurAgentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurAuthRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurAuthRow] = obj["value"]
      pass

class Erp_Tablesets_PurAgentAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BuyerID:str = obj["BuyerID"]
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

class Erp_Tablesets_PurAgentListRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. This can be used in place of deleting the master.  Inactive records are not displayed in data entry selection lists/browses.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Descriptive code assigned by user which uniquely identifies a purchase agent (buyer) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Name:str = obj["Name"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.ApprovalPerson:str = obj["ApprovalPerson"]
      """  The user id of the default  person who approves purchases for this buyer when their purchasing limit is exceeded.  This can reference users who are approvers (UserFile.CanApprovePO = Yes)  """  
      self.POLimit:int = obj["POLimit"]
      """  The purchasing limit for the purchase agent (buyer).  If a PO exceeds this limit then it will need to be approved before it can be printed.  A limit of zero is considers as no limit.  """  
      self.ApprovalName:str = obj["ApprovalName"]
      self.IsDCDUserIDAuthorized:bool = obj["IsDCDUserIDAuthorized"]
      """  Yes if the current DCDUserID is authorized for this Buyer ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsPrimaryUser:bool = obj["IsPrimaryUser"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurAgentRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. This can be used in place of deleting the master.  Inactive records are not displayed in data entry selection lists/browses.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Descriptive code assigned by user which uniquely identifies a purchase agent (buyer) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Name:str = obj["Name"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.ApprovalPerson:str = obj["ApprovalPerson"]
      """  The user id of the default  person who approves purchases for this buyer when their purchasing limit is exceeded.  This can reference users who are approvers (UserFile.CanApprovePO = Yes)  """  
      self.POLimit:int = obj["POLimit"]
      """  The purchasing limit for the purchase agent (buyer).  If a PO exceeds this limit then it will need to be approved before it can be printed.  A limit of zero is considers as no limit.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the purchase agent  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      """  Purchasing Requisitions that need approval from this buyer will  be sent to the Consolidated Purchasing company for approval.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemDefault:bool = obj["IsSystemDefault"]
      self.ApprovalName:str = obj["ApprovalName"]
      """  Name of Approval Person  """  
      self.IsDCDUserIDAuthorized:bool = obj["IsDCDUserIDAuthorized"]
      """  Yes if the current DCDUserID is authorized for this Buyer ID.  """  
      self.PerConName:str = obj["PerConName"]
      """  The name for the person contact.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurAuthRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID of the related PurAgent record.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID of the related UserFile record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsPrimaryUser:bool = obj["IsPrimaryUser"]
      self.Name:str = obj["Name"]
      self.EnableDefaultBuyer:bool = obj["EnableDefaultBuyer"]
      """  Set to true if there is a UserComp record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   buyerID
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PurAgentAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BuyerID:str = obj["BuyerID"]
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

class Erp_Tablesets_PurAgentListRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. This can be used in place of deleting the master.  Inactive records are not displayed in data entry selection lists/browses.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Descriptive code assigned by user which uniquely identifies a purchase agent (buyer) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Name:str = obj["Name"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.ApprovalPerson:str = obj["ApprovalPerson"]
      """  The user id of the default  person who approves purchases for this buyer when their purchasing limit is exceeded.  This can reference users who are approvers (UserFile.CanApprovePO = Yes)  """  
      self.POLimit:int = obj["POLimit"]
      """  The purchasing limit for the purchase agent (buyer).  If a PO exceeds this limit then it will need to be approved before it can be printed.  A limit of zero is considers as no limit.  """  
      self.ApprovalName:str = obj["ApprovalName"]
      self.IsDCDUserIDAuthorized:bool = obj["IsDCDUserIDAuthorized"]
      """  Yes if the current DCDUserID is authorized for this Buyer ID.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsPrimaryUser:bool = obj["IsPrimaryUser"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurAgentListTableset:
   def __init__(self, obj):
      self.PurAgentList:list[Erp_Tablesets_PurAgentListRow] = obj["PurAgentList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PurAgentRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to indicate the record is inactive. This can be used in place of deleting the master.  Inactive records are not displayed in data entry selection lists/browses.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Descriptive code assigned by user which uniquely identifies a purchase agent (buyer) master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Name:str = obj["Name"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.ApprovalPerson:str = obj["ApprovalPerson"]
      """  The user id of the default  person who approves purchases for this buyer when their purchasing limit is exceeded.  This can reference users who are approvers (UserFile.CanApprovePO = Yes)  """  
      self.POLimit:int = obj["POLimit"]
      """  The purchasing limit for the purchase agent (buyer).  If a PO exceeds this limit then it will need to be approved before it can be printed.  A limit of zero is considers as no limit.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the purchase agent  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      """  Purchasing Requisitions that need approval from this buyer will  be sent to the Consolidated Purchasing company for approval.  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsSystemDefault:bool = obj["IsSystemDefault"]
      self.ApprovalName:str = obj["ApprovalName"]
      """  Name of Approval Person  """  
      self.IsDCDUserIDAuthorized:bool = obj["IsDCDUserIDAuthorized"]
      """  Yes if the current DCDUserID is authorized for this Buyer ID.  """  
      self.PerConName:str = obj["PerConName"]
      """  The name for the person contact.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurAgentTableset:
   def __init__(self, obj):
      self.PurAgent:list[Erp_Tablesets_PurAgentRow] = obj["PurAgent"]
      self.PurAgentAttch:list[Erp_Tablesets_PurAgentAttchRow] = obj["PurAgentAttch"]
      self.PurAuth:list[Erp_Tablesets_PurAuthRow] = obj["PurAuth"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PurAuthRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer ID of the related PurAgent record.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID of the related UserFile record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IsPrimaryUser:bool = obj["IsPrimaryUser"]
      self.Name:str = obj["Name"]
      self.EnableDefaultBuyer:bool = obj["EnableDefaultBuyer"]
      """  Set to true if there is a UserComp record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BuyerIDName:str = obj["BuyerIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPurAgentTableset:
   def __init__(self, obj):
      self.PurAgent:list[Erp_Tablesets_PurAgentRow] = obj["PurAgent"]
      self.PurAgentAttch:list[Erp_Tablesets_PurAgentAttchRow] = obj["PurAgentAttch"]
      self.PurAuth:list[Erp_Tablesets_PurAuthRow] = obj["PurAuth"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   buyerID
   """  
   def __init__(self, obj):
      self.buyerID:str = obj["buyerID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurAgentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurAgentTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurAgentTableset] = obj["returnObj"]
      pass

class GetListCustom_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   customClause
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The search criteria  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      self.customClause:str = obj["customClause"]
      """  Custom WhereClause  """  
      pass

class GetListCustom_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurAgentListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.returnObj:list[Erp_Tablesets_PurAgentListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPurAgentAttch_input:
   """ Required : 
   ds
   buyerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      self.buyerID:str = obj["buyerID"]
      pass

class GetNewPurAgentAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurAgent_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

class GetNewPurAgent_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurAuth_input:
   """ Required : 
   ds
   buyerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      self.buyerID:str = obj["buyerID"]
      pass

class GetNewPurAuth_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPerConData_input:
   """ Required : 
   perConID
   ds
   """  
   def __init__(self, obj):
      self.perConID:int = obj["perConID"]
      """  Person Contact ID  """  
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

class GetPerConData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePurAgent
   whereClausePurAgentAttch
   whereClausePurAuth
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePurAgent:str = obj["whereClausePurAgent"]
      self.whereClausePurAgentAttch:str = obj["whereClausePurAgentAttch"]
      self.whereClausePurAuth:str = obj["whereClausePurAuth"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurAgentTableset] = obj["returnObj"]
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

class OnChangeIsPrimaryUser_input:
   """ Required : 
   BuyerID
   DCDUserID
   ds
   """  
   def __init__(self, obj):
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer for this user.  """  
      self.DCDUserID:str = obj["DCDUserID"]
      """  Authorized user ID.  """  
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

class OnChangeIsPrimaryUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedofAuthUser_input:
   """ Required : 
   BuyerID
   DCDUserID
   ds
   """  
   def __init__(self, obj):
      self.BuyerID:str = obj["BuyerID"]
      """  Buyer for this user.  """  
      self.DCDUserID:str = obj["DCDUserID"]
      """  Authorized user ID.  """  
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

class OnChangedofAuthUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPurAgentTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPurAgentTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurAgentTableset] = obj["ds"]
      pass

      """  output parameters  """  

