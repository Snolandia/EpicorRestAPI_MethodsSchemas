import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OpMasterSvc
# Description: Production operation codes master file.
DELETE: Not allowed if referenced in  JobOper, OpStd or BomOper files.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasters
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters",headers=creds) as resp:
           return await resp.json()

async def post_OpMasters(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode(Company, OpCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMaster item
   Description: Calls GetByID to retrieve the OpMaster item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMaster
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasters_Company_OpCode(Company, OpCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMaster for the service
   Description: Calls UpdateExt to update OpMaster. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMaster
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasters_Company_OpCode(Company, OpCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMaster item
   Description: Call UpdateExt to delete OpMaster item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMaster
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasRestrictions(Company, OpCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasRestrictions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasRestrictions",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company, OpCode, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasRestriction item
   Description: Calls GetByID to retrieve the OpMasRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestriction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasterActions(Company, OpCode, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasterActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterActions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterActions",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasterActions_Company_OpCode_ActionSeq(Company, OpCode, ActionSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterAction item
   Description: Calls GetByID to retrieve the OpMasterAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasterInsps(Company, OpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasterInsps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterInsps1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterInsps",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasterInsps_Company_OpCode_PlanSeq(Company, OpCode, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterInsp item
   Description: Calls GetByID to retrieve the OpMasterInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterInsp1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasDtls(Company, OpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasDtls",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasDtls_Company_OpCode_OpDtlSeq(Company, OpCode, OpDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasDtl item
   Description: Calls GetByID to retrieve the OpMasDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasterAttches(Company, OpCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasterAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterAttches",headers=creds) as resp:
           return await resp.json()

async def get_OpMasters_Company_OpCode_OpMasterAttches_Company_OpCode_DrawingSeq(Company, OpCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterAttch item
   Description: Calls GetByID to retrieve the OpMasterAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasters(" + Company + "," + OpCode + ")/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasRestrictions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasRestrictions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_OpMasRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company, OpCode, RestrictionTypeID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasRestriction item
   Description: Calls GetByID to retrieve the OpMasRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company, OpCode, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasRestriction for the service
   Description: Calls UpdateExt to update OpMasRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasRestrictions_Company_OpCode_RestrictionTypeID(Company, OpCode, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasRestriction item
   Description: Call UpdateExt to delete OpMasRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasRestrictions_Company_OpCode_RestrictionTypeID_OpMasRestrictSubsts(Company, OpCode, RestrictionTypeID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasRestrictSubsts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasRestrictSubsts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")/OpMasRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def get_OpMasRestrictions_Company_OpCode_RestrictionTypeID_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company, OpCode, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasRestrictSubst item
   Description: Calls GetByID to retrieve the OpMasRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestrictSubst1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictions(" + Company + "," + OpCode + "," + RestrictionTypeID + ")/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasRestrictSubsts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasRestrictSubsts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasRestrictSubsts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts",headers=creds) as resp:
           return await resp.json()

async def post_OpMasRestrictSubsts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasRestrictSubsts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company, OpCode, RestrictionTypeID, SubstanceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasRestrictSubst item
   Description: Calls GetByID to retrieve the OpMasRestrictSubst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company, OpCode, RestrictionTypeID, SubstanceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasRestrictSubst for the service
   Description: Calls UpdateExt to update OpMasRestrictSubst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasRestrictSubstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasRestrictSubsts_Company_OpCode_RestrictionTypeID_SubstanceID(Company, OpCode, RestrictionTypeID, SubstanceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasRestrictSubst item
   Description: Call UpdateExt to delete OpMasRestrictSubst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasRestrictSubst
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param SubstanceID: Desc: SubstanceID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasRestrictSubsts(" + Company + "," + OpCode + "," + RestrictionTypeID + "," + SubstanceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasterActions(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasterActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterActions
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions",headers=creds) as resp:
           return await resp.json()

async def post_OpMasterActions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterActions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasterActions_Company_OpCode_ActionSeq(Company, OpCode, ActionSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterAction item
   Description: Calls GetByID to retrieve the OpMasterAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasterActions_Company_OpCode_ActionSeq(Company, OpCode, ActionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasterAction for the service
   Description: Calls UpdateExt to update OpMasterAction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterActionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasterActions_Company_OpCode_ActionSeq(Company, OpCode, ActionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasterAction item
   Description: Call UpdateExt to delete OpMasterAction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterAction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasterActions_Company_OpCode_ActionSeq_OpMasterActionParams(Company, OpCode, ActionSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get OpMasterActionParams items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_OpMasterActionParams1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")/OpMasterActionParams",headers=creds) as resp:
           return await resp.json()

async def get_OpMasterActions_Company_OpCode_ActionSeq_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company, OpCode, ActionSeq, ActionParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterActionParam item
   Description: Calls GetByID to retrieve the OpMasterActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterActionParam1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActions(" + Company + "," + OpCode + "," + ActionSeq + ")/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasterActionParams(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasterActionParams items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterActionParams
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams",headers=creds) as resp:
           return await resp.json()

async def post_OpMasterActionParams(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterActionParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company, OpCode, ActionSeq, ActionParamSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterActionParam item
   Description: Calls GetByID to retrieve the OpMasterActionParam item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company, OpCode, ActionSeq, ActionParamSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasterActionParam for the service
   Description: Calls UpdateExt to update OpMasterActionParam. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterActionParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasterActionParams_Company_OpCode_ActionSeq_ActionParamSeq(Company, OpCode, ActionSeq, ActionParamSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasterActionParam item
   Description: Call UpdateExt to delete OpMasterActionParam item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterActionParam
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param ActionSeq: Desc: ActionSeq   Required: True
      :param ActionParamSeq: Desc: ActionParamSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterActionParams(" + Company + "," + OpCode + "," + ActionSeq + "," + ActionParamSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasterInsps(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasterInsps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterInsps
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps",headers=creds) as resp:
           return await resp.json()

async def post_OpMasterInsps(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterInsps
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasterInsps_Company_OpCode_PlanSeq(Company, OpCode, PlanSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterInsp item
   Description: Calls GetByID to retrieve the OpMasterInsp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasterInsps_Company_OpCode_PlanSeq(Company, OpCode, PlanSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasterInsp for the service
   Description: Calls UpdateExt to update OpMasterInsp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PlanSeq: Desc: PlanSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterInspRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasterInsps_Company_OpCode_PlanSeq(Company, OpCode, PlanSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasterInsp item
   Description: Call UpdateExt to delete OpMasterInsp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterInsp
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param PlanSeq: Desc: PlanSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterInsps(" + Company + "," + OpCode + "," + PlanSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls",headers=creds) as resp:
           return await resp.json()

async def post_OpMasDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasDtls_Company_OpCode_OpDtlSeq(Company, OpCode, OpDtlSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasDtl item
   Description: Calls GetByID to retrieve the OpMasDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasDtls_Company_OpCode_OpDtlSeq(Company, OpCode, OpDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasDtl for the service
   Description: Calls UpdateExt to update OpMasDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasDtls_Company_OpCode_OpDtlSeq(Company, OpCode, OpDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasDtl item
   Description: Call UpdateExt to delete OpMasDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param OpDtlSeq: Desc: OpDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasDtls(" + Company + "," + OpCode + "," + OpDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_OpMasterAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get OpMasterAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_OpMasterAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches",headers=creds) as resp:
           return await resp.json()

async def post_OpMasterAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_OpMasterAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_OpMasterAttches_Company_OpCode_DrawingSeq(Company, OpCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the OpMasterAttch item
   Description: Calls GetByID to retrieve the OpMasterAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_OpMasterAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_OpMasterAttches_Company_OpCode_DrawingSeq(Company, OpCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update OpMasterAttch for the service
   Description: Calls UpdateExt to update OpMasterAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_OpMasterAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.OpMasterAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_OpMasterAttches_Company_OpCode_DrawingSeq(Company, OpCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete OpMasterAttch item
   Description: Call UpdateExt to delete OpMasterAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_OpMasterAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param OpCode: Desc: OpCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/OpMasterAttches(" + Company + "," + OpCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.OpMasterListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseOpMaster, whereClauseOpMasterAttch, whereClauseOpMasRestriction, whereClauseOpMasRestrictSubst, whereClauseOpMasterAction, whereClauseOpMasterActionParam, whereClauseOpMasterInsp, whereClauseOpMasDtl, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseOpMaster=" + whereClauseOpMaster
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasterAttch=" + whereClauseOpMasterAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasRestriction=" + whereClauseOpMasRestriction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasRestrictSubst=" + whereClauseOpMasRestrictSubst
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasterAction=" + whereClauseOpMasterAction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasterActionParam=" + whereClauseOpMasterActionParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasterInsp=" + whereClauseOpMasterInsp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseOpMasDtl=" + whereClauseOpMasDtl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(opCode, epicorHeaders = None):
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
   params += "opCode=" + opCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangedCharacteristicAttrClassID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangedCharacteristicAttrClassID
   Description: Method that is called when the Characteristic Attribute ID is changed.
   OperationID: ChangedCharacteristicAttrClassID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangedCharacteristicAttrClassID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangedCharacteristicAttrClassID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCapabilityID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCapabilityID
   Description: Method to call when changing the Capability ID. Blank is a valid entry for Capability ID.
   OperationID: ChangeCapabilityID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCapabilityID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCapabilityID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpMasRestrictionType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpMasRestrictionType
   Description: This methods assigns associated fields when OpMasRestriction.RestrictionTypeID changes.
   OperationID: ChangeOpMasRestrictionType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMasRestrictionType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasRestrictionType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpMasRestrictSubstance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpMasRestrictSubstance
   Description: This methods assigns associated fields when OpMasRestrictSubst.SubstanceID changes.
   OperationID: ChangeOpMasRestrictSubstance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMasRestrictSubstance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasRestrictSubstance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpMasterPrimaryProdOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpMasterPrimaryProdOpDtl
   Description: This method checks if the entered primary production operation detail is valid.
This method should run when the OpMaster.ScrPrimaryProdOpDtl field changes.
   OperationID: ChangeOpMasterPrimaryProdOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMasterPrimaryProdOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasterPrimaryProdOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOpMasterPrimarySetupOpDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOpMasterPrimarySetupOpDtl
   Description: This method checks if the entered primary setup operation detail is valid.
This method should run when the OpMaster.ScrPrimarySetupOpDtl field changes.
   OperationID: ChangeOpMasterPrimarySetupOpDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOpMasterPrimarySetupOpDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOpMasterPrimarySetupOpDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResourceGrpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResourceGrpID
   Description: Method to call when changing the Resource Group ID.  This method will update OpMasDtl
with the default labor and burden rates from the new resource group.  Blank is a valid
entry for Resource Group ID.
   OperationID: ChangeResourceGrpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResourceGrpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceGrpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeResourceID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeResourceID
   Description: Method to call when changing the Resource ID.  Blank is a valid entry for Resource ID.
   OperationID: ChangeResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendorNumVendorID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendorNumVendorID
   Description: Method to call when changing the Vendor Num. Blank is a valid entry for Vendor Num.
   OperationID: ChangeVendorNumVendorID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendorNumVendorID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendorNumVendorID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckInactiveSchedRequirement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckInactiveSchedRequirement
   Description: Method to call check the capability, resource group, or resource is active.
This method should be called prior to calling the Update method on an OpMasDtl record.
Will return message text to present to the user if the code is inactive.  The
message is asking the user if it is OK to save the record with an inactive code.
If the user answers yes, the record can be saved.  If a blank value is returned
for InactiveMessage, continue as normal - no special processing needs to occur.
   OperationID: CheckInactiveSchedRequirement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckInactiveSchedRequirement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInactiveSchedRequirement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDandOpType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDandOpType
   Description: A variation of the standard GetByID. Gets a OpMaster for a specific OpCode with consideration of OpType(s).
Note OpType is a comma separated list of Operation types to be considered valid for this Get.
Used as a predecessor to calling GetByID.
   OperationID: GetByIDandOpType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDandOpType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDandOpType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetProjectRoles(epicorHeaders = None):
   """  
   Summary: Invoke method GetProjectRoles
   OperationID: GetProjectRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProjectRoles_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_InsertCapability(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertCapability
   Description: This methods allows for the insertion of Capability on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertCapability
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertCapability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertCapability_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertResource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertResource
   Description: This methods allows for the insertion of Resource on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertResource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_InsertResourceGroup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method InsertResourceGroup
   Description: This methods allows for the insertion of Resource Group on an operation to create
operation detail for drag/drop functionality.
   OperationID: InsertResourceGroup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/InsertResourceGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InsertResourceGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasDtlForOPMasDtlType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasDtlForOPMasDtlType
   Description: This method overrides the original GetNewOpMasDtl and populates the OpMasDtlType with the given argument.
   OperationID: GetNewOpMasDtlForOPMasDtlType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasDtlForOPMasDtlType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasDtlForOPMasDtlType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateInspection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateInspection
   Description: Method to validate the Inspection control fields. (EQM)
   OperationID: ValidateInspection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateInspection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateInspection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetIfCurrentSiteHasExternalMES(epicorHeaders = None):
   """  
   Summary: Invoke method GetIfCurrentSiteHasExternalMES
   OperationID: GetIfCurrentSiteHasExternalMES
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetIfCurrentSiteHasExternalMES_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_EnterpriseGetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnterpriseGetList
   Description: Will invoke GetList or perform the Enterprise Search when enterpriseSearchText / enterpriseBAQID is provided
   OperationID: EnterpriseGetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnterpriseGetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnterpriseGetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingActionSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingActionSeq
   Description: Performs validation an change of the Action sequence and syncs the child Action Parameter sequence
   OperationID: OnChangingActionSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingActionSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingActionSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingActionParamSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingActionParamSeq
   Description: Performs validation an change of the Action Parameter sequence
   OperationID: OnChangingActionParamSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingActionParamSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingActionParamSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMaster(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMaster
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMaster
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMaster_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMaster_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasterAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasterAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasRestrictSubst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasRestrictSubst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasRestrictSubst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasRestrictSubst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasRestrictSubst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasterAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasterAction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasterActionParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasterActionParam
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterActionParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterActionParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterActionParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasterInsp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasterInsp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasterInsp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasterInsp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasterInsp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewOpMasDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewOpMasDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewOpMasDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewOpMasDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewOpMasDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OpMasterSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictSubstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasRestrictSubstRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasRestrictionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasRestrictionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasterActionParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterActionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasterActionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasterAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterInspRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasterInspRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasterListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_OpMasterRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_OpMasterRow] = obj["value"]
      pass

class Erp_Tablesets_OpMasDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Cannot be blank.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production phase the resource is needed.   Valid values are "S", indicating the resource is required for the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the OpMasDtl is created.   If the OpMasDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Production Crew Size  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Setup Crew Size  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryProd:bool = obj["PrimaryProd"]
      """  PrimaryProd  """  
      self.PrimarySetup:bool = obj["PrimarySetup"]
      """  PrimarySetup  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      self.SchedResourceDesc:str = obj["SchedResourceDesc"]
      self.Location:bool = obj["Location"]
      self.OPMasDtlType:str = obj["OPMasDtlType"]
      self.ResourceCharAttrClassID:str = obj["ResourceCharAttrClassID"]
      """  Resource Characteristic Attribute Class ID  """  
      self.ResourceCharAttrSetID:int = obj["ResourceCharAttrSetID"]
      """  Resource Characteristic Attribute Set ID  """  
      self.ResourceSysRowID:str = obj["ResourceSysRowID"]
      """  Resource SysRowID  """  
      self.ResourceGrpCharAttrClassID:str = obj["ResourceGrpCharAttrClassID"]
      """  Resource Group Characteristic Attribute Class ID  """  
      self.ResourceGrpCharAttrSetID:int = obj["ResourceGrpCharAttrSetID"]
      """  Resource Group Characteristic Attribute Set ID  """  
      self.ResourceGrpSysRowID:str = obj["ResourceGrpSysRowID"]
      """  Resource Group SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then weight is disregarded in compliance roll-up.  """  
      self.ExemptDate:str = obj["ExemptDate"]
      """  The date when exempt status for this substance expires.  """  
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      """  Optional. Exemption certificate.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Operation Restriction Substance is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Exempt:bool = obj["Exempt"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  """  
      self.Compliance:str = obj["Compliance"]
      """  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  """  
      self.ComplianceDate:str = obj["ComplianceDate"]
      """  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Operation Restriction Type is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Weight:bool = obj["Weight"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Unique identity of Operation master record.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  ActionParamFieldDataType  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Unique identity of Operation master record.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicates if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OpCode:str = obj["OpCode"]
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

class Erp_Tablesets_OpMasterInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the PartOprInsp ecord within the Part operation  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  """  
      self.BuyerName:str = obj["BuyerName"]
      self.OPType:str = obj["OPType"]
      """  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  """  
      self.AllowInCurPlant:bool = obj["AllowInCurPlant"]
      self.Subcontract:bool = obj["Subcontract"]
      """  SubContract Operation  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasCharacteristics:bool = obj["HasCharacteristics"]
      """  Operation has Characteristics  """  
      self.HasActions:bool = obj["HasActions"]
      """  Operations has some Actions.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.OpTextID:str = obj["OpTextID"]
      """  Key of the OpText record that is to be associated with this operation.  This is an optional field.  If entered it must be valid.  The purpose is that the OpText.Text data will be printed on the router after the operation detail.  The OpText is intended to be used for things such as creating inspection check off lines on the router.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  """  
      self.APSPrepOpF:bool = obj["APSPrepOpF"]
      """  Advanced Planning and Scheduling (eScheduling) preparatory operation flag.  A prep operation is usually a kitting operation.  Not used by the Manufacturing System scheduling module.  """  
      self.OPType:str = obj["OPType"]
      """  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  """  
      self.CommentText:str = obj["CommentText"]
      """  FS - Editor widget for Operation comments.  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  FS - Labor rate used for  time on an operation.  Time per hour per technician.  """  
      self.EstLabHours:int = obj["EstLabHours"]
      """  FS - The estimated Labor hours for the operation.  """  
      self.SchedPrecedence:int = obj["SchedPrecedence"]
      """  Used to sort operations when load leveling by Op Code.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.Subcontract:bool = obj["Subcontract"]
      """  SubContract Operation  """  
      self.PrdYldRecalcExpected:bool = obj["PrdYldRecalcExpected"]
      """   Indicates whether the expected production yield quantity should be changed based on actual production quantity and the PrdYldRecalc under percent threshold established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldRecalcUnderPct:int = obj["PrdYldRecalcUnderPct"]
      """   Indicates the shrink percent which will cause the expected production yield quantity to be recalculated based on actual production quantity if PrdYldRecalcExpected = true.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrnAlert:bool = obj["PrdYldShopWrnAlert"]
      """   Indicates whether shop warning alerts should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrn:bool = obj["PrdYldShopWrn"]
      """   Indicates whether shop warning messages should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrnUnderPct:int = obj["PrdYldShopWrnUnderPct"]
      """   Indicates the shrink percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on  the settings of PrdYldShopWrnAlert and PrdYldShopWrn
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrnOverPct:int = obj["PrdYldShopWrnOverPct"]
      """   Indicates the increased production percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on the settings of PrdYldShopWrnAlert and PrdYldShopWrn.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.RestrictSubstance:bool = obj["RestrictSubstance"]
      """  Indicate if the operation adds restricted substances.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for a job operation.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.RoleCodeDefault:str = obj["RoleCodeDefault"]
      """  Role Default (should be in selected)  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Indicates if Operation includes all roles  """  
      self.JDFMaterial:str = obj["JDFMaterial"]
      """  JDFMaterial  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.JDFOperation:str = obj["JDFOperation"]
      """  JDFOperation  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AllowInCurPlant:bool = obj["AllowInCurPlant"]
      self.OpMasDtlExists:bool = obj["OpMasDtlExists"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.ScrPrimaryProdOpDtl:int = obj["ScrPrimaryProdOpDtl"]
      self.ScrPrimarySetupOpDtl:int = obj["ScrPrimarySetupOpDtl"]
      self.HasActions:bool = obj["HasActions"]
      """  Operations has some Actions.  """  
      self.HasCharacteristics:bool = obj["HasCharacteristics"]
      """  Operation has Characteristics  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.BuyerName:str = obj["BuyerName"]
      self.OPTextDescription:str = obj["OPTextDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeCapabilityID_input:
   """ Required : 
   ProposedCapID
   ds
   """  
   def __init__(self, obj):
      self.ProposedCapID:str = obj["ProposedCapID"]
      """  The proposed Capability ID  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeCapabilityID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpMasRestrictSubstance_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeOpMasRestrictSubstance_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpMasRestrictionType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeOpMasRestrictionType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpMasterPrimaryProdOpDtl_input:
   """ Required : 
   ProposedProdOpDtl
   ds
   """  
   def __init__(self, obj):
      self.ProposedProdOpDtl:int = obj["ProposedProdOpDtl"]
      """  The proposed primary production operation detail sequence  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeOpMasterPrimaryProdOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOpMasterPrimarySetupOpDtl_input:
   """ Required : 
   ProposedSetupOpDtl
   ds
   """  
   def __init__(self, obj):
      self.ProposedSetupOpDtl:int = obj["ProposedSetupOpDtl"]
      """  The proposed primary setup operation detail sequence  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeOpMasterPrimarySetupOpDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeResourceGrpID_input:
   """ Required : 
   ProposedResGrpID
   ds
   """  
   def __init__(self, obj):
      self.ProposedResGrpID:str = obj["ProposedResGrpID"]
      """  The proposed Resource Group ID  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeResourceGrpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeResourceID_input:
   """ Required : 
   ProposedResourceID
   ds
   """  
   def __init__(self, obj):
      self.ProposedResourceID:str = obj["ProposedResourceID"]
      """  The proposed Resource ID  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeResourceID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendorNumVendorID_input:
   """ Required : 
   ProposedVendorNumVendorID
   ds
   """  
   def __init__(self, obj):
      self.ProposedVendorNumVendorID:str = obj["ProposedVendorNumVendorID"]
      """  The proposed Vendor ID  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangeVendorNumVendorID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangedCharacteristicAttrClassID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ChangedCharacteristicAttrClassID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckInactiveSchedRequirement_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class CheckInactiveSchedRequirement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.InactiveMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   opCode
   """  
   def __init__(self, obj):
      self.opCode:str = obj["opCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EnterpriseGetList_input:
   """ Required : 
   whereClause
   enterpriseBAQID
   enterpriseSearchText
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.enterpriseBAQID:str = obj["enterpriseBAQID"]
      """  Enterprise BAQ ID  """  
      self.enterpriseSearchText:str = obj["enterpriseSearchText"]
      """  Enterprise Search  """  
      self.pageSize:int = obj["pageSize"]
      """  pageSize  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class EnterpriseGetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Erp_Tablesets_OpMasDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Cannot be blank.  This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl.  System assigned.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production phase the resource is needed.   Valid values are "S", indicating the resource is required for the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the OpMasDtl is created.   If the OpMasDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Production Crew Size  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Setup Crew Size  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryProd:bool = obj["PrimaryProd"]
      """  PrimaryProd  """  
      self.PrimarySetup:bool = obj["PrimarySetup"]
      """  PrimarySetup  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      self.SchedResourceDesc:str = obj["SchedResourceDesc"]
      self.Location:bool = obj["Location"]
      self.OPMasDtlType:str = obj["OPMasDtlType"]
      self.ResourceCharAttrClassID:str = obj["ResourceCharAttrClassID"]
      """  Resource Characteristic Attribute Class ID  """  
      self.ResourceCharAttrSetID:int = obj["ResourceCharAttrSetID"]
      """  Resource Characteristic Attribute Set ID  """  
      self.ResourceSysRowID:str = obj["ResourceSysRowID"]
      """  Resource SysRowID  """  
      self.ResourceGrpCharAttrClassID:str = obj["ResourceGrpCharAttrClassID"]
      """  Resource Group Characteristic Attribute Class ID  """  
      self.ResourceGrpCharAttrSetID:int = obj["ResourceGrpCharAttrSetID"]
      """  Resource Group Characteristic Attribute Set ID  """  
      self.ResourceGrpSysRowID:str = obj["ResourceGrpSysRowID"]
      """  Resource Group SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then weight is disregarded in compliance roll-up.  """  
      self.ExemptDate:str = obj["ExemptDate"]
      """  The date when exempt status for this substance expires.  """  
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      """  Optional. Exemption certificate.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Operation Restriction Substance is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Exempt:bool = obj["Exempt"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.Manual:bool = obj["Manual"]
      """  When true then no roll-up will be calculated for this Restriction type. Compliance date is set when this flag is set. D/I Roll-Up radio Button will be disabled.  """  
      self.Compliance:str = obj["Compliance"]
      """  Displays one of the compliance statuses: 1. Not applicable (Yellow) (when no substances are selected) 2. Non compliant (Red) (one or more substances are selected but roll-up has not been executed or roll-up has failed) 3. Compliant (Green) (one or more substances are selected and roll-up was successful) 4. Exempt (Yellow) (when all substances are exempt ? verify exempt date)  """  
      self.ComplianceDate:str = obj["ComplianceDate"]
      """  Set when Manual flag is checked or after compliance roll-up is successful. Cleared Manual flag is unchecked or after compliance roll-up is unsuccessful.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the Operation Restriction Type is inactive and the Roll-Up process will not take it in count and it won?t be copied when the operation is selected.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Weight:bool = obj["Weight"]
      self.BitFlag:int = obj["BitFlag"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Unique identity of Operation master record.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  ActionParamFieldDataType  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Unique identity of Operation master record.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicates if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.OpCode:str = obj["OpCode"]
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

class Erp_Tablesets_OpMasterInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the PartOprInsp ecord within the Part operation  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  """  
      self.BuyerName:str = obj["BuyerName"]
      self.OPType:str = obj["OPType"]
      """  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  """  
      self.AllowInCurPlant:bool = obj["AllowInCurPlant"]
      self.Subcontract:bool = obj["Subcontract"]
      """  SubContract Operation  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.HasCharacteristics:bool = obj["HasCharacteristics"]
      """  Operation has Characteristics  """  
      self.HasActions:bool = obj["HasActions"]
      """  Operations has some Actions.  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterListTableset:
   def __init__(self, obj):
      self.OpMasterList:list[Erp_Tablesets_OpMasterListRow] = obj["OpMasterList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_OpMasterRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.OpTextID:str = obj["OpTextID"]
      """  Key of the OpText record that is to be associated with this operation.  This is an optional field.  If entered it must be valid.  The purpose is that the OpText.Text data will be printed on the router after the operation detail.  The OpText is intended to be used for things such as creating inspection check off lines on the router.  """  
      self.BuyerID:str = obj["BuyerID"]
      """  Identifies the Buyer for the subcontract operation.  Used as the default in the Automated Purchasing process.  """  
      self.APSPrepOpF:bool = obj["APSPrepOpF"]
      """  Advanced Planning and Scheduling (eScheduling) preparatory operation flag.  A prep operation is usually a kitting operation.  Not used by the Manufacturing System scheduling module.  """  
      self.OPType:str = obj["OPType"]
      """  Operation Type - "SRV" Service Call Operation
                           "MFG" Manufacturing operation  """  
      self.CommentText:str = obj["CommentText"]
      """  FS - Editor widget for Operation comments.  """  
      self.BillLaborRate:int = obj["BillLaborRate"]
      """  FS - Labor rate used for  time on an operation.  Time per hour per technician.  """  
      self.EstLabHours:int = obj["EstLabHours"]
      """  FS - The estimated Labor hours for the operation.  """  
      self.SchedPrecedence:int = obj["SchedPrecedence"]
      """  Used to sort operations when load leveling by Op Code.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.Subcontract:bool = obj["Subcontract"]
      """  SubContract Operation  """  
      self.PrdYldRecalcExpected:bool = obj["PrdYldRecalcExpected"]
      """   Indicates whether the expected production yield quantity should be changed based on actual production quantity and the PrdYldRecalc under percent threshold established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldRecalcUnderPct:int = obj["PrdYldRecalcUnderPct"]
      """   Indicates the shrink percent which will cause the expected production yield quantity to be recalculated based on actual production quantity if PrdYldRecalcExpected = true.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrnAlert:bool = obj["PrdYldShopWrnAlert"]
      """   Indicates whether shop warning alerts should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrn:bool = obj["PrdYldShopWrn"]
      """   Indicates whether shop warning messages should be created based on actual production quantity and the PrdYldShopWrn over/under threshold percents established for this operation.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrnUnderPct:int = obj["PrdYldShopWrnUnderPct"]
      """   Indicates the shrink percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on  the settings of PrdYldShopWrnAlert and PrdYldShopWrn
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.PrdYldShopWrnOverPct:int = obj["PrdYldShopWrnOverPct"]
      """   Indicates the increased production percent (based on the difference between expected production yield and actual production quantity) which will cause a shop warning and alerts/memos to be created depending on the settings of PrdYldShopWrnAlert and PrdYldShopWrn.
This will only have an effect if Job.Head.ProductionYield = true.  """  
      self.RestrictSubstance:bool = obj["RestrictSubstance"]
      """  Indicate if the operation adds restricted substances.  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for a job operation.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.RoleCodeDefault:str = obj["RoleCodeDefault"]
      """  Role Default (should be in selected)  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Indicates if Operation includes all roles  """  
      self.JDFMaterial:str = obj["JDFMaterial"]
      """  JDFMaterial  """  
      self.JDFDevice:str = obj["JDFDevice"]
      """  JDFDevice  """  
      self.JDFOperation:str = obj["JDFOperation"]
      """  JDFOperation  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.CharacteristicAttrClassID:str = obj["CharacteristicAttrClassID"]
      """  ID of related Attribute Class, the class must be of type Characteristics.  """  
      self.CharacteristicAttributeSetID:int = obj["CharacteristicAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AllowInCurPlant:bool = obj["AllowInCurPlant"]
      self.OpMasDtlExists:bool = obj["OpMasDtlExists"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      self.ScrPrimaryProdOpDtl:int = obj["ScrPrimaryProdOpDtl"]
      self.ScrPrimarySetupOpDtl:int = obj["ScrPrimarySetupOpDtl"]
      self.HasActions:bool = obj["HasActions"]
      """  Operations has some Actions.  """  
      self.HasCharacteristics:bool = obj["HasCharacteristics"]
      """  Operation has Characteristics  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.BuyerName:str = obj["BuyerName"]
      self.OPTextDescription:str = obj["OPTextDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OpMasterTableset:
   def __init__(self, obj):
      self.OpMaster:list[Erp_Tablesets_OpMasterRow] = obj["OpMaster"]
      self.OpMasterAttch:list[Erp_Tablesets_OpMasterAttchRow] = obj["OpMasterAttch"]
      self.OpMasRestriction:list[Erp_Tablesets_OpMasRestrictionRow] = obj["OpMasRestriction"]
      self.OpMasRestrictSubst:list[Erp_Tablesets_OpMasRestrictSubstRow] = obj["OpMasRestrictSubst"]
      self.OpMasterAction:list[Erp_Tablesets_OpMasterActionRow] = obj["OpMasterAction"]
      self.OpMasterActionParam:list[Erp_Tablesets_OpMasterActionParamRow] = obj["OpMasterActionParam"]
      self.OpMasterInsp:list[Erp_Tablesets_OpMasterInspRow] = obj["OpMasterInsp"]
      self.OpMasDtl:list[Erp_Tablesets_OpMasDtlRow] = obj["OpMasDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtOpMasterTableset:
   def __init__(self, obj):
      self.OpMaster:list[Erp_Tablesets_OpMasterRow] = obj["OpMaster"]
      self.OpMasterAttch:list[Erp_Tablesets_OpMasterAttchRow] = obj["OpMasterAttch"]
      self.OpMasRestriction:list[Erp_Tablesets_OpMasRestrictionRow] = obj["OpMasRestriction"]
      self.OpMasRestrictSubst:list[Erp_Tablesets_OpMasRestrictSubstRow] = obj["OpMasRestrictSubst"]
      self.OpMasterAction:list[Erp_Tablesets_OpMasterActionRow] = obj["OpMasterAction"]
      self.OpMasterActionParam:list[Erp_Tablesets_OpMasterActionParamRow] = obj["OpMasterActionParam"]
      self.OpMasterInsp:list[Erp_Tablesets_OpMasterInspRow] = obj["OpMasterInsp"]
      self.OpMasDtl:list[Erp_Tablesets_OpMasDtlRow] = obj["OpMasDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   opCode
   """  
   def __init__(self, obj):
      self.opCode:str = obj["opCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
      pass

class GetByIDandOpType_input:
   """ Required : 
   opCode
   opType
   """  
   def __init__(self, obj):
      self.opCode:str = obj["opCode"]
      """  Opmaster.OpCode  """  
      self.opType:str = obj["opType"]
      """  Opmaster.OpType  """  
      pass

class GetByIDandOpType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
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

class GetIfCurrentSiteHasExternalMES_output:
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
      self.returnObj:list[Erp_Tablesets_OpMasterListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewOpMasDtlForOPMasDtlType_input:
   """ Required : 
   ds
   OpCode
   OPMasDtlType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.OpCode:str = obj["OpCode"]
      self.OPMasDtlType:str = obj["OPMasDtlType"]
      pass

class GetNewOpMasDtlForOPMasDtlType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasDtl_input:
   """ Required : 
   ds
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewOpMasDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasRestrictSubst_input:
   """ Required : 
   ds
   opCode
   restrictionTypeID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      self.restrictionTypeID:str = obj["restrictionTypeID"]
      pass

class GetNewOpMasRestrictSubst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasRestriction_input:
   """ Required : 
   ds
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewOpMasRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasterActionParam_input:
   """ Required : 
   ds
   opCode
   actionSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      self.actionSeq:int = obj["actionSeq"]
      pass

class GetNewOpMasterActionParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasterAction_input:
   """ Required : 
   ds
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewOpMasterAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasterAttch_input:
   """ Required : 
   ds
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewOpMasterAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMasterInsp_input:
   """ Required : 
   ds
   opCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      self.opCode:str = obj["opCode"]
      pass

class GetNewOpMasterInsp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewOpMaster_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class GetNewOpMaster_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetProjectRoles_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class GetRows_input:
   """ Required : 
   whereClauseOpMaster
   whereClauseOpMasterAttch
   whereClauseOpMasRestriction
   whereClauseOpMasRestrictSubst
   whereClauseOpMasterAction
   whereClauseOpMasterActionParam
   whereClauseOpMasterInsp
   whereClauseOpMasDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseOpMaster:str = obj["whereClauseOpMaster"]
      self.whereClauseOpMasterAttch:str = obj["whereClauseOpMasterAttch"]
      self.whereClauseOpMasRestriction:str = obj["whereClauseOpMasRestriction"]
      self.whereClauseOpMasRestrictSubst:str = obj["whereClauseOpMasRestrictSubst"]
      self.whereClauseOpMasterAction:str = obj["whereClauseOpMasterAction"]
      self.whereClauseOpMasterActionParam:str = obj["whereClauseOpMasterActionParam"]
      self.whereClauseOpMasterInsp:str = obj["whereClauseOpMasterInsp"]
      self.whereClauseOpMasDtl:str = obj["whereClauseOpMasDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
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

class InsertCapability_input:
   """ Required : 
   ipOpMasterRowID
   ipCapabilityID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   """  
   def __init__(self, obj):
      self.ipOpMasterRowID:str = obj["ipOpMasterRowID"]
      """  The rowid of the OpMaster record to add the operation detail to  """  
      self.ipCapabilityID:str = obj["ipCapabilityID"]
      """  The Capability ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      pass

class InsertCapability_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
      pass

class InsertResourceGroup_input:
   """ Required : 
   ipOpMasterRowID
   ipResourceGrpID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   """  
   def __init__(self, obj):
      self.ipOpMasterRowID:str = obj["ipOpMasterRowID"]
      """  The rowid of the OpMaster record to add the operation detail to  """  
      self.ipResourceGrpID:str = obj["ipResourceGrpID"]
      """  The Resource Group ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      pass

class InsertResourceGroup_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
      pass

class InsertResource_input:
   """ Required : 
   ipOpMasterRowID
   ipResourceID
   ipNewOpDtlSeq
   ipBeforeOpDtlRowid
   """  
   def __init__(self, obj):
      self.ipOpMasterRowID:str = obj["ipOpMasterRowID"]
      """  The rowid of the OpMaster record to add the operation detail to  """  
      self.ipResourceID:str = obj["ipResourceID"]
      """  The Resource ID being added  """  
      self.ipNewOpDtlSeq:int = obj["ipNewOpDtlSeq"]
      """  The new operation detail seq  """  
      self.ipBeforeOpDtlRowid:str = obj["ipBeforeOpDtlRowid"]
      """  The operation detail rowid to insert operation detail before  """  
      pass

class InsertResource_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OpMasterTableset] = obj["returnObj"]
      pass

class OnChangingActionParamSeq_input:
   """ Required : 
   actionParamSeq
   ds
   """  
   def __init__(self, obj):
      self.actionParamSeq:int = obj["actionParamSeq"]
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class OnChangingActionParamSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingActionSeq_input:
   """ Required : 
   newActionSeq
   ds
   """  
   def __init__(self, obj):
      self.newActionSeq:int = obj["newActionSeq"]
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class OnChangingActionSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtOpMasterTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtOpMasterTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateInspection_input:
   """ Required : 
   ipProposedInspPlan
   ipProposedSpecId
   ds
   """  
   def __init__(self, obj):
      self.ipProposedInspPlan:str = obj["ipProposedInspPlan"]
      """  The new proposed InspPlanPartNum value  """  
      self.ipProposedSpecId:str = obj["ipProposedSpecId"]
      """  The new proposed SpecID value  """  
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

class ValidateInspection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OpMasterTableset] = obj["ds"]
      pass

      """  output parameters  """  

