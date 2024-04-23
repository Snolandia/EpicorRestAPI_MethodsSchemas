import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ConfiguratorRuleSvc
# Description: This Business Object allows the modification of configurator method and structure rules
            The configurator is the design portion that is run during a configuration.
           
            Business Object for the configurator rule designer
            Brock Mulqueen
            07/12/12
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ConfiguratorRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ConfiguratorRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules",headers=creds) as resp:
           return await resp.json()

async def post_ConfiguratorRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ConfiguratorRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartRevRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ConfiguratorRules_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, PartNum, RevisionNum, AltMethod, ProcessMfgID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ConfiguratorRule item
   Description: Calls GetByID to retrieve the ConfiguratorRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ConfiguratorRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartRevRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ConfiguratorRules_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, PartNum, RevisionNum, AltMethod, ProcessMfgID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ConfiguratorRule for the service
   Description: Calls UpdateExt to update ConfiguratorRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ConfiguratorRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartRevRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ConfiguratorRules_Company_PartNum_RevisionNum_AltMethod_ProcessMfgID(Company, PartNum, RevisionNum, AltMethod, ProcessMfgID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ConfiguratorRule item
   Description: Call UpdateExt to delete ConfiguratorRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ConfiguratorRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param ProcessMfgID: Desc: ProcessMfgID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/ConfiguratorRules(" + Company + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + ProcessMfgID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcMethodVars(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcMethodVars items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcMethodVars
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcMethodVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars",headers=creds) as resp:
           return await resp.json()

async def post_PcMethodVars(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcMethodVars
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcMethodVarRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcMethodVarRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcMethodVars_Company_ConfigID_PartNum_RevisionNum_AltMethod_VarNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, VarNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcMethodVar item
   Description: Calls GetByID to retrieve the PcMethodVar item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcMethodVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param VarNum: Desc: VarNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcMethodVarRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + VarNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcMethodVars_Company_ConfigID_PartNum_RevisionNum_AltMethod_VarNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, VarNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcMethodVar for the service
   Description: Calls UpdateExt to update PcMethodVar. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcMethodVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param VarNum: Desc: VarNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcMethodVarRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + VarNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcMethodVars_Company_ConfigID_PartNum_RevisionNum_AltMethod_VarNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, VarNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcMethodVar item
   Description: Call UpdateExt to delete PcMethodVar item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcMethodVar
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param VarNum: Desc: VarNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcMethodVars(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + VarNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcRuleSets(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcRuleSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcRuleSets
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRuleSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets",headers=creds) as resp:
           return await resp.json()

async def post_PcRuleSets(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcRuleSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcRuleSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcRuleSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID(Company, ConfigID, PartNum, RevisionNum, AltMethod, BOMElementTableName, BOMElementSysRowID, RuleTag, RuleSetID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcRuleSet item
   Description: Calls GetByID to retrieve the PcRuleSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRuleSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param BOMElementTableName: Desc: BOMElementTableName   Required: True   Allow empty value : True
      :param BOMElementSysRowID: Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      :param RuleTag: Desc: RuleTag   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcRuleSetRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID(Company, ConfigID, PartNum, RevisionNum, AltMethod, BOMElementTableName, BOMElementSysRowID, RuleTag, RuleSetID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcRuleSet for the service
   Description: Calls UpdateExt to update PcRuleSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcRuleSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param BOMElementTableName: Desc: BOMElementTableName   Required: True   Allow empty value : True
      :param BOMElementSysRowID: Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      :param RuleTag: Desc: RuleTag   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcRuleSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID(Company, ConfigID, PartNum, RevisionNum, AltMethod, BOMElementTableName, BOMElementSysRowID, RuleTag, RuleSetID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcRuleSet item
   Description: Call UpdateExt to delete PcRuleSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcRuleSet
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param BOMElementTableName: Desc: BOMElementTableName   Required: True   Allow empty value : True
      :param BOMElementSysRowID: Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      :param RuleTag: Desc: RuleTag   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID_PcRules(Company, ConfigID, PartNum, RevisionNum, AltMethod, BOMElementTableName, BOMElementSysRowID, RuleTag, RuleSetID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcRules1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param BOMElementTableName: Desc: BOMElementTableName   Required: True   Allow empty value : True
      :param BOMElementSysRowID: Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      :param RuleTag: Desc: RuleTag   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")/PcRules",headers=creds) as resp:
           return await resp.json()

async def get_PcRuleSets_Company_ConfigID_PartNum_RevisionNum_AltMethod_BOMElementTableName_BOMElementSysRowID_RuleTag_RuleSetID_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company, ConfigID, PartNum, RevisionNum, AltMethod, BOMElementTableName, BOMElementSysRowID, RuleTag, RuleSetID, RuleSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcRule item
   Description: Calls GetByID to retrieve the PcRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRule1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param BOMElementTableName: Desc: BOMElementTableName   Required: True   Allow empty value : True
      :param BOMElementSysRowID: Desc: BOMElementSysRowID   Required: True   Allow empty value : True
      :param RuleTag: Desc: RuleTag   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcRulesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRuleSets(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + BOMElementTableName + "," + BOMElementSysRowID + "," + RuleTag + "," + RuleSetID + ")/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcRules(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcRules
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules",headers=creds) as resp:
           return await resp.json()

async def post_PcRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcRulesRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcRulesRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcRule item
   Description: Calls GetByID to retrieve the PcRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcRulesRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcRule for the service
   Description: Calls UpdateExt to update PcRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcRulesRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcRule item
   Description: Call UpdateExt to delete PcRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_PcRulesExprs(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PcRulesExprs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PcRulesExprs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")/PcRulesExprs",headers=creds) as resp:
           return await resp.json()

async def get_PcRules_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcRulesExpr item
   Description: Calls GetByID to retrieve the PcRulesExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRulesExpr1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRules(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + ")/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PcRulesExprs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PcRulesExprs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PcRulesExprs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PcRulesExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs",headers=creds) as resp:
           return await resp.json()

async def post_PcRulesExprs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PcRulesExprs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, TypeCode, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PcRulesExpr item
   Description: Calls GetByID to retrieve the PcRulesExpr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PcRulesExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, TypeCode, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PcRulesExpr for the service
   Description: Calls UpdateExt to update PcRulesExpr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PcRulesExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PcRulesExprRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PcRulesExprs_Company_ConfigID_PartNum_RevisionNum_AltMethod_RuleSetID_RuleSeq_TypeCode_SeqNum(Company, ConfigID, PartNum, RevisionNum, AltMethod, RuleSetID, RuleSeq, TypeCode, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PcRulesExpr item
   Description: Call UpdateExt to delete PcRulesExpr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PcRulesExpr
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ConfigID: Desc: ConfigID   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param RevisionNum: Desc: RevisionNum   Required: True   Allow empty value : True
      :param AltMethod: Desc: AltMethod   Required: True   Allow empty value : True
      :param RuleSetID: Desc: RuleSetID   Required: True
      :param RuleSeq: Desc: RuleSeq   Required: True
      :param TypeCode: Desc: TypeCode   Required: True   Allow empty value : True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/PcRulesExprs(" + Company + "," + ConfigID + "," + PartNum + "," + RevisionNum + "," + AltMethod + "," + RuleSetID + "," + RuleSeq + "," + TypeCode + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartRevListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartRev, whereClausePcMethodVar, whereClausePcRuleSet, whereClausePcRules, whereClausePcRulesExpr, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePartRev=" + whereClausePartRev
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcMethodVar=" + whereClausePcMethodVar
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcRuleSet=" + whereClausePcRuleSet
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcRules=" + whereClausePcRules
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePcRulesExpr=" + whereClausePcRulesExpr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, revisionNum, altMethod, processMfgID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "revisionNum=" + revisionNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "altMethod=" + altMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "processMfgID=" + processMfgID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Method to call to get a Code Description list.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SalesKitConfiguration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SalesKitConfiguration
   Description: If a partplant record is available for the current plant then check the SourceType
If not partplant available then check the typecode on the part record.
   OperationID: SalesKitConfiguration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SalesKitConfiguration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SalesKitConfiguration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckIsConfigured(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckIsConfigured
   Description: This methods is called prior to expanding a tree node on the Rules tab.  If the
part is a configureable part, the node will not be expanded
   OperationID: CheckIsConfigured
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckIsConfigured_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckIsConfigured_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RulesMoveDown(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RulesMoveDown
   Description: Move a rule down in the order of configuration rules.
   OperationID: RulesMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RulesMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RulesMoveUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RulesMoveUp
   Description: Move a rule up in the order of configuration rules.
   OperationID: RulesMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RulesMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RulesMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters but only for the main revision the alternate methods will only will be add the ParRev record
This method will also allow you to return the whole dataset or allow the user to specify how
the revision to return possible "part" records for.
   OperationID: GetDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllAlternateTrees(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllAlternateTrees
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
ALL ALTERNATES OF THE PARTREVISION WILL BE RETURNED if ipcomplete is true
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
Vdavila - To allow keep the position of the current element in tree view when refresh we are going to use the
lastNodeKey to continue building the BOM for non-configure subassemblies
   OperationID: GetAllAlternateTrees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllAlternateTrees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllAlternateTrees_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PromptForPassword(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PromptForPassword
   Description: This method checks the BMSyst record to see if a password should prompted for and then
validated by the ValidatePassword method in UserFile BO.  Run this before SyncRevision method is called.
   OperationID: PromptForPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PromptForPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PromptForPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SyncRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SyncRevision
   Description: This method synchronizes the part revision approval flag when the PcStatus.Approved
flag changes
   OperationID: SyncRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SyncRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SyncRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangingEntConf(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangingEntConf
   Description: This methods checks to see if any enterprise configurator specific settings
have been created.  If so then a message should be displayed prior to unchecking
the enterprise configurator checkbox
   OperationID: ChangingEntConf
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangingEntConf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangingEntConf_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcRulesExprExprType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcRulesExprExprType
   Description: This method is executed when changing the ExprType column of PcRulesExpr, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcRulesExprExprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcRulesExprExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcRulesExprExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcRulesRuleType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcRulesRuleType
   Description: This method is executed when changing the RuleType column of PcRules, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcRulesRuleType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcRulesRuleType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcRulesRuleType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePcRulesExprLValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePcRulesExprLValue
   Description: This method is executed when changing the LValue column of PcRulesExpr, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcRulesExprLValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcRulesExprLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcRulesExprLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePcRulesLValue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePcRulesLValue
   Description: This method is executed when changing the LValue column of PcRules, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangePcRulesLValue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePcRulesLValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePcRulesLValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Validate if exists PartNum and returns the partnum
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedRuleSetCompany(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedRuleSetCompany
   Description: Change Company when click check boxes for Multi-Company or Local company
Must clear the list of companies in case already selected in picker list
   OperationID: OnChangedRuleSetCompany
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedRuleSetCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedRuleSetCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePcRulesDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePcRulesDelete
   Description: Validate if exist child record when try to delete
   OperationID: ValidatePcRulesDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePcRulesDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePcRulesDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EditorFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EditorFilter
   Description: Return filter for editor
   OperationID: EditorFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EditorFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EditorFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetValidTargetEntitiesAndInputs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetValidTargetEntitiesAndInputs
   Description: Gathers valid target entities
   OperationID: GetValidTargetEntitiesAndInputs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidTargetEntitiesAndInputs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidTargetEntitiesAndInputs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingPcMethodVarDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingPcMethodVarDataType
   Description: Validate variable is not being used.
   OperationID: OnChangingPcMethodVarDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPcMethodVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcMethodVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcMethodVarDataType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcMethodVarDataType
   Description: Clean DataType when dataType is changed
   OperationID: OnChangedPcMethodVarDataType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcMethodVarDataType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcMethodVarDataType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingPcMethodVarVarName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingPcMethodVarVarName
   Description: Validate Changing VarName
   OperationID: OnChangingPcMethodVarVarName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingPcMethodVarVarName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingPcMethodVarVarName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedPcMethodVarExprType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedPcMethodVarExprType
   Description: This method is executed when changing the ExprType column of PcMethod, it is used to validate the new value and set
defaults based on it.
   OperationID: OnChangedPcMethodVarExprType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedPcMethodVarExprType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedPcMethodVarExprType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MethodVarMoveDown(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MethodVarMoveDown
   Description: Move a Variable down in the order of method variables.
   OperationID: MethodVarMoveDown
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MethodVarMoveDown_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MethodVarMoveDown_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MethodVarMoveUp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MethodVarMoveUp
   Description: Move a Variable up in the order of method variables.
   OperationID: MethodVarMoveUp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MethodVarMoveUp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MethodVarMoveUp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailMethodVariables(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailMethodVariables
   Description: Get the available method variables that may be used in code editor.
   OperationID: GetAvailMethodVariables
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailMethodVariables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailMethodVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRevisionNum
   Description: When type a revision in revision combo it validates if revision exists
   OperationID: ValidateRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangedConfigID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangedConfigID
   Description: Assign the configurator id to alt methods
   OperationID: OnChangedConfigID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedConfigID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedConfigID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BeforeStartTestRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BeforeStartTestRules
   Description: Generates the configuration sequence and validate if non of the configurators has rules then throw exception and will not open Test Rules window,
and build the message that will send when there are configurators not approved
   OperationID: BeforeStartTestRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BeforeStartTestRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BeforeStartTestRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyMethodRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyMethodRules
   Description: Copy rules from the Source part to the part selected in Copy Rules Form
-CopyActions:
-Replace: Will delete the existing rules from target part
-Append:  Will search if already exists a rule set using rule tag if exists will not copy anything neither rule set, rules or rulesexpr
Create results data to display it in a grid.
-Copied: rules copied successfully
-Not Copied: rules not copied because already exists rule set or does not exists element in target BOM
-Exception: will not display anything when element does not exists in target BOM and source BOM
-
   OperationID: CopyMethodRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyMethodRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyMethodRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimaryPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimaryPartNum
   Description: Find the Primary Part Number for a Configuration ID
   OperationID: GetPrimaryPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartRev(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartRev
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartRev
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartRev_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartRev_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcMethodVar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcMethodVar
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcMethodVar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcMethodVar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcMethodVar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcRuleSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcRuleSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcRuleSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcRuleSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcRuleSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcRules
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPcRulesExpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPcRulesExpr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPcRulesExpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPcRulesExpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPcRulesExpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ConfiguratorRuleSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartRevListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartRevRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcMethodVarRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcMethodVarRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRuleSetRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcRuleSetRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesExprRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcRulesExprRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PcRulesRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PcRulesRow] = obj["value"]
      pass

class Erp_Tablesets_PartRevListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.ProdCode:str = obj["ProdCode"]
      self.NonStock:bool = obj["NonStock"]
      self.Class:str = obj["Class"]
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      """  The description of the inspection plan  """  
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      """  Describes the Part.  """  
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      """  Full description of the rough cut parameter set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      """  SIValuesGroupSeq  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      """  SIValuesHeadNum  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.DefaultConfigPart:bool = obj["DefaultConfigPart"]
      """  DefaultConfigPart  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  Number of COPart required in the Revision  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  Material Cost Factor  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  Labor Cost Factor  """  
      self.CoPartsPerOp:int = obj["CoPartsPerOp"]
      """  Number of COParts per Operation  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      """  Customs BOM  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: General, Site, Master.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ProcessMfgLastGroupID:str = obj["ProcessMfgLastGroupID"]
      """  The last Group to modify this Revision for Recipe Authoring.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      """  This field will be set to true if two or more ECOCoParts records exist for the revision.  """  
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part Number of the Parent Part  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  Revision number  of Parent Part.  """  
      self.ProdCode:str = obj["ProdCode"]
      self.RevStatusAsOfDate:int = obj["RevStatusAsOfDate"]
      """   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.Class:str = obj["Class"]
      self.NonStock:bool = obj["NonStock"]
      self.IsRootNode:bool = obj["IsRootNode"]
      """  Indicates that the PartRev is the root node in the tree  """  
      self.EngineeringApproved:bool = obj["EngineeringApproved"]
      """  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      self.PartDescriptionTypeCode:str = obj["PartDescriptionTypeCode"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PlantName:str = obj["PlantName"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcMethodVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.VarNum:int = obj["VarNum"]
      """  VarNum  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.VarSeq:int = obj["VarSeq"]
      """  VarSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DispLinkString:str = obj["DispLinkString"]
      """  Temporal column to show link phrase  """  
      self.Format:str = obj["Format"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRuleSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      """  BOMElementSysRowID  """  
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      """  BOMElementTableName  """  
      self.BOMElementType:str = obj["BOMElementType"]
      """  BOMElementType  """  
      self.RuleTag:str = obj["RuleTag"]
      """  RuleTag  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  MtlSeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  OpDtlSeq  """  
      self.UseKeepWhen:bool = obj["UseKeepWhen"]
      """  UseKeepWhen  """  
      self.KeepWhenExpr:str = obj["KeepWhenExpr"]
      """  KeepWhenExpr  """  
      self.KeepWhenLValue:str = obj["KeepWhenLValue"]
      """  KeepWhenLValue  """  
      self.KeepWhenCompareOpr:str = obj["KeepWhenCompareOpr"]
      """  KeepWhenCompareOpr  """  
      self.KeepWhenRValue:str = obj["KeepWhenRValue"]
      """  KeepWhenRValue  """  
      self.KeepWhenRValueType:str = obj["KeepWhenRValueType"]
      """  KeepWhenRValueType  """  
      self.KeepWhenType:str = obj["KeepWhenType"]
      """  KeepWhenType  """  
      self.ExtCompanyList:str = obj["ExtCompanyList"]
      """  ExtCompanyList  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  Indicates if is allowed Enterprise Configuration  """  
      self.KeepWhenField:str = obj["KeepWhenField"]
      self.KeepWhenTable:str = obj["KeepWhenTable"]
      self.MultiCompany:bool = obj["MultiCompany"]
      """  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.CompanyName:str = obj["CompanyName"]
      """  If is Enterprise configuration allowed it will update if is Local Company or MultiCompany  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  The sequence the rule is going to be applied.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Operation Sequence Number  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number  """  
      self.ParPartNum:str = obj["ParPartNum"]
      """  Stores the parent part number within the multi-level BOM for which the rule is related.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this rule.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  Method Rule Expression  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ProcessOrder:int = obj["ProcessOrder"]
      """  ProcessOrder  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.ExprXMLItem:str = obj["ExprXMLItem"]
      """  ExprXMLItem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispActionString:str = obj["DispActionString"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.RuleTag:str = obj["RuleTag"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.dbField:str = obj["dbField"]
      self.dbTable:str = obj["dbTable"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  The sequence the rule is going to be applied.  """  
      self.RuleString:str = obj["RuleString"]
      """  Method Rule String  """  
      self.RuleType:str = obj["RuleType"]
      """  Method Rule Type  """  
      self.RuleExpr:str = obj["RuleExpr"]
      """  Method Rule Expression  """  
      self.CalcName:str = obj["CalcName"]
      """  Name for the calculated field  """  
      self.CalcDataType:str = obj["CalcDataType"]
      """  Calculated field data type  """  
      self.dbField:str = obj["dbField"]
      """  Database Field  """  
      self.dbTable:str = obj["dbTable"]
      """  Database Table  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Operation Sequence Number  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number  """  
      self.ParPartNum:str = obj["ParPartNum"]
      """  Stores the parent part number within the multi-level BOM for which the rule is related.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.ElementType:str = obj["ElementType"]
      """  Defines what the rule is related to.  Valid values include Par, Opr, Mtl, Asm.  This is used in Gencode.p when creating the compiled code.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this rule.  """  
      self.RuleID:int = obj["RuleID"]
      """  A unique identifier for the rule.  This will be generated in the database trigger.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Process Sequence  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CurrentNode:str = obj["CurrentNode"]
      """  The node that is currently selected in the tree.  """  
      self.CurrentRuleLineage:str = obj["CurrentRuleLineage"]
      self.ParentNode:str = obj["ParentNode"]
      """  The parent node of the current node that is selected in the tree  """  
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.DispLinkString:str = obj["DispLinkString"]
      """  Temporal column to show link phrase  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BeforeStartTestRules_input:
   """ Required : 
   configID
   partNum
   revisionNum
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      pass

class BeforeStartTestRules_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ChangingEntConf_input:
   """ Required : 
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Current Configuration ID  """  
      pass

class ChangingEntConf_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.settingsExist:bool = obj["settingsExist"]
      pass

      """  output parameters  """  

class CheckIsConfigured_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The proposed part number  """  
      pass

class CheckIsConfigured_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isConfigured:bool = obj["isConfigured"]
      pass

      """  output parameters  """  

class CopyMethodRules_input:
   """ Required : 
   ds
   CopyAction
   UpdateComments
   SourceConfigID
   SourcePartNum
   SourceRevisionNum
   SourceAltMethod
   TargetPartNum
   TargetRevisionNum
   TargetAltMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.CopyAction:str = obj["CopyAction"]
      """  Append or Replace  """  
      self.UpdateComments:bool = obj["UpdateComments"]
      """  Update comments  """  
      self.SourceConfigID:str = obj["SourceConfigID"]
      """  Source ConfigID  """  
      self.SourcePartNum:str = obj["SourcePartNum"]
      """  Source Part Num  """  
      self.SourceRevisionNum:str = obj["SourceRevisionNum"]
      """  Source Revision Num  """  
      self.SourceAltMethod:str = obj["SourceAltMethod"]
      """  Source Alternate Method  """  
      self.TargetPartNum:str = obj["TargetPartNum"]
      """  Source Part Num  """  
      self.TargetRevisionNum:str = obj["TargetRevisionNum"]
      """  Source Revision Num  """  
      self.TargetAltMethod:str = obj["TargetAltMethod"]
      """  Source Alternate Method  """  
      pass

class CopyMethodRules_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CopyRulesResultsTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EditorFilter_input:
   """ Required : 
   type
   configID
   partNum
   revisionNum
   altMethod
   ruleSetID
   """  
   def __init__(self, obj):
      self.type:str = obj["type"]
      """  Indicates if will be for session filter or for ColumnFilter  """  
      self.configID:str = obj["configID"]
      """  ConfigID  """  
      self.partNum:str = obj["partNum"]
      """  Part Num  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision Num  """  
      self.altMethod:str = obj["altMethod"]
      """  AltMethod  """  
      self.ruleSetID:int = obj["ruleSetID"]
      """  RuleSetID  """  
      pass

class EditorFilter_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class Erp_Tablesets_CodeEditorPCDatasetTableset:
   def __init__(self, obj):
      self.CodeEditorPCTargets:list[Erp_Tablesets_CodeEditorPCTargetsRow] = obj["CodeEditorPCTargets"]
      self.CodeEditorPCDocVars:list[Erp_Tablesets_CodeEditorPCDocVarsRow] = obj["CodeEditorPCDocVars"]
      self.CodeEditorPCInputs:list[Erp_Tablesets_CodeEditorPCInputsRow] = obj["CodeEditorPCInputs"]
      self.CodeEditorPCMethodVars:list[Erp_Tablesets_CodeEditorPCMethodVarsRow] = obj["CodeEditorPCMethodVars"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CodeEditorPCDocVarsRow:
   def __init__(self, obj):
      self.VarName:str = obj["VarName"]
      self.DataType:str = obj["DataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCInputsRow:
   def __init__(self, obj):
      self.InputName:str = obj["InputName"]
      self.InputType:str = obj["InputType"]
      self.DataType:str = obj["DataType"]
      self.PcDynLstCount:int = obj["PcDynLstCount"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCMethodVarsRow:
   def __init__(self, obj):
      self.VarName:str = obj["VarName"]
      self.DataType:str = obj["DataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CodeEditorPCTargetsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TableName:str = obj["TableName"]
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnFormat:str = obj["ColumnFormat"]
      """  Reserved for future development  """  
      self.ColumnSyntax:str = obj["ColumnSyntax"]
      self.UDColumn:bool = obj["UDColumn"]
      """  Indicates if the column is from the UD table  """  
      self.DataType:str = obj["DataType"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ConfiguratorRuleListTableset:
   def __init__(self, obj):
      self.PartRevList:list[Erp_Tablesets_PartRevListRow] = obj["PartRevList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ConfiguratorRuleTableset:
   def __init__(self, obj):
      self.PartRev:list[Erp_Tablesets_PartRevRow] = obj["PartRev"]
      self.PcMethodVar:list[Erp_Tablesets_PcMethodVarRow] = obj["PcMethodVar"]
      self.PcRuleSet:list[Erp_Tablesets_PcRuleSetRow] = obj["PcRuleSet"]
      self.PcRules:list[Erp_Tablesets_PcRulesRow] = obj["PcRules"]
      self.PcRulesExpr:list[Erp_Tablesets_PcRulesExprRow] = obj["PcRulesExpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CopyPcRuleSetRow:
   def __init__(self, obj):
      self.Description:str = obj["Description"]
      self.Copied:bool = obj["Copied"]
      self.BOMElementType:str = obj["BOMElementType"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.TotalRules:int = obj["TotalRules"]
      self.TotalActions:int = obj["TotalActions"]
      self.ID:str = obj["ID"]
      self.Assembly:str = obj["Assembly"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CopyRulesResultsTableset:
   def __init__(self, obj):
      self.CopyPcRuleSet:list[Erp_Tablesets_CopyPcRuleSetRow] = obj["CopyPcRuleSet"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCRulesBOMTableset:
   def __init__(self, obj):
      self.PCRulesMtl:list[Erp_Tablesets_PCRulesMtlRow] = obj["PCRulesMtl"]
      self.PcRulesOpDtl:list[Erp_Tablesets_PcRulesOpDtlRow] = obj["PcRulesOpDtl"]
      self.PcRulesOpr:list[Erp_Tablesets_PcRulesOprRow] = obj["PcRulesOpr"]
      self.PCRulesRev:list[Erp_Tablesets_PCRulesRevRow] = obj["PCRulesRev"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCRulesMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.RelatedOperation:int = obj["RelatedOperation"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.RuleTag:str = obj["RuleTag"]
      self.GeneratedRuleTag:str = obj["GeneratedRuleTag"]
      self.OpDesc:str = obj["OpDesc"]
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      self.PullAsAsm:bool = obj["PullAsAsm"]
      self.ViewAsAsm:bool = obj["ViewAsAsm"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.KitComponent:bool = obj["KitComponent"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCRulesRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.EffectiveDate:str = obj["EffectiveDate"]
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      self.RuleTag:str = obj["RuleTag"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.CurrentRevision:bool = obj["CurrentRevision"]
      self.DispAltMethod:str = obj["DispAltMethod"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.ProdCode:str = obj["ProdCode"]
      self.NonStock:bool = obj["NonStock"]
      self.Class:str = obj["Class"]
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      """  The description of the inspection plan  """  
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      """  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  """  
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      """   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  """  
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      """  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  """  
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      """  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  """  
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      """  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  """  
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      """  Describes the Part.  """  
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      """   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  """  
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      """  Indicates if this part is serial number tracked  """  
      self.PlantName:str = obj["PlantName"]
      """  The Plant name. Used on shipping reports.  """  
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      """  Full description of the rough cut parameter set.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      """  SIValuesGroupSeq  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      """  SIValuesHeadNum  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.DefaultConfigPart:bool = obj["DefaultConfigPart"]
      """  DefaultConfigPart  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  Number of COPart required in the Revision  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  Material Cost Factor  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  Labor Cost Factor  """  
      self.CoPartsPerOp:int = obj["CoPartsPerOp"]
      """  Number of COParts per Operation  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      """  Customs BOM  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: General, Site, Master.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ProcessMfgLastGroupID:str = obj["ProcessMfgLastGroupID"]
      """  The last Group to modify this Revision for Recipe Authoring.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      """  This field will be set to true if two or more ECOCoParts records exist for the revision.  """  
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part Number of the Parent Part  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  Revision number  of Parent Part.  """  
      self.ProdCode:str = obj["ProdCode"]
      self.RevStatusAsOfDate:int = obj["RevStatusAsOfDate"]
      """   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.Class:str = obj["Class"]
      self.NonStock:bool = obj["NonStock"]
      self.IsRootNode:bool = obj["IsRootNode"]
      """  Indicates that the PartRev is the root node in the tree  """  
      self.EngineeringApproved:bool = obj["EngineeringApproved"]
      """  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      self.PartDescriptionTypeCode:str = obj["PartDescriptionTypeCode"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PlantName:str = obj["PlantName"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcMethodVarRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.VarNum:int = obj["VarNum"]
      """  VarNum  """  
      self.VarName:str = obj["VarName"]
      """  VarName  """  
      self.DataType:str = obj["DataType"]
      """  DataType  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.VarSeq:int = obj["VarSeq"]
      """  VarSeq  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DispLinkString:str = obj["DispLinkString"]
      """  Temporal column to show link phrase  """  
      self.Format:str = obj["Format"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRuleSetRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      """  BOMElementSysRowID  """  
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      """  BOMElementTableName  """  
      self.BOMElementType:str = obj["BOMElementType"]
      """  BOMElementType  """  
      self.RuleTag:str = obj["RuleTag"]
      """  RuleTag  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  MtlSeq  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  OpDtlSeq  """  
      self.UseKeepWhen:bool = obj["UseKeepWhen"]
      """  UseKeepWhen  """  
      self.KeepWhenExpr:str = obj["KeepWhenExpr"]
      """  KeepWhenExpr  """  
      self.KeepWhenLValue:str = obj["KeepWhenLValue"]
      """  KeepWhenLValue  """  
      self.KeepWhenCompareOpr:str = obj["KeepWhenCompareOpr"]
      """  KeepWhenCompareOpr  """  
      self.KeepWhenRValue:str = obj["KeepWhenRValue"]
      """  KeepWhenRValue  """  
      self.KeepWhenRValueType:str = obj["KeepWhenRValueType"]
      """  KeepWhenRValueType  """  
      self.KeepWhenType:str = obj["KeepWhenType"]
      """  KeepWhenType  """  
      self.ExtCompanyList:str = obj["ExtCompanyList"]
      """  ExtCompanyList  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.Expression:str = obj["Expression"]
      """  Expression  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.EntprsConf:bool = obj["EntprsConf"]
      """  Indicates if is allowed Enterprise Configuration  """  
      self.KeepWhenField:str = obj["KeepWhenField"]
      self.KeepWhenTable:str = obj["KeepWhenTable"]
      self.MultiCompany:bool = obj["MultiCompany"]
      """  When Enterprise Configuration is enable (allow multi company setup), will have the option to set for local company only or to set multi - company to allow select the external companies  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.CompanyName:str = obj["CompanyName"]
      """  If is Enterprise configuration allowed it will update if is Local Company or MultiCompany  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesExprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  The sequence the rule is going to be applied.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Operation Sequence Number  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number  """  
      self.ParPartNum:str = obj["ParPartNum"]
      """  Stores the parent part number within the multi-level BOM for which the rule is related.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this rule.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Sequence Number.  """  
      self.Expression:str = obj["Expression"]
      """  Method Rule Expression  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Ex: Customization, Personalization  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.ProcessOrder:int = obj["ProcessOrder"]
      """  ProcessOrder  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.ExprType:str = obj["ExprType"]
      """  ExprType  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.ExprXMLItem:str = obj["ExprXMLItem"]
      """  ExprXMLItem  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispActionString:str = obj["DispActionString"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.RuleTag:str = obj["RuleTag"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.dbField:str = obj["dbField"]
      self.dbTable:str = obj["dbTable"]
      self.CanUpdate:bool = obj["CanUpdate"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      self.RuleTag:str = obj["RuleTag"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpCode:str = obj["OpCode"]
      self.SubContract:bool = obj["SubContract"]
      self.OpDesc:str = obj["OpDesc"]
      self.RuleTag:str = obj["RuleTag"]
      self.ParentRuleTag:str = obj["ParentRuleTag"]
      self.HasRuleSet:bool = obj["HasRuleSet"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PcRulesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number of the associated configurator  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number of the associated configurator  """  
      self.RuleSeq:int = obj["RuleSeq"]
      """  The sequence the rule is going to be applied.  """  
      self.RuleString:str = obj["RuleString"]
      """  Method Rule String  """  
      self.RuleType:str = obj["RuleType"]
      """  Method Rule Type  """  
      self.RuleExpr:str = obj["RuleExpr"]
      """  Method Rule Expression  """  
      self.CalcName:str = obj["CalcName"]
      """  Name for the calculated field  """  
      self.CalcDataType:str = obj["CalcDataType"]
      """  Calculated field data type  """  
      self.dbField:str = obj["dbField"]
      """  Database Field  """  
      self.dbTable:str = obj["dbTable"]
      """  Database Table  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Operation Sequence Number  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number  """  
      self.ParPartNum:str = obj["ParPartNum"]
      """  Stores the parent part number within the multi-level BOM for which the rule is related.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Stores the assembly part number within the multi-level BOM for which the rule is related.  """  
      self.ElementType:str = obj["ElementType"]
      """  Defines what the rule is related to.  Valid values include Par, Opr, Mtl, Asm.  This is used in Gencode.p when creating the compiled code.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this rule.  """  
      self.RuleID:int = obj["RuleID"]
      """  A unique identifier for the rule.  This will be generated in the database trigger.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an OpDtl  """  
      self.SourceDBRecid:str = obj["SourceDBRecid"]
      """  Recid of this record in the source database.  This is necessary because this table does not have a unique index that can be used to find the record in another database.  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag  """  
      self.ProcessSeq:int = obj["ProcessSeq"]
      """  Process Sequence  """  
      self.LValue:str = obj["LValue"]
      """  LValue  """  
      self.CompareOpr:str = obj["CompareOpr"]
      """  CompareOpr  """  
      self.RValue:str = obj["RValue"]
      """  RValue  """  
      self.RValueType:str = obj["RValueType"]
      """  RValueType  """  
      self.RuleSetID:int = obj["RuleSetID"]
      """  RuleSetID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CanUpdate:bool = obj["CanUpdate"]
      self.CurrentNode:str = obj["CurrentNode"]
      """  The node that is currently selected in the tree.  """  
      self.CurrentRuleLineage:str = obj["CurrentRuleLineage"]
      self.ParentNode:str = obj["ParentNode"]
      """  The parent node of the current node that is selected in the tree  """  
      self.BOMElementTableName:str = obj["BOMElementTableName"]
      self.BOMElementSysRowID:str = obj["BOMElementSysRowID"]
      self.Format:str = obj["Format"]
      """  Assing the default format for the constant editor  """  
      self.DispLinkString:str = obj["DispLinkString"]
      """  Temporal column to show link phrase  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtConfiguratorRuleTableset:
   def __init__(self, obj):
      self.PartRev:list[Erp_Tablesets_PartRevRow] = obj["PartRev"]
      self.PcMethodVar:list[Erp_Tablesets_PcMethodVarRow] = obj["PcMethodVar"]
      self.PcRuleSet:list[Erp_Tablesets_PcRuleSetRow] = obj["PcRuleSet"]
      self.PcRules:list[Erp_Tablesets_PcRulesRow] = obj["PcRules"]
      self.PcRulesExpr:list[Erp_Tablesets_PcRulesExprRow] = obj["PcRulesExpr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAllAlternateTrees_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipSingLevelConf
   lastNodeKey
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipSingLevelConf:bool = obj["ipSingLevelConf"]
      """  If BOM will retrieve only first level  """  
      self.lastNodeKey:str = obj["lastNodeKey"]
      """  Correspond to the path from the last element selected in TreeView  """  
      pass

class GetAllAlternateTrees_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PCRulesBOMTableset] = obj["returnObj"]
      pass

class GetAvailMethodVariables_input:
   """ Required : 
   configID
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  The configuration ID  """  
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class GetAvailMethodVariables_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.availMethodVars:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   processMfgID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.processMfgID:str = obj["processMfgID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  The table name  """  
      self.fieldName:str = obj["fieldName"]
      """  The field name.  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDatasetForTree_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipRuleTag
   ipSingLevelConf
   ipConfigId
   ipMainPartNum
   ipMainRevisionNum
   ipMainAltMethod
   ds
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return data for.  """  
      self.ipRuleTag:str = obj["ipRuleTag"]
      """  if is the main revision or alternate revision will not have any ruletag only for materials  """  
      self.ipSingLevelConf:bool = obj["ipSingLevelConf"]
      """  If BOM will retrieve only first level  """  
      self.ipConfigId:str = obj["ipConfigId"]
      """  Main ConfigID to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  """  
      self.ipMainPartNum:str = obj["ipMainPartNum"]
      """  Main PartNum to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  """  
      self.ipMainRevisionNum:str = obj["ipMainRevisionNum"]
      """  Main RevisionNum to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  """  
      self.ipMainAltMethod:str = obj["ipMainAltMethod"]
      """  Main AltMethod to find if the PartOpr or PartMtl or PartOpDtl has a PcRuleSet  """  
      self.ds:list[Erp_Tablesets_PCRulesBOMTableset] = obj["ds"]
      pass

class GetDatasetForTree_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCRulesBOMTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_ConfiguratorRuleListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartRev_input:
   """ Required : 
   ds
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class GetNewPartRev_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcMethodVar_input:
   """ Required : 
   ds
   configID
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      pass

class GetNewPcMethodVar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcRuleSet_input:
   """ Required : 
   ds
   configID
   partNum
   revisionNum
   altMethod
   boMElementTableName
   boMElementSysRowID
   ruleTag
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.boMElementTableName:str = obj["boMElementTableName"]
      self.boMElementSysRowID:str = obj["boMElementSysRowID"]
      self.ruleTag:str = obj["ruleTag"]
      pass

class GetNewPcRuleSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcRulesExpr_input:
   """ Required : 
   ds
   configID
   partNum
   revisionNum
   altMethod
   ruleSetID
   ruleSeq
   typeCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.ruleSetID:int = obj["ruleSetID"]
      self.ruleSeq:int = obj["ruleSeq"]
      self.typeCode:str = obj["typeCode"]
      pass

class GetNewPcRulesExpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPcRules_input:
   """ Required : 
   ds
   configID
   partNum
   revisionNum
   altMethod
   ruleSetID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.configID:str = obj["configID"]
      self.partNum:str = obj["partNum"]
      self.revisionNum:str = obj["revisionNum"]
      self.altMethod:str = obj["altMethod"]
      self.ruleSetID:int = obj["ruleSetID"]
      pass

class GetNewPcRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPrimaryPartNum_input:
   """ Required : 
   configID
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      pass

class GetPrimaryPartNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The Part Number is returned  """  
      pass

class GetRows_input:
   """ Required : 
   whereClausePartRev
   whereClausePcMethodVar
   whereClausePcRuleSet
   whereClausePcRules
   whereClausePcRulesExpr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartRev:str = obj["whereClausePartRev"]
      self.whereClausePcMethodVar:str = obj["whereClausePcMethodVar"]
      self.whereClausePcRuleSet:str = obj["whereClausePcRuleSet"]
      self.whereClausePcRules:str = obj["whereClausePcRules"]
      self.whereClausePcRulesExpr:str = obj["whereClausePcRulesExpr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetValidTargetEntitiesAndInputs_input:
   """ Required : 
   configID
   targetEntityFilter
   filteredColumnList
   partNum
   revisionNum
   altMethod
   """  
   def __init__(self, obj):
      self.configID:str = obj["configID"]
      self.targetEntityFilter:str = obj["targetEntityFilter"]
      self.filteredColumnList:bool = obj["filteredColumnList"]
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision Numerb  """  
      self.altMethod:str = obj["altMethod"]
      """  Alternate method  """  
      pass

class GetValidTargetEntitiesAndInputs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CodeEditorPCDatasetTableset] = obj["returnObj"]
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

class MethodVarMoveDown_input:
   """ Required : 
   PcMethodVarRowid
   ds
   """  
   def __init__(self, obj):
      self.PcMethodVarRowid:str = obj["PcMethodVarRowid"]
      """  The RowIdent of the rule to be moved down  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class MethodVarMoveDown_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class MethodVarMoveUp_input:
   """ Required : 
   PcMethodVarRowid
   ds
   """  
   def __init__(self, obj):
      self.PcMethodVarRowid:str = obj["PcMethodVarRowid"]
      """  The RowIdent of the rule to be moved up  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class MethodVarMoveUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   PartNum
   configID
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  Part Num field  """  
      self.configID:str = obj["configID"]
      """  Configuration ID  """  
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  if exists PartNum  """  
      pass

   def parameters(self, obj):
      self.outPartNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePcRulesExprLValue_input:
   """ Required : 
   newValue
   ds
   """  
   def __init__(self, obj):
      self.newValue:str = obj["newValue"]
      """  New value for LValue column  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangePcRulesExprLValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePcRulesLValue_input:
   """ Required : 
   newValue
   ds
   """  
   def __init__(self, obj):
      self.newValue:str = obj["newValue"]
      """  New value for LValue column  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangePcRulesLValue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedConfigID_input:
   """ Required : 
   partNum
   revisionNum
   altMethod
   configID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Num  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision Num  """  
      self.altMethod:str = obj["altMethod"]
      """  Alt Method  """  
      self.configID:str = obj["configID"]
      """  proposed ConfigID  """  
      pass

class OnChangedConfigID_output:
   def __init__(self, obj):
      pass

class OnChangedPcMethodVarDataType_input:
   """ Required : 
   newDataType
   ds
   """  
   def __init__(self, obj):
      self.newDataType:str = obj["newDataType"]
      """  New DataType  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangedPcMethodVarDataType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcMethodVarExprType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangedPcMethodVarExprType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcRulesExprExprType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangedPcRulesExprExprType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedPcRulesRuleType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangedPcRulesRuleType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangedRuleSetCompany_input:
   """ Required : 
   multiCompany
   ds
   """  
   def __init__(self, obj):
      self.multiCompany:bool = obj["multiCompany"]
      """  Indicate if is multi company  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangedRuleSetCompany_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingPcMethodVarDataType_input:
   """ Required : 
   newDataType
   ds
   """  
   def __init__(self, obj):
      self.newDataType:str = obj["newDataType"]
      """  New Data Type  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangingPcMethodVarDataType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingPcMethodVarVarName_input:
   """ Required : 
   newVarName
   ds
   """  
   def __init__(self, obj):
      self.newVarName:str = obj["newVarName"]
      """  New DataType  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class OnChangingPcMethodVarVarName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PromptForPassword_input:
   """ Required : 
   ipConfigID
   """  
   def __init__(self, obj):
      self.ipConfigID:str = obj["ipConfigID"]
      """  Configuration ID of the revisions being synched.  """  
      pass

class PromptForPassword_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPromptForPassword:bool = obj["opPromptForPassword"]
      self.opRevisionStatus:bool = obj["opRevisionStatus"]
      self.opRevisionFound:bool = obj["opRevisionFound"]
      pass

      """  output parameters  """  

class RulesMoveDown_input:
   """ Required : 
   PcRulesRowid
   ds
   """  
   def __init__(self, obj):
      self.PcRulesRowid:str = obj["PcRulesRowid"]
      """  The RowIdent of the rule to be moved down  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class RulesMoveDown_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RulesMoveUp_input:
   """ Required : 
   PcRulesRowid
   ds
   """  
   def __init__(self, obj):
      self.PcRulesRowid:str = obj["PcRulesRowid"]
      """  The RowIdent of the rule to be moved up  """  
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class RulesMoveUp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SalesKitConfiguration_input:
   """ Required : 
   PcPartNum
   """  
   def __init__(self, obj):
      self.PcPartNum:str = obj["PcPartNum"]
      """  The current part number  """  
      pass

class SalesKitConfiguration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.SalesKit:bool = obj["SalesKit"]
      pass

      """  output parameters  """  

class SyncRevision_input:
   """ Required : 
   ipApproved
   ipValidPassword
   ipConfigID
   ipAuditDesc
   """  
   def __init__(self, obj):
      self.ipApproved:bool = obj["ipApproved"]
      """  The proposed approval flag  """  
      self.ipValidPassword:bool = obj["ipValidPassword"]
      """  Did the user supply a valid password to run this functionality?
            The value for this parameter should come from running the ValidatePassword method
            in the UserFile BO.  """  
      self.ipConfigID:str = obj["ipConfigID"]
      """  The configurator ID of the revisions to synchronize  """  
      self.ipAuditDesc:str = obj["ipAuditDesc"]
      """  The audit description entered for the configuration approval  """  
      pass

class SyncRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.revSynched:bool = obj["revSynched"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorRuleTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtConfiguratorRuleTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePcRulesDelete_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      pass

class ValidatePcRulesDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ConfiguratorRuleTableset] = obj["ds"]
      self.outMsgDeletion:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateRevisionNum_input:
   """ Required : 
   CurrConfigID
   PartNum
   RevisionNum
   AltMethod
   """  
   def __init__(self, obj):
      self.CurrConfigID:str = obj["CurrConfigID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      pass

class ValidateRevisionNum_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.CurrConfigID:str = obj["parameters"]
      self.typeMessage:int = obj["parameters"]
      pass

      """  output parameters  """  

