import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BankAcctSvc
# Description: bo/BankAcct/BankAcct.p
           BankAcct Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankAccts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankAccts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts",headers=creds) as resp:
           return await resp.json()

async def post_BankAccts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankAccts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankAcctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankAcctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID(Company, BankAcctID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankAcct item
   Description: Calls GetByID to retrieve the BankAcct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankAcctRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankAccts_Company_BankAcctID(Company, BankAcctID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankAcct for the service
   Description: Calls UpdateExt to update BankAcct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankAcctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankAccts_Company_BankAcctID(Company, BankAcctID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankAcct item
   Description: Call UpdateExt to delete BankAcct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankAcct
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_BankPayMethods(Company, BankAcctID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankPayMethods items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankPayMethods1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankPayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankPayMethods",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_BankPayMethods_Company_BankAcctID_PMUID(Company, BankAcctID, PMUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankPayMethod item
   Description: Calls GetByID to retrieve the BankPayMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankPayMethod1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_Partners(Company, BankAcctID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Partners items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Partners1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/Partners",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, BankAcctID, PartnerNum, PartnerType, PartnerID, SearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_EntityGLCs(Company, BankAcctID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, BankAcctID, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_BankAcctAttches(Company, BankAcctID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get BankAcctAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BankAcctAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankAcctAttches",headers=creds) as resp:
           return await resp.json()

async def get_BankAccts_Company_BankAcctID_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company, BankAcctID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankAcctAttch item
   Description: Calls GetByID to retrieve the BankAcctAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAcctAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAccts(" + Company + "," + BankAcctID + ")/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankPayMethods(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankPayMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankPayMethods
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankPayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods",headers=creds) as resp:
           return await resp.json()

async def post_BankPayMethods(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankPayMethods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankPayMethods_Company_BankAcctID_PMUID(Company, BankAcctID, PMUID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankPayMethod item
   Description: Calls GetByID to retrieve the BankPayMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankPayMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankPayMethods_Company_BankAcctID_PMUID(Company, BankAcctID, PMUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankPayMethod for the service
   Description: Calls UpdateExt to update BankPayMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankPayMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankPayMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankPayMethods_Company_BankAcctID_PMUID(Company, BankAcctID, PMUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankPayMethod item
   Description: Call UpdateExt to delete BankPayMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankPayMethod
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param PMUID: Desc: PMUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankPayMethods(" + Company + "," + BankAcctID + "," + PMUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Partners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners",headers=creds) as resp:
           return await resp.json()

async def post_Partners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_BankAcctAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get BankAcctAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BankAcctAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches",headers=creds) as resp:
           return await resp.json()

async def post_BankAcctAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BankAcctAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company, BankAcctID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the BankAcctAttch item
   Description: Calls GetByID to retrieve the BankAcctAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BankAcctAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company, BankAcctID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update BankAcctAttch for the service
   Description: Calls UpdateExt to update BankAcctAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BankAcctAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.BankAcctAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_BankAcctAttches_Company_BankAcctID_DrawingSeq(Company, BankAcctID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete BankAcctAttch item
   Description: Call UpdateExt to delete BankAcctAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BankAcctAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param BankAcctID: Desc: BankAcctID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/BankAcctAttches(" + Company + "," + BankAcctID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BankAcctListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseBankAcct, whereClauseBankAcctAttch, whereClauseBankPayMethod, whereClausePartner, whereClauseEntityGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseBankAcct=" + whereClauseBankAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankAcctAttch=" + whereClauseBankAcctAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseBankPayMethod=" + whereClauseBankPayMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartner=" + whereClausePartner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(bankAcctID, epicorHeaders = None):
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
   params += "bankAcctID=" + bankAcctID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBankBranchCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBankBranchCode
   Description: Check if the Bank Branch code changed.
   OperationID: ChangeBankBranchCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankBranchCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankBranchCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDebNoteOnly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDebNoteOnly
   Description: Check if the Bank DebNoteOnly flag could be changed.
   OperationID: ChangeDebNoteOnly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDebNoteOnly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDebNoteOnly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLOCLimit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLOCLimit
   Description: Method to call when changing the Limit of Credit amount on an Bank record.  Updates BankAcct
amounts based on the new Limit of Credit amount.
   OperationID: ChangeLOCLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLOCLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLOCLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBankCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBankCustNum
   Description: Check Bank Customer Number
At this time this method is specific to Switzerland localization
   OperationID: CheckBankCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBankCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckISRPartyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckISRPartyID
   Description: Check ISR Party ID
At this time this method is specific to Switzerland localization
   OperationID: CheckISRPartyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckISRPartyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckISRPartyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPLOCClosed(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPLOCClosed
   Description: This method will retrieve information about Letter of Credit with status Closed
   OperationID: GetAPLOCClosed
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCClosed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCClosed_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPLOCOpen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAPLOCOpen
   Description: This method will retrieve information about Letter of Credit with status Open
   OperationID: GetAPLOCOpen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAPLOCOpen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPLOCOpen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankBal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankBal
   Description: Get bank balance.
   OperationID: GetBankBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBankBalFromDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBankBalFromDate
   Description: Get bank balance from a date. First we need to get the fiscal year that has that particular date in range and then get the balance for that fiscal year.
   OperationID: GetBankBalFromDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBankBalFromDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBankBalFromDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCurrencyBase(epicorHeaders = None):
   """  
   Summary: Invoke method GetCurrencyBase
   Description: This method returns the Base Currency
   OperationID: GetCurrencyBase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCurrencyBase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetBaseCurrencySymbol(epicorHeaders = None):
   """  
   Summary: Invoke method GetBaseCurrencySymbol
   OperationID: GetBaseCurrencySymbol
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBaseCurrencySymbol_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsForMandate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsForMandate
   Description: Returns BankAcct records, for which Creditor ID is not empty.
   OperationID: GetRowsForMandate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsForMandate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsForMandate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifySearchIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartner
   Description: validate PartnerID
   OperationID: ValidatePartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetEnableMICR(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetEnableMICR
   Description: Return EnableMICR as true when theres at least one MICR Payment
   OperationID: GetEnableMICR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetEnableMICR_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEnableMICR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankAcct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankAcctAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankAcctAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankAcctAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankAcctAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankAcctAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewBankPayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewBankPayMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBankPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewBankPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBankPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BankAcctSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankAcctAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankAcctListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankAcctRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankAcctRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BankPayMethodRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_BankPayMethodRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartnerRow] = obj["value"]
      pass

class Erp_Tablesets_BankAcctAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BankAcctID:str = obj["BankAcctID"]
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

class Erp_Tablesets_BankAcctListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description of the bank account.  """  
      self.CheckingAccount:str = obj["CheckingAccount"]
      """  The account number for the bank account. Used for reference only.  """  
      self.Closed:bool = obj["Closed"]
      """  Indicates whether or not the bank account is an active account.  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.APPaymentUseBankAvg:bool = obj["APPaymentUseBankAvg"]
      """  Use the bank average value as the rate for payments from this account.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenStatement:bool = obj["OpenStatement"]
      """  Indicates of bank account that now have an open statement waiting to be finally matched/posted.  """  
      self.PositivePayRemoteID:str = obj["PositivePayRemoteID"]
      """  PositivePayRemoteID  """  
      self.PositivePayBatchID:str = obj["PositivePayBatchID"]
      """  PositivePayBatchID  """  
      self.DefPosPayEFTHeadUID:int = obj["DefPosPayEFTHeadUID"]
      """  DefPosPayEFTHeadUID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description of the bank account.  """  
      self.CheckingAccount:str = obj["CheckingAccount"]
      """  The account number for the bank account. Used for reference only.  """  
      self.Closed:bool = obj["Closed"]
      """  Indicates whether or not the bank account is an active account.  """  
      self.OpeningBalance:int = obj["OpeningBalance"]
      """  The Opening Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance and becomes the opening balance for the next statement.  """  
      self.OpeningDate:str = obj["OpeningDate"]
      """  The Opening Date of the Bank Account.  When a bank reconciliation is posted, the next statement's opening date is set to the posted reconciliation's Closing Date + 1 and becomes the opening date for the next statement.  """  
      self.ClosingBalance:int = obj["ClosingBalance"]
      """  The Closing Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance.  """  
      self.ClosingDate:str = obj["ClosingDate"]
      """  The Closing Date of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing date.  """  
      self.BankRoutingNum:str = obj["BankRoutingNum"]
      """  The bank's routing number.  """  
      self.BankCheckDigit:int = obj["BankCheckDigit"]
      """  The check digit for the bank.  """  
      self.BankName:str = obj["BankName"]
      """  The Bank's full name.  """  
      self.ServClassCode:str = obj["ServClassCode"]
      """   Service Class Code 200 = Mixed debit or credit entries and pre-notification entries.

Contact your bank for the appropriate value.  """  
      self.EntryClassCode:str = obj["EntryClassCode"]
      """   PPD - Prearranged Payments and Deposits for consumer items.
CCD - Cash concentration and disbursements for non-consumer items.
REV - Reversal Items.

Contact your bank for the appropriate value.  """  
      self.CDJournalCode:str = obj["CDJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for A/P checks.  Normally this would be called Cash Disbursements Journal.  """  
      self.PRJournalCode:str = obj["PRJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for P/R checks.  Normally this would be called Payroll Journal.  """  
      self.CRJournalCode:str = obj["CRJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for A/R cash receipts. Normally this would be called the Cash Receipts Journal.  """  
      self.BKJournalCode:str = obj["BKJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for Bank transactions made in the check reconciliation process.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement.) The user enters a bank slip during the bank reconciliation process.  This is then written into the related GLJrnDtl records. Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.ExportDecimalPoint:bool = obj["ExportDecimalPoint"]
      """  Indicates if the decimal point in decimal fields should be exported when exporting electronic payments. For example, if this is set to no then 10.00 it would be exported as 1000.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency that the bank account is denominated in.  """  
      self.BankCompID:str = obj["BankCompID"]
      """  Assigned by the bank.  Uniquely identifies your company to the bank.  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account is for Debit Notes only.  If this flag is yes the bank could be used in Cash Receipts  only.  """  
      self.ReconciledBalance:bool = obj["ReconciledBalance"]
      """  Allows you to keep a reconciled balance in AR when this check box is  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  Allows you to keep a reconciled balance in AP when this check box is  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.APPaymentUseBankAvg:bool = obj["APPaymentUseBankAvg"]
      """  Use the bank average value as the rate for payments from this account.  """  
      self.PayerRef:str = obj["PayerRef"]
      """  Payer Reference  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  Tax Payer ID  """  
      self.NextPINum:int = obj["NextPINum"]
      """  Future Use - Starting Number for Bank level PI Numbering  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.NumPIDigits:int = obj["NumPIDigits"]
      """  Future Use - Number of digits allowed in PI Numbering  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Free Form Type Code. Used in localizations.  """  
      self.TransferPersonName:str = obj["TransferPersonName"]
      """  Free Form Person Name. Used in localizations.  """  
      self.TransferPersonCode:str = obj["TransferPersonCode"]
      """  Free Form Person code. Used in localizations.  """  
      self.AccountType:str = obj["AccountType"]
      """  Account Type.  """  
      self.LOCLimit:int = obj["LOCLimit"]
      """  Letter of Credit Limit.  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name of Bank, which is consistent with Legal Names field for trading partners.  """  
      self.FloatAmt:int = obj["FloatAmt"]
      """  Float amount for the bank account.  """  
      self.DocLOCLimit:int = obj["DocLOCLimit"]
      """  Letter of Credit Limit in bank's currency.  """  
      self.Rpt1LOCLimit:int = obj["Rpt1LOCLimit"]
      """  Letter of Credit Limit in reporting currency 1.  """  
      self.Rpt2LOCLimit:int = obj["Rpt2LOCLimit"]
      """  Letter of Credit Limit in reporting currency 2.  """  
      self.Rpt3LOCLimit:int = obj["Rpt3LOCLimit"]
      """  Letter of Credit Limit in reporting currency 3.  """  
      self.AutoStatementImport:bool = obj["AutoStatementImport"]
      """  Auto Statement Import  """  
      self.AutoMatchStatement:bool = obj["AutoMatchStatement"]
      """  Specifies whether the application automatically attempts to extract invoice numbers from the statement lines  """  
      self.AutoRecDocuments:bool = obj["AutoRecDocuments"]
      """  Auto Rec Documents  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Specifies a default electronic interface for importing bank statements for  """  
      self.AutoRetrieve:bool = obj["AutoRetrieve"]
      """  If this check box is selected, then after importing a bank statement the application automatically displays all  """  
      self.FilterByLine:bool = obj["FilterByLine"]
      """  Filter By Line  """  
      self.CreditorID:str = obj["CreditorID"]
      """  CreditorID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoRcgARRefNum:bool = obj["AutoRcgARRefNum"]
      """  Specify whether reference number verification is applied during automatic  """  
      self.AutoRcgARCustomer:bool = obj["AutoRcgARCustomer"]
      """  Specify whether customer verification is applied during automatic  """  
      self.AutoRcgARTranDate:bool = obj["AutoRcgARTranDate"]
      """  Specify whether transaction date verification is applied during automatic  """  
      self.AutoRcgAPRefNum:bool = obj["AutoRcgAPRefNum"]
      """  Specify whether reference number verification is applied during automatic  """  
      self.AutoRcgAPSupplier:bool = obj["AutoRcgAPSupplier"]
      """  Specify whether supplier verification is applied during automatic  """  
      self.AutoRcgAPTranDate:bool = obj["AutoRcgAPTranDate"]
      """  Specify whether transaction date verification is applied during automatic  """  
      self.AutoRcgUnknownTran:bool = obj["AutoRcgUnknownTran"]
      """  This parameter defines the application behavior in case the transactions do  """  
      self.CHDTAID:str = obj["CHDTAID"]
      """  CHDTAID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.BankType:str = obj["BankType"]
      """  BankType  """  
      self.AutoCashMovement:bool = obj["AutoCashMovement"]
      """  Select this checkbox to enable the automatic creation of invoice cash receipts.  """  
      self.ParamCode:str = obj["ParamCode"]
      """  Specify the parsing parameter ID which is used during automatic bank  """  
      self.AutoOnAccountReceipt:bool = obj["AutoOnAccountReceipt"]
      """  This check box determines the application logic when it cannot find invoices where customer, amount and date  """  
      self.AutoInvoicePayment:bool = obj["AutoInvoicePayment"]
      """  Auto Invoice Payment  """  
      self.AutoBankTransferSameCurr:bool = obj["AutoBankTransferSameCurr"]
      """  Select this checkbox to enable the automatic creation of same currency bank transfer transactions during automatic  """  
      self.AutoBankTransferCrossCurr:bool = obj["AutoBankTransferCrossCurr"]
      """  Select this checkbox to enable the automatic creation of cross currency bank transfer transactions during automatic  """  
      self.AutoBankAdjustment:bool = obj["AutoBankAdjustment"]
      """  Select this checkbox to enable the automatic creation of bank adjustment transactions during automatic bank  """  
      self.POBankAcctNum:str = obj["POBankAcctNum"]
      """  POBankAcctNum  """  
      self.BankCustNum:str = obj["BankCustNum"]
      """  BankCustNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  Select this check box to enable the automatic creation of reverse cash receipts and voided AP payments transactions  """  
      self.PeriodThreshold:int = obj["PeriodThreshold"]
      """  Specifies the number of periods before opening date which will be retrieved during bank reconciliation. If you  """  
      self.PRAlignTax:bool = obj["PRAlignTax"]
      """  PRAlignTax  """  
      self.PRLinePerPRCheck:int = obj["PRLinePerPRCheck"]
      """  PRLinePerPRCheck  """  
      self.PRPreprintedCheckNumber:bool = obj["PRPreprintedCheckNumber"]
      """  PRPreprintedCheckNumber  """  
      self.PayrollCheckingAccount:bool = obj["PayrollCheckingAccount"]
      """  If you select this check box, the application sets the type of lines with  """  
      self.RBankNum:str = obj["RBankNum"]
      """  RBankNum  """  
      self.RBranchNum:str = obj["RBranchNum"]
      """  RBranchNum  """  
      self.JPBankName:str = obj["JPBankName"]
      """  JPBankName  """  
      self.JPBranchName:str = obj["JPBranchName"]
      """  JPBranchName  """  
      self.BankTranfAccountType:str = obj["BankTranfAccountType"]
      """  BankTranfAccountType  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.PostalCode:str = obj["PostalCode"]
      """  PostalCode  """  
      self.State:str = obj["State"]
      """  State  """  
      self.CountryNum:int = obj["CountryNum"]
      """  CountryNum  """  
      self.LName:str = obj["LName"]
      """  LName  """  
      self.MsgIDCounter:str = obj["MsgIDCounter"]
      """  MsgIDCounter  """  
      self.ConsInvPmt:bool = obj["ConsInvPmt"]
      """  ConsInvPmt  """  
      self.PreprintedCheckNum:bool = obj["PreprintedCheckNum"]
      """  PreprintedCheckNum  """  
      self.InvPerCheckStub:int = obj["InvPerCheckStub"]
      """  InvPerCheckStub  """  
      self.ReconcileOtherBalances:bool = obj["ReconcileOtherBalances"]
      """  Allows you to keep a reconciled balance for transactions other than AP payments and AR cash receipts (such as  """  
      self.RecBalFiscalYear:int = obj["RecBalFiscalYear"]
      """  RecBalFiscalYear  """  
      self.RecBalFiscalPeriod:int = obj["RecBalFiscalPeriod"]
      """  RecBalFiscalPeriod  """  
      self.RecBalFiscalYearSuffix:str = obj["RecBalFiscalYearSuffix"]
      """  RecBalFiscalYearSuffix  """  
      self.RevalueUseRecBal:bool = obj["RevalueUseRecBal"]
      """  RevalueUseRecBal  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.COIsOneTimeBankAcct:bool = obj["COIsOneTimeBankAcct"]
      """  COIsOneTimeBankAcct  """  
      self.AutoCustBalanceReceipt:bool = obj["AutoCustBalanceReceipt"]
      """  Select this checkbox to enable the automatic creation of cash receipts based on customer balance. This option  """  
      self.MatchTolerance:int = obj["MatchTolerance"]
      """  This parameter determines maximum allowed percent difference between amounts of the unallocated statement  """  
      self.TranTemplateID:str = obj["TranTemplateID"]
      """  Specify the ID of template with the set of transaction codes. It is assigned to the bank account. Refer to the Bank  """  
      self.AutoCustBalanceReceiptApplyAll:bool = obj["AutoCustBalanceReceiptApplyAll"]
      """  This check box changes the application logic when it creates cash receipts based on customer balance.  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.MXSATNameShort:str = obj["MXSATNameShort"]
      """  MXSATNameShort  """  
      self.MXSATNameFull:str = obj["MXSATNameFull"]
      """  MXSATNameFull  """  
      self.CNSellerBankName:str = obj["CNSellerBankName"]
      """  CNSellerBankName  """  
      self.CNSellerAddress:str = obj["CNSellerAddress"]
      """  CNSellerAddress  """  
      self.ClearBankExchRate:str = obj["ClearBankExchRate"]
      """  ClearBankExchRate  """  
      self.PositivePayRemoteID:str = obj["PositivePayRemoteID"]
      """  PositivePayRemoteID  """  
      self.PositivePayBatchID:str = obj["PositivePayBatchID"]
      """  PositivePayBatchID  """  
      self.DefPosPayEFTHeadUID:int = obj["DefPosPayEFTHeadUID"]
      """  DefPosPayEFTHeadUID  """  
      self.LogoFont:str = obj["LogoFont"]
      """  Font used when printing the logo in MICR check.  """  
      self.LogoType:str = obj["LogoType"]
      """  Logo type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  """  
      self.LogoImageID:str = obj["LogoImageID"]
      """  Image ID for the image used as logo in MICR check.  """  
      self.LogoText01:str = obj["LogoText01"]
      """  First line for logo's text.  """  
      self.LogoText02:str = obj["LogoText02"]
      """  Second line for logo's text.  """  
      self.LogoText03:str = obj["LogoText03"]
      """  Third line for logo's text.  """  
      self.LogoText04:str = obj["LogoText04"]
      """  Fourth line for logo's text.  """  
      self.LogoText05:str = obj["LogoText05"]
      """  Fifth line for logo's text.  """  
      self.LogoText06:str = obj["LogoText06"]
      """  Sixth line for logo's text.  """  
      self.SignatureFont:str = obj["SignatureFont"]
      """  Font used when printing the signature in MICR check.  """  
      self.SignatureType:str = obj["SignatureType"]
      """  Signature type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  """  
      self.SignatureImageID:str = obj["SignatureImageID"]
      """  Image ID for the image used as signature in MICR check.  """  
      self.SignatureText01:str = obj["SignatureText01"]
      """  First line for signature's text.  """  
      self.SignatureText02:str = obj["SignatureText02"]
      """  Second line for signature's text.  """  
      self.SignatureText03:str = obj["SignatureText03"]
      """  Third line for signature's text.  """  
      self.SignatureText04:str = obj["SignatureText04"]
      """  Fourth line for signature's text.  """  
      self.SignatureText05:str = obj["SignatureText05"]
      """  Fifth line for signature's text.  """  
      self.SignatureText06:str = obj["SignatureText06"]
      """  Sixth line for signature's text.  """  
      self.PREntryClassCode:str = obj["PREntryClassCode"]
      """  To be used when processing the electronic interface for direct deposit check deductions.  """  
      self.PRPMEFTHeadUID:int = obj["PRPMEFTHeadUID"]
      """  Id of the Electronic Interface to be used when processing a Payroll Group.  """  
      self.PEDetNationalBank:bool = obj["PEDetNationalBank"]
      """  PEDetNationalBank  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """  BankGiroAcctNbr  """  
      self.ParentPlant:str = obj["ParentPlant"]
      """  Default Parent Site. This site is a default site that is paying for invoices.  """  
      self.ChildPlantList:str = obj["ChildPlantList"]
      """  Default Child Sites. This is a default list of sites, which can be child sites at the time of payment  """  
      self.BalanceType:int = obj["BalanceType"]
      """  This option is to select which balances will be displayed (ongoing, reconciled, or non Reconciled).  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrencyCode:str = obj["BaseCurrCurrencyCode"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CHScrISRPartyID:str = obj["CHScrISRPartyID"]
      """  ISR Party Number in format XX-#####V-P (CSF Switzerland)  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type for Denmark localization  """  
      self.PendingCashAcctDesc:str = obj["PendingCashAcctDesc"]
      """  Pending Cash Account Description  """  
      self.PORateGrp:str = obj["PORateGrp"]
      """  Purchase and Expenditure Rate Group  """  
      self.PORateGrpDescription:str = obj["PORateGrpDescription"]
      """  PO RateGrp Description  """  
      self.VarianceAcctDesc:str = obj["VarianceAcctDesc"]
      """  Variance Account Description  """  
      self.AssociatedToDoc:bool = obj["AssociatedToDoc"]
      """  This external field is created to hold the validation for the bank to be associated for any document. this will help to enable/disable field in case a crated bank account is already associated to any document or transaction.  """  
      self.EnableMICR:bool = obj["EnableMICR"]
      """  Enable MICR Check panel  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.BKJournalCodeDescJrnlDescription:str = obj["BKJournalCodeDescJrnlDescription"]
      self.CDJournalCodeDescJrnlDescription:str = obj["CDJournalCodeDescJrnlDescription"]
      self.CRJournalCodeDescJrnlDescription:str = obj["CRJournalCodeDescJrnlDescription"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.DefPosPayEFTHeadUIDName:str = obj["DefPosPayEFTHeadUIDName"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.PRJournalCodeDescJrnlDescription:str = obj["PRJournalCodeDescJrnlDescription"]
      self.PRPMEFTHeadUIDName:str = obj["PRPMEFTHeadUIDName"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankPayMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Flag for default payment method  """  
      self.PMSource:int = obj["PMSource"]
      """   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  """  
      self.PaymentNumMask:str = obj["PaymentNumMask"]
      """  PaymentNumMask  """  
      self.StartingSeqNum:str = obj["StartingSeqNum"]
      """  StartingSeqNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.DeleteFromParent:bool = obj["DeleteFromParent"]
      """  This field will allow us to delete record marked as default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBankBranchCode_input:
   """ Required : 
   proposedBankBranchCode
   ds
   """  
   def __init__(self, obj):
      self.proposedBankBranchCode:str = obj["proposedBankBranchCode"]
      """  The proposed Bank Branch code  """  
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class ChangeBankBranchCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDebNoteOnly_input:
   """ Required : 
   ds
   debNoteOnly
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      self.debNoteOnly:bool = obj["debNoteOnly"]
      """  Proposed value of the flag  """  
      pass

class ChangeDebNoteOnly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLOCLimit_input:
   """ Required : 
   proposedLOCLimit
   ds
   """  
   def __init__(self, obj):
      self.proposedLOCLimit:int = obj["proposedLOCLimit"]
      """  The proposed Limit amount  """  
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class ChangeLOCLimit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBankCustNum_input:
   """ Required : 
   ipBankCustNum
   """  
   def __init__(self, obj):
      self.ipBankCustNum:str = obj["ipBankCustNum"]
      """  New value of Bank Customer Number.  """  
      pass

class CheckBankCustNum_output:
   def __init__(self, obj):
      pass

class CheckISRPartyID_input:
   """ Required : 
   ipISRPartyID
   ds
   """  
   def __init__(self, obj):
      self.ipISRPartyID:str = obj["ipISRPartyID"]
      """  New value of ISR Party ID.  """  
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class CheckISRPartyID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   bankAcctID
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_APLOCClosedRow:
   def __init__(self, obj):
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.RemLCValue:int = obj["RemLCValue"]
      """  Remaining Value  """  
      self.OutPOValue:int = obj["OutPOValue"]
      """  Outstanding PO Value  """  
      self.LCValue:int = obj["LCValue"]
      """  LC Value  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description  """  
      self.CurrName:str = obj["CurrName"]
      """  Currency Name  """  
      self.CumInvValue:int = obj["CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.APLCID:str = obj["APLCID"]
      """  Letter of Credit ID.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.DocCumInvValue:int = obj["DocCumInvValue"]
      """  Cumulative Invoice Value  """  
      self.Rpt1CumInvValue:int = obj["Rpt1CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.Rpt2CumInvValue:int = obj["Rpt2CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.Rpt3CumInvValue:int = obj["Rpt3CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Letter of Credit Value  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Letter of Credit Value  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Letter of Credit Value  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Letter of Credit Value  """  
      self.DocOutPOValue:int = obj["DocOutPOValue"]
      """  Outstanding PO Value  """  
      self.Rpt2OutPOValue:int = obj["Rpt2OutPOValue"]
      """  Outstanding PO Value  """  
      self.Rpt3OutPOValue:int = obj["Rpt3OutPOValue"]
      """  Outstanding PO Value  """  
      self.DocRemLCValue:int = obj["DocRemLCValue"]
      """  Remaining Value  """  
      self.Rpt1RemLCValue:int = obj["Rpt1RemLCValue"]
      """  Remaining Value  """  
      self.Rpt2RemLCValue:int = obj["Rpt2RemLCValue"]
      """  Remaining Value  """  
      self.Rpt3RemLCValue:int = obj["Rpt3RemLCValue"]
      """  Remaining Value  """  
      self.Rpt1OutPOValue:int = obj["Rpt1OutPOValue"]
      """  Outstanding PO Value  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_APLOCOpenRow:
   def __init__(self, obj):
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name  """  
      self.APLCID:str = obj["APLCID"]
      """  Letter of Credit ID  """  
      self.CumInvValue:int = obj["CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.CurrName:str = obj["CurrName"]
      """  Currency Name  """  
      self.Description:str = obj["Description"]
      """  Letter of Credit Description  """  
      self.InvoiceBal:int = obj["InvoiceBal"]
      """  Invoices Balance  """  
      self.LCValue:int = obj["LCValue"]
      """  LC Value  """  
      self.OutPOValue:int = obj["OutPOValue"]
      """  Outstanding PO Value  """  
      self.RemLCValue:int = obj["RemLCValue"]
      """  Remaining Value  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID  """  
      self.DocCumInvValue:int = obj["DocCumInvValue"]
      """  Cumulative Invoice Value  """  
      self.Rpt1CumInvValue:int = obj["Rpt1CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.Rpt2CumInvValue:int = obj["Rpt2CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.Rpt3CumInvValue:int = obj["Rpt3CumInvValue"]
      """  Cumulative Invoice Value  """  
      self.DocInvoiceBal:int = obj["DocInvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt1InvoiceBal:int = obj["Rpt1InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt2InvoiceBal:int = obj["Rpt2InvoiceBal"]
      """  Invoices Balance  """  
      self.Rpt3InvoiceBal:int = obj["Rpt3InvoiceBal"]
      """  Invoices Balance  """  
      self.DocLCValue:int = obj["DocLCValue"]
      """  Letter of Credit Value  """  
      self.Rpt1LCValue:int = obj["Rpt1LCValue"]
      """  Letter of Credit Value  """  
      self.Rpt2LCValue:int = obj["Rpt2LCValue"]
      """  Letter of Credit Value  """  
      self.Rpt3LCValue:int = obj["Rpt3LCValue"]
      """  Letter of Credit Value  """  
      self.DocOutPOValue:int = obj["DocOutPOValue"]
      """  Outstanding PO Value  """  
      self.Rpt1OutPOValue:int = obj["Rpt1OutPOValue"]
      """  Outstanding PO Value  """  
      self.Rpt2OutPOValue:int = obj["Rpt2OutPOValue"]
      """  Outstanding PO Value  """  
      self.Rpt3OutPOValue:int = obj["Rpt3OutPOValue"]
      """  Outstanding PO Value  """  
      self.DocRemLCValue:int = obj["DocRemLCValue"]
      """  Remaining Value  """  
      self.Rpt1RemLCValue:int = obj["Rpt1RemLCValue"]
      """  Remaining Value  """  
      self.Rpt2RemLCValue:int = obj["Rpt2RemLCValue"]
      """  Remaining Value  """  
      self.Rpt3RemLCValue:int = obj["Rpt3RemLCValue"]
      """  Remaining Value  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BalanceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BankAcctID:str = obj["BankAcctID"]
      self.FiscalYear:int = obj["FiscalYear"]
      """  Enter the fiscal year whose balances you want to display. By default, the current fiscal year is selected.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.ExchangeRate:int = obj["ExchangeRate"]
      self.RefToBaseRate:int = obj["RefToBaseRate"]
      self.RefCode:str = obj["RefCode"]
      self.DocToRef:bool = obj["DocToRef"]
      self.RefToBase:bool = obj["RefToBase"]
      self.DbBalance:int = obj["DbBalance"]
      self.CrBalance:int = obj["CrBalance"]
      self.OpeningBalance:int = obj["OpeningBalance"]
      self.DocDbBalance:int = obj["DocDbBalance"]
      self.DocCrBalance:int = obj["DocCrBalance"]
      self.DocOpeningBalance:int = obj["DocOpeningBalance"]
      self.CurrentBalance:int = obj["CurrentBalance"]
      """  The current balance total  """  
      self.DocCurrentBalance:int = obj["DocCurrentBalance"]
      """  The document current balance total.  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      """  The currency switch flag  """  
      self.CurrSymbol:str = obj["CurrSymbol"]
      """  The currency symbol.  """  
      self.BaseCurrencySymbol:str = obj["BaseCurrencySymbol"]
      """  Base Currency Symbol based on the current Company  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Enter the fiscal year suffix whose balances you want to display.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.Rpt1CrBalance:int = obj["Rpt1CrBalance"]
      self.Rpt2CrBalance:int = obj["Rpt2CrBalance"]
      self.Rpt3CrBalance:int = obj["Rpt3CrBalance"]
      self.Rpt1DbBalance:int = obj["Rpt1DbBalance"]
      self.Rpt2DbBalance:int = obj["Rpt2DbBalance"]
      self.Rpt3DbBalance:int = obj["Rpt3DbBalance"]
      self.Rpt1OpeningBalance:int = obj["Rpt1OpeningBalance"]
      self.Rpt2OpeningBalance:int = obj["Rpt2OpeningBalance"]
      self.Rpt3OpeningBalance:int = obj["Rpt3OpeningBalance"]
      self.Rpt1CurrentBalance:int = obj["Rpt1CurrentBalance"]
      self.Rpt2CurrentBalance:int = obj["Rpt2CurrentBalance"]
      self.Rpt3CurrentBalance:int = obj["Rpt3CurrentBalance"]
      self.OpeningBalanceRec:int = obj["OpeningBalanceRec"]
      self.CrBalanceRec:int = obj["CrBalanceRec"]
      self.DbBalanceRec:int = obj["DbBalanceRec"]
      self.CurrentBalanceRec:int = obj["CurrentBalanceRec"]
      self.DocOpeningBalanceRec:int = obj["DocOpeningBalanceRec"]
      self.DocCrBalanceRec:int = obj["DocCrBalanceRec"]
      self.DocDbBalanceRec:int = obj["DocDbBalanceRec"]
      self.DocCurrentBalanceRec:int = obj["DocCurrentBalanceRec"]
      self.Rpt1OpeningBalanceRec:int = obj["Rpt1OpeningBalanceRec"]
      self.Rpt1CrBalanceRec:int = obj["Rpt1CrBalanceRec"]
      self.Rpt1DbBalanceRec:int = obj["Rpt1DbBalanceRec"]
      self.Rpt1CurrentBalanceRec:int = obj["Rpt1CurrentBalanceRec"]
      self.Rpt2OpeningBalanceRec:int = obj["Rpt2OpeningBalanceRec"]
      self.Rpt2CrBalanceRec:int = obj["Rpt2CrBalanceRec"]
      self.Rpt2DbBalanceRec:int = obj["Rpt2DbBalanceRec"]
      self.Rpt2CurrentBalanceRec:int = obj["Rpt2CurrentBalanceRec"]
      self.Rpt3OpeningBalanceRec:int = obj["Rpt3OpeningBalanceRec"]
      self.Rpt3CrBalanceRec:int = obj["Rpt3CrBalanceRec"]
      self.Rpt3DbBalanceRec:int = obj["Rpt3DbBalanceRec"]
      self.Rpt3CurrentBalanceRec:int = obj["Rpt3CurrentBalanceRec"]
      self.OpeningBalanceNonRec:int = obj["OpeningBalanceNonRec"]
      self.CrBalanceNonRec:int = obj["CrBalanceNonRec"]
      self.DbBalanceNonRec:int = obj["DbBalanceNonRec"]
      self.CurrentBalanceNonRec:int = obj["CurrentBalanceNonRec"]
      self.DocOpeningBalanceNonRec:int = obj["DocOpeningBalanceNonRec"]
      self.DocCrBalanceNonRec:int = obj["DocCrBalanceNonRec"]
      self.DocDbBalanceNonRec:int = obj["DocDbBalanceNonRec"]
      self.DocCurrentBalanceNonRec:int = obj["DocCurrentBalanceNonRec"]
      self.Rpt1OpeningBalanceNonRec:int = obj["Rpt1OpeningBalanceNonRec"]
      self.Rpt1CrBalanceNonRec:int = obj["Rpt1CrBalanceNonRec"]
      self.Rpt1DbBalanceNonRec:int = obj["Rpt1DbBalanceNonRec"]
      self.Rpt1CurrentBalanceNonRec:int = obj["Rpt1CurrentBalanceNonRec"]
      self.Rpt2OpeningBalanceNonRec:int = obj["Rpt2OpeningBalanceNonRec"]
      self.Rpt2CrBalanceNonRec:int = obj["Rpt2CrBalanceNonRec"]
      self.Rpt2DbBalanceNonRec:int = obj["Rpt2DbBalanceNonRec"]
      self.Rpt2CurrentBalanceNonRec:int = obj["Rpt2CurrentBalanceNonRec"]
      self.Rpt3OpeningBalanceNonRec:int = obj["Rpt3OpeningBalanceNonRec"]
      self.Rpt3CrBalanceNonRec:int = obj["Rpt3CrBalanceNonRec"]
      self.Rpt3DbBalanceNonRec:int = obj["Rpt3DbBalanceNonRec"]
      self.Rpt3CurrentBalanceNonRec:int = obj["Rpt3CurrentBalanceNonRec"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BalanceTableset:
   def __init__(self, obj):
      self.Balance:list[Erp_Tablesets_BalanceRow] = obj["Balance"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankAcctAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.BankAcctID:str = obj["BankAcctID"]
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

class Erp_Tablesets_BankAcctListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description of the bank account.  """  
      self.CheckingAccount:str = obj["CheckingAccount"]
      """  The account number for the bank account. Used for reference only.  """  
      self.Closed:bool = obj["Closed"]
      """  Indicates whether or not the bank account is an active account.  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.APPaymentUseBankAvg:bool = obj["APPaymentUseBankAvg"]
      """  Use the bank average value as the rate for payments from this account.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OpenStatement:bool = obj["OpenStatement"]
      """  Indicates of bank account that now have an open statement waiting to be finally matched/posted.  """  
      self.PositivePayRemoteID:str = obj["PositivePayRemoteID"]
      """  PositivePayRemoteID  """  
      self.PositivePayBatchID:str = obj["PositivePayBatchID"]
      """  PositivePayBatchID  """  
      self.DefPosPayEFTHeadUID:int = obj["DefPosPayEFTHeadUID"]
      """  DefPosPayEFTHeadUID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankAcctListTableset:
   def __init__(self, obj):
      self.BankAcctList:list[Erp_Tablesets_BankAcctListRow] = obj["BankAcctList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankAcctRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account assigned by the user.  """  
      self.Description:str = obj["Description"]
      """  Full description of the bank account.  """  
      self.CheckingAccount:str = obj["CheckingAccount"]
      """  The account number for the bank account. Used for reference only.  """  
      self.Closed:bool = obj["Closed"]
      """  Indicates whether or not the bank account is an active account.  """  
      self.OpeningBalance:int = obj["OpeningBalance"]
      """  The Opening Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance and becomes the opening balance for the next statement.  """  
      self.OpeningDate:str = obj["OpeningDate"]
      """  The Opening Date of the Bank Account.  When a bank reconciliation is posted, the next statement's opening date is set to the posted reconciliation's Closing Date + 1 and becomes the opening date for the next statement.  """  
      self.ClosingBalance:int = obj["ClosingBalance"]
      """  The Closing Balance of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing balance.  """  
      self.ClosingDate:str = obj["ClosingDate"]
      """  The Closing Date of the Bank Account. When a bank reconciliation is posted, this field is set to the posted reconciliation's closing date.  """  
      self.BankRoutingNum:str = obj["BankRoutingNum"]
      """  The bank's routing number.  """  
      self.BankCheckDigit:int = obj["BankCheckDigit"]
      """  The check digit for the bank.  """  
      self.BankName:str = obj["BankName"]
      """  The Bank's full name.  """  
      self.ServClassCode:str = obj["ServClassCode"]
      """   Service Class Code 200 = Mixed debit or credit entries and pre-notification entries.

Contact your bank for the appropriate value.  """  
      self.EntryClassCode:str = obj["EntryClassCode"]
      """   PPD - Prearranged Payments and Deposits for consumer items.
CCD - Cash concentration and disbursements for non-consumer items.
REV - Reversal Items.

Contact your bank for the appropriate value.  """  
      self.CDJournalCode:str = obj["CDJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for A/P checks.  Normally this would be called Cash Disbursements Journal.  """  
      self.PRJournalCode:str = obj["PRJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for P/R checks.  Normally this would be called Payroll Journal.  """  
      self.CRJournalCode:str = obj["CRJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for A/R cash receipts. Normally this would be called the Cash Receipts Journal.  """  
      self.BKJournalCode:str = obj["BKJournalCode"]
      """  The JrnlCode.JournalCode value of the Journal that will be used for Bank transactions made in the check reconciliation process.  """  
      self.BankSlip:str = obj["BankSlip"]
      """  The identifier of the Bank Slip document (bank statement.) The user enters a bank slip during the bank reconciliation process.  This is then written into the related GLJrnDtl records. Pertains to transactions related to a bank (checks, receipts, transfers, adjustments)  """  
      self.ExportDecimalPoint:bool = obj["ExportDecimalPoint"]
      """  Indicates if the decimal point in decimal fields should be exported when exporting electronic payments. For example, if this is set to no then 10.00 it would be exported as 1000.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency.CurrencyCode of the currency that the bank account is denominated in.  """  
      self.BankCompID:str = obj["BankCompID"]
      """  Assigned by the bank.  Uniquely identifies your company to the bank.  """  
      self.DebNoteOnly:bool = obj["DebNoteOnly"]
      """  Indicates whether or not the bank account is for Debit Notes only.  If this flag is yes the bank could be used in Cash Receipts  only.  """  
      self.ReconciledBalance:bool = obj["ReconciledBalance"]
      """  Allows you to keep a reconciled balance in AR when this check box is  """  
      self.UsePendAcct:bool = obj["UsePendAcct"]
      """  Allows you to keep a reconciled balance in AP when this check box is  """  
      self.BankIdentifier:str = obj["BankIdentifier"]
      """  Swift Number or ABA Routing Number  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code  """  
      self.APPaymentUseBankAvg:bool = obj["APPaymentUseBankAvg"]
      """  Use the bank average value as the rate for payments from this account.  """  
      self.PayerRef:str = obj["PayerRef"]
      """  Payer Reference  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  Tax Payer ID  """  
      self.NextPINum:int = obj["NextPINum"]
      """  Future Use - Starting Number for Bank level PI Numbering  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.NumPIDigits:int = obj["NumPIDigits"]
      """  Future Use - Number of digits allowed in PI Numbering  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Free Form Type Code. Used in localizations.  """  
      self.TransferPersonName:str = obj["TransferPersonName"]
      """  Free Form Person Name. Used in localizations.  """  
      self.TransferPersonCode:str = obj["TransferPersonCode"]
      """  Free Form Person code. Used in localizations.  """  
      self.AccountType:str = obj["AccountType"]
      """  Account Type.  """  
      self.LOCLimit:int = obj["LOCLimit"]
      """  Letter of Credit Limit.  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name of Bank, which is consistent with Legal Names field for trading partners.  """  
      self.FloatAmt:int = obj["FloatAmt"]
      """  Float amount for the bank account.  """  
      self.DocLOCLimit:int = obj["DocLOCLimit"]
      """  Letter of Credit Limit in bank's currency.  """  
      self.Rpt1LOCLimit:int = obj["Rpt1LOCLimit"]
      """  Letter of Credit Limit in reporting currency 1.  """  
      self.Rpt2LOCLimit:int = obj["Rpt2LOCLimit"]
      """  Letter of Credit Limit in reporting currency 2.  """  
      self.Rpt3LOCLimit:int = obj["Rpt3LOCLimit"]
      """  Letter of Credit Limit in reporting currency 3.  """  
      self.AutoStatementImport:bool = obj["AutoStatementImport"]
      """  Auto Statement Import  """  
      self.AutoMatchStatement:bool = obj["AutoMatchStatement"]
      """  Specifies whether the application automatically attempts to extract invoice numbers from the statement lines  """  
      self.AutoRecDocuments:bool = obj["AutoRecDocuments"]
      """  Auto Rec Documents  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Specifies a default electronic interface for importing bank statements for  """  
      self.AutoRetrieve:bool = obj["AutoRetrieve"]
      """  If this check box is selected, then after importing a bank statement the application automatically displays all  """  
      self.FilterByLine:bool = obj["FilterByLine"]
      """  Filter By Line  """  
      self.CreditorID:str = obj["CreditorID"]
      """  CreditorID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AutoRcgARRefNum:bool = obj["AutoRcgARRefNum"]
      """  Specify whether reference number verification is applied during automatic  """  
      self.AutoRcgARCustomer:bool = obj["AutoRcgARCustomer"]
      """  Specify whether customer verification is applied during automatic  """  
      self.AutoRcgARTranDate:bool = obj["AutoRcgARTranDate"]
      """  Specify whether transaction date verification is applied during automatic  """  
      self.AutoRcgAPRefNum:bool = obj["AutoRcgAPRefNum"]
      """  Specify whether reference number verification is applied during automatic  """  
      self.AutoRcgAPSupplier:bool = obj["AutoRcgAPSupplier"]
      """  Specify whether supplier verification is applied during automatic  """  
      self.AutoRcgAPTranDate:bool = obj["AutoRcgAPTranDate"]
      """  Specify whether transaction date verification is applied during automatic  """  
      self.AutoRcgUnknownTran:bool = obj["AutoRcgUnknownTran"]
      """  This parameter defines the application behavior in case the transactions do  """  
      self.CHDTAID:str = obj["CHDTAID"]
      """  CHDTAID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.BankType:str = obj["BankType"]
      """  BankType  """  
      self.AutoCashMovement:bool = obj["AutoCashMovement"]
      """  Select this checkbox to enable the automatic creation of invoice cash receipts.  """  
      self.ParamCode:str = obj["ParamCode"]
      """  Specify the parsing parameter ID which is used during automatic bank  """  
      self.AutoOnAccountReceipt:bool = obj["AutoOnAccountReceipt"]
      """  This check box determines the application logic when it cannot find invoices where customer, amount and date  """  
      self.AutoInvoicePayment:bool = obj["AutoInvoicePayment"]
      """  Auto Invoice Payment  """  
      self.AutoBankTransferSameCurr:bool = obj["AutoBankTransferSameCurr"]
      """  Select this checkbox to enable the automatic creation of same currency bank transfer transactions during automatic  """  
      self.AutoBankTransferCrossCurr:bool = obj["AutoBankTransferCrossCurr"]
      """  Select this checkbox to enable the automatic creation of cross currency bank transfer transactions during automatic  """  
      self.AutoBankAdjustment:bool = obj["AutoBankAdjustment"]
      """  Select this checkbox to enable the automatic creation of bank adjustment transactions during automatic bank  """  
      self.POBankAcctNum:str = obj["POBankAcctNum"]
      """  POBankAcctNum  """  
      self.BankCustNum:str = obj["BankCustNum"]
      """  BankCustNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  Select this check box to enable the automatic creation of reverse cash receipts and voided AP payments transactions  """  
      self.PeriodThreshold:int = obj["PeriodThreshold"]
      """  Specifies the number of periods before opening date which will be retrieved during bank reconciliation. If you  """  
      self.PRAlignTax:bool = obj["PRAlignTax"]
      """  PRAlignTax  """  
      self.PRLinePerPRCheck:int = obj["PRLinePerPRCheck"]
      """  PRLinePerPRCheck  """  
      self.PRPreprintedCheckNumber:bool = obj["PRPreprintedCheckNumber"]
      """  PRPreprintedCheckNumber  """  
      self.PayrollCheckingAccount:bool = obj["PayrollCheckingAccount"]
      """  If you select this check box, the application sets the type of lines with  """  
      self.RBankNum:str = obj["RBankNum"]
      """  RBankNum  """  
      self.RBranchNum:str = obj["RBranchNum"]
      """  RBranchNum  """  
      self.JPBankName:str = obj["JPBankName"]
      """  JPBankName  """  
      self.JPBranchName:str = obj["JPBranchName"]
      """  JPBranchName  """  
      self.BankTranfAccountType:str = obj["BankTranfAccountType"]
      """  BankTranfAccountType  """  
      self.Address1:str = obj["Address1"]
      """  Address1  """  
      self.Address2:str = obj["Address2"]
      """  Address2  """  
      self.Address3:str = obj["Address3"]
      """  Address3  """  
      self.City:str = obj["City"]
      """  City  """  
      self.PostalCode:str = obj["PostalCode"]
      """  PostalCode  """  
      self.State:str = obj["State"]
      """  State  """  
      self.CountryNum:int = obj["CountryNum"]
      """  CountryNum  """  
      self.LName:str = obj["LName"]
      """  LName  """  
      self.MsgIDCounter:str = obj["MsgIDCounter"]
      """  MsgIDCounter  """  
      self.ConsInvPmt:bool = obj["ConsInvPmt"]
      """  ConsInvPmt  """  
      self.PreprintedCheckNum:bool = obj["PreprintedCheckNum"]
      """  PreprintedCheckNum  """  
      self.InvPerCheckStub:int = obj["InvPerCheckStub"]
      """  InvPerCheckStub  """  
      self.ReconcileOtherBalances:bool = obj["ReconcileOtherBalances"]
      """  Allows you to keep a reconciled balance for transactions other than AP payments and AR cash receipts (such as  """  
      self.RecBalFiscalYear:int = obj["RecBalFiscalYear"]
      """  RecBalFiscalYear  """  
      self.RecBalFiscalPeriod:int = obj["RecBalFiscalPeriod"]
      """  RecBalFiscalPeriod  """  
      self.RecBalFiscalYearSuffix:str = obj["RecBalFiscalYearSuffix"]
      """  RecBalFiscalYearSuffix  """  
      self.RevalueUseRecBal:bool = obj["RevalueUseRecBal"]
      """  RevalueUseRecBal  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.COIsOneTimeBankAcct:bool = obj["COIsOneTimeBankAcct"]
      """  COIsOneTimeBankAcct  """  
      self.AutoCustBalanceReceipt:bool = obj["AutoCustBalanceReceipt"]
      """  Select this checkbox to enable the automatic creation of cash receipts based on customer balance. This option  """  
      self.MatchTolerance:int = obj["MatchTolerance"]
      """  This parameter determines maximum allowed percent difference between amounts of the unallocated statement  """  
      self.TranTemplateID:str = obj["TranTemplateID"]
      """  Specify the ID of template with the set of transaction codes. It is assigned to the bank account. Refer to the Bank  """  
      self.AutoCustBalanceReceiptApplyAll:bool = obj["AutoCustBalanceReceiptApplyAll"]
      """  This check box changes the application logic when it creates cash receipts based on customer balance.  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MXSATCode  """  
      self.MXSATNameShort:str = obj["MXSATNameShort"]
      """  MXSATNameShort  """  
      self.MXSATNameFull:str = obj["MXSATNameFull"]
      """  MXSATNameFull  """  
      self.CNSellerBankName:str = obj["CNSellerBankName"]
      """  CNSellerBankName  """  
      self.CNSellerAddress:str = obj["CNSellerAddress"]
      """  CNSellerAddress  """  
      self.ClearBankExchRate:str = obj["ClearBankExchRate"]
      """  ClearBankExchRate  """  
      self.PositivePayRemoteID:str = obj["PositivePayRemoteID"]
      """  PositivePayRemoteID  """  
      self.PositivePayBatchID:str = obj["PositivePayBatchID"]
      """  PositivePayBatchID  """  
      self.DefPosPayEFTHeadUID:int = obj["DefPosPayEFTHeadUID"]
      """  DefPosPayEFTHeadUID  """  
      self.LogoFont:str = obj["LogoFont"]
      """  Font used when printing the logo in MICR check.  """  
      self.LogoType:str = obj["LogoType"]
      """  Logo type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  """  
      self.LogoImageID:str = obj["LogoImageID"]
      """  Image ID for the image used as logo in MICR check.  """  
      self.LogoText01:str = obj["LogoText01"]
      """  First line for logo's text.  """  
      self.LogoText02:str = obj["LogoText02"]
      """  Second line for logo's text.  """  
      self.LogoText03:str = obj["LogoText03"]
      """  Third line for logo's text.  """  
      self.LogoText04:str = obj["LogoText04"]
      """  Fourth line for logo's text.  """  
      self.LogoText05:str = obj["LogoText05"]
      """  Fifth line for logo's text.  """  
      self.LogoText06:str = obj["LogoText06"]
      """  Sixth line for logo's text.  """  
      self.SignatureFont:str = obj["SignatureFont"]
      """  Font used when printing the signature in MICR check.  """  
      self.SignatureType:str = obj["SignatureType"]
      """  Signature type, stores "I" when is Image and "T" when is text and "Override in Blank" when the bank check doesn't need modifications.  """  
      self.SignatureImageID:str = obj["SignatureImageID"]
      """  Image ID for the image used as signature in MICR check.  """  
      self.SignatureText01:str = obj["SignatureText01"]
      """  First line for signature's text.  """  
      self.SignatureText02:str = obj["SignatureText02"]
      """  Second line for signature's text.  """  
      self.SignatureText03:str = obj["SignatureText03"]
      """  Third line for signature's text.  """  
      self.SignatureText04:str = obj["SignatureText04"]
      """  Fourth line for signature's text.  """  
      self.SignatureText05:str = obj["SignatureText05"]
      """  Fifth line for signature's text.  """  
      self.SignatureText06:str = obj["SignatureText06"]
      """  Sixth line for signature's text.  """  
      self.PREntryClassCode:str = obj["PREntryClassCode"]
      """  To be used when processing the electronic interface for direct deposit check deductions.  """  
      self.PRPMEFTHeadUID:int = obj["PRPMEFTHeadUID"]
      """  Id of the Electronic Interface to be used when processing a Payroll Group.  """  
      self.PEDetNationalBank:bool = obj["PEDetNationalBank"]
      """  PEDetNationalBank  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """  BankGiroAcctNbr  """  
      self.ParentPlant:str = obj["ParentPlant"]
      """  Default Parent Site. This site is a default site that is paying for invoices.  """  
      self.ChildPlantList:str = obj["ChildPlantList"]
      """  Default Child Sites. This is a default list of sites, which can be child sites at the time of payment  """  
      self.BalanceType:int = obj["BalanceType"]
      """  This option is to select which balances will be displayed (ongoing, reconciled, or non Reconciled).  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrencyCode:str = obj["BaseCurrCurrencyCode"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CHScrISRPartyID:str = obj["CHScrISRPartyID"]
      """  ISR Party Number in format XX-#####V-P (CSF Switzerland)  """  
      self.CurrencySwitch:bool = obj["CurrencySwitch"]
      self.PayMethod:str = obj["PayMethod"]
      """  Pay Method Type for Denmark localization  """  
      self.PendingCashAcctDesc:str = obj["PendingCashAcctDesc"]
      """  Pending Cash Account Description  """  
      self.PORateGrp:str = obj["PORateGrp"]
      """  Purchase and Expenditure Rate Group  """  
      self.PORateGrpDescription:str = obj["PORateGrpDescription"]
      """  PO RateGrp Description  """  
      self.VarianceAcctDesc:str = obj["VarianceAcctDesc"]
      """  Variance Account Description  """  
      self.AssociatedToDoc:bool = obj["AssociatedToDoc"]
      """  This external field is created to hold the validation for the bank to be associated for any document. this will help to enable/disable field in case a crated bank account is already associated to any document or transaction.  """  
      self.EnableMICR:bool = obj["EnableMICR"]
      """  Enable MICR Check panel  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.BKJournalCodeDescJrnlDescription:str = obj["BKJournalCodeDescJrnlDescription"]
      self.CDJournalCodeDescJrnlDescription:str = obj["CDJournalCodeDescJrnlDescription"]
      self.CRJournalCodeDescJrnlDescription:str = obj["CRJournalCodeDescJrnlDescription"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.DefPosPayEFTHeadUIDName:str = obj["DefPosPayEFTHeadUIDName"]
      self.EFTHeadName:str = obj["EFTHeadName"]
      self.PRJournalCodeDescJrnlDescription:str = obj["PRJournalCodeDescJrnlDescription"]
      self.PRPMEFTHeadUIDName:str = obj["PRPMEFTHeadUIDName"]
      self.XbSystSiteIsLegalEntity:bool = obj["XbSystSiteIsLegalEntity"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_BankAcctTableset:
   def __init__(self, obj):
      self.BankAcct:list[Erp_Tablesets_BankAcctRow] = obj["BankAcct"]
      self.BankAcctAttch:list[Erp_Tablesets_BankAcctAttchRow] = obj["BankAcctAttch"]
      self.BankPayMethod:list[Erp_Tablesets_BankPayMethodRow] = obj["BankPayMethod"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankAcctTrackerTableset:
   def __init__(self, obj):
      self.APLOCClosed:list[Erp_Tablesets_APLOCClosedRow] = obj["APLOCClosed"]
      self.APLOCOpen:list[Erp_Tablesets_APLOCOpenRow] = obj["APLOCOpen"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_BankPayMethodRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  Unique identifier of the bank account  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.IsDefault:bool = obj["IsDefault"]
      """  Flag for default payment method  """  
      self.PMSource:int = obj["PMSource"]
      """   Indicated the source of payment method
0 = AP payment method
1 = AR payment method  """  
      self.PaymentNumMask:str = obj["PaymentNumMask"]
      """  PaymentNumMask  """  
      self.StartingSeqNum:str = obj["StartingSeqNum"]
      """  StartingSeqNum  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  System row ID - GUID  """  
      self.DeleteFromParent:bool = obj["DeleteFromParent"]
      """  This field will allow us to delete record marked as default.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtBankAcctTableset:
   def __init__(self, obj):
      self.BankAcct:list[Erp_Tablesets_BankAcctRow] = obj["BankAcct"]
      self.BankAcctAttch:list[Erp_Tablesets_BankAcctAttchRow] = obj["BankAcctAttch"]
      self.BankPayMethod:list[Erp_Tablesets_BankPayMethodRow] = obj["BankPayMethod"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAPLOCClosed_input:
   """ Required : 
   bankAcctID
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  Bank Account ID  """  
      pass

class GetAPLOCClosed_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAcctTrackerTableset] = obj["returnObj"]
      pass

class GetAPLOCOpen_input:
   """ Required : 
   bankAcctID
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      """  Bank Account ID  """  
      pass

class GetAPLOCOpen_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAcctTrackerTableset] = obj["returnObj"]
      pass

class GetBankBalFromDate_input:
   """ Required : 
   date
   bankID
   """  
   def __init__(self, obj):
      self.date:str = obj["date"]
      """  Date  """  
      self.bankID:str = obj["bankID"]
      """  Bank ID  """  
      pass

class GetBankBalFromDate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BalanceTableset] = obj["returnObj"]
      pass

class GetBankBal_input:
   """ Required : 
   fyear
   fyearsuffix
   bankID
   """  
   def __init__(self, obj):
      self.fyear:int = obj["fyear"]
      """  Fiscal Year  """  
      self.fyearsuffix:str = obj["fyearsuffix"]
      """  Fiscal Year Suffix  """  
      self.bankID:str = obj["bankID"]
      """  Bank ID  """  
      pass

class GetBankBal_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BalanceTableset] = obj["returnObj"]
      pass

class GetBaseCurrencySymbol_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   bankAcctID
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAcctTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankAcctTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankAcctTableset] = obj["returnObj"]
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

class GetCurrencyBase_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCurrencyBase:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetEnableMICR_input:
   """ Required : 
   bankAcctID
   """  
   def __init__(self, obj):
      self.bankAcctID:str = obj["bankAcctID"]
      pass

class GetEnableMICR_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_BankAcctListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewBankAcctAttch_input:
   """ Required : 
   ds
   bankAcctID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      pass

class GetNewBankAcctAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankAcct_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class GetNewBankAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewBankPayMethod_input:
   """ Required : 
   ds
   bankAcctID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      self.bankAcctID:str = obj["bankAcctID"]
      pass

class GetNewBankPayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartner_input:
   """ Required : 
   ds
   partnerNum
   partnerType
   partnerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      self.partnerNum:int = obj["partnerNum"]
      self.partnerType:int = obj["partnerType"]
      self.partnerID:str = obj["partnerID"]
      pass

class GetNewPartner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsForMandate_input:
   """ Required : 
   whereClauseBankAcct
   whereClauseBankAcctAttch
   whereClauseBankPayMethod
   whereClauseEntityGLC
   whereClausePartner
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBankAcct:str = obj["whereClauseBankAcct"]
      """  Base Whereclause for BankAcct table.  """  
      self.whereClauseBankAcctAttch:str = obj["whereClauseBankAcctAttch"]
      """  Base Whereclause for BankAcctAttch.  """  
      self.whereClauseBankPayMethod:str = obj["whereClauseBankPayMethod"]
      """  Whereclause for BankPayMethod table  """  
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      """  Whereclause for EntityGLC table  """  
      self.whereClausePartner:str = obj["whereClausePartner"]
      """  Whereclause for Partner table  """  
      self.pageSize:int = obj["pageSize"]
      """  Page size.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Absolute page.  """  
      pass

class GetRowsForMandate_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAcctTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseBankAcct
   whereClauseBankAcctAttch
   whereClauseBankPayMethod
   whereClausePartner
   whereClauseEntityGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseBankAcct:str = obj["whereClauseBankAcct"]
      self.whereClauseBankAcctAttch:str = obj["whereClauseBankAcctAttch"]
      self.whereClauseBankPayMethod:str = obj["whereClauseBankPayMethod"]
      self.whereClausePartner:str = obj["whereClausePartner"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BankAcctTableset] = obj["returnObj"]
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

class ModifySearchIDs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class ModifySearchIDs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankAcctTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtBankAcctTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePartner_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

class ValidatePartner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BankAcctTableset] = obj["ds"]
      pass

      """  output parameters  """  

