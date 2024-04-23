import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PCashDeskSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDesks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDesks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks",headers=creds) as resp:
           return await resp.json()

async def post_PCashDesks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDesks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID(Company, CashDeskID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDesk item
   Description: Calls GetByID to retrieve the PCashDesk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDesk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDesks_Company_CashDeskID(Company, CashDeskID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDesk for the service
   Description: Calls UpdateExt to update PCashDesk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDesk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDesks_Company_CashDeskID(Company, CashDeskID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDesk item
   Description: Call UpdateExt to delete PCashDesk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDesk
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_EntityGLCs(Company, CashDeskID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, CashDeskID, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_PCashDeskAuths(Company, CashDeskID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PCashDeskAuths items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDeskAuths1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAuths",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company, CashDeskID, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDeskAuth item
   Description: Calls GetByID to retrieve the PCashDeskAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAuth1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_PCashDeskOprs(Company, CashDeskID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PCashDeskOprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDeskOprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskOprs",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company, CashDeskID, OprTypeCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDeskOpr item
   Description: Calls GetByID to retrieve the PCashDeskOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskOpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param OprTypeCode: Desc: OprTypeCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_PCashDeskAttches(Company, CashDeskID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PCashDeskAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PCashDeskAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAttches",headers=creds) as resp:
           return await resp.json()

async def get_PCashDesks_Company_CashDeskID_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company, CashDeskID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDeskAttch item
   Description: Calls GetByID to retrieve the PCashDeskAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDesks(" + Company + "," + CashDeskID + ")/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDeskAuths(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDeskAuths items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDeskAuths
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths",headers=creds) as resp:
           return await resp.json()

async def post_PCashDeskAuths(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDeskAuths
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company, CashDeskID, DcdUserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDeskAuth item
   Description: Calls GetByID to retrieve the PCashDeskAuth item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company, CashDeskID, DcdUserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDeskAuth for the service
   Description: Calls UpdateExt to update PCashDeskAuth. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDeskAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskAuthRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDeskAuths_Company_CashDeskID_DcdUserID(Company, CashDeskID, DcdUserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDeskAuth item
   Description: Call UpdateExt to delete PCashDeskAuth item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDeskAuth
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAuths(" + Company + "," + CashDeskID + "," + DcdUserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDeskOprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDeskOprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDeskOprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs",headers=creds) as resp:
           return await resp.json()

async def post_PCashDeskOprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDeskOprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company, CashDeskID, OprTypeCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDeskOpr item
   Description: Calls GetByID to retrieve the PCashDeskOpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param OprTypeCode: Desc: OprTypeCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company, CashDeskID, OprTypeCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDeskOpr for the service
   Description: Calls UpdateExt to update PCashDeskOpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDeskOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param OprTypeCode: Desc: OprTypeCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskOprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDeskOprs_Company_CashDeskID_OprTypeCode(Company, CashDeskID, OprTypeCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDeskOpr item
   Description: Call UpdateExt to delete PCashDeskOpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDeskOpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param OprTypeCode: Desc: OprTypeCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskOprs(" + Company + "," + CashDeskID + "," + OprTypeCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PCashDeskAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PCashDeskAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PCashDeskAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches",headers=creds) as resp:
           return await resp.json()

async def post_PCashDeskAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PCashDeskAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company, CashDeskID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PCashDeskAttch item
   Description: Calls GetByID to retrieve the PCashDeskAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PCashDeskAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company, CashDeskID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PCashDeskAttch for the service
   Description: Calls UpdateExt to update PCashDeskAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PCashDeskAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PCashDeskAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PCashDeskAttches_Company_CashDeskID_DrawingSeq(Company, CashDeskID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PCashDeskAttch item
   Description: Call UpdateExt to delete PCashDeskAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PCashDeskAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CashDeskID: Desc: CashDeskID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/PCashDeskAttches(" + Company + "," + CashDeskID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PCashDeskListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePCashDesk, whereClausePCashDeskAttch, whereClausePCashDeskAuth, whereClausePCashDeskOpr, whereClauseEntityGLC, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePCashDesk=" + whereClausePCashDesk
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePCashDeskAttch=" + whereClausePCashDeskAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePCashDeskAuth=" + whereClausePCashDeskAuth
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePCashDeskOpr=" + whereClausePCashDeskOpr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(cashDeskID, epicorHeaders = None):
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
   params += "cashDeskID=" + cashDeskID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Method to get the Code Description List.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskCurrencyCode
   Description: Method to call when changing the currency code.
   OperationID: ChangePCashDeskCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskEntrustedCashier(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskEntrustedCashier
   Description: Method to call when changing the entrusted cashier.
   OperationID: ChangePCashDeskEntrustedCashier
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskEntrustedCashier_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskEntrustedCashier_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskInitPayrollBal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskInitPayrollBal
   Description: Method to call when changing the initial payroll balance.
   OperationID: ChangePCashDeskInitPayrollBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskInitPayrollBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskInitPayrollBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskInitTotalBal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskInitTotalBal
   Description: Method to call when changing the initial balance.
   OperationID: ChangePCashDeskInitTotalBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskInitTotalBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskInitTotalBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskOpenedFrom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskOpenedFrom
   Description: Method to call when changing the initial balances date.
   OperationID: ChangePCashDeskOpenedFrom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskOpenedFrom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskOpenedFrom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskOprOprTypeCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskOprOprTypeCode
   Description: Method to call when changing the operation type code.
   OperationID: ChangePCashDeskOprOprTypeCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskOprOprTypeCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskOprOprTypeCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskOprTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskOprTranDocTypeID
   Description: Method to call when changing the tran doc type id.
   OperationID: ChangePCashDeskOprTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskOprTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskOprTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskRateGrpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskRateGrpCode
   Description: Method to call when changing the rate group code.
   OperationID: ChangePCashDeskRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCashDeskReportTranDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCashDeskReportTranDocType
   Description: Method to call when changing the report tran document type.
   OperationID: ChangePCashDeskReportTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCashDeskReportTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCashDeskReportTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDeskBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDeskBalance
   Description: Get overall balance for defined Cash Desk
   OperationID: GetCashDeskBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeskBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeskBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDeskBalHist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDeskBalHist
   Description: Get day balances for defined Cash Desk
   OperationID: GetCashDeskBalHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeskBalHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeskBalHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCashDeskDocsHist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCashDeskDocsHist
   Description: Get documents for defined Cash Desk and Date
   OperationID: GetCashDeskDocsHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCashDeskDocsHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeskDocsHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSecurity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSecurity
   Description: Purpose:
Parameters:  none
Notes:
   OperationID: CheckSecurity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSecurity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSecurity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDesk(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDesk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDesk
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDesk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDesk_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDeskAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDeskAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDeskAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDeskAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDeskAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDeskAuth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDeskAuth
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDeskAuth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDeskAuth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDeskAuth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCashDeskOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCashDeskOpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPCashDeskOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCashDeskOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCashDeskOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PCashDeskSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDeskAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskAuthRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDeskAuthRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDeskListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskOprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDeskOprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PCashDeskRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PCashDeskRow] = obj["value"]
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

class Erp_Tablesets_PCashDeskAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashDeskID:str = obj["CashDeskID"]
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

class Erp_Tablesets_PCashDeskAuthRow:
   def __init__(self, obj):
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.CashIssue:bool = obj["CashIssue"]
      """   Checked: User can enter/modify and print petty cash issues (including authorization of draft documents).
Unchecked: User cannot enter/modify cash issues.  """  
      self.CashReceipts:bool = obj["CashReceipts"]
      """   Checked: User can enter/modify and print petty cash receipts (including authorization of draft documents)
Unchecked (default): User cannot enter/modify cash receipts.  """  
      self.ChangeSetup:bool = obj["ChangeSetup"]
      """   Checked: User can change Petty Cash Desk Definition (including modification of authorized users, available operations and GL controls)
Unchecked : User cannot change Petty Cash Desk Definition.  """  
      self.CloseCashDays:bool = obj["CloseCashDays"]
      """  If Yes, user can perform day closing and print daily reports for not yet closed cash days. If No, user cannot perform day closing.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID of the related UserFile record.  """  
      self.ReadOnlyAccess:bool = obj["ReadOnlyAccess"]
      """  If yes, user access is restricted by read-only mode (access to petty cash tracker, reprint authorized and posted  documents and daily documents for closed days only).If No, user has no access to Petty cash Desk.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.UserFileName:str = obj["UserFileName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskListRow:
   def __init__(self, obj):
      self.AllowDraftCI:bool = obj["AllowDraftCI"]
      """   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  """  
      self.AllowDraftCR:bool = obj["AllowDraftCR"]
      """   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  """  
      self.AllowNegBal:bool = obj["AllowNegBal"]
      """  Allow Negative Balance  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DayCloseMode:str = obj["DayCloseMode"]
      """   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  """  
      self.DocInitPayrollBal:int = obj["DocInitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.DocInitTotalBal:int = obj["DocInitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.EntrustedCashier:str = obj["EntrustedCashier"]
      """  Entrusted Cashier  """  
      self.EntrustedFrom:str = obj["EntrustedFrom"]
      """   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  """  
      self.EntrustedTill:str = obj["EntrustedTill"]
      """   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  """  
      self.InitTotalBal:int = obj["InitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.InitPayrollBal:int = obj["InitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.LimitExptPayroll:int = obj["LimitExptPayroll"]
      """  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  """  
      self.LimitTotal:int = obj["LimitTotal"]
      """  Defines Limit (in Cash Desk Currency)  """  
      self.Location:str = obj["Location"]
      """  Cash Desk Location  """  
      self.Name:str = obj["Name"]
      """  Cash Desk Name  """  
      self.OpenedFrom:str = obj["OpenedFrom"]
      """  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.PostingOpt:str = obj["PostingOpt"]
      """   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type  """  
      self.Rpt1InitPayrollBal:int = obj["Rpt1InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt2InitPayrollBal:int = obj["Rpt2InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt3InitPayrollBal:int = obj["Rpt3InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt1InitTotalBal:int = obj["Rpt1InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt2InitTotalBal:int = obj["Rpt2InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt3InitTotalBal:int = obj["Rpt3InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.UseExtnNumForCI:bool = obj["UseExtnNumForCI"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.UseExtnNumForCR:bool = obj["UseExtnNumForCR"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OperationExists:bool = obj["OperationExists"]
      """  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  """  
      self.IsAuthorizedUser:bool = obj["IsAuthorizedUser"]
      """  Indicates if the user is authorized to make changes.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskOprRow:
   def __init__(self, obj):
      self.AllowDraftDoc:bool = obj["AllowDraftDoc"]
      """   Checked: Draft Documents can be used.
Unchecked: Draft Documents are not used.  """  
      self.AllowUseExtnNum:bool = obj["AllowUseExtnNum"]
      """   Checked: External document numbers can be used.
Unchecked: External document numbers are not used.  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.OprTypeEnabled:bool = obj["OprTypeEnabled"]
      """  Indicates that operation type is enabled for this petty cash desk.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  Defines Legal Number related to Transaction Document Type and therefore used for this Operation type.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Cash Operation Type.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Used only in case of Supplier/Customer Recipient/Payer Type and defines contact used to retrieve personal data.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for system transactions PCashRcpt and PCashIssue  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID to define Document Template used for printing  """  
      self.ReportStyleNum:int = obj["ReportStyleNum"]
      """  Report Style to define document template for printing  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OprClassDesc:str = obj["OprClassDesc"]
      """  Description of the operation class  """  
      self.DirectionDesc:str = obj["DirectionDesc"]
      """  Direction description  """  
      self.RecPayerTypeDesc:str = obj["RecPayerTypeDesc"]
      """  Description of the RecPayerType  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  The system transaction type - PCI or PCR.  Used to filter combo list for TranDocTypeID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LegalNumCnfgDescription:str = obj["LegalNumCnfgDescription"]
      self.PCashOprTypeDirection:str = obj["PCashOprTypeDirection"]
      self.PCashOprTypePayrollBal:bool = obj["PCashOprTypePayrollBal"]
      self.PCashOprTypeOprClass:str = obj["PCashOprTypeOprClass"]
      self.PCashOprTypeDescription:str = obj["PCashOprTypeDescription"]
      self.PCashOprTypeRecPayerType:str = obj["PCashOprTypeRecPayerType"]
      self.ReportRptDescription:str = obj["ReportRptDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskRow:
   def __init__(self, obj):
      self.AllowDraftCI:bool = obj["AllowDraftCI"]
      """   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  """  
      self.AllowDraftCR:bool = obj["AllowDraftCR"]
      """   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  """  
      self.AllowNegBal:bool = obj["AllowNegBal"]
      """  Allow Negative Balance  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DayCloseMode:str = obj["DayCloseMode"]
      """   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  """  
      self.DocInitPayrollBal:int = obj["DocInitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.DocInitTotalBal:int = obj["DocInitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.EntrustedCashier:str = obj["EntrustedCashier"]
      """  Entrusted Cashier  """  
      self.EntrustedFrom:str = obj["EntrustedFrom"]
      """   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  """  
      self.EntrustedTill:str = obj["EntrustedTill"]
      """   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  """  
      self.InitTotalBal:int = obj["InitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.InitPayrollBal:int = obj["InitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.LimitExptPayroll:int = obj["LimitExptPayroll"]
      """  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  """  
      self.LimitTotal:int = obj["LimitTotal"]
      """  Defines Limit (in Cash Desk Currency)  """  
      self.Location:str = obj["Location"]
      """  Cash Desk Location  """  
      self.Name:str = obj["Name"]
      """  Cash Desk Name  """  
      self.OpenedFrom:str = obj["OpenedFrom"]
      """  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.PostingOpt:str = obj["PostingOpt"]
      """   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type  """  
      self.Rpt1InitPayrollBal:int = obj["Rpt1InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt2InitPayrollBal:int = obj["Rpt2InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt3InitPayrollBal:int = obj["Rpt3InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt1InitTotalBal:int = obj["Rpt1InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt2InitTotalBal:int = obj["Rpt2InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt3InitTotalBal:int = obj["Rpt3InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.UseExtnNumForCI:bool = obj["UseExtnNumForCI"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.UseExtnNumForCR:bool = obj["UseExtnNumForCR"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.FloatAmt:int = obj["FloatAmt"]
      """  FloatAmt  """  
      self.CashPayMethodPMUID:int = obj["CashPayMethodPMUID"]
      """  CashPayMethodPMUID  """  
      self.CashPayMethodName:str = obj["CashPayMethodName"]
      """  CashPayMethodName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintLastPage:int = obj["PrintLastPage"]
      """  PrintLastPage  """  
      self.PrintPerPage:int = obj["PrintPerPage"]
      """  PrintPerPage  """  
      self.ReportTranDocType:str = obj["ReportTranDocType"]
      """  ReportTranDocType  """  
      self.IsAuthorizedUser:bool = obj["IsAuthorizedUser"]
      """  Indicates if the user is authorized to make changes.  """  
      self.LegalNumberDesc:str = obj["LegalNumberDesc"]
      self.OperationExists:bool = obj["OperationExists"]
      """  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  """  
      self.ReportTranDocTypeDesc:str = obj["ReportTranDocTypeDesc"]
      self.Direction:str = obj["Direction"]
      """  BD ? Both Directions; CI ? Only Issues; CR ? Only Receipts;  """  
      self.IsAuthorizedCR:bool = obj["IsAuthorizedCR"]
      """  The user is authorized for Cash Receipt  """  
      self.IsAuthorizedCI:bool = obj["IsAuthorizedCI"]
      """  The user is authorized for Cash Issue  """  
      self.UserCanRead:bool = obj["UserCanRead"]
      """  User has access to read the Petty Cash Desk.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangePCashDeskCurrencyCode_input:
   """ Required : 
   proposedCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.proposedCurrencyCode:str = obj["proposedCurrencyCode"]
      """  The proposed currency code  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskEntrustedCashier_input:
   """ Required : 
   proposedEntrustedCashier
   ds
   """  
   def __init__(self, obj):
      self.proposedEntrustedCashier:str = obj["proposedEntrustedCashier"]
      """  The proposed entrusted cashier  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskEntrustedCashier_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskInitPayrollBal_input:
   """ Required : 
   proposedInitPayrollBal
   docOrBase
   ds
   """  
   def __init__(self, obj):
      self.proposedInitPayrollBal:int = obj["proposedInitPayrollBal"]
      """  The proposed initial payroll balance  """  
      self.docOrBase:str = obj["docOrBase"]
      """  Was the base amount (Base) or doc amount (Doc) changed  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskInitPayrollBal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskInitTotalBal_input:
   """ Required : 
   proposedInitTotalBal
   docOrBase
   ds
   """  
   def __init__(self, obj):
      self.proposedInitTotalBal:int = obj["proposedInitTotalBal"]
      """  The proposed initial balance  """  
      self.docOrBase:str = obj["docOrBase"]
      """  Was the base amount (Base) or doc amount (Doc) changed  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskInitTotalBal_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskOpenedFrom_input:
   """ Required : 
   proposedOpenedFrom
   ds
   """  
   def __init__(self, obj):
      self.proposedOpenedFrom:str = obj["proposedOpenedFrom"]
      """  The proposed opened from date  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskOpenedFrom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskOprOprTypeCode_input:
   """ Required : 
   proposedOprTypeCode
   ds
   """  
   def __init__(self, obj):
      self.proposedOprTypeCode:str = obj["proposedOprTypeCode"]
      """  The proposed operation type code  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskOprOprTypeCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskOprTranDocTypeID_input:
   """ Required : 
   proposedTranDocTypeID
   ds
   """  
   def __init__(self, obj):
      self.proposedTranDocTypeID:str = obj["proposedTranDocTypeID"]
      """  The proposed tran doc type id  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskOprTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskRateGrpCode_input:
   """ Required : 
   proposedRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.proposedRateGrpCode:str = obj["proposedRateGrpCode"]
      """  The proposed rate group code  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskRateGrpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCashDeskReportTranDocType_input:
   """ Required : 
   proposedReportTranDocType
   ds
   """  
   def __init__(self, obj):
      self.proposedReportTranDocType:str = obj["proposedReportTranDocType"]
      """  The proposed report tran document type  """  
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class ChangePCashDeskReportTranDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckSecurity_input:
   """ Required : 
   cashDeskID
   raiseException
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      self.raiseException:bool = obj["raiseException"]
      pass

class CheckSecurity_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   cashDeskID
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
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

class Erp_Tablesets_PCashDeskAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CashDeskID:str = obj["CashDeskID"]
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

class Erp_Tablesets_PCashDeskAuthRow:
   def __init__(self, obj):
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.CashIssue:bool = obj["CashIssue"]
      """   Checked: User can enter/modify and print petty cash issues (including authorization of draft documents).
Unchecked: User cannot enter/modify cash issues.  """  
      self.CashReceipts:bool = obj["CashReceipts"]
      """   Checked: User can enter/modify and print petty cash receipts (including authorization of draft documents)
Unchecked (default): User cannot enter/modify cash receipts.  """  
      self.ChangeSetup:bool = obj["ChangeSetup"]
      """   Checked: User can change Petty Cash Desk Definition (including modification of authorized users, available operations and GL controls)
Unchecked : User cannot change Petty Cash Desk Definition.  """  
      self.CloseCashDays:bool = obj["CloseCashDays"]
      """  If Yes, user can perform day closing and print daily reports for not yet closed cash days. If No, user cannot perform day closing.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID of the related UserFile record.  """  
      self.ReadOnlyAccess:bool = obj["ReadOnlyAccess"]
      """  If yes, user access is restricted by read-only mode (access to petty cash tracker, reprint authorized and posted  documents and daily documents for closed days only).If No, user has no access to Petty cash Desk.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.UserFileName:str = obj["UserFileName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskBalHistRow:
   def __init__(self, obj):
      self.Date:str = obj["Date"]
      self.Closed:bool = obj["Closed"]
      self.OpeningBalance:int = obj["OpeningBalance"]
      self.DocOpeningBalance:int = obj["DocOpeningBalance"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Rpt1OpeningBalance:int = obj["Rpt1OpeningBalance"]
      self.Rpt2OpeningBalance:int = obj["Rpt2OpeningBalance"]
      self.Rpt3OpeningBalance:int = obj["Rpt3OpeningBalance"]
      self.Receipts:int = obj["Receipts"]
      self.AmountReceived:int = obj["AmountReceived"]
      self.DocAmountReceived:int = obj["DocAmountReceived"]
      self.Rpt1AmountReceived:int = obj["Rpt1AmountReceived"]
      self.Rpt2AmountReceived:int = obj["Rpt2AmountReceived"]
      self.Rpt3AmountReceived:int = obj["Rpt3AmountReceived"]
      self.Issues:int = obj["Issues"]
      self.AmountIssued:int = obj["AmountIssued"]
      """  Amount issued per Cash Day  """  
      self.DocAmountIssued:int = obj["DocAmountIssued"]
      self.Rpt1AmountIssued:int = obj["Rpt1AmountIssued"]
      self.Rpt2AmountIssued:int = obj["Rpt2AmountIssued"]
      self.Rpt3AmountIssued:int = obj["Rpt3AmountIssued"]
      self.ClosingBalance:int = obj["ClosingBalance"]
      self.DocClosingBalance:int = obj["DocClosingBalance"]
      self.Rpt1ClosingBalance:int = obj["Rpt1ClosingBalance"]
      self.Rpt2ClosingBalance:int = obj["Rpt2ClosingBalance"]
      self.Rpt3ClosingBalance:int = obj["Rpt3ClosingBalance"]
      self.GainLossBal:int = obj["GainLossBal"]
      """  Revaluation Gain / Loss  """  
      self.Rpt1GainLossBal:int = obj["Rpt1GainLossBal"]
      self.Rpt2GainLossBal:int = obj["Rpt2GainLossBal"]
      self.Rpt3GainLossBal:int = obj["Rpt3GainLossBal"]
      self.DocGainLossBal:int = obj["DocGainLossBal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskBalanceRow:
   def __init__(self, obj):
      self.DateLastClosed:str = obj["DateLastClosed"]
      """  The Last Petty Cash Desk Closed Date  """  
      self.LastClosedDayBalTotal:int = obj["LastClosedDayBalTotal"]
      """  Total Balance as per above date  """  
      self.DocLastClosedDayBalTotal:int = obj["DocLastClosedDayBalTotal"]
      """  Total Balance as per above date in document currency  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.Rpt1LastClosedDayBalTotal:int = obj["Rpt1LastClosedDayBalTotal"]
      self.Rpt2LastClosedDayBalTotal:int = obj["Rpt2LastClosedDayBalTotal"]
      self.Rpt3LastClosedDayBalTotal:int = obj["Rpt3LastClosedDayBalTotal"]
      self.LastClosedDayBalPayroll:int = obj["LastClosedDayBalPayroll"]
      """  Payroll Balance as per above date  """  
      self.DocLastClosedDayBalPayroll:int = obj["DocLastClosedDayBalPayroll"]
      self.Rpt1LastClosedDayBalPayroll:int = obj["Rpt1LastClosedDayBalPayroll"]
      self.Rpt2LastClosedDayBalPayroll:int = obj["Rpt2LastClosedDayBalPayroll"]
      self.Rpt3LastClosedDayBalPayroll:int = obj["Rpt3LastClosedDayBalPayroll"]
      self.LatestAuthDocDate:str = obj["LatestAuthDocDate"]
      """  Latest Authorized Document Date  """  
      self.CurrBalTotal:int = obj["CurrBalTotal"]
      """  Current Balance (Total)  """  
      self.DocCurrBalTotal:int = obj["DocCurrBalTotal"]
      self.Rpt1CurrBalTotal:int = obj["Rpt1CurrBalTotal"]
      self.Rpt2CurrBalTotal:int = obj["Rpt2CurrBalTotal"]
      self.Rpt3CurrBalTotal:int = obj["Rpt3CurrBalTotal"]
      self.CurrBalPayroll:int = obj["CurrBalPayroll"]
      """  Payroll Balance as per above date  """  
      self.DocCurrBalPayroll:int = obj["DocCurrBalPayroll"]
      """  Payroll Balance as per above date  """  
      self.Rpt1CurrBalPayroll:int = obj["Rpt1CurrBalPayroll"]
      """  Payroll Balance as per above date  """  
      self.Rpt2CurrBalPayroll:int = obj["Rpt2CurrBalPayroll"]
      """  Payroll Balance as per above date  """  
      self.Rpt3CurrBalPayroll:int = obj["Rpt3CurrBalPayroll"]
      """  Payroll Balance as per above date  """  
      self.LastDraftDocDate:str = obj["LastDraftDocDate"]
      """  Date of Last Draft Document  """  
      self.CurrDraftBalTotal:int = obj["CurrDraftBalTotal"]
      """  Total Balance as per above date (including draft documents)  """  
      self.Rpt1CurrDraftBalTotal:int = obj["Rpt1CurrDraftBalTotal"]
      self.DocCurrDraftBalTotal:int = obj["DocCurrDraftBalTotal"]
      self.Rpt2CurrDraftBalTotal:int = obj["Rpt2CurrDraftBalTotal"]
      self.Rpt3CurrDraftBalTotal:int = obj["Rpt3CurrDraftBalTotal"]
      self.CurrDraftBalPayroll:int = obj["CurrDraftBalPayroll"]
      self.DocCurrDraftBalPayroll:int = obj["DocCurrDraftBalPayroll"]
      self.Rpt1CurrDraftBalPayroll:int = obj["Rpt1CurrDraftBalPayroll"]
      self.Rpt2CurrDraftBalPayroll:int = obj["Rpt2CurrDraftBalPayroll"]
      self.Rpt3CurrDraftBalPayroll:int = obj["Rpt3CurrDraftBalPayroll"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskDocsHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.ReferenceNum:int = obj["ReferenceNum"]
      """  Reference Number, unique identifier of Petty Cash Document, sequentially assigned for each Petty Cash Desk internal number (never reused)  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Apply Date of Operation  """  
      self.AuthorizedBy:str = obj["AuthorizedBy"]
      """  User Id of the user who authorize the record.  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Comment:str = obj["Comment"]
      """  Comment  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  User ID of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Date when the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency  """  
      self.DaySeqNum:int = obj["DaySeqNum"]
      """  Sequential number of Cash Receipt or Cash Issue for Petty Cask Desk within Apply Cash Day. Used for Authorized documents only.  """  
      self.Direction:str = obj["Direction"]
      """   CI ? Cash Issue
CR ? Cash Receipt  """  
      self.Draft:bool = obj["Draft"]
      """  Available only when configuration of operation type allows using of draft documents.  """  
      self.ExternalNum:str = obj["ExternalNum"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar is Company Calendar  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Defined by Apply Date for Company Calendar  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Defined by Apply Date for Company Calendar  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Defined by Apply Date for Company Calendar  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number of the record. Available only for Authorized Documents.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Petty Cash Operation Type  """  
      self.PayrollBalOpr:bool = obj["PayrollBalOpr"]
      """  According to Operation Type  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.Printed:bool = obj["Printed"]
      """  Printed  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason  """  
      self.RvJrnUID:int = obj["RvJrnUID"]
      """  Review Journal.  """  
      self.RecipientType:str = obj["RecipientType"]
      """   According to Operation type definition:
E - Employee; S - Supplier; C - Customer; B - Bank; CD - Cash Desk; O - Other  """  
      self.CustNum:int = obj["CustNum"]
      """  Customer  """  
      self.CustShipTo:str = obj["CustShipTo"]
      """  Ship To Customer (CustCon.ShipToNum)  """  
      self.CustConNum:int = obj["CustConNum"]
      """  Customer Contact Number (CustCon.ConNum)  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier  """  
      self.VendPurPoint:str = obj["VendPurPoint"]
      """  Purchase point from Vendor.(VendCon.PurPoint)  """  
      self.VendConNum:int = obj["VendConNum"]
      """  Supplier Contact number (VendCon.ConNum)  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      self.BankAcctID:str = obj["BankAcctID"]
      """  Bank Account  """  
      self.OrganizationID:str = obj["OrganizationID"]
      """  Depending on Recipient Type: Supplier ID; Customer ID; Bank Account ID; Cash Desk ID. Not available for Employee and Other.  """  
      self.OrganizationName:str = obj["OrganizationName"]
      """   Depending on Recipient Type: Supplier Name; Customer Name;
Bank Account Name; Cash Desk Name; Company Name (default for Employee and Other Recipient types).  """  
      self.PersonName:str = obj["PersonName"]
      """   Depending on Recipient type: Employee Display Name (composed from First Name, Middle Initial and Last Name); Supplier Contact Display Name; Customer Contact Display Name; Cash Desk Cashier Name, or Entrusted Cashier Name (recipient of cash transfer); Own Cash Desk Cashier name.
Person Name can be modified. There is no default for Bank and Other recipient.  """  
      self.PersonalData:str = obj["PersonalData"]
      """  Default of Personal Data can be composed using BPM, and can be adjusted by user.  """  
      self.DocCashAmt:int = obj["DocCashAmt"]
      """  Amount to be paid/received in cash  """  
      self.CashAmt:int = obj["CashAmt"]
      """  Amount to be paid/received in cash  """  
      self.Rpt1CashAmt:int = obj["Rpt1CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.Rpt2CashAmt:int = obj["Rpt2CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.Rpt3CashAmt:int = obj["Rpt3CashAmt"]
      """  Amount to be paid/received in cash in reporting Currency  """  
      self.DocGrossAmt:int = obj["DocGrossAmt"]
      """  Gross Amount to update AP or AR  """  
      self.GrossAmt:int = obj["GrossAmt"]
      """  Gross Amount to update AP or AR  """  
      self.Rpt1GrossAmt:int = obj["Rpt1GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.Rpt2GrossAmt:int = obj["Rpt2GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.Rpt3GrossAmt:int = obj["Rpt3GrossAmt"]
      """  Gross Amount in reporting Currency  """  
      self.DocDiscount:int = obj["DocDiscount"]
      """  Amount of Applied Cash Discount (AP or AR)  """  
      self.Discount:int = obj["Discount"]
      """  Amount of Applied Cash Discount (AP or AR)  """  
      self.Rpt1Discount:int = obj["Rpt1Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.Rpt2Discount:int = obj["Rpt2Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.Rpt3Discount:int = obj["Rpt3Discount"]
      """  Amount of Applied Cash Discount  in reporting Currency  """  
      self.DocWithholdAmt:int = obj["DocWithholdAmt"]
      """  Amount of calculated withhold taxes (AR or AP)  """  
      self.WithholdAmt:int = obj["WithholdAmt"]
      """  Amount of calculated withhold taxes (AR or AP)  """  
      self.Rpt1WithholdAmt:int = obj["Rpt1WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.Rpt2WithholdAmt:int = obj["Rpt2WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.Rpt3WithholdAmt:int = obj["Rpt3WithholdAmt"]
      """  Amount of calculated withhold taxes  in reporting currency  """  
      self.DocBankAmt:int = obj["DocBankAmt"]
      """  Bank Amount(Bank To Cash / Cash To Bank)  """  
      self.BankAmt:int = obj["BankAmt"]
      """  Bank Amount(Bank To Cash / Cash To Bank)  """  
      self.Rpt1BankAmt:int = obj["Rpt1BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.Rpt2BankAmt:int = obj["Rpt2BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.Rpt3BankAmt:int = obj["Rpt3BankAmt"]
      """  Bank Amount in reporting currency  """  
      self.DocBankFeeAmt:int = obj["DocBankFeeAmt"]
      """  Bank Fee Amount(Bank To Cash / Cash To Bank)  """  
      self.BankFeeAmt:int = obj["BankFeeAmt"]
      """  Bank Fee Amount(Bank To Cash / Cash To Bank)  """  
      self.Rpt1BankFeeAmt:int = obj["Rpt1BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.Rpt2BankFeeAmt:int = obj["Rpt2BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.Rpt3BankFeeAmt:int = obj["Rpt3BankFeeAmt"]
      """  Bank Fee Amount in reporting currency  """  
      self.RateGrpType:str = obj["RateGrpType"]
      """  Rate Type  """  
      self.OnAccount:bool = obj["OnAccount"]
      """  OnAccount  """  
      self.OnAcctBankAcctID:str = obj["OnAcctBankAcctID"]
      """  OnAcctBankAcctID  """  
      self.ReceiptAmt:int = obj["ReceiptAmt"]
      """  ReceiptAmt  """  
      self.Reference:str = obj["Reference"]
      """  Reference  """  
      self.Payee:str = obj["Payee"]
      """  Payee  """  
      self.AccountNumber:str = obj["AccountNumber"]
      """  AccountNumber  """  
      self.OtherDetails:str = obj["OtherDetails"]
      """  OtherDetails  """  
      self.PayMethodPMUID:int = obj["PayMethodPMUID"]
      """  PayMethodPMUID  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  PayMethodName  """  
      self.PayMethodReference:str = obj["PayMethodReference"]
      """  PayMethodReference  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CashDeskIDTransfer:str = obj["CashDeskIDTransfer"]
      """  CashDeskIDTransfer  """  
      self.ExchangeRateDate:str = obj["ExchangeRateDate"]
      """  ExchangeRateDate  """  
      self.ExchRateDateUserDefined:bool = obj["ExchRateDateUserDefined"]
      """  ExchRateDateUserDefined  """  
      self.PrintPage:int = obj["PrintPage"]
      """  PrintPage  """  
      self.PrintPageLegalNum:str = obj["PrintPageLegalNum"]
      """  PrintPageLegalNum  """  
      self.Reason:str = obj["Reason"]
      """  Reason  """  
      self.ReverseDate:str = obj["ReverseDate"]
      """  Cash Head Reverse Date  """  
      self.ReverseAmt:int = obj["ReverseAmt"]
      """  Cash Head Reverse Amount  """  
      self.OprTypeDescription:str = obj["OprTypeDescription"]
      self.OprTypeOpClassName:str = obj["OprTypeOpClassName"]
      self.OprTypeReason:str = obj["OprTypeReason"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskListRow:
   def __init__(self, obj):
      self.AllowDraftCI:bool = obj["AllowDraftCI"]
      """   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  """  
      self.AllowDraftCR:bool = obj["AllowDraftCR"]
      """   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  """  
      self.AllowNegBal:bool = obj["AllowNegBal"]
      """  Allow Negative Balance  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DayCloseMode:str = obj["DayCloseMode"]
      """   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  """  
      self.DocInitPayrollBal:int = obj["DocInitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.DocInitTotalBal:int = obj["DocInitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.EntrustedCashier:str = obj["EntrustedCashier"]
      """  Entrusted Cashier  """  
      self.EntrustedFrom:str = obj["EntrustedFrom"]
      """   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  """  
      self.EntrustedTill:str = obj["EntrustedTill"]
      """   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  """  
      self.InitTotalBal:int = obj["InitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.InitPayrollBal:int = obj["InitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.LimitExptPayroll:int = obj["LimitExptPayroll"]
      """  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  """  
      self.LimitTotal:int = obj["LimitTotal"]
      """  Defines Limit (in Cash Desk Currency)  """  
      self.Location:str = obj["Location"]
      """  Cash Desk Location  """  
      self.Name:str = obj["Name"]
      """  Cash Desk Name  """  
      self.OpenedFrom:str = obj["OpenedFrom"]
      """  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.PostingOpt:str = obj["PostingOpt"]
      """   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type  """  
      self.Rpt1InitPayrollBal:int = obj["Rpt1InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt2InitPayrollBal:int = obj["Rpt2InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt3InitPayrollBal:int = obj["Rpt3InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt1InitTotalBal:int = obj["Rpt1InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt2InitTotalBal:int = obj["Rpt2InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt3InitTotalBal:int = obj["Rpt3InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.UseExtnNumForCI:bool = obj["UseExtnNumForCI"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.UseExtnNumForCR:bool = obj["UseExtnNumForCR"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OperationExists:bool = obj["OperationExists"]
      """  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  """  
      self.IsAuthorizedUser:bool = obj["IsAuthorizedUser"]
      """  Indicates if the user is authorized to make changes.  """  
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      """  Description of the currency  """  
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      """  Description of the currency  """  
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      """  Description  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskListTableset:
   def __init__(self, obj):
      self.PCashDeskList:list[Erp_Tablesets_PCashDeskListRow] = obj["PCashDeskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCashDeskOprRow:
   def __init__(self, obj):
      self.AllowDraftDoc:bool = obj["AllowDraftDoc"]
      """   Checked: Draft Documents can be used.
Unchecked: Draft Documents are not used.  """  
      self.AllowUseExtnNum:bool = obj["AllowUseExtnNum"]
      """   Checked: External document numbers can be used.
Unchecked: External document numbers are not used.  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.OprTypeEnabled:bool = obj["OprTypeEnabled"]
      """  Indicates that operation type is enabled for this petty cash desk.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  Defines Legal Number related to Transaction Document Type and therefore used for this Operation type.  """  
      self.OprTypeCode:str = obj["OprTypeCode"]
      """  Unique identifier of Cash Operation Type.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Used only in case of Supplier/Customer Recipient/Payer Type and defines contact used to retrieve personal data.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type for system transactions PCashRcpt and PCashIssue  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID to define Document Template used for printing  """  
      self.ReportStyleNum:int = obj["ReportStyleNum"]
      """  Report Style to define document template for printing  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OprClassDesc:str = obj["OprClassDesc"]
      """  Description of the operation class  """  
      self.DirectionDesc:str = obj["DirectionDesc"]
      """  Direction description  """  
      self.RecPayerTypeDesc:str = obj["RecPayerTypeDesc"]
      """  Description of the RecPayerType  """  
      self.SystemTranType:str = obj["SystemTranType"]
      """  The system transaction type - PCI or PCR.  Used to filter combo list for TranDocTypeID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LegalNumCnfgDescription:str = obj["LegalNumCnfgDescription"]
      self.PCashOprTypeDirection:str = obj["PCashOprTypeDirection"]
      self.PCashOprTypePayrollBal:bool = obj["PCashOprTypePayrollBal"]
      self.PCashOprTypeOprClass:str = obj["PCashOprTypeOprClass"]
      self.PCashOprTypeDescription:str = obj["PCashOprTypeDescription"]
      self.PCashOprTypeRecPayerType:str = obj["PCashOprTypeRecPayerType"]
      self.ReportRptDescription:str = obj["ReportRptDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskRow:
   def __init__(self, obj):
      self.AllowDraftCI:bool = obj["AllowDraftCI"]
      """   Checked: Draft Documents can be used for Cash Issues
Unchecked: Draft Documents are not used for Cash Issues.  """  
      self.AllowDraftCR:bool = obj["AllowDraftCR"]
      """   Checked: Draft Documents can be used for Cash Receipts
Unchecked: Draft Documents are not used for Cash Receipts.  """  
      self.AllowNegBal:bool = obj["AllowNegBal"]
      """  Allow Negative Balance  """  
      self.CashDeskID:str = obj["CashDeskID"]
      """  Unique identifier of Cash Desk  """  
      self.Cashier:str = obj["Cashier"]
      """  Cashier Name  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DayCloseMode:str = obj["DayCloseMode"]
      """   Available values: Soft - Soft Closing;
Strict - Strict Closing (Until Cash Day is not closed, Operations for following days cannot be created)  """  
      self.DocInitPayrollBal:int = obj["DocInitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.DocInitTotalBal:int = obj["DocInitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.EntrustedCashier:str = obj["EntrustedCashier"]
      """  Entrusted Cashier  """  
      self.EntrustedFrom:str = obj["EntrustedFrom"]
      """   Not available when Entrusted Cashier is not defined
Required when Entrusted Cashier is defined  """  
      self.EntrustedTill:str = obj["EntrustedTill"]
      """   Not available when Entrusted Cashier is not defined.
Required when Entrusted Cashier is defined.  """  
      self.Inactive:bool = obj["Inactive"]
      """   Indicates that Cash Desk is Active/Inactive
Cash operations cannot be entered for inactive cash desk.  """  
      self.InitTotalBal:int = obj["InitTotalBal"]
      """  Defines initial Cash Desk balance (balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.InitPayrollBal:int = obj["InitPayrollBal"]
      """  Defines initial Cash Desk Payroll balance (payroll balance for Opening Date). Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.LimitExptPayroll:int = obj["LimitExptPayroll"]
      """  Defines Limit, which  are verified for all except Payroll Balances (in Cash Desk Currency)  """  
      self.LimitTotal:int = obj["LimitTotal"]
      """  Defines Limit (in Cash Desk Currency)  """  
      self.Location:str = obj["Location"]
      """  Cash Desk Location  """  
      self.Name:str = obj["Name"]
      """  Cash Desk Name  """  
      self.OpenedFrom:str = obj["OpenedFrom"]
      """  Defines the date when Cash Desk was put into Operation, or when Petty Cash Desk was established in the system. Cannot be changed after at least one operation is entered for Petty Cash Desk.  """  
      self.PostingOpt:str = obj["PostingOpt"]
      """   Available values:
SEP - Each Cash Document is posted as separate accounting transaction;  ALL - All Documents for Cash Day are posted in one accounting transaction.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      """  Rate Type  """  
      self.Rpt1InitPayrollBal:int = obj["Rpt1InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt2InitPayrollBal:int = obj["Rpt2InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt3InitPayrollBal:int = obj["Rpt3InitPayrollBal"]
      """  Value of InitPayrollBal in Reporting Currency  """  
      self.Rpt1InitTotalBal:int = obj["Rpt1InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt2InitTotalBal:int = obj["Rpt2InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.Rpt3InitTotalBal:int = obj["Rpt3InitTotalBal"]
      """  Value of InitTotalBal in Reporting Currency  """  
      self.UseExtnNumForCI:bool = obj["UseExtnNumForCI"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.UseExtnNumForCR:bool = obj["UseExtnNumForCR"]
      """   Checked: External document numbers can be used
Unchecked: External document numbers are not used.  """  
      self.FloatAmt:int = obj["FloatAmt"]
      """  FloatAmt  """  
      self.CashPayMethodPMUID:int = obj["CashPayMethodPMUID"]
      """  CashPayMethodPMUID  """  
      self.CashPayMethodName:str = obj["CashPayMethodName"]
      """  CashPayMethodName  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrintLastPage:int = obj["PrintLastPage"]
      """  PrintLastPage  """  
      self.PrintPerPage:int = obj["PrintPerPage"]
      """  PrintPerPage  """  
      self.ReportTranDocType:str = obj["ReportTranDocType"]
      """  ReportTranDocType  """  
      self.IsAuthorizedUser:bool = obj["IsAuthorizedUser"]
      """  Indicates if the user is authorized to make changes.  """  
      self.LegalNumberDesc:str = obj["LegalNumberDesc"]
      self.OperationExists:bool = obj["OperationExists"]
      """  Indicates if an operation exists for the cash desk record.  Used for UI row rules.  """  
      self.ReportTranDocTypeDesc:str = obj["ReportTranDocTypeDesc"]
      self.Direction:str = obj["Direction"]
      """  BD ? Both Directions; CI ? Only Issues; CR ? Only Receipts;  """  
      self.IsAuthorizedCR:bool = obj["IsAuthorizedCR"]
      """  The user is authorized for Cash Receipt  """  
      self.IsAuthorizedCI:bool = obj["IsAuthorizedCI"]
      """  The user is authorized for Cash Issue  """  
      self.UserCanRead:bool = obj["UserCanRead"]
      """  User has access to read the Petty Cash Desk.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BaseCurrCurrDesc:str = obj["BaseCurrCurrDesc"]
      self.BaseCurrCurrSymbol:str = obj["BaseCurrCurrSymbol"]
      self.BaseCurrCurrName:str = obj["BaseCurrCurrName"]
      self.BaseCurrCurrencyID:str = obj["BaseCurrCurrencyID"]
      self.BaseCurrDocumentDesc:str = obj["BaseCurrDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCashDeskTableset:
   def __init__(self, obj):
      self.PCashDesk:list[Erp_Tablesets_PCashDeskRow] = obj["PCashDesk"]
      self.PCashDeskAttch:list[Erp_Tablesets_PCashDeskAttchRow] = obj["PCashDeskAttch"]
      self.PCashDeskAuth:list[Erp_Tablesets_PCashDeskAuthRow] = obj["PCashDeskAuth"]
      self.PCashDeskOpr:list[Erp_Tablesets_PCashDeskOprRow] = obj["PCashDeskOpr"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCashDeskTrackerTableset:
   def __init__(self, obj):
      self.PCashDeskBalance:list[Erp_Tablesets_PCashDeskBalanceRow] = obj["PCashDeskBalance"]
      self.PCashDeskBalHist:list[Erp_Tablesets_PCashDeskBalHistRow] = obj["PCashDeskBalHist"]
      self.PCashDeskDocsHist:list[Erp_Tablesets_PCashDeskDocsHistRow] = obj["PCashDeskDocsHist"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPCashDeskTableset:
   def __init__(self, obj):
      self.PCashDesk:list[Erp_Tablesets_PCashDeskRow] = obj["PCashDesk"]
      self.PCashDeskAttch:list[Erp_Tablesets_PCashDeskAttchRow] = obj["PCashDeskAttch"]
      self.PCashDeskAuth:list[Erp_Tablesets_PCashDeskAuthRow] = obj["PCashDeskAuth"]
      self.PCashDeskOpr:list[Erp_Tablesets_PCashDeskOprRow] = obj["PCashDeskOpr"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   cashDeskID
   """  
   def __init__(self, obj):
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashDeskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashDeskTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PCashDeskTableset] = obj["returnObj"]
      pass

class GetCashDeskBalHist_input:
   """ Required : 
   ipCashDeskID
   ipFromDate
   ipToDate
   ipIncludeDrafts
   ipPayrollOnly
   ds
   """  
   def __init__(self, obj):
      self.ipCashDeskID:str = obj["ipCashDeskID"]
      """  Cash Desk ID  """  
      self.ipFromDate:str = obj["ipFromDate"]
      """  From Date  """  
      self.ipToDate:str = obj["ipToDate"]
      """  To Date  """  
      self.ipIncludeDrafts:bool = obj["ipIncludeDrafts"]
      """  Include Drafts  """  
      self.ipPayrollOnly:bool = obj["ipPayrollOnly"]
      """  Payroll Only  """  
      self.ds:list[Erp_Tablesets_PCashDeskTrackerTableset] = obj["ds"]
      pass

class GetCashDeskBalHist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCashDeskBalance_input:
   """ Required : 
   ipCashDeskID
   ds
   """  
   def __init__(self, obj):
      self.ipCashDeskID:str = obj["ipCashDeskID"]
      """  Cash Desk ID  """  
      self.ds:list[Erp_Tablesets_PCashDeskTrackerTableset] = obj["ds"]
      pass

class GetCashDeskBalance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCashDeskDocsHist_input:
   """ Required : 
   ipCashDeskID
   ipDate
   ipDirection
   ds
   """  
   def __init__(self, obj):
      self.ipCashDeskID:str = obj["ipCashDeskID"]
      """  Cash Desk ID  """  
      self.ipDate:str = obj["ipDate"]
      """  To Date  """  
      self.ipDirection:str = obj["ipDirection"]
      """  To Date  """  
      self.ds:list[Erp_Tablesets_PCashDeskTrackerTableset] = obj["ds"]
      pass

class GetCashDeskDocsHist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name to get Code List  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name to get Code List  """  
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
      self.returnObj:list[Erp_Tablesets_PCashDeskListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDeskAttch_input:
   """ Required : 
   ds
   cashDeskID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class GetNewPCashDeskAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDeskAuth_input:
   """ Required : 
   ds
   cashDeskID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class GetNewPCashDeskAuth_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDeskOpr_input:
   """ Required : 
   ds
   cashDeskID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      self.cashDeskID:str = obj["cashDeskID"]
      pass

class GetNewPCashDeskOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCashDesk_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class GetNewPCashDesk_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePCashDesk
   whereClausePCashDeskAttch
   whereClausePCashDeskAuth
   whereClausePCashDeskOpr
   whereClauseEntityGLC
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePCashDesk:str = obj["whereClausePCashDesk"]
      self.whereClausePCashDeskAttch:str = obj["whereClausePCashDeskAttch"]
      self.whereClausePCashDeskAuth:str = obj["whereClausePCashDeskAuth"]
      self.whereClausePCashDeskOpr:str = obj["whereClausePCashDeskOpr"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCashDeskTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCashDeskTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPCashDeskTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCashDeskTableset] = obj["ds"]
      pass

      """  output parameters  """  

