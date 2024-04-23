import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EquipSvc
# Description: Equipment Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Equips(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Equips items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Equips
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips",headers=creds) as resp:
           return await resp.json()

async def post_Equips(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Equips
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EquipRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Equips_Company_EquipID(Company, EquipID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Equip item
   Description: Calls GetByID to retrieve the Equip item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Equip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Equips_Company_EquipID(Company, EquipID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Equip for the service
   Description: Calls UpdateExt to update Equip. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Equip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Equips_Company_EquipID(Company, EquipID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Equip item
   Description: Call UpdateExt to delete Equip item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Equip
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Equips_Company_EquipID_EquipPlans(Company, EquipID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EquipPlans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EquipPlans1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipPlans",headers=creds) as resp:
           return await resp.json()

async def get_Equips_Company_EquipID_EquipPlans_Company_EquipID_PlanNum(Company, EquipID, PlanNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EquipPlan item
   Description: Calls GetByID to retrieve the EquipPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlan1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Equips_Company_EquipID_EquipAttches(Company, EquipID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EquipAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EquipAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipAttches",headers=creds) as resp:
           return await resp.json()

async def get_Equips_Company_EquipID_EquipAttches_Company_EquipID_DrawingSeq(Company, EquipID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EquipAttch item
   Description: Calls GetByID to retrieve the EquipAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/Equips(" + Company + "," + EquipID + ")/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EquipPlans(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EquipPlans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EquipPlans
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans",headers=creds) as resp:
           return await resp.json()

async def post_EquipPlans(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EquipPlans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EquipPlans_Company_EquipID_PlanNum(Company, EquipID, PlanNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EquipPlan item
   Description: Calls GetByID to retrieve the EquipPlan item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlan
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EquipPlans_Company_EquipID_PlanNum(Company, EquipID, PlanNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EquipPlan for the service
   Description: Calls UpdateExt to update EquipPlan. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EquipPlan
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipPlanRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EquipPlans_Company_EquipID_PlanNum(Company, EquipID, PlanNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EquipPlan item
   Description: Call UpdateExt to delete EquipPlan item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EquipPlan
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EquipPlans_Company_EquipID_PlanNum_EquipPlanAttches(Company, EquipID, PlanNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EquipPlanAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EquipPlanAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")/EquipPlanAttches",headers=creds) as resp:
           return await resp.json()

async def get_EquipPlans_Company_EquipID_PlanNum_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company, EquipID, PlanNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EquipPlanAttch item
   Description: Calls GetByID to retrieve the EquipPlanAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlanAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlans(" + Company + "," + EquipID + "," + PlanNum + ")/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EquipPlanAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EquipPlanAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EquipPlanAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipPlanAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches",headers=creds) as resp:
           return await resp.json()

async def post_EquipPlanAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EquipPlanAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company, EquipID, PlanNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EquipPlanAttch item
   Description: Calls GetByID to retrieve the EquipPlanAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipPlanAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company, EquipID, PlanNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EquipPlanAttch for the service
   Description: Calls UpdateExt to update EquipPlanAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EquipPlanAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipPlanAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EquipPlanAttches_Company_EquipID_PlanNum_DrawingSeq(Company, EquipID, PlanNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EquipPlanAttch item
   Description: Call UpdateExt to delete EquipPlanAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EquipPlanAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param PlanNum: Desc: PlanNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipPlanAttches(" + Company + "," + EquipID + "," + PlanNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EquipAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EquipAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EquipAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches",headers=creds) as resp:
           return await resp.json()

async def post_EquipAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EquipAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EquipAttches_Company_EquipID_DrawingSeq(Company, EquipID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EquipAttch item
   Description: Calls GetByID to retrieve the EquipAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EquipAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EquipAttches_Company_EquipID_DrawingSeq(Company, EquipID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EquipAttch for the service
   Description: Calls UpdateExt to update EquipAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EquipAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EquipAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EquipAttches_Company_EquipID_DrawingSeq(Company, EquipID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EquipAttch item
   Description: Call UpdateExt to delete EquipAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EquipAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EquipID: Desc: EquipID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/EquipAttches(" + Company + "," + EquipID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EquipListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEquip, whereClauseEquipAttch, whereClauseEquipPlan, whereClauseEquipPlanAttch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseEquip=" + whereClauseEquip
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEquipAttch=" + whereClauseEquipAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEquipPlan=" + whereClauseEquipPlan
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEquipPlanAttch=" + whereClauseEquipPlanAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(equipID, epicorHeaders = None):
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
   params += "equipID=" + equipID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CalcAvgUsage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalcAvgUsage
   Description: This method returns the Average Daily Usage
   OperationID: CalcAvgUsage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalcAvgUsage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalcAvgUsage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportAssets(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportAssets
   Description: This method should be called when Import Assets records.
   OperationID: ImportAssets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportAssets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportAssets_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportResources(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportResources
   Description: This method should be called when Import Resources records.
   OperationID: ImportResources
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportResources_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportResources_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsMaintPlant(epicorHeaders = None):
   """  
   Summary: Invoke method IsMaintPlant
   Description: Returns true if Current Plant is a Maintenance plant.
Created to be called from EquipEntry.
If not a Maintenance plan the form will be in "Read Only" mode
   OperationID: IsMaintPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsMaintPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssetNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssetNum
   Description: This method should be called when AssetNum change.
   OperationID: OnChangeAssetNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssetNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssetNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeEquipTemplateJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeEquipTemplateJobNum
   Description: This method should be called when Equip.TemplateJobNum changes.
   OperationID: OnChangeEquipTemplateJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeEquipTemplateJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipTemplateJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIssueTopics(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIssueTopics
   Description: This method should be invoked when the IssueTopics changes.
Validates and sets the individual IssueTopic fields.
   OperationID: OnChangeIssueTopics
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIssueTopics_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIssueTopics_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMeterFreq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMeterFreq
   Description: This method should be called when MeterFreq change.
   OperationID: OnChangeMeterFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMeterFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMeterFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeParentEquipID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeParentEquipID
   Description: This method should be called when ParentEquipID change.
   OperationID: OnChangeParentEquipID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeParentEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeParentEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeProjectID
   Description: This method should be called when ProjectID change.
   OperationID: OnChangeProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeResourceID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeResourceID
   Description: This method should be called when ResourceID change.
   OperationID: OnChangeResourceID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeResourceID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResourceID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSellingPurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSellingPurPoint
   Description: This method should be called when SellingPurPoint change.
   OperationID: OnChangeSellingPurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSellingPurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSellingPurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSellingVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSellingVendor
   Description: This method should be called when SellingVendor change.
   OperationID: OnChangeSellingVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSellingVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSellingVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeServicePurPoint(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeServicePurPoint
   Description: This method should be called when ServicePurPoint change.
   OperationID: OnChangeServicePurPoint
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeServicePurPoint_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeServicePurPoint_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeServiceVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeServiceVendor
   Description: This method should be called when ServiceVendor change.
   OperationID: OnChangeServiceVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeServiceVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeServiceVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTemplateJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTemplateJobNum
   Description: This method should be called when EquipPlan.TemplateJobNum change.
   OperationID: OnChangeTemplateJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTemplateJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTemplateJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTimeFreq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTimeFreq
   Description: This method should be called when TimeFreq change.
   OperationID: OnChangeTimeFreq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTimeFreq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeFreq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTimeUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTimeUOM
   Description: This method should be called when TimeUOM change.
   OperationID: OnChangeTimeUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTimeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTimeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEquip(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEquip
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquip
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEquipAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEquipAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquipAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEquipAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquipAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEquipPlan(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEquipPlan
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquipPlan
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEquipPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquipPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEquipPlanAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEquipPlanAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEquipPlanAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEquipPlanAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEquipPlanAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EquipSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EquipAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EquipListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EquipPlanAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipPlanRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EquipPlanRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EquipRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EquipRow] = obj["value"]
      pass

class Erp_Tablesets_EquipAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EquipID:str = obj["EquipID"]
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

class Erp_Tablesets_EquipListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.DisablePlant:bool = obj["DisablePlant"]
      """  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  """  
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      """  Mandatory description of the asset.  """  
      self.EquipLocDescription:str = obj["EquipLocDescription"]
      """  Description the Location.  Cannot be blank.  """  
      self.EquipStatusDescription:str = obj["EquipStatusDescription"]
      """  Description of Equipment Status. Cannot be blank.  """  
      self.EquipTypeDescription:str = obj["EquipTypeDescription"]
      """  Description of Equipment Type. Cannot be blank.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ProjectDescription:str = obj["ProjectDescription"]
      """  Full description of Project Management Code.  """  
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      """  Description  """  
      self.ResourceDescription:str = obj["ResourceDescription"]
      """  Full description of Resource.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      """  Long description of the Resource Group.  """  
      self.SellingVendorNameName:str = obj["SellingVendorNameName"]
      """  Purchase Point Name...can't be blank.  """  
      self.SellingVendorNumVendorID:str = obj["SellingVendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.ServiceVendorNameName:str = obj["ServiceVendorNameName"]
      """  Purchase Point Name...can't be blank.  """  
      self.ServiceVendorNumVendorID:str = obj["ServiceVendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.UOMClassIDDescription:str = obj["UOMClassIDDescription"]
      """  A decription for the UOMClass.  Mandatory.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EquipPlanAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EquipID:str = obj["EquipID"]
      self.PlanNum:int = obj["PlanNum"]
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

class Erp_Tablesets_EquipPlanRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID that this EquipPlan record is for. A foreign key component to parent Equip record.  """  
      self.PlanNum:int = obj["PlanNum"]
      """  A number which uniquely identifies a preventative maintenance plan for a specific piece of equipment.  Generated by the system as PlanNum of last EquipPlan of a specific Company/EquipID + 1.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """   Description of maintenance plan. Cannot be blank.
Example: "30,000 Mile Checkup".  
Note: Will be used as the JobHead.PartDescription when the maintenance job is created.  """  
      self.TimeFreq:int = obj["TimeFreq"]
      """  Time Based Frequency. Examples Days, Weeks, Months  """  
      self.TimeUOM:str = obj["TimeUOM"]
      """  Qualifies the TimeFreq value as "Days, Weeks,  or Months"  """  
      self.MeterFreq:int = obj["MeterFreq"]
      """  A metered value, that when reached triggers the maintenance plan. Example: At  5000 miles this Maintenance is required. The Equip.MeterUOM qualifies this value.  """  
      self.Recurs:bool = obj["Recurs"]
      """   Indicates if Plan is to be performed at every occurance or only the first occurance of the defined frequencies.
Example of a Recurring Plan would be "Change oil every 5000 miles".
An example of a non recurring plan would be "Initial Break in checkup".  """  
      self.NextDate:str = obj["NextDate"]
      """  Next Date that this Maintenance Plan should be performed. This is relevant only to a "time based" maintenance plan (TimeFreq > 0) otherwise it is null and not maintainable. If TimeFreq, TimeUOM changes or when Plan is executed, it is set as today + time frequency (in days). Note; can be manually updated allowing the user to control the next time based event.  """  
      self.NextMeter:int = obj["NextMeter"]
      """  Next Meter Reading at which this Maintenance Plan should be performed. This is relevant only to a "meter based" maintenance plan (MeterFreq > 0) otherwise it is zero and not maintainable. If MeterFreq changes or when Plan is executed, it is set as CurrentMeter + MeterFreq.  Note; can be manually updated allowing the user to control the next meter event.  For example, the frequency is 3000 Miles, however, you set NextMeter to 500 Miles for the Initial Break In Checkup.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.ActionStatus:str = obj["ActionStatus"]
      """  Internal field indicating if it is time current action being taken. Used by the PMPP (Preventive Maintenance Plan Processor) to quickly find Plans which need to be performed. Set to "P" (Pending), when the Maintenance Job is closed or deleted. Set to "Q" (Queued) when the Plans frequencies are met.  That is, NextMeter > 0 and <= Current or NextDate <> ? and <= Today. Setting based on meter occurs as part of the Meter Reading process. Setting based on Date, is done, periodically by the PMPP. Set to "I" (Initiated) by the PMPP when a Job is generated.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.MaintBuffer:int = obj["MaintBuffer"]
      """  Number of days prior to the actual  maintenance event that the system should create the Maintenance Job.    This applies to both time based and meter based plans. Defaults to  MMSyst.MaintBuffer value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      self.IssueTopics:str = obj["IssueTopics"]
      """  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EquipRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.DisablePlant:bool = obj["DisablePlant"]
      """  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      self.EquipLocDescription:str = obj["EquipLocDescription"]
      self.EquipStatusDescription:str = obj["EquipStatusDescription"]
      self.EquipTypeDescription:str = obj["EquipTypeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ParentDescription:str = obj["ParentDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.SellingVendorNameName:str = obj["SellingVendorNameName"]
      self.SellingVendorNumVendorID:str = obj["SellingVendorNumVendorID"]
      self.ServiceVendorNameName:str = obj["ServiceVendorNameName"]
      self.ServiceVendorNumVendorID:str = obj["ServiceVendorNumVendorID"]
      self.UOMClassIDDescription:str = obj["UOMClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CalcAvgUsage_input:
   """ Required : 
   equipID
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      """  equipID  """  
      pass

class CalcAvgUsage_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.avgUsage:int = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   equipID
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EquipAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EquipID:str = obj["EquipID"]
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

class Erp_Tablesets_EquipListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.DisablePlant:bool = obj["DisablePlant"]
      """  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  """  
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      """  Mandatory description of the asset.  """  
      self.EquipLocDescription:str = obj["EquipLocDescription"]
      """  Description the Location.  Cannot be blank.  """  
      self.EquipStatusDescription:str = obj["EquipStatusDescription"]
      """  Description of Equipment Status. Cannot be blank.  """  
      self.EquipTypeDescription:str = obj["EquipTypeDescription"]
      """  Description of Equipment Type. Cannot be blank.  """  
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ParentDescription:str = obj["ParentDescription"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.ProjectDescription:str = obj["ProjectDescription"]
      """  Full description of Project Management Code.  """  
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      """  Description  """  
      self.ResourceDescription:str = obj["ResourceDescription"]
      """  Full description of Resource.  """  
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      """  Long description of the Resource Group.  """  
      self.SellingVendorNameName:str = obj["SellingVendorNameName"]
      """  Purchase Point Name...can't be blank.  """  
      self.SellingVendorNumVendorID:str = obj["SellingVendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.ServiceVendorNameName:str = obj["ServiceVendorNameName"]
      """  Purchase Point Name...can't be blank.  """  
      self.ServiceVendorNumVendorID:str = obj["ServiceVendorNumVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.UOMClassIDDescription:str = obj["UOMClassIDDescription"]
      """  A decription for the UOMClass.  Mandatory.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EquipListTableset:
   def __init__(self, obj):
      self.EquipList:list[Erp_Tablesets_EquipListRow] = obj["EquipList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EquipPlanAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EquipID:str = obj["EquipID"]
      self.PlanNum:int = obj["PlanNum"]
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

class Erp_Tablesets_EquipPlanRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  EquipID that this EquipPlan record is for. A foreign key component to parent Equip record.  """  
      self.PlanNum:int = obj["PlanNum"]
      """  A number which uniquely identifies a preventative maintenance plan for a specific piece of equipment.  Generated by the system as PlanNum of last EquipPlan of a specific Company/EquipID + 1.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """   Description of maintenance plan. Cannot be blank.
Example: "30,000 Mile Checkup".  
Note: Will be used as the JobHead.PartDescription when the maintenance job is created.  """  
      self.TimeFreq:int = obj["TimeFreq"]
      """  Time Based Frequency. Examples Days, Weeks, Months  """  
      self.TimeUOM:str = obj["TimeUOM"]
      """  Qualifies the TimeFreq value as "Days, Weeks,  or Months"  """  
      self.MeterFreq:int = obj["MeterFreq"]
      """  A metered value, that when reached triggers the maintenance plan. Example: At  5000 miles this Maintenance is required. The Equip.MeterUOM qualifies this value.  """  
      self.Recurs:bool = obj["Recurs"]
      """   Indicates if Plan is to be performed at every occurance or only the first occurance of the defined frequencies.
Example of a Recurring Plan would be "Change oil every 5000 miles".
An example of a non recurring plan would be "Initial Break in checkup".  """  
      self.NextDate:str = obj["NextDate"]
      """  Next Date that this Maintenance Plan should be performed. This is relevant only to a "time based" maintenance plan (TimeFreq > 0) otherwise it is null and not maintainable. If TimeFreq, TimeUOM changes or when Plan is executed, it is set as today + time frequency (in days). Note; can be manually updated allowing the user to control the next time based event.  """  
      self.NextMeter:int = obj["NextMeter"]
      """  Next Meter Reading at which this Maintenance Plan should be performed. This is relevant only to a "meter based" maintenance plan (MeterFreq > 0) otherwise it is zero and not maintainable. If MeterFreq changes or when Plan is executed, it is set as CurrentMeter + MeterFreq.  Note; can be manually updated allowing the user to control the next meter event.  For example, the frequency is 3000 Miles, however, you set NextMeter to 500 Miles for the Initial Break In Checkup.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.ActionStatus:str = obj["ActionStatus"]
      """  Internal field indicating if it is time current action being taken. Used by the PMPP (Preventive Maintenance Plan Processor) to quickly find Plans which need to be performed. Set to "P" (Pending), when the Maintenance Job is closed or deleted. Set to "Q" (Queued) when the Plans frequencies are met.  That is, NextMeter > 0 and <= Current or NextDate <> ? and <= Today. Setting based on meter occurs as part of the Meter Reading process. Setting based on Date, is done, periodically by the PMPP. Set to "I" (Initiated) by the PMPP when a Job is generated.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.MaintBuffer:int = obj["MaintBuffer"]
      """  Number of days prior to the actual  maintenance event that the system should create the Maintenance Job.    This applies to both time based and meter based plans. Defaults to  MMSyst.MaintBuffer value.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      self.IssueTopics:str = obj["IssueTopics"]
      """  Used as an alternate method to enter Issue Topics.  A space separated list of IssueTopicID's. They will update the physical IssueTopicID1 - 10 fields.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EquipRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EquipID:str = obj["EquipID"]
      """  Descriptive code assigned by the user to uniquely identify the Equipment. Cannot be blank.  """  
      self.Plant:str = obj["Plant"]
      """  Site in which the equipment is currently located.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if Equipment is considered as "Inactive".  """  
      self.Description:str = obj["Description"]
      """  Full description of Equipment. Cannot be blank.  """  
      self.StatusID:str = obj["StatusID"]
      """  The User Defined status assigned to the Equipment. A foreign key to EquipStatus. Optional, but if entered must be valid in EquipStatus  """  
      self.OEM:str = obj["OEM"]
      """  OEM Number  """  
      self.SerialNum:str = obj["SerialNum"]
      """  Serial Number of equipment  """  
      self.Brand:str = obj["Brand"]
      """  Brand of equipment  """  
      self.Model:str = obj["Model"]
      """  Model Number  """  
      self.InServiceDate:str = obj["InServiceDate"]
      """  Date that equipment was first put into service. Required field.  """  
      self.WarrantyExpDate:str = obj["WarrantyExpDate"]
      """  Warrenty Expiration Date  """  
      self.TypeID:str = obj["TypeID"]
      """  Equipment Type ID. Foreign key component of EquipType.  Required and must be valid in EquipType table.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  A code that identifies the Resource Group that the resource belongs to.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource.  """  
      self.SellingVendorNum:int = obj["SellingVendorNum"]
      """  VendorNum of the Supplier that sold equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.SellingPurPoint:str = obj["SellingPurPoint"]
      """  The Selling Vendors Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.ServiceVendorNum:int = obj["ServiceVendorNum"]
      """  VendorNum of the Supplier that services the equipment. Optional field, but if entered must be valid. Informational only. Foreign key component to VendorPP table. Not directly maintainable, instead user enters "VendorID", system assigns he VendorNum of the Vendor that has this VendorID.  """  
      self.ServicePurPoint:str = obj["ServicePurPoint"]
      """  The Service Suppliers Purchase Point ID.  Along with the VendorNum is used to tie back to the VendorPP master file.   Foreign key component to VendorPP table.  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Foreign Component key to the FAsset table.  """  
      self.Comments:str = obj["Comments"]
      """  Comments about the Equipment.  """  
      self.Specs:str = obj["Specs"]
      """  Allows entry of freeform equipment specifications.  """  
      self.MeterUOM:str = obj["MeterUOM"]
      """  Qualifies the MeterFreq value. This can be blank, which indicates that Maintenance is not based a meter nor can meter readings be entered for this equipment. If not blank it must be valid in the UOM table and be a UOM belonging to the UOMClass assigned to the Equip.  """  
      self.CurrentMeter:int = obj["CurrentMeter"]
      """  Current Meter reading.  A readonly field, indirectly updated via the Meter Reading process.  """  
      self.ReadingComment:str = obj["ReadingComment"]
      """  Contains the latest Meter Reading Comment.  As the Meter Reading UI updates the Equip record a record is also created in EquipMeter.  EquipMeter.ReadingComment is set to this value.  """  
      self.LocID:str = obj["LocID"]
      """  Location of the Equipment. A foreign key component to EquipLoc table.  It not blank must be valid in EquipLoc table.  """  
      self.ParentEquipID:str = obj["ParentEquipID"]
      """  The EquipID that is considered the Parent Equipment.  Can be blank. If entered must be valid in the Equip table and cannot be = to the current Equip.EquipID.  Used primarly for grouping equipement together for reporting.  """  
      self.LaborMeterOpt:str = obj["LaborMeterOpt"]
      """   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  """  
      self.ReadingDate:str = obj["ReadingDate"]
      """  Read only, set by the system, set as current system date when updated from Meter Entry. Uses Labor Clock Out Date when updated via Labor Entry.  This value is used to set EquipMeter.ReadingDate  """  
      self.ReadingTime:int = obj["ReadingTime"]
      """  Read only, Read only, set by the system, set as current system time when updated from Meter Entry. Uses Labor Clock Out Time when updated via Labor Entry.  This value is used to set EquipMeter.ReadingTime. Represented in milliseconds since midnight.  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number) to be used for inspection results entry process.  Must be a valid part number in the Part master table.  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID to be used for inspection results entry process.  Must be a valid SpecID in the SpecHed master table.  """  
      self.LastCalDate:str = obj["LastCalDate"]
      """  This field will be automatically populated when the item has been calibrated using the Inspection Data Entry process  """  
      self.InspPlanRevNum:str = obj["InspPlanRevNum"]
      """  The inspection plan revision number (configurator revision number).  """  
      self.SpecRevNum:str = obj["SpecRevNum"]
      """  The specification revision number.  Must be valid in the SpecRev table.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the Equip with a project in the Project table.  This can be blank.  Provides default when a Job is created for this Equip.  """  
      self.UOMClassID:str = obj["UOMClassID"]
      """   The UOM Class that will be used for the Equip. The UOM Class establishes the list of unit of measures that can be used for the MeterUOM
Must be valid in the UOMClass table.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.Lineage:str = obj["Lineage"]
      """  Stores the keys (EquipID) of the records ancestors, as a tilde delimited list (... Great GrandParent~ GrandParent~ParentKey~ChildKey)  This field is word indexed providing searches using the Contains phrase.  """  
      self.TemplateJobNum:str = obj["TemplateJobNum"]
      """  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  """  
      self.AvgDailyUsage:int = obj["AvgDailyUsage"]
      self.GlobalEquip:bool = obj["GlobalEquip"]
      """  Marks this Equip as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JCDeptDesc:str = obj["JCDeptDesc"]
      self.DisablePlant:bool = obj["DisablePlant"]
      """  Indicates the Equip.Plant field should be disabled/readonly. Set to true if Jobs or Maintenance Request exist for the Equipment.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssetNumAssetDescription:str = obj["AssetNumAssetDescription"]
      self.EquipLocDescription:str = obj["EquipLocDescription"]
      self.EquipStatusDescription:str = obj["EquipStatusDescription"]
      self.EquipTypeDescription:str = obj["EquipTypeDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.ParentDescription:str = obj["ParentDescription"]
      self.PlantName:str = obj["PlantName"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      self.ResourceDescription:str = obj["ResourceDescription"]
      self.ResourceGroupDescription:str = obj["ResourceGroupDescription"]
      self.SellingVendorNameName:str = obj["SellingVendorNameName"]
      self.SellingVendorNumVendorID:str = obj["SellingVendorNumVendorID"]
      self.ServiceVendorNameName:str = obj["ServiceVendorNameName"]
      self.ServiceVendorNumVendorID:str = obj["ServiceVendorNumVendorID"]
      self.UOMClassIDDescription:str = obj["UOMClassIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EquipTableset:
   def __init__(self, obj):
      self.Equip:list[Erp_Tablesets_EquipRow] = obj["Equip"]
      self.EquipAttch:list[Erp_Tablesets_EquipAttchRow] = obj["EquipAttch"]
      self.EquipPlan:list[Erp_Tablesets_EquipPlanRow] = obj["EquipPlan"]
      self.EquipPlanAttch:list[Erp_Tablesets_EquipPlanAttchRow] = obj["EquipPlanAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtEquipTableset:
   def __init__(self, obj):
      self.Equip:list[Erp_Tablesets_EquipRow] = obj["Equip"]
      self.EquipAttch:list[Erp_Tablesets_EquipAttchRow] = obj["EquipAttch"]
      self.EquipPlan:list[Erp_Tablesets_EquipPlanRow] = obj["EquipPlan"]
      self.EquipPlanAttch:list[Erp_Tablesets_EquipPlanAttchRow] = obj["EquipPlanAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   equipID
   """  
   def __init__(self, obj):
      self.equipID:str = obj["equipID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EquipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EquipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EquipTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EquipListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEquipAttch_input:
   """ Required : 
   ds
   equipID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      self.equipID:str = obj["equipID"]
      pass

class GetNewEquipAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEquipPlanAttch_input:
   """ Required : 
   ds
   equipID
   planNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      self.equipID:str = obj["equipID"]
      self.planNum:int = obj["planNum"]
      pass

class GetNewEquipPlanAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEquipPlan_input:
   """ Required : 
   ds
   equipID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      self.equipID:str = obj["equipID"]
      pass

class GetNewEquipPlan_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEquip_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class GetNewEquip_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEquip
   whereClauseEquipAttch
   whereClauseEquipPlan
   whereClauseEquipPlanAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEquip:str = obj["whereClauseEquip"]
      self.whereClauseEquipAttch:str = obj["whereClauseEquipAttch"]
      self.whereClauseEquipPlan:str = obj["whereClauseEquipPlan"]
      self.whereClauseEquipPlanAttch:str = obj["whereClauseEquipPlanAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EquipTableset] = obj["returnObj"]
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

class ImportAssets_input:
   """ Required : 
   ipAssetNum
   ds
   """  
   def __init__(self, obj):
      self.ipAssetNum:str = obj["ipAssetNum"]
      """  Asset Num  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class ImportAssets_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportResources_input:
   """ Required : 
   ipResourceID
   ds
   """  
   def __init__(self, obj):
      self.ipResourceID:str = obj["ipResourceID"]
      """  ResourceID  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class ImportResources_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class IsMaintPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isMaintPlant:bool = obj["isMaintPlant"]
      pass

      """  output parameters  """  

class OnChangeAssetNum_input:
   """ Required : 
   assetNum
   ds
   """  
   def __init__(self, obj):
      self.assetNum:str = obj["assetNum"]
      """  assetNum  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeAssetNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeEquipTemplateJobNum_input:
   """ Required : 
   ipJobNum
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Num  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeEquipTemplateJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeIssueTopics_input:
   """ Required : 
   topics
   ds
   """  
   def __init__(self, obj):
      self.topics:str = obj["topics"]
      """  Proposed topics string id  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeIssueTopics_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMeterFreq_input:
   """ Required : 
   ipMeterFreq
   ds
   """  
   def __init__(self, obj):
      self.ipMeterFreq:int = obj["ipMeterFreq"]
      """  Meter Freq  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeMeterFreq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeParentEquipID_input:
   """ Required : 
   parentID
   ds
   """  
   def __init__(self, obj):
      self.parentID:str = obj["parentID"]
      """  parentID  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeParentEquipID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeProjectID_input:
   """ Required : 
   projectID
   ds
   """  
   def __init__(self, obj):
      self.projectID:str = obj["projectID"]
      """  projectID  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeResourceID_input:
   """ Required : 
   resourceID
   ds
   """  
   def __init__(self, obj):
      self.resourceID:str = obj["resourceID"]
      """  resourceID  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeResourceID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSellingPurPoint_input:
   """ Required : 
   sellingPurPoint
   ds
   """  
   def __init__(self, obj):
      self.sellingPurPoint:str = obj["sellingPurPoint"]
      """  sellingPurPoint  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeSellingPurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSellingVendor_input:
   """ Required : 
   vendorID
   ds
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      """  vendorID  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeSellingVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeServicePurPoint_input:
   """ Required : 
   servicePurPoint
   ds
   """  
   def __init__(self, obj):
      self.servicePurPoint:str = obj["servicePurPoint"]
      """  sellingPurPoint  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeServicePurPoint_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeServiceVendor_input:
   """ Required : 
   vendorID
   ds
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      """  vendorID  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeServiceVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTemplateJobNum_input:
   """ Required : 
   ipJobNum
   ds
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  Job Num  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeTemplateJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTimeFreq_input:
   """ Required : 
   ipTimeFreq
   ds
   """  
   def __init__(self, obj):
      self.ipTimeFreq:int = obj["ipTimeFreq"]
      """  Time Freq  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeTimeFreq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTimeUOM_input:
   """ Required : 
   ipTimeUOM
   ds
   """  
   def __init__(self, obj):
      self.ipTimeUOM:str = obj["ipTimeUOM"]
      """  Time UOM  """  
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class OnChangeTimeUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEquipTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEquipTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EquipTableset] = obj["ds"]
      pass

      """  output parameters  """  

