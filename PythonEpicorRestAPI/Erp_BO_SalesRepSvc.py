import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SalesRepSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SalesReps(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesReps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesReps
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesRepRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps",headers=creds) as resp:
           return await resp.json()

async def post_SalesReps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesReps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesRepRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesRepRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesReps_Company_SalesRepCode(Company, SalesRepCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesRep item
   Description: Calls GetByID to retrieve the SalesRep item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesRep
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesRepRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesReps_Company_SalesRepCode(Company, SalesRepCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesRep for the service
   Description: Calls UpdateExt to update SalesRep. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesRep
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesRepRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesReps_Company_SalesRepCode(Company, SalesRepCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesRep item
   Description: Call UpdateExt to delete SalesRep item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesRep
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesReps_Company_SalesRepCode_SaleAuths(Company, SalesRepCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SaleAuths items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SaleAuths1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SaleAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")/SaleAuths",headers=creds) as resp:
           return await resp.json()

async def get_SalesReps_Company_SalesRepCode_SaleAuths_Company_SalesRepCode_DcdUserID(Company, SalesRepCode, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SaleAuth item
   Description: Calls GetByID to retrieve the SaleAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SaleAuth1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SaleAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")/SaleAuths(" + Company + "," + SalesRepCode + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesReps_Company_SalesRepCode_SalesRepAttches(Company, SalesRepCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get SalesRepAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_SalesRepAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesRepAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")/SalesRepAttches",headers=creds) as resp:
           return await resp.json()

async def get_SalesReps_Company_SalesRepCode_SalesRepAttches_Company_SalesRepCode_DrawingSeq(Company, SalesRepCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesRepAttch item
   Description: Calls GetByID to retrieve the SalesRepAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesRepAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesRepAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesReps(" + Company + "," + SalesRepCode + ")/SalesRepAttches(" + Company + "," + SalesRepCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_SaleAuths(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SaleAuths items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SaleAuths
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SaleAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SaleAuths",headers=creds) as resp:
           return await resp.json()

async def post_SaleAuths(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SaleAuths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SaleAuthRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SaleAuthRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SaleAuths", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SaleAuths_Company_SalesRepCode_DcdUserID(Company, SalesRepCode, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SaleAuth item
   Description: Calls GetByID to retrieve the SaleAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SaleAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SaleAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SaleAuths(" + Company + "," + SalesRepCode + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SaleAuths_Company_SalesRepCode_DcdUserID(Company, SalesRepCode, DcdUserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SaleAuth for the service
   Description: Calls UpdateExt to update SaleAuth. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SaleAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SaleAuthRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SaleAuths(" + Company + "," + SalesRepCode + "," + DcdUserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SaleAuths_Company_SalesRepCode_DcdUserID(Company, SalesRepCode, DcdUserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SaleAuth item
   Description: Call UpdateExt to delete SaleAuth item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SaleAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SaleAuths(" + Company + "," + SalesRepCode + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_SalesRepAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SalesRepAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SalesRepAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesRepAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesRepAttches",headers=creds) as resp:
           return await resp.json()

async def post_SalesRepAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SalesRepAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SalesRepAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SalesRepAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesRepAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SalesRepAttches_Company_SalesRepCode_DrawingSeq(Company, SalesRepCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SalesRepAttch item
   Description: Calls GetByID to retrieve the SalesRepAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SalesRepAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SalesRepAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesRepAttches(" + Company + "," + SalesRepCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SalesRepAttches_Company_SalesRepCode_DrawingSeq(Company, SalesRepCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SalesRepAttch for the service
   Description: Calls UpdateExt to update SalesRepAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SalesRepAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SalesRepAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesRepAttches(" + Company + "," + SalesRepCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SalesRepAttches_Company_SalesRepCode_DrawingSeq(Company, SalesRepCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SalesRepAttch item
   Description: Call UpdateExt to delete SalesRepAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SalesRepAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param SalesRepCode: Desc: SalesRepCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/SalesRepAttches(" + Company + "," + SalesRepCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SalesRepListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSalesRep, whereClauseSalesRepAttch, whereClauseSaleAuth, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSalesRep=" + whereClauseSalesRep
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSalesRepAttch=" + whereClauseSalesRepAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseSaleAuth=" + whereClauseSaleAuth
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(salesRepCode, epicorHeaders = None):
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
   params += "salesRepCode=" + salesRepCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_DefaultDefaultUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultDefaultUser
   Description: Used to determine the default setting for the DefaultUser flag when creating
a new SaleAuth record. This method can be called after the SaleAuth.DCDUserId
field has been assigned but prior to calling the Update method.
Will return as true when
1. SalesRep is not already a default for a user and
2. The user does not have a primary salesrep.
   OperationID: DefaultDefaultUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultDefaultUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultDefaultUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConData
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUserID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUserID
   Description: This method should be called when the Terms Code changes.
   OperationID: OnChangeUserID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUserID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUserID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesRep(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesRep
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesRep
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesRep_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesRep_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalesRepAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalesRepAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSalesRepAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalesRepAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalesRepAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSaleAuth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSaleAuth
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSaleAuth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSaleAuth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSaleAuth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SalesRepSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SaleAuthRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SaleAuthRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesRepAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesRepListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SalesRepRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SalesRepRow] = obj["value"]
      pass

class Erp_Tablesets_SaleAuthRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales Rep that this record is linked to.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID that will be able to access the related SalesRep's information.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultUser:bool = obj["DefaultUser"]
      self.BitFlag:int = obj["BitFlag"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      self.UserIDName:str = obj["UserIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesRepAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SalesRepCode:str = obj["SalesRepCode"]
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

class Erp_Tablesets_SalesRepListRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to determine whether or not this individual appears in selection lists.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  A unique identifier of this individual assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesRepRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to determine whether or not this individual appears in selection lists.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  A unique identifier of this individual assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.CommissionPercent:int = obj["CommissionPercent"]
      """  The default commission percent for this individual that is used as the default in Order Entry and Invoicing.  """  
      self.CommissionEarnedAt:bool = obj["CommissionEarnedAt"]
      """  Indicates when commissions are considered as earned.  """  
      self.AlertFlag:bool = obj["AlertFlag"]
      """  Determines whether or not this individual will receive email alert messages.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.OfficePhoneNum:str = obj["OfficePhoneNum"]
      """  The individual's office phone Number.  """  
      self.FaxPhoneNum:str = obj["FaxPhoneNum"]
      """  The individual's fax number.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The individual's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The individual's pager number.  """  
      self.HomePhoneNum:str = obj["HomePhoneNum"]
      """  The individual's home phone number.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  the individual's email address.  """  
      self.SalesRepTitle:str = obj["SalesRepTitle"]
      """  The individual's title.  """  
      self.RepReportsTo:str = obj["RepReportsTo"]
      """  The SalesRep.SalesRepCode value of the person that this individual reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific individual.  """  
      self.SalesMgrConfidence:int = obj["SalesMgrConfidence"]
      """  The Sales Manager's confidence factor, entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders.  Not viewable by the individual sales reps.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Roles can be used to assign Tasks.  """  
      self.ViewAllTer:bool = obj["ViewAllTer"]
      """  Setting this flag will give the individual the ability to view all territories when searching customers and opportunities.  This is only valid for the primary user for the salesperson.  """  
      self.ViewCompPipe:bool = obj["ViewCompPipe"]
      """  Setting this flag will give this individual the ability to view the entire company when rolling up quota and pipeline information.  This is only valid for the primary user for the salesperson.  """  
      self.WebSaleGetsCommission:bool = obj["WebSaleGetsCommission"]
      """  Does a sale that originated via Customer Connect garner a Commission?  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.MgrWorstCsPct:int = obj["MgrWorstCsPct"]
      """  The Sales Manager's worst case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  """  
      self.MgrBestCsPct:int = obj["MgrBestCsPct"]
      """  The Sales Manager's best case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebSalesRep:bool = obj["WebSalesRep"]
      """  This salesperson has access to ECC  """  
      self.ECCSalesRepCode:str = obj["ECCSalesRepCode"]
      """  Addisonal ECC ID this salesperson may be related to.  """  
      self.PerConName:str = obj["PerConName"]
      """  Full name of the contact.  """  
      self.RepReportsToName:str = obj["RepReportsToName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DefaultDefaultUser_input:
   """ Required : 
   SalesRepCode
   DCDUserID
   """  
   def __init__(self, obj):
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.DCDUserID:str = obj["DCDUserID"]
      pass

class DefaultDefaultUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.DefaultUser:bool = obj["DefaultUser"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   salesRepCode
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SaleAuthRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The Sales Rep that this record is linked to.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID that will be able to access the related SalesRep's information.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DefaultUser:bool = obj["DefaultUser"]
      self.BitFlag:int = obj["BitFlag"]
      self.SalesRepCodeName:str = obj["SalesRepCodeName"]
      self.UserIDName:str = obj["UserIDName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesRepAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.SalesRepCode:str = obj["SalesRepCode"]
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

class Erp_Tablesets_SalesRepListRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to determine whether or not this individual appears in selection lists.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  A unique identifier of this individual assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesRepListTableset:
   def __init__(self, obj):
      self.SalesRepList:list[Erp_Tablesets_SalesRepListRow] = obj["SalesRepList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SalesRepRow:
   def __init__(self, obj):
      self.InActive:bool = obj["InActive"]
      """  Used to determine whether or not this individual appears in selection lists.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  A unique identifier of this individual assigned by the user.  """  
      self.Name:str = obj["Name"]
      """  Name  """  
      self.CommissionPercent:int = obj["CommissionPercent"]
      """  The default commission percent for this individual that is used as the default in Order Entry and Invoicing.  """  
      self.CommissionEarnedAt:bool = obj["CommissionEarnedAt"]
      """  Indicates when commissions are considered as earned.  """  
      self.AlertFlag:bool = obj["AlertFlag"]
      """  Determines whether or not this individual will receive email alert messages.  """  
      self.Address1:str = obj["Address1"]
      """  Address line 1  """  
      self.Address2:str = obj["Address2"]
      """  Address line 2  """  
      self.Address3:str = obj["Address3"]
      """  Address line 3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.State:str = obj["State"]
      """  State/Province  """  
      self.Zip:str = obj["Zip"]
      """  Zip/Postal Code  """  
      self.Country:str = obj["Country"]
      """  Country is used as part of the mailing address. It can be left blank.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  The Country.CountryNum value related to the SalesRep.Country value.  """  
      self.OfficePhoneNum:str = obj["OfficePhoneNum"]
      """  The individual's office phone Number.  """  
      self.FaxPhoneNum:str = obj["FaxPhoneNum"]
      """  The individual's fax number.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The individual's cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The individual's pager number.  """  
      self.HomePhoneNum:str = obj["HomePhoneNum"]
      """  The individual's home phone number.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  the individual's email address.  """  
      self.SalesRepTitle:str = obj["SalesRepTitle"]
      """  The individual's title.  """  
      self.RepReportsTo:str = obj["RepReportsTo"]
      """  The SalesRep.SalesRepCode value of the person that this individual reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific individual.  """  
      self.SalesMgrConfidence:int = obj["SalesMgrConfidence"]
      """  The Sales Manager's confidence factor, entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders.  Not viewable by the individual sales reps.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Roles can be used to assign Tasks.  """  
      self.ViewAllTer:bool = obj["ViewAllTer"]
      """  Setting this flag will give the individual the ability to view all territories when searching customers and opportunities.  This is only valid for the primary user for the salesperson.  """  
      self.ViewCompPipe:bool = obj["ViewCompPipe"]
      """  Setting this flag will give this individual the ability to view the entire company when rolling up quota and pipeline information.  This is only valid for the primary user for the salesperson.  """  
      self.WebSaleGetsCommission:bool = obj["WebSaleGetsCommission"]
      """  Does a sale that originated via Customer Connect garner a Commission?  """  
      self.CnvEmpID:str = obj["CnvEmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      """  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's Website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.MgrWorstCsPct:int = obj["MgrWorstCsPct"]
      """  The Sales Manager's worst case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  """  
      self.MgrBestCsPct:int = obj["MgrBestCsPct"]
      """  The Sales Manager's best case confidence factor entered as a percentage, that this Sales Rep's leads, opportunities or quotes will be turned into actual sales orders. Not viewable by the individual sales reps.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WebSalesRep:bool = obj["WebSalesRep"]
      """  This salesperson has access to ECC  """  
      self.ECCSalesRepCode:str = obj["ECCSalesRepCode"]
      """  Addisonal ECC ID this salesperson may be related to.  """  
      self.PerConName:str = obj["PerConName"]
      """  Full name of the contact.  """  
      self.RepReportsToName:str = obj["RepReportsToName"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SalesRepTableset:
   def __init__(self, obj):
      self.SalesRep:list[Erp_Tablesets_SalesRepRow] = obj["SalesRep"]
      self.SalesRepAttch:list[Erp_Tablesets_SalesRepAttchRow] = obj["SalesRepAttch"]
      self.SaleAuth:list[Erp_Tablesets_SaleAuthRow] = obj["SaleAuth"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSalesRepTableset:
   def __init__(self, obj):
      self.SalesRep:list[Erp_Tablesets_SalesRepRow] = obj["SalesRep"]
      self.SalesRepAttch:list[Erp_Tablesets_SalesRepAttchRow] = obj["SalesRepAttch"]
      self.SaleAuth:list[Erp_Tablesets_SaleAuthRow] = obj["SaleAuth"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   salesRepCode
   """  
   def __init__(self, obj):
      self.salesRepCode:str = obj["salesRepCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesRepTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesRepTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesRepTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SalesRepListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSaleAuth_input:
   """ Required : 
   ds
   salesRepCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      self.salesRepCode:str = obj["salesRepCode"]
      pass

class GetNewSaleAuth_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesRepAttch_input:
   """ Required : 
   ds
   salesRepCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      self.salesRepCode:str = obj["salesRepCode"]
      pass

class GetNewSalesRepAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalesRep_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

class GetNewSalesRep_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPerConData_input:
   """ Required : 
   PerConID
   ds
   """  
   def __init__(self, obj):
      self.PerConID:int = obj["PerConID"]
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

class GetPerConData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSalesRep
   whereClauseSalesRepAttch
   whereClauseSaleAuth
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSalesRep:str = obj["whereClauseSalesRep"]
      self.whereClauseSalesRepAttch:str = obj["whereClauseSalesRepAttch"]
      self.whereClauseSaleAuth:str = obj["whereClauseSaleAuth"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SalesRepTableset] = obj["returnObj"]
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

class OnChangeUserID_input:
   """ Required : 
   SalesRepCode
   NewUserID
   ds
   """  
   def __init__(self, obj):
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.NewUserID:str = obj["NewUserID"]
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

class OnChangeUserID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesRepTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSalesRepTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SalesRepTableset] = obj["ds"]
      pass

      """  output parameters  """  

