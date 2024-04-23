import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.NonConfSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_NonConfs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NonConfs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NonConfs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs",headers=creds) as resp:
           return await resp.json()

async def post_NonConfs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NonConfs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NonConfRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NonConfRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NonConfs_Company_TranID(Company, TranID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NonConf item
   Description: Calls GetByID to retrieve the NonConf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonConf
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NonConfRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NonConfs_Company_TranID(Company, TranID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NonConf for the service
   Description: Calls UpdateExt to update NonConf. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NonConf
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NonConfRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NonConfs_Company_TranID(Company, TranID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NonConf item
   Description: Call UpdateExt to delete NonConf item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NonConf
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")",headers=creds) as resp:
           return await resp.json()

async def get_NonConfs_Company_TranID_NonConfAttches(Company, TranID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get NonConfAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_NonConfAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")/NonConfAttches",headers=creds) as resp:
           return await resp.json()

async def get_NonConfs_Company_TranID_NonConfAttches_Company_TranID_DrawingSeq(Company, TranID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NonConfAttch item
   Description: Calls GetByID to retrieve the NonConfAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonConfAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfs(" + Company + "," + TranID + ")/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_NonConfAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NonConfAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NonConfAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches",headers=creds) as resp:
           return await resp.json()

async def post_NonConfAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NonConfAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NonConfAttches_Company_TranID_DrawingSeq(Company, TranID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NonConfAttch item
   Description: Calls GetByID to retrieve the NonConfAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NonConfAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NonConfAttches_Company_TranID_DrawingSeq(Company, TranID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NonConfAttch for the service
   Description: Calls UpdateExt to update NonConfAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NonConfAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NonConfAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NonConfAttches_Company_TranID_DrawingSeq(Company, TranID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NonConfAttch item
   Description: Call UpdateExt to delete NonConfAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NonConfAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranID: Desc: TranID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/NonConfAttches(" + Company + "," + TranID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumGenOpts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumGenOpts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumGenOpts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumGenOpts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumGenOpt item
   Description: Calls GetByID to retrieve the LegalNumGenOpt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumGenOpt for the service
   Description: Calls UpdateExt to update LegalNumGenOpt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumGenOptsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumGenOpts_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumGenOpt item
   Description: Call UpdateExt to delete LegalNumGenOpt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumGenOpt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/LegalNumGenOpts(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SelectedSerialNumbers(" + Company + "," + PartNum + "," + SerialNumber + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/SNFormats(" + Company + "," + PartNum + "," + Plant + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NonConfListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseNonConf, whereClauseNonConfAttch, whereClauseLegalNumGenOpts, whereClauseSelectedSerialNumbers, whereClauseSNFormat, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseNonConf=" + whereClauseNonConf
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseNonConfAttch=" + whereClauseNonConfAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumGenOpts=" + whereClauseLegalNumGenOpts
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tranID, epicorHeaders = None):
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
   params += "tranID=" + tranID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AddNewNonConfRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNewNonConfRow
   Description: Add NonConf of a certain type.  Valid types are Operation, Inventory, JobMaterial, SubContract, and Other.
Since Update() disallows changes to the TrnTyp field, you MUST use this instead of GetNewNonConf().
This method added to call from Kinetic UI
   OperationID: AddNewNonConfRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNewNonConfRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNewNonConfRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddNonConf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddNonConf
   Description: Add NonConf of a certain type.  Valid types are Operation, Inventory, JobMaterial, SubContract, and Other.
Since Update() disallows changes to the TrnTyp field, you MUST use this instead of GetNewNonConf().
   OperationID: AddNonConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddNonConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddNonConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChkPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChkPartXRefInfo
   Description: This method checks whether a cross-reference exists for the new part.
It should be executed when the Part number changed.
   OperationID: ChkPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChkPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChkPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Get_PartRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Get_PartRev
   Description: Get the latest Revision (as of TODAY) for the given Part.
   OperationID: Get_PartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Get_PartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Get_PartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableQty
   Description: Get the available quantity for the part/warehouse/bin/dim code/lot.
   OperationID: GetAvailableQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlQueueSeqValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlQueueSeqValue
   Description: Search for the MtlQueueSeq value from the MtlQueue row related to the current Non Conformance.
   OperationID: GetMtlQueueSeqValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlQueueSeqValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlQueueSeqValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMtlSources(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMtlSources
   Description: To retrieve the list of possible Material Sources for the given Job Material, as a dataset, to
facilitate presenting them to the user to pick one.  See the Pick Material Source dialog in
v6.10 (qae10-ml.w).
The purpose of determining the material source is to set NonConf.VendorNum and NonConf.PurPoint
in the case where the tranType = "PUR-MTL".
The user's selection of one of these should be stored in the NonConf.MtlSourceTrnType field
(i.e. NonConf.MtlSourceTrnType = NonConfSource.TrnType).
Note that in v6.10, the user is only presented with the dialog if the Job Material has
more than one possible source.  To support that behavior, this routine sets the output parameter
pcMtlSourceTrnType to the PartTran.TranType when it is unambiguous.
   OperationID: GetMtlSources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMtlSources_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMtlSources_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartInfo
   Description: For a given Part Number, retrieve the current Revision, Unit of Measure, Default Warehouse,
and whether it is tracked by Lot, and/or Dimension.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
   OperationID: GetPartInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartTranPKs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartTranPKs
   Description: Returns primary keys of the part transaction related to the particular non conformance.
   OperationID: GetPartTranPKs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartTranPKs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartTranPKs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbers(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbers
   Description: This method will populate the SelectedSerialNumber datatable for the Non Conf RowIdent.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectedSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectedSerialNumbersParams
   Description: This method will populate the SelectedSerialNumber datatable for the Non Conf RowIdent.
   OperationID: GetSelectedSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectedSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectedSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobAsm
   Description: This method validates the ProposedAssemblySeq, then updates the following assembly-related fields:
NonConf.PartNum
NonConf.PartNumPartDescription
NonConf.RevisionNum
NonConf.ScrapUM
NonConf.WarehouseCode
NonConf.BinNum
NonConf.PartNumTrackSerialNum
NonConf.PartNumTrackLots
NonConf.PartNumTrackDimension
NonConf.OprSeq
NonConf.MtlSeq
NonConf.ResourceID
NonConf.ResourceIDDescription
            
This method should be run when the NonConf.AssemblySeq field changes.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job Assembly exists with the given Assembly Sequence Number
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobMtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobMtl
   Description: This method validates the piProposedMtlSeq, then updates the following material-related fields:
NonConf.PartNum
NonConf.PartNumPartDescription
NonConf.RevisionNum
NonConf.ScrapUM
            
This method should be run when the NonConf.MtlSeq field changes.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job Material exists with the given MtlSeq Number
   OperationID: OnChangeJobMtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobMtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobMtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the JobNum, then updates the following Job-related fields:
PartNum, AssemblySeq, MtlSeq, OprSeq, ResourceID, ResourceIDDescription,
JobNumPartDescription, Plant
This method should be run when the NonConf.JobNum field changes.
            
If the Part related to the job has only one possible Assembly, the appropriate
assembly information is returned, and the plAsmReturned flag is returned as TRUE.  This
should be used to disable the Assembly Number field and lookup, if appropriate.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job exists with the given JobNum
- Job is not for current plant
- Job has been closed
- Job has not been released
- Job is for a service call that has been invoiced
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBinNum
   Description: Method validates bins - both to and from
   OperationID: OnChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWarehouseCode
   Description: Method validates warehouse codes - both to and from
   OperationID: OnChangeWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobOpr
   Description: This method validates the piProposedOprSeq, then updates the following operation-related fields:
NonConf.OprSeq
NonConf.WCCode
NonConf.WrkCntrDesc
NonConf.WarehouseCode
NonConf.WarehouseCodeDescription
NonConf.BinNum
            
This method should be run when the NonConf.OprSeq field changes.
            
Any time the Part has changed, the Lot-, Dimension-, and SerialNumber-tracking attributes
need to be checked, and corresponding fields enabled/disabled as appropriate.  Also, the
SelectedSerialNumbers dataset needs to be cleared out.
            
An exception is thrown if:
- No Job Operation exists with the given OprSeq Number
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranQty
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.TranQty changes.
This method performs validation on TranQty and sets the Issued Complete flag.
   OperationID: OnChangeTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUM
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.UM changes.
   OperationID: OnChangeUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromPCID
   Description: Validates that PCID exists
   OperationID: OnChangeFromPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToPCID
   Description: Validates that PCID exists
   OperationID: OnChangeToPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedCOPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedCOPartNum
   Description: Call this method after coPartnum changes
   OperationID: OnChangedCOPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedCOPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedCOPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method does:
1 - Returns a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReasonWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReasonWhereClause
   Description: Provides a WHERE clause for obtaining a list of Reason codes suitable for the given type of
NonConformance.  Valid types are Operation, Inventory, JobMaterial, SubContract, and Other.
   OperationID: GetReasonWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReasonWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReasonWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateQtyInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateQtyInventoryTest
   OperationID: ValidateQtyInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQtyInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQtyInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateQtyInventoryTestIncludingPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateQtyInventoryTestIncludingPCID
   OperationID: ValidateQtyInventoryTestIncludingPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateQtyInventoryTestIncludingPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateQtyInventoryTestIncludingPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNonConf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNonConf
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNonConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNonConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNonConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNonConfAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNonConfAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNonConfAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNonConfAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNonConfAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NonConfSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NonConfAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NonConfListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NonConfRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NonConfRow] = obj["value"]
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

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NonConfAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TranID:int = obj["TranID"]
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

class Erp_Tablesets_NonConfListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ScrapLaborCost:int = obj["ScrapLaborCost"]
      """  Scrap Labor Cost.  """  
      self.ScrapBurdenCost:int = obj["ScrapBurdenCost"]
      """  Scrap Burden Cost.  """  
      self.ScrapMaterialCost:int = obj["ScrapMaterialCost"]
      """  Scrap Material Cost.  """  
      self.ScrapMaterialBurCost:int = obj["ScrapMaterialBurCost"]
      """  Scrap Material Bur Cost.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.ScrapUM:str = obj["ScrapUM"]
      """  Defines the Unit of Measure used when part is scrapped.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  The conversion factor used to convert the material.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as a foreign key for LaborDtl record.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Contains comments about the transaction.  """  
      self.FldCommentText:str = obj["FldCommentText"]
      """  Contains comments about the transaction.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Non conformance warehosue code  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.ScrapSubCost:int = obj["ScrapSubCost"]
      """  Scrap Labor Cost.  """  
      self.QtyFrm:str = obj["QtyFrm"]
      """  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  """  
      self.TranID:int = obj["TranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.Plant:str = obj["Plant"]
      """   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Receipt Number of related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Disposition Number of related RMADisp record.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the Non-Conformance transaction.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Mtl Sub Unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Material  Burd unit component cost to date  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.MoveCostsToDMR:bool = obj["MoveCostsToDMR"]
      """   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.MtlSourceTrnType:str = obj["MtlSourceTrnType"]
      """  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WrkCntrDesc:str = obj["WrkCntrDesc"]
      """  Long description of the Work Center.  """  
      self.TrnTypDescription:str = obj["TrnTypDescription"]
      """  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.AllowNegQty:bool = obj["AllowNegQty"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.Closed:bool = obj["Closed"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.TranQty:int = obj["TranQty"]
      """  The ?Quantity? field converted to the UOM defined in the job material  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.InspectorIDName:str = obj["InspectorIDName"]
      """  Inspector's Full Name.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      """  Full description of Resource.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.ToWareHouseCodeDescDescription:str = obj["ToWareHouseCodeDescDescription"]
      """  Description.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NonConfRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ScrapLaborCost:int = obj["ScrapLaborCost"]
      """  Scrap Labor Cost.  """  
      self.ScrapBurdenCost:int = obj["ScrapBurdenCost"]
      """  Scrap Burden Cost.  """  
      self.ScrapMaterialCost:int = obj["ScrapMaterialCost"]
      """  Scrap Material Cost.  """  
      self.ScrapMaterialBurCost:int = obj["ScrapMaterialBurCost"]
      """  Scrap Material Bur Cost.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.ScrapUM:str = obj["ScrapUM"]
      """  Defines the Unit of Measure used when part is scrapped.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  The conversion factor used to convert the material.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as a foreign key for LaborDtl record.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Contains comments about the transaction.  """  
      self.FldCommentText:str = obj["FldCommentText"]
      """  Contains comments about the transaction.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Non conformance warehosue code  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.ScrapSubCost:int = obj["ScrapSubCost"]
      """  Scrap Labor Cost.  """  
      self.QtyFrm:str = obj["QtyFrm"]
      """  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  """  
      self.TranID:int = obj["TranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.Plant:str = obj["Plant"]
      """   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Receipt Number of related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Disposition Number of related RMADisp record.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the Non-Conformance transaction.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Mtl Sub Unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Material  Burd unit component cost to date  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.MoveCostsToDMR:bool = obj["MoveCostsToDMR"]
      """   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  Originating PCID.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      self.Closed:bool = obj["Closed"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation code for reporting operation  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  The operation reporting the nonconformance  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.MtlSourceTrnType:str = obj["MtlSourceTrnType"]
      """  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  """  
      self.ProcessID:str = obj["ProcessID"]
      """  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  """  
      self.TranQty:int = obj["TranQty"]
      """  The ?Quantity? field converted to the UOM defined in the job material  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.TrnTypDescription:str = obj["TrnTypDescription"]
      """  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  """  
      self.WrkCntrDesc:str = obj["WrkCntrDesc"]
      """  Long description of the Work Center.  """  
      self.AllowNegQty:bool = obj["AllowNegQty"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.JobProdAttrSearch:str = obj["JobProdAttrSearch"]
      """  Search filter for AttributeSetID from multiple JobProd records  """  
      self.MultipleJobProd:bool = obj["MultipleJobProd"]
      """  multiple jobprod flag  """  
      self.FromOpCodeOpDesc:str = obj["FromOpCodeOpDesc"]
      """  Operation Description  """  
      self.EnablePartNum:bool = obj["EnablePartNum"]
      """  True if TrnTyp = ‘I’ or TrnTyp = “D” (Operations) and co-parts exist for the job and AssemblySeq = 0 and it’s the final operation.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PlantName:str = obj["PlantName"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.ToBinNumDescription:str = obj["ToBinNumDescription"]
      self.ToWareHouseCodeDescDescription:str = obj["ToWareHouseCodeDescDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
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
class AddNewNonConfRow_input:
   """ Required : 
   pcNonConfType
   ds
   """  
   def __init__(self, obj):
      self.pcNonConfType:str = obj["pcNonConfType"]
      """  Type/origin of NonConformance.  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class AddNewNonConfRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class AddNonConf_input:
   """ Required : 
   pcNonConfType
   """  
   def __init__(self, obj):
      self.pcNonConfType:str = obj["pcNonConfType"]
      """  Type/origin of NonConformance.  """  
      pass

class AddNonConf_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NonConfTableset] = obj["returnObj"]
      pass

class ChkPartXRefInfo_input:
   """ Required : 
   newPartNum
   SysRowID
   rowType
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.newPartNum:str = obj["newPartNum"]
      """  New Part Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class ChkPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.newPartNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   tranID
   """  
   def __init__(self, obj):
      self.tranID:int = obj["tranID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NonConfAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TranID:int = obj["TranID"]
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

class Erp_Tablesets_NonConfListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ScrapLaborCost:int = obj["ScrapLaborCost"]
      """  Scrap Labor Cost.  """  
      self.ScrapBurdenCost:int = obj["ScrapBurdenCost"]
      """  Scrap Burden Cost.  """  
      self.ScrapMaterialCost:int = obj["ScrapMaterialCost"]
      """  Scrap Material Cost.  """  
      self.ScrapMaterialBurCost:int = obj["ScrapMaterialBurCost"]
      """  Scrap Material Bur Cost.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.ScrapUM:str = obj["ScrapUM"]
      """  Defines the Unit of Measure used when part is scrapped.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  The conversion factor used to convert the material.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as a foreign key for LaborDtl record.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Contains comments about the transaction.  """  
      self.FldCommentText:str = obj["FldCommentText"]
      """  Contains comments about the transaction.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Non conformance warehosue code  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.ScrapSubCost:int = obj["ScrapSubCost"]
      """  Scrap Labor Cost.  """  
      self.QtyFrm:str = obj["QtyFrm"]
      """  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  """  
      self.TranID:int = obj["TranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.Plant:str = obj["Plant"]
      """   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Receipt Number of related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Disposition Number of related RMADisp record.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the Non-Conformance transaction.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Mtl Sub Unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Material  Burd unit component cost to date  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.MoveCostsToDMR:bool = obj["MoveCostsToDMR"]
      """   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.MtlSourceTrnType:str = obj["MtlSourceTrnType"]
      """  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.WrkCntrDesc:str = obj["WrkCntrDesc"]
      """  Long description of the Work Center.  """  
      self.TrnTypDescription:str = obj["TrnTypDescription"]
      """  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.AllowNegQty:bool = obj["AllowNegQty"]
      self.AvailableQty:int = obj["AvailableQty"]
      self.Closed:bool = obj["Closed"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.TranQty:int = obj["TranQty"]
      """  The ?Quantity? field converted to the UOM defined in the job material  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  """  
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      """  Description for the Part on the assembly record.  This cannot be blank.  Use Part.Description as default if a valid Part record exists.  """  
      self.BinNumDescription:str = obj["BinNumDescription"]
      """  This field can be used to describe the physical location, dimensions or other attributes of the warehouse bin. It possibly could even be used to record a "Heat" number for an item. The description is optional and can be left blank.  """  
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      """  Description for the dimension code.  """  
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      """  Describes the Part.  System maintained, not user modifiable.  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.InspectorIDName:str = obj["InspectorIDName"]
      """  Inspector's Full Name.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      """  Describes the Part.  """  
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartNumIUM:str = obj["PartNumIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      """  Supplier Part Number  """  
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      """  Defaults from JobOper, JobMtl or Part depending on the reference to the job records.  If no job reference then uses the Part.PartDescription if it is a valid PartNum.  """  
      self.POLinePartNum:str = obj["POLinePartNum"]
      """  OUR internal Part number for this item.  """  
      self.PORelNumRefCodeDesc:str = obj["PORelNumRefCodeDesc"]
      """  (THIS SHOULD BE DELETED WITH SONOMA!) GL Reference Code description.  """  
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      """  Full description of Resource.  """  
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.ToWareHouseCodeDescDescription:str = obj["ToWareHouseCodeDescDescription"]
      """  Description.  """  
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorNumName:str = obj["VendorNumName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      """  First address line of the Supplier  """  
      self.VendorNumState:str = obj["VendorNumState"]
      """  Can be blank.  """  
      self.VendorNumCity:str = obj["VendorNumCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NonConfListTableset:
   def __init__(self, obj):
      self.NonConfList:list[Erp_Tablesets_NonConfListRow] = obj["NonConfList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_NonConfRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Quantity:int = obj["Quantity"]
      """  Quantity of the material to be scrapped.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Scrap reason code.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the JobAsmbl record.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  A sequence number that uniquely identifies the JobAsmbl record within the JobNum.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number which uniquely identifies the material record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.PartNum:str = obj["PartNum"]
      """  The field that identifies the Part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ScrapLaborCost:int = obj["ScrapLaborCost"]
      """  Scrap Labor Cost.  """  
      self.ScrapBurdenCost:int = obj["ScrapBurdenCost"]
      """  Scrap Burden Cost.  """  
      self.ScrapMaterialCost:int = obj["ScrapMaterialCost"]
      """  Scrap Material Cost.  """  
      self.ScrapMaterialBurCost:int = obj["ScrapMaterialBurCost"]
      """  Scrap Material Bur Cost.  """  
      self.TrnTyp:str = obj["TrnTyp"]
      """   Internal code to identify the type of non-conformance.
Valid codes are:
"F" - First Article
"D" - Defective assemblies
"I" - Inventory
"M" - Job Materials
"S" - Subcontract
"P" - Purchase Order
"R" - RMA receipt
"O" - Other.  """  
      self.DimCode:str = obj["DimCode"]
      """  Default dimension code for the part.  Set by selecting a PartDim record as default.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  The operation sequence of the Job/Assembly.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource.  """  
      self.Description:str = obj["Description"]
      """  Describes the Part.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user creates the new transaction.  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.ScrapUM:str = obj["ScrapUM"]
      """  Defines the Unit of Measure used when part is scrapped.  """  
      self.InspectedBy:str = obj["InspectedBy"]
      """  The ID of the person that did the inspection.  Defaults to current DCD-UserID when the item has been inspected.  """  
      self.InspectorID:str = obj["InspectorID"]
      """  The assigned Inspector ID that is going to perform the inspection. Assigned by the system using the current DCD-UserID when the item is being inspected.  Must be a valid Inspector ID, else it will be blank.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """  The conversion factor used to convert the material.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborDtl record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  Used as a foreign key for LaborDtl record.  """  
      self.PassedQty:int = obj["PassedQty"]
      """  Total quantity that passed inspection to date.  In receiving unit of measure.  This is a summary maintained by the DMR process.  """  
      self.FailedQty:int = obj["FailedQty"]
      """  Total to date quantity that has failed inspection.  This is a summary maintained by the DMR process.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.PsdCommentText:str = obj["PsdCommentText"]
      """  Contains comments about the transaction.  """  
      self.FldCommentText:str = obj["FldCommentText"]
      """  Contains comments about the transaction.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Supplier Purchase Point  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Non conformance warehosue code  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.ScrapSubCost:int = obj["ScrapSubCost"]
      """  Scrap Labor Cost.  """  
      self.QtyFrm:str = obj["QtyFrm"]
      """  Indicate if the record was created from issued material or manufactured material. Valid values are "WIP", "INV" or blank.  """  
      self.TranID:int = obj["TranID"]
      """  A unique number for the transaction.  Auto increment.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR Number to identify the DMR record.  Auto assign/increment starting at 1000.  Cannot be blank.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order that this release record is related to.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of  PODetail record that the PORel record is related to.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  """  
      self.Plant:str = obj["Plant"]
      """   Site Identifier. Always set as the Site that nonconf was created in.
Used as a filter to show only nonconf for the current Site.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Material Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  Receipt Number of related RMARcpt record.  """  
      self.RMADisp:int = obj["RMADisp"]
      """  Disposition Number of related RMADisp record.  """  
      self.CommentText:str = obj["CommentText"]
      """  Contains comments about the Non-Conformance transaction.  """  
      self.MaterialMtlCost:int = obj["MaterialMtlCost"]
      """  Mtl Mtl unit cost to date.  """  
      self.MaterialLabCost:int = obj["MaterialLabCost"]
      """  Mtl Lab unit cost to date  """  
      self.MaterialSubCost:int = obj["MaterialSubCost"]
      """  Mtl Sub Unit cost to date  """  
      self.MaterialBurCost:int = obj["MaterialBurCost"]
      """  Material  Burd unit component cost to date  """  
      self.OpCode:str = obj["OpCode"]
      """  Operation Master Code  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  Warehouse where the quantity is moving to.  Defaults to "Inspection Warehouse" but can be overriden. Used in the Advanced material management.  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin location that quantity will be moved to.  Used by Advanced Material Mgmt.  """  
      self.AQMNCMNum:str = obj["AQMNCMNum"]
      """  This field holds the Non-conformance number that is generated by the Advanced Quality Module.  """  
      self.RequestMove:bool = obj["RequestMove"]
      """  Material Queue Records will only be updated if the "Request Move" box is checked  """  
      self.MoveCostsToDMR:bool = obj["MoveCostsToDMR"]
      """   Move Cost to DMR option is used to define if some DMR transactions are accounted or not. In particular, for Non-Conformance Inspections, INS-DMR transactions related to Operation (NonConf.TrnTyp = 'D') are only booked when 'Moving Cost to DMR' is activated.
Default for 'Move Cost To DMR' flag is defined in Company level (Modules-Production-QA-Move Cost to DMR), however user can redefine it on Inspection processing UI for each Inspection.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.FromPCID:str = obj["FromPCID"]
      """  Originating PCID.  """  
      self.AvailableQty:int = obj["AvailableQty"]
      self.Closed:bool = obj["Closed"]
      """  To indicate if the record has been inspected (Open/Closed).  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  """  
      self.FromOpCode:str = obj["FromOpCode"]
      """  Operation code for reporting operation  """  
      self.FromOprSeq:int = obj["FromOprSeq"]
      """  The operation reporting the nonconformance  """  
      self.LegalNumber:str = obj["LegalNumber"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.MtlSourceTrnType:str = obj["MtlSourceTrnType"]
      """  For use with Material-type NonConfs: Holds the PartTran.TranType from the PartTran selected by the user, or "PUR-MTL"  """  
      self.ProcessID:str = obj["ProcessID"]
      """  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  """  
      self.ReasonDescription:str = obj["ReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  Descriptive code assigned by user which uniquely identifies a work center master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  """  
      self.TranQty:int = obj["TranQty"]
      """  The ?Quantity? field converted to the UOM defined in the job material  """  
      self.TranUOM:str = obj["TranUOM"]
      """  The UOM defined in the job material  """  
      self.TrnTypDescription:str = obj["TrnTypDescription"]
      """  D='Operation' I="Inventory' M='Material' S='Subcontract' O='Other'  """  
      self.WrkCntrDesc:str = obj["WrkCntrDesc"]
      """  Long description of the Work Center.  """  
      self.AllowNegQty:bool = obj["AllowNegQty"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.JobProdAttrSearch:str = obj["JobProdAttrSearch"]
      """  Search filter for AttributeSetID from multiple JobProd records  """  
      self.MultipleJobProd:bool = obj["MultipleJobProd"]
      """  multiple jobprod flag  """  
      self.FromOpCodeOpDesc:str = obj["FromOpCodeOpDesc"]
      """  Operation Description  """  
      self.EnablePartNum:bool = obj["EnablePartNum"]
      """  True if TrnTyp = ‘I’ or TrnTyp = “D” (Operations) and co-parts exist for the job and AssemblySeq = 0 and it’s the final operation.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.InspectorIDName:str = obj["InspectorIDName"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PlantName:str = obj["PlantName"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.ResourceIDDescription:str = obj["ResourceIDDescription"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.ToBinNumDescription:str = obj["ToBinNumDescription"]
      self.ToWareHouseCodeDescDescription:str = obj["ToWareHouseCodeDescDescription"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NonConfSourceRow:
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.TrnType:str = obj["TrnType"]
      """  Field that indicates the type of transaction: copied from PartTran.TranType  """  
      self.TrnQty:int = obj["TrnQty"]
      """  Transaction Quantity  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NonConfSourceTableset:
   def __init__(self, obj):
      self.NonConfSource:list[Erp_Tablesets_NonConfSourceRow] = obj["NonConfSource"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_NonConfTableset:
   def __init__(self, obj):
      self.NonConf:list[Erp_Tablesets_NonConfRow] = obj["NonConf"]
      self.NonConfAttch:list[Erp_Tablesets_NonConfAttchRow] = obj["NonConfAttch"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_UpdExtNonConfTableset:
   def __init__(self, obj):
      self.NonConf:list[Erp_Tablesets_NonConfRow] = obj["NonConf"]
      self.NonConfAttch:list[Erp_Tablesets_NonConfAttchRow] = obj["NonConfAttch"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailableQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class GetAvailableQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   tranID
   """  
   def __init__(self, obj):
      self.tranID:int = obj["tranID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NonConfTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NonConfTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NonConfTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NonConfListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMtlQueueSeqValue_input:
   """ Required : 
   company
   nonConfTranID
   tranType
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.nonConfTranID:int = obj["nonConfTranID"]
      self.tranType:str = obj["tranType"]
      pass

class GetMtlQueueSeqValue_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GetMtlSources_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   piMtlSeq
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job number of the Job Material.  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  Job Assembly Sequence of the Job Material.  """  
      self.piMtlSeq:int = obj["piMtlSeq"]
      """  Material Sequence of the Job Material.  """  
      pass

class GetMtlSources_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NonConfSourceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcMtlSourceTrnType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewNonConfAttch_input:
   """ Required : 
   ds
   tranID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      self.tranID:int = obj["tranID"]
      pass

class GetNewNonConfAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewNonConf_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class GetNewNonConf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartInfo_input:
   """ Required : 
   pcPartNum
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part Number.  """  
      pass

class GetPartInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcRevisionNum:str = obj["parameters"]
      self.pcUM:str = obj["parameters"]
      self.pcWarehouseCode:str = obj["parameters"]
      self.plLotTracked:bool = obj["plLotTracked"]
      self.plDimTracked:bool = obj["plDimTracked"]
      self.pcWareHseCodeDesc:str = obj["parameters"]
      self.pcBinNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartTranPKs_input:
   """ Required : 
   tranID
   """  
   def __init__(self, obj):
      self.tranID:int = obj["tranID"]
      """  NonConf.TranID.  """  
      pass

class GetPartTranPKs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetReasonWhereClause_input:
   """ Required : 
   pcNonConfType
   """  
   def __init__(self, obj):
      self.pcNonConfType:str = obj["pcNonConfType"]
      """  Type/origin of NonConformance.  """  
      pass

class GetReasonWhereClause_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  WHERE clause suitable for use with Reason.GetList()  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseNonConf
   whereClauseNonConfAttch
   whereClauseLegalNumGenOpts
   whereClauseSelectedSerialNumbers
   whereClauseSNFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseNonConf:str = obj["whereClauseNonConf"]
      self.whereClauseNonConfAttch:str = obj["whereClauseNonConfAttch"]
      self.whereClauseLegalNumGenOpts:str = obj["whereClauseLegalNumGenOpts"]
      self.whereClauseSelectedSerialNumbers:str = obj["whereClauseSelectedSerialNumbers"]
      self.whereClauseSNFormat:str = obj["whereClauseSNFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NonConfTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   serialControlPlantIsFromPlt
   serialControlPlant
   serialControlPlant2
   snIsEnabled
   partNum
   attributeSetID
   BinNum
   warehouseCode
   jobNum
   assemblySeq
   quantity
   scrapUM
   tranUOM
   sourceRowID
   pcProcessID
   trnTyp
   materialSeq
   """  
   def __init__(self, obj):
      self.serialControlPlantIsFromPlt:bool = obj["serialControlPlantIsFromPlt"]
      """  Indicates if the from plant is controlling the serial processing (UI Application).  """  
      self.serialControlPlant:str = obj["serialControlPlant"]
      """  The plant that is controlling serial behavior for the transaction(UI Application).  """  
      self.serialControlPlant2:str = obj["serialControlPlant2"]
      """  The to plant for the transaction if from plant is controlling (UI Application).  """  
      self.snIsEnabled:bool = obj["snIsEnabled"]
      """  Indicates if the transaction requires serial number selection (UI Application).  """  
      self.partNum:str = obj["partNum"]
      """  The part number for the transaction(UI Application).  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The part attribute set  """  
      self.BinNum:str = obj["BinNum"]
      """  The bin for the transaction(UI Application).  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  The warehouse for the transaction(UI Application).  """  
      self.jobNum:str = obj["jobNum"]
      """  The job for the transaction(UI Application).  """  
      self.assemblySeq:str = obj["assemblySeq"]
      """  The assembly for the transaction(UI Application).  """  
      self.quantity:int = obj["quantity"]
      """  The quantity for the transaction(UI Application).  """  
      self.scrapUM:str = obj["scrapUM"]
      """  The unit of measure for the transaction(UI Application).  """  
      self.tranUOM:str = obj["tranUOM"]
      """  The the converted UOM for the transaction(UI Application).  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  The RowIdent of the NonConf line for the transaction(UI Application).  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  The name of the calling process (UI Application).  """  
      self.trnTyp:str = obj["trnTyp"]
      """  The name of the calling process (UI Application).  """  
      self.materialSeq:int = obj["materialSeq"]
      """  The Material Sequence for the transaction.  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetSelectedSerialNumbersParams_input:
   """ Required : 
   processID
   ds
   """  
   def __init__(self, obj):
      self.processID:str = obj["processID"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectedSerialNumbers_input:
   """ Required : 
   pcNonConfRowIdent
   snIsEnabled
   serialControlPlant
   ds
   """  
   def __init__(self, obj):
      self.pcNonConfRowIdent:str = obj["pcNonConfRowIdent"]
      """  Input RowIdent field of NonConf datatable  """  
      self.snIsEnabled:bool = obj["snIsEnabled"]
      """  Indicates if serial numbers are requied for the NonConf line  """  
      self.serialControlPlant:str = obj["serialControlPlant"]
      """  The plant that is controlling the serial behavior for the NonConf line  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class GetSelectedSerialNumbers_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Get_PartRev_input:
   """ Required : 
   pcPartNum
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part Number.  """  
      pass

class Get_PartRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcRevisionNum:str = obj["parameters"]
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

class NegativeInventoryTest_input:
   """ Required : 
   pcPartNum
   pcWhseCode
   pcBinNum
   pcLotNum
   pcAttributeSetID
   pcPCID
   pcDimCode
   pdDimConvFactor
   ipSellingQuantity
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcPCID:str = obj["pcPCID"]
      self.pcDimCode:str = obj["pcDimCode"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      self.ipSellingQuantity:int = obj["ipSellingQuantity"]
      pass

class NegativeInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeBinNum_input:
   """ Required : 
   pBin
   lfrom
   ds
   """  
   def __init__(self, obj):
      self.pBin:str = obj["pBin"]
      """  Bin Number  """  
      self.lfrom:bool = obj["lfrom"]
      """  Bool indicating to or from bin  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromPCID_input:
   """ Required : 
   pcid
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.pCallProcess:str = obj["pCallProcess"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeFromPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeJobAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobMtl_input:
   """ Required : 
   piProposedMtlSeq
   ds
   """  
   def __init__(self, obj):
      self.piProposedMtlSeq:int = obj["piProposedMtlSeq"]
      """  The new proposed Job Material value  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeJobMtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plAsmReturned:bool = obj["plAsmReturned"]
      self.snWarning:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobOpr_input:
   """ Required : 
   piProposedOprSeq
   lNCOpr
   ds
   """  
   def __init__(self, obj):
      self.piProposedOprSeq:int = obj["piProposedOprSeq"]
      """  The new proposed Job Operation Sequence value  """  
      self.lNCOpr:bool = obj["lNCOpr"]
      """  Boolean. true = nonconfroming Operation, false = reporting Operation  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeJobOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToPCID_input:
   """ Required : 
   pcid
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.pCallProcess:str = obj["pCallProcess"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeToPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranQty_input:
   """ Required : 
   pdTranQty
   ds
   """  
   def __init__(self, obj):
      self.pdTranQty:int = obj["pdTranQty"]
      """  Transaction Qty  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeTranQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUM_input:
   """ Required : 
   pUM
   ds
   """  
   def __init__(self, obj):
      self.pUM:str = obj["pUM"]
      """  Transaction UOM  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWarehouseCode_input:
   """ Required : 
   pWhse
   lfrom
   ds
   """  
   def __init__(self, obj):
      self.pWhse:str = obj["pWhse"]
      """  Warehouse Code  """  
      self.lfrom:bool = obj["lfrom"]
      """  Bool indicating to or from warehouse  """  
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangeWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedCOPartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangedCOPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      self.whBinWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNonConfTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNonConfTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateQtyInventoryTestIncludingPCID_input:
   """ Required : 
   pcPartNum
   pcWhseCode
   pcBinNum
   pcLotNum
   pcAttributeSetID
   pcPCID
   pcDimCode
   pdDimConvFactor
   ipSellingQuantity
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcPCID:str = obj["pcPCID"]
      self.pcDimCode:str = obj["pcDimCode"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      self.ipSellingQuantity:int = obj["ipSellingQuantity"]
      pass

class ValidateQtyInventoryTestIncludingPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateQtyInventoryTest_input:
   """ Required : 
   pcPartNum
   pcWhseCode
   pcBinNum
   pcLotNum
   pcAttributeSetID
   pcDimCode
   pdDimConvFactor
   ipSellingQuantity
   tran
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcDimCode:str = obj["pcDimCode"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      self.ipSellingQuantity:int = obj["ipSellingQuantity"]
      self.tran:int = obj["tran"]
      pass

class ValidateQtyInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NonConfTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

