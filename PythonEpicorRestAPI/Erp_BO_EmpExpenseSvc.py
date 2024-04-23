import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.EmpExpenseSvc
# Description: Employee Expense Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpExpenses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenses
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses",headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum(Company, EmpID, EmpExpenseNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpense item
   Description: Calls GetByID to retrieve the EmpExpense item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpExpenses_Company_EmpID_EmpExpenseNum(Company, EmpID, EmpExpenseNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpExpense for the service
   Description: Calls UpdateExt to update EmpExpense. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpExpenses_Company_EmpID_EmpExpenseNum(Company, EmpID, EmpExpenseNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpExpense item
   Description: Call UpdateExt to delete EmpExpense item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpense
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseComments(Company, EmpID, EmpExpenseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpExpenseComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpExpenseComments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseComments",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpenseComment item
   Description: Calls GetByID to retrieve the EmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseComment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseTaxes(Company, EmpID, EmpExpenseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpExpenseTaxes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpExpenseTaxes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseTaxes",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company, EmpID, EmpExpenseNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpenseTax item
   Description: Calls GetByID to retrieve the EmpExpenseTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseTax1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseAttches(Company, EmpID, EmpExpenseNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EmpExpenseAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EmpExpenseAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseAttches",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenses_Company_EmpID_EmpExpenseNum_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpenseAttch item
   Description: Calls GetByID to retrieve the EmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenses(" + Company + "," + EmpID + "," + EmpExpenseNum + ")/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenseComments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpExpenseComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenseComments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments",headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenseComments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenseComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpenseComment item
   Description: Calls GetByID to retrieve the EmpExpenseComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpExpenseComment for the service
   Description: Calls UpdateExt to update EmpExpenseComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpenseComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpExpenseComments_Company_EmpID_EmpExpenseNum_CommentNum(Company, EmpID, EmpExpenseNum, CommentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpExpenseComment item
   Description: Call UpdateExt to delete EmpExpenseComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpenseComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseComments(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenseTaxes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpExpenseTaxes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenseTaxes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes",headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenseTaxes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenseTaxes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company, EmpID, EmpExpenseNum, TaxCode, RateCode, ECAcquisitionSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpenseTax item
   Description: Calls GetByID to retrieve the EmpExpenseTax item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company, EmpID, EmpExpenseNum, TaxCode, RateCode, ECAcquisitionSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpExpenseTax for the service
   Description: Calls UpdateExt to update EmpExpenseTax. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpenseTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseTaxRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpExpenseTaxes_Company_EmpID_EmpExpenseNum_TaxCode_RateCode_ECAcquisitionSeq(Company, EmpID, EmpExpenseNum, TaxCode, RateCode, ECAcquisitionSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpExpenseTax item
   Description: Call UpdateExt to delete EmpExpenseTax item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpenseTax
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param ECAcquisitionSeq: Desc: ECAcquisitionSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseTaxes(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + TaxCode + "," + RateCode + "," + ECAcquisitionSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenseAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EmpExpenseAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EmpExpenseAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches",headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenseAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EmpExpenseAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EmpExpenseAttch item
   Description: Calls GetByID to retrieve the EmpExpenseAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EmpExpenseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EmpExpenseAttch for the service
   Description: Calls UpdateExt to update EmpExpenseAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EmpExpenseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EmpExpenseAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EmpExpenseAttches_Company_EmpID_EmpExpenseNum_DrawingSeq(Company, EmpID, EmpExpenseNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EmpExpenseAttch item
   Description: Call UpdateExt to delete EmpExpenseAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EmpExpenseAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param EmpExpenseNum: Desc: EmpExpenseNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/EmpExpenseAttches(" + Company + "," + EmpID + "," + EmpExpenseNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EmpExpenseListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseEmpExpense, whereClauseEmpExpenseAttch, whereClauseEmpExpenseComment, whereClauseEmpExpenseTax, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseEmpExpense=" + whereClauseEmpExpense
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpExpenseAttch=" + whereClauseEmpExpenseAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpExpenseComment=" + whereClauseEmpExpenseComment
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEmpExpenseTax=" + whereClauseEmpExpenseTax
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empID, empExpenseNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "empID=" + empID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "empExpenseNum=" + empExpenseNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ApproveReject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects EmpExpense records for reject or approve
   OperationID: ApproveReject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseClaimCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseClaimCurrencyCode
   Description: Method to call when changing the Claim Currency Code.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseClaimCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseClaimExchangeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseClaimExchangeRate
   Description: Method to call when changing the claim exchange rate.
   OperationID: ChangeEmpExpenseClaimExchangeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimExchangeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimExchangeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseClaimLockRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseClaimLockRate
   Description: Method to call when changing the Claim Lock Rate.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseClaimLockRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimLockRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimLockRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseClaimRateGrpCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseClaimRateGrpCode
   Description: Method to call when changing the Claim Rate Group Code.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseClaimRateGrpCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseClaimRateGrpCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseClaimRateGrpCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseDispClaimAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseDispClaimAmt
   Description: Method to call when changing the Claim Amount.  The field DispClaimAmt
is the field that should trigger the call to this procedure.
   OperationID: ChangeEmpExpenseDispClaimAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseDispClaimAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseDispClaimAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseDocExpenseAmt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseDocExpenseAmt
   Description: Method to call when changing the Doc Expense Amount.
   OperationID: ChangeEmpExpenseDocExpenseAmt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseDocExpenseAmt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseDocExpenseAmt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseExpCurrencyCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseExpCurrencyCode
   Description: Method to call when changing the Expense Currency Code.  Exchange rate
is reevaluted
   OperationID: ChangeEmpExpenseExpCurrencyCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseExpCurrencyCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseExpCurrencyCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseExpenseDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseExpenseDate
   Description: Method to call when changing the Expense Date.  This can affect the exchange rate.
   OperationID: ChangeEmpExpenseExpenseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseExpenseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseExpenseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseIndirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseIndirect
   Description: Method to call when changing Indirect.
   OperationID: ChangeEmpExpenseIndirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseIndirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseIndirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseMiscCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseMiscCode
   Description: Method to call when changing the Miscellaneous Code.
   OperationID: ChangeEmpExpenseMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpensePayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpensePayMethod
   Description: Method to call when changing the Payment Method.
   OperationID: ChangeEmpExpensePayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpensePayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpensePayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpensePhaseID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpensePhaseID
   Description: Method to call when changing the WBS Phase ID.
   OperationID: ChangeEmpExpensePhaseID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpensePhaseID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpensePhaseID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseProjectID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseProjectID
   Description: Method to call when changing the Project ID.
   OperationID: ChangeEmpExpenseProjectID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseProjectID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseProjectID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseQuickEntryCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseQuickEntryCode
   Description: Method to call when changing the quick entry code.  Quick entry values
are used for default values on the expense.
   OperationID: ChangeEmpExpenseQuickEntryCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseQuickEntryCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseQuickEntryCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseUnitRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseUnitRate
   Description: Method to call when changing the Unit Rate.
   OperationID: ChangeEmpExpenseUnitRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseUnitRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseUnitRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmpExpenseUnits(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmpExpenseUnits
   Description: Method to call when changing the Units.
   OperationID: ChangeEmpExpenseUnits
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmpExpenseUnits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmpExpenseUnits_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRecallFromApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRecallFromApproval
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyEmpExpense
   Description: Method to copy the vales from one EmpExpense record to a new EmpExpense record.
   OperationID: CopyEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetListExpenses(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListExpenses
   Description: This method returns a list of Expenses to be viewed in the Time and Expense Entry
screen based on Claim Reference, Invoice Num, Invoice Status and Expense Status.
This method builds the where clause instead of having the UI build the where clause
on their end.
   OperationID: GetListExpenses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListExpenses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListExpenses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MobileGetRowsTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MobileGetRowsTran
   Description: Called from Mobile time and expense application to retrieve expense transactions and to also check
whether we are retrieving comments / attachments as part of the dataset.
   OperationID: MobileGetRowsTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MobileGetRowsTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MobileGetRowsTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsTran
   Description: Called from Approvals screen to get related task expense transactions
   OperationID: GetRowsTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallEmpExpense
   Description: Method to call when recalling submitted expense records
   OperationID: RecallEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallFromApproval(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallFromApproval
   Description: Method to call when recalling from approval entry
   OperationID: RecallFromApproval
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApproval_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApproval_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SubmitSelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitSelected
   Description: Method to call to submit selected expenses
   OperationID: SubmitSelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRateCodeInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRateCodeInfo
   Description: This method updates the dataset when the RateCode field changes
   OperationID: GetRateCodeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRateCodeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRateCodeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenseAfterGetRowsWrapper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EmpExpenseAfterGetRowsWrapper
   Description: Calls EmpExpenseAfterGetRows for the passed in EmpExpense row
   OperationID: EmpExpenseAfterGetRowsWrapper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EmpExpenseAfterGetRowsWrapper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmpExpenseAfterGetRowsWrapper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenseCommentAfterGetRowsWrapper(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EmpExpenseCommentAfterGetRowsWrapper
   Description: Calls EmpExpenseCommentAfterGetRows for the passed in EmpExpenseComment row
   OperationID: EmpExpenseCommentAfterGetRowsWrapper
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EmpExpenseCommentAfterGetRowsWrapper_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmpExpenseCommentAfterGetRowsWrapper_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpExpenseForDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpExpenseForDate
   Description: Create a new EmpExpense record for a specific date
   OperationID: GetNewEmpExpenseForDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseForDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseForDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EmpExpenseRetrieveOptionsClause(epicorHeaders = None):
   """  
   Summary: Invoke method EmpExpenseRetrieveOptionsClause
   Description: Returns a string that contains EmpExpense retrieve options based on user settings.  This string
is intended to be appended to an existing where clause for GetRows/GetList calls.
   OperationID: EmpExpenseRetrieveOptionsClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EmpExpenseRetrieveOptionsClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_SubmitForApprovalBySelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitForApprovalBySelected
   Description: Method to submit Expense records for Approval using RowSelected flag.
   OperationID: SubmitForApprovalBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitForApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitForApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallFromApprovalBySelected(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallFromApprovalBySelected
   Description: Method to recall EmpExpense for Approval using RowSelected flag.
   OperationID: RecallFromApprovalBySelected
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallFromApprovalBySelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallFromApprovalBySelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CopyEmpExpenseByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyEmpExpenseByID
   Description: Method to copy EmpExpense by Expense ID
   OperationID: CopyEmpExpenseByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyEmpExpenseByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyEmpExpenseByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteExpense
   Description: Method to delete multiple expenses by ExpNum
   OperationID: DeleteExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpExpense(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpExpense
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpense
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpense_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpense_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpExpenseAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpExpenseAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpenseAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpExpenseComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpExpenseComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpenseComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpExpenseTax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpExpenseTax
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEmpExpenseTax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpExpenseTax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpExpenseTax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.EmpExpenseSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpExpenseAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseCommentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpExpenseCommentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpExpenseListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpExpenseRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EmpExpenseTaxRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EmpExpenseTaxRow] = obj["value"]
      pass

class Erp_Tablesets_EmpExpenseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
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

class Erp_Tablesets_EmpExpenseCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense comment record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.SubmitCommentInstr:str = obj["SubmitCommentInstr"]
      """  Submit comment instructions  """  
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ExpEntryCommentTypeList:str = obj["ExpEntryCommentTypeList"]
      """  List of valid comment types for Expense Entry  """  
      self.CommentTypeDesc:str = obj["CommentTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpExpenseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.UBFromEffectiveDate:str = obj["UBFromEffectiveDate"]
      """  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseTaxAmt:int = obj["DocExpenseTaxAmt"]
      """  The tax of the expense in the expense currency.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ChargeCurrencyCode:str = obj["ChargeCurrencyCode"]
      """  The charge currency.  This is derived from the currency on the related project.  """  
      self.ChargeExchangeRate:int = obj["ChargeExchangeRate"]
      """  The charge exchange rate.  This is derived from the exchange rate on the related project.  """  
      self.ChargeRateGrpCode:str = obj["ChargeRateGrpCode"]
      """  The charge rate group code.  This is derived from the rate group code on the related projec.t  """  
      self.DocChargeAmt:int = obj["DocChargeAmt"]
      """  The charge amount of the expense in the charge currency.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier number used on the employee of the expense.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The ap invoice number the expense was invoiced on.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line created for this expense.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.IsReversal:bool = obj["IsReversal"]
      """  Indicates if this expense is a reversal (full or partial) of an existing expense.  """  
      self.ReversedExpenseNum:int = obj["ReversedExpenseNum"]
      """  Reversed Expense Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ClaimExchangeRate:int = obj["ClaimExchangeRate"]
      """  The exchange rate between the claim currency and the base currency based on expense date.  """  
      self.ClaimLockRate:bool = obj["ClaimLockRate"]
      """  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ClaimRateGrpCode:str = obj["ClaimRateGrpCode"]
      """  The claim rate group code.  """  
      self.DocClaimTaxAmt:int = obj["DocClaimTaxAmt"]
      """  The tax of the claim in the claim currency.  """  
      self.DocClaimAmt:int = obj["DocClaimAmt"]
      """  The amount of the claim in the claim currency.  """  
      self.DocTotalClaimAmt:int = obj["DocTotalClaimAmt"]
      """  The total amount of the claim in the claim currency.  This value includes taxes.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.DocExpWithholdAmt:int = obj["DocExpWithholdAmt"]
      """  Expense Withholding Tax Amount.  """  
      self.DocClaimWithholdAmt:int = obj["DocClaimWithholdAmt"]
      """  Claim Withholding Tax Amount.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.DocChargeTaxAmt:int = obj["DocChargeTaxAmt"]
      """  The tax of the claim in the charge currency.  """  
      self.DocTotalChargeAmt:int = obj["DocTotalChargeAmt"]
      """  The total charge amount in the charge currency.  This value includes taxes.  """  
      self.ClaimToBaseExchangeRate:int = obj["ClaimToBaseExchangeRate"]
      """  The exchange rate between the claim currency and the base currency.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the misc charge jobmtl record  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number of the misc charge jobmtl record  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence of the misc charge jobmtl record  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates if the expense has been invoiced.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpCommentInstr:str = obj["ExpCommentInstr"]
      """  Expense Comment Instruction  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Indicates that this record has been process by the project analysis build process  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.VoucherReceiptNo:str = obj["VoucherReceiptNo"]
      """  The voucher or receipt number reference.  """  
      self.VoucherReceiptDate:str = obj["VoucherReceiptDate"]
      """  The date for the voucher/receipt reference  """  
      self.DocAdvanceBalance:int = obj["DocAdvanceBalance"]
      """  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  """  
      self.DocMatchedClaimAmt:int = obj["DocMatchedClaimAmt"]
      """  The amount that has been matched from advance requests to this expense.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this expense is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this expense is linked to  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order that this expense is linked to  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UnitsLabel:str = obj["UnitsLabel"]
      """  The label value for Units field.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  A list of people who have approved the expense  """  
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      """  A list of people who need to approve the expense  """  
      self.DisplayStatus:str = obj["DisplayStatus"]
      """  External field to display a descriptive status of the record  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.IsSelected:bool = obj["IsSelected"]
      """  Indicates if this record is selected to be submitted  """  
      self.DispClaimAmt:int = obj["DispClaimAmt"]
      """  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.InvoiceStatus:str = obj["InvoiceStatus"]
      """  If invoiced, the status of the invoice.  """  
      self.ExpWeek:str = obj["ExpWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  """  
      self.ExpDay:str = obj["ExpDay"]
      """  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  """  
      self.ExpMonth:str = obj["ExpMonth"]
      """  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      """  Indicates if the record has been submitted or not  """  
      self.DispTotalClaimAmt:int = obj["DispTotalClaimAmt"]
      """  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.MultiCurrency:bool = obj["MultiCurrency"]
      """  Indicates if multi-currency is licensed  """  
      self.ExpenseDisableDelete:bool = obj["ExpenseDisableDelete"]
      self.ExpenseDisableUpdate:bool = obj["ExpenseDisableUpdate"]
      self.EnableClaimLockRate:bool = obj["EnableClaimLockRate"]
      self.APInvLineAmt:int = obj["APInvLineAmt"]
      self.APInvLineTaxAmt:int = obj["APInvLineTaxAmt"]
      self.APInvLineTotAmt:int = obj["APInvLineTotAmt"]
      self.EnableUnitRate:bool = obj["EnableUnitRate"]
      """  Indicates if UnitRate is enabled  """  
      self.EnableClaimCurrencyCode:bool = obj["EnableClaimCurrencyCode"]
      self.ExpenseCurrencyList:str = obj["ExpenseCurrencyList"]
      self.DispClaimTaxAmt:int = obj["DispClaimTaxAmt"]
      """  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user retrieving the record has access to view the row or not.  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available in approval entry  """  
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open approval task.  """  
      self.ChargeCurrencyBaseCurr:bool = obj["ChargeCurrencyBaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ChargeCurrencyCurrencyID:str = obj["ChargeCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.ChargeCurrencyDocumentDesc:str = obj["ChargeCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ChargeCurrencyCurrName:str = obj["ChargeCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.ChargeCurrencyCurrDesc:str = obj["ChargeCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.ChargeCurrencyCurrSymbol:str = obj["ChargeCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.ChargeRateTypeDescription:str = obj["ChargeRateTypeDescription"]
      """  Description  """  
      self.ClaimCurrencyDocumentDesc:str = obj["ClaimCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ClaimCurrencyCurrName:str = obj["ClaimCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.ClaimCurrencyCurrDesc:str = obj["ClaimCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.ClaimCurrencyCurrSymbol:str = obj["ClaimCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.ClaimCurrencyCurrencyID:str = obj["ClaimCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.ClaimCurrencyBaseCurr:bool = obj["ClaimCurrencyBaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      """  Description  """  
      self.EmpBasicName:str = obj["EmpBasicName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      """  Last name of employee  """  
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      """  First name of employee.  """  
      self.ExpCurrencyCurrSymbol:str = obj["ExpCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.ExpCurrencyCurrencyID:str = obj["ExpCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.ExpCurrencyDocumentDesc:str = obj["ExpCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ExpCurrencyCurrName:str = obj["ExpCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.ExpCurrencyCurrDesc:str = obj["ExpCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.ExpCurrencyBaseCurr:bool = obj["ExpCurrencyBaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.PayMethodReimbursable:bool = obj["PayMethodReimbursable"]
      """  Reimbursable  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.ProjectDescription:str = obj["ProjectDescription"]
      """  Full description of Project Management Code.  """  
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      """  Description  """  
      self.PurMiscExpChargeable:bool = obj["PurMiscExpChargeable"]
      """  When an expense charge, indicates if the code is chargeable.  """  
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.PurMiscExpUnitBased:bool = obj["PurMiscExpUnitBased"]
      """  When an expense charge, indicates if the code is unit based.  """  
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      """  Description of the task set.  """  
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      """  Full description for the Tax Region.  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.UBFromEffectiveDate:str = obj["UBFromEffectiveDate"]
      """  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseTaxAmt:int = obj["DocExpenseTaxAmt"]
      """  The tax of the expense in the expense currency.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ChargeCurrencyCode:str = obj["ChargeCurrencyCode"]
      """  The charge currency.  This is derived from the currency on the related project.  """  
      self.ChargeExchangeRate:int = obj["ChargeExchangeRate"]
      """  The charge exchange rate.  This is derived from the exchange rate on the related project.  """  
      self.ChargeRateGrpCode:str = obj["ChargeRateGrpCode"]
      """  The charge rate group code.  This is derived from the rate group code on the related projec.t  """  
      self.DocChargeAmt:int = obj["DocChargeAmt"]
      """  The charge amount of the expense in the charge currency.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier number used on the employee of the expense.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The ap invoice number the expense was invoiced on.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line created for this expense.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.IsReversal:bool = obj["IsReversal"]
      """  Indicates if this expense is a reversal (full or partial) of an existing expense.  """  
      self.ReversedExpenseNum:int = obj["ReversedExpenseNum"]
      """  Reversed Expense Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ClaimExchangeRate:int = obj["ClaimExchangeRate"]
      """  The exchange rate between the claim currency and the base currency based on expense date.  """  
      self.ClaimLockRate:bool = obj["ClaimLockRate"]
      """  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ClaimRateGrpCode:str = obj["ClaimRateGrpCode"]
      """  The claim rate group code.  """  
      self.DocClaimTaxAmt:int = obj["DocClaimTaxAmt"]
      """  The tax of the claim in the claim currency.  """  
      self.DocClaimAmt:int = obj["DocClaimAmt"]
      """  The amount of the claim in the claim currency.  """  
      self.DocTotalClaimAmt:int = obj["DocTotalClaimAmt"]
      """  The total amount of the claim in the claim currency.  This value includes taxes.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.DocExpWithholdAmt:int = obj["DocExpWithholdAmt"]
      """  Expense Withholding Tax Amount.  """  
      self.DocClaimWithholdAmt:int = obj["DocClaimWithholdAmt"]
      """  Claim Withholding Tax Amount.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.DocChargeTaxAmt:int = obj["DocChargeTaxAmt"]
      """  The tax of the claim in the charge currency.  """  
      self.DocTotalChargeAmt:int = obj["DocTotalChargeAmt"]
      """  The total charge amount in the charge currency.  This value includes taxes.  """  
      self.ClaimToBaseExchangeRate:int = obj["ClaimToBaseExchangeRate"]
      """  The exchange rate between the claim currency and the base currency.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the misc charge jobmtl record  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number of the misc charge jobmtl record  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence of the misc charge jobmtl record  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates if the expense has been invoiced.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpCommentInstr:str = obj["ExpCommentInstr"]
      """  Expense Comment Instruction  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Indicates that this record has been process by the project analysis build process  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.VoucherReceiptNo:str = obj["VoucherReceiptNo"]
      """  The voucher or receipt number reference.  """  
      self.VoucherReceiptDate:str = obj["VoucherReceiptDate"]
      """  The date for the voucher/receipt reference  """  
      self.DocAdvanceBalance:int = obj["DocAdvanceBalance"]
      """  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  """  
      self.DocMatchedClaimAmt:int = obj["DocMatchedClaimAmt"]
      """  The amount that has been matched from advance requests to this expense.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this expense is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this expense is linked to  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order that this expense is linked to  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartTranSysRowID:str = obj["PartTranSysRowID"]
      """  PartTranSysRowID  """  
      self.ExpenseAutoSubmit:bool = obj["ExpenseAutoSubmit"]
      """  ExpenseAutoSubmit  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.MobileExpense:bool = obj["MobileExpense"]
      """  MobileExpense  """  
      self.APInvLineAmt:int = obj["APInvLineAmt"]
      self.APInvLineTaxAmt:int = obj["APInvLineTaxAmt"]
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  A list of people who have approved the expense  """  
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open approval task.  """  
      self.DispClaimAmt:int = obj["DispClaimAmt"]
      """  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.DispClaimTaxAmt:int = obj["DispClaimTaxAmt"]
      """  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  """  
      self.DisplayStatus:str = obj["DisplayStatus"]
      """  External field to display a descriptive status of the record  """  
      self.DispTotalClaimAmt:int = obj["DispTotalClaimAmt"]
      """  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.EnableClaimCurrencyCode:bool = obj["EnableClaimCurrencyCode"]
      self.EnableClaimLockRate:bool = obj["EnableClaimLockRate"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available in approval entry  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EnableUnitRate:bool = obj["EnableUnitRate"]
      """  Indicates if UnitRate is enabled  """  
      self.ExpDay:str = obj["ExpDay"]
      """  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  """  
      self.ExpenseCurrencyList:str = obj["ExpenseCurrencyList"]
      self.ExpenseDisableDelete:bool = obj["ExpenseDisableDelete"]
      self.ExpenseDisableUpdate:bool = obj["ExpenseDisableUpdate"]
      self.ExpMonth:str = obj["ExpMonth"]
      """  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  """  
      self.ExpWeek:str = obj["ExpWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user retrieving the record has access to view the row or not.  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the expense detail has attachments  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the expense detail has comments  """  
      self.InvoiceStatus:str = obj["InvoiceStatus"]
      """  If invoiced, the status of the invoice.  """  
      self.IsSelected:bool = obj["IsSelected"]
      """  Indicates if this record is selected to be submitted  """  
      self.MultiCurrency:bool = obj["MultiCurrency"]
      """  Indicates if multi-currency is licensed  """  
      self.NewDifDateFlag:bool = obj["NewDifDateFlag"]
      self.NotSubmitted:bool = obj["NotSubmitted"]
      """  Indicates if the record has been submitted or not  """  
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      """  A list of people who need to approve the expense  """  
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnitsLabel:str = obj["UnitsLabel"]
      """  The label value for Units field.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.APInvLineTotAmt:int = obj["APInvLineTotAmt"]
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates of the row is selected for submit or recall  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.AppointmentIsAllDay:bool = obj["AppointmentIsAllDay"]
      """  Is calendar appointment all day  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChargeCurrencyCurrSymbol:str = obj["ChargeCurrencyCurrSymbol"]
      self.ChargeCurrencyCurrDesc:str = obj["ChargeCurrencyCurrDesc"]
      self.ChargeCurrencyCurrName:str = obj["ChargeCurrencyCurrName"]
      self.ChargeCurrencyCurrencyID:str = obj["ChargeCurrencyCurrencyID"]
      self.ChargeCurrencyDocumentDesc:str = obj["ChargeCurrencyDocumentDesc"]
      self.ChargeCurrencyBaseCurr:bool = obj["ChargeCurrencyBaseCurr"]
      self.ChargeRateGrpDescription:str = obj["ChargeRateGrpDescription"]
      self.ClaimCurrencyCurrName:str = obj["ClaimCurrencyCurrName"]
      self.ClaimCurrencyBaseCurr:bool = obj["ClaimCurrencyBaseCurr"]
      self.ClaimCurrencyDocumentDesc:str = obj["ClaimCurrencyDocumentDesc"]
      self.ClaimCurrencyCurrSymbol:str = obj["ClaimCurrencyCurrSymbol"]
      self.ClaimCurrencyCurrDesc:str = obj["ClaimCurrencyCurrDesc"]
      self.ClaimCurrencyCurrencyID:str = obj["ClaimCurrencyCurrencyID"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.ExpCurrencyDocumentDesc:str = obj["ExpCurrencyDocumentDesc"]
      self.ExpCurrencyCurrSymbol:str = obj["ExpCurrencyCurrSymbol"]
      self.ExpCurrencyBaseCurr:bool = obj["ExpCurrencyBaseCurr"]
      self.ExpCurrencyCurrName:str = obj["ExpCurrencyCurrName"]
      self.ExpCurrencyCurrDesc:str = obj["ExpCurrencyCurrDesc"]
      self.ExpCurrencyCurrencyID:str = obj["ExpCurrencyCurrencyID"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodReimbursable:bool = obj["PayMethodReimbursable"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      self.PurMiscExpUnitBased:bool = obj["PurMiscExpUnitBased"]
      self.PurMiscExpChargeable:bool = obj["PurMiscExpChargeable"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorName:str = obj["VendorName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpExpenseTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate code  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an expense.  When the sales tax field EcAquisition is checked then 2 expense tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.ExpReportableAmt:int = obj["ExpReportableAmt"]
      """  The reportable amount to the tax jurisdiction in the expense currency.  """  
      self.ClaimReportableAmt:int = obj["ClaimReportableAmt"]
      """  The reportable amount to the tax jurisdiction in the claim currency.  """  
      self.ExpTaxableAmt:int = obj["ExpTaxableAmt"]
      """  Taxable Amount for this expense in the expense currency  """  
      self.ClaimTaxableAmt:int = obj["ClaimTaxableAmt"]
      """  Taxable Amount for this expense in the claim currency.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this expense. This is defaulted from the SalesTax.Percent.  """  
      self.ExpTaxAmt:int = obj["ExpTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in the expense currency.  """  
      self.ClaimTaxAmt:int = obj["ClaimTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in the claim currency  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.ExpDefTaxableAmt:int = obj["ExpDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment.  In expense currency  """  
      self.ClaimDefTaxableAmt:int = obj["ClaimDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment.  In claim currency.  """  
      self.ExpDefTaxAmt:int = obj["ExpDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment.  In expense currency.  """  
      self.ClaimDefTaxAmt:int = obj["ClaimDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment.  In claim currency  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.ExpDedTaxAmt:int = obj["ExpDedTaxAmt"]
      """  Deducatable Tax Amount in expense currency  """  
      self.ClaimDedTaxAmt:int = obj["ClaimDedTaxAmt"]
      """  Deducatable Tax Amount in claim currency  """  
      self.ExpFixedAmount:int = obj["ExpFixedAmount"]
      """  Fixed Tax Amount in expense currency  """  
      self.ClaimFixedAmount:int = obj["ClaimFixedAmount"]
      """  Document Fixed Tax Amount in claim currency  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.ExpTaxAmtVar:int = obj["ExpTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate in expense currency  """  
      self.ClaimTaxAmtVar:int = obj["ClaimTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate in claim currency  """  
      self.SysCalcClaimTaxableAmt:int = obj["SysCalcClaimTaxableAmt"]
      """  System calculated Taxable amount for this expense in the claim currency  """  
      self.SysCalcExpTaxableAmt:int = obj["SysCalcExpTaxableAmt"]
      """  System calculated Taxable amount for this expense in the expense currency.  """  
      self.SysCalcExpReportableAmt:int = obj["SysCalcExpReportableAmt"]
      """  System calculated reportable amount to the tax jurisdiction in the expense currency  """  
      self.SysCalcClaimReportableAmt:int = obj["SysCalcClaimReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction expressed in the claim currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      self.ExpCurrencyDesc:str = obj["ExpCurrencyDesc"]
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      self.ClaimCurrencyDesc:str = obj["ClaimCurrencyDesc"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApproveReject_input:
   """ Required : 
   ipSalesRepCode
   ipAction
   ipComment
   ds
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ipAction:str = obj["ipAction"]
      """  Action to take A = approver, R = reject.  """  
      self.ipComment:str = obj["ipComment"]
      """  Comment text if comments are to be created.  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ApproveReject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseClaimCurrencyCode_input:
   """ Required : 
   ProposedClaimCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedClaimCurrencyCode:str = obj["ProposedClaimCurrencyCode"]
      """  The proposed claim currency code  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseClaimCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseClaimExchangeRate_input:
   """ Required : 
   ProposedClaimExchangeRate
   ds
   """  
   def __init__(self, obj):
      self.ProposedClaimExchangeRate:int = obj["ProposedClaimExchangeRate"]
      """  The proposed claim exchange rate  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseClaimExchangeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseClaimLockRate_input:
   """ Required : 
   ProposedClaimLockRate
   ds
   """  
   def __init__(self, obj):
      self.ProposedClaimLockRate:bool = obj["ProposedClaimLockRate"]
      """  The proposed claim lock rate  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseClaimLockRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseClaimRateGrpCode_input:
   """ Required : 
   ProposedClaimRateGrpCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedClaimRateGrpCode:str = obj["ProposedClaimRateGrpCode"]
      """  The proposed expense currency code  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseClaimRateGrpCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseDispClaimAmt_input:
   """ Required : 
   ProposedDispClaimAmt
   ds
   """  
   def __init__(self, obj):
      self.ProposedDispClaimAmt:int = obj["ProposedDispClaimAmt"]
      """  The proposed claim amount  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseDispClaimAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseDocExpenseAmt_input:
   """ Required : 
   ProposedDocExpenseAmt
   ds
   """  
   def __init__(self, obj):
      self.ProposedDocExpenseAmt:int = obj["ProposedDocExpenseAmt"]
      """  The proposed doc expense amount  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseDocExpenseAmt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseExpCurrencyCode_input:
   """ Required : 
   ProposedExpCurrencyCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedExpCurrencyCode:str = obj["ProposedExpCurrencyCode"]
      """  The proposed expense currency code  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseExpCurrencyCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseExpenseDate_input:
   """ Required : 
   ProposedExpenseDate
   ds
   """  
   def __init__(self, obj):
      self.ProposedExpenseDate:str = obj["ProposedExpenseDate"]
      """  The proposed expense date  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseExpenseDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseIndirect_input:
   """ Required : 
   ProposedIndirect
   ds
   """  
   def __init__(self, obj):
      self.ProposedIndirect:bool = obj["ProposedIndirect"]
      """  The proposed indirect value  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseIndirect_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseMiscCode_input:
   """ Required : 
   ProposedMiscCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedMiscCode:str = obj["ProposedMiscCode"]
      """  The proposed miscellaneous code  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseMiscCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpensePayMethod_input:
   """ Required : 
   ProposedPMUID
   ds
   """  
   def __init__(self, obj):
      self.ProposedPMUID:int = obj["ProposedPMUID"]
      """  The proposed pay method id  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpensePayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpensePhaseID_input:
   """ Required : 
   ProposedPhaseID
   ds
   """  
   def __init__(self, obj):
      self.ProposedPhaseID:str = obj["ProposedPhaseID"]
      """  The proposed phase  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpensePhaseID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseProjectID_input:
   """ Required : 
   ProposedProjectID
   ds
   """  
   def __init__(self, obj):
      self.ProposedProjectID:str = obj["ProposedProjectID"]
      """  The proposed project  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseProjectID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseQuickEntryCode_input:
   """ Required : 
   ProposedQuickEntryCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedQuickEntryCode:str = obj["ProposedQuickEntryCode"]
      """  The proposed quick entry code  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseQuickEntryCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseUnitRate_input:
   """ Required : 
   ProposedUnitRate
   ds
   """  
   def __init__(self, obj):
      self.ProposedUnitRate:int = obj["ProposedUnitRate"]
      """  The proposed unit rate  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseUnitRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmpExpenseUnits_input:
   """ Required : 
   ProposedUnits
   ds
   """  
   def __init__(self, obj):
      self.ProposedUnits:int = obj["ProposedUnits"]
      """  The proposed units  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class ChangeEmpExpenseUnits_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckRecallFromApproval_input:
   """ Required : 
   ipSalesRepCode
   ds
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class CheckRecallFromApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.outRecallMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyEmpExpenseByID_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      self.empExpenseNum:int = obj["empExpenseNum"]
      """  EmpExpense Number  """  
      pass

class CopyEmpExpenseByID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class CopyEmpExpense_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class CopyEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteExpense_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class DeleteExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EmpExpenseAfterGetRowsWrapper_input:
   """ Required : 
   empExpenseRow
   """  
   def __init__(self, obj):
      self.empExpenseRow:list[Erp_Tablesets_EmpExpenseRow] = obj["empExpenseRow"]
      pass

class EmpExpenseAfterGetRowsWrapper_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.empExpenseRow:list[Erp_Tablesets_EmpExpenseRow] = obj["empExpenseRow"]
      pass

      """  output parameters  """  

class EmpExpenseCommentAfterGetRowsWrapper_input:
   """ Required : 
   empExpenseCommentRow
   """  
   def __init__(self, obj):
      self.empExpenseCommentRow:list[Erp_Tablesets_EmpExpenseCommentRow] = obj["empExpenseCommentRow"]
      pass

class EmpExpenseCommentAfterGetRowsWrapper_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.empExpenseCommentRow:list[Erp_Tablesets_EmpExpenseCommentRow] = obj["empExpenseCommentRow"]
      pass

      """  output parameters  """  

class EmpExpenseRetrieveOptionsClause_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.empExpenseRetrieveOptionsClause:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_EmpExpenseAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmpID:str = obj["EmpID"]
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
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

class Erp_Tablesets_EmpExpenseCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense comment record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID links the comment to a specific EmpExpense record.  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpExpenseNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.SubmitCommentInstr:str = obj["SubmitCommentInstr"]
      """  Submit comment instructions  """  
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ExpEntryCommentTypeList:str = obj["ExpEntryCommentTypeList"]
      """  List of valid comment types for Expense Entry  """  
      self.CommentTypeDesc:str = obj["CommentTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpExpenseListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.UBFromEffectiveDate:str = obj["UBFromEffectiveDate"]
      """  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseTaxAmt:int = obj["DocExpenseTaxAmt"]
      """  The tax of the expense in the expense currency.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ChargeCurrencyCode:str = obj["ChargeCurrencyCode"]
      """  The charge currency.  This is derived from the currency on the related project.  """  
      self.ChargeExchangeRate:int = obj["ChargeExchangeRate"]
      """  The charge exchange rate.  This is derived from the exchange rate on the related project.  """  
      self.ChargeRateGrpCode:str = obj["ChargeRateGrpCode"]
      """  The charge rate group code.  This is derived from the rate group code on the related projec.t  """  
      self.DocChargeAmt:int = obj["DocChargeAmt"]
      """  The charge amount of the expense in the charge currency.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier number used on the employee of the expense.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The ap invoice number the expense was invoiced on.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line created for this expense.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.IsReversal:bool = obj["IsReversal"]
      """  Indicates if this expense is a reversal (full or partial) of an existing expense.  """  
      self.ReversedExpenseNum:int = obj["ReversedExpenseNum"]
      """  Reversed Expense Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ClaimExchangeRate:int = obj["ClaimExchangeRate"]
      """  The exchange rate between the claim currency and the base currency based on expense date.  """  
      self.ClaimLockRate:bool = obj["ClaimLockRate"]
      """  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ClaimRateGrpCode:str = obj["ClaimRateGrpCode"]
      """  The claim rate group code.  """  
      self.DocClaimTaxAmt:int = obj["DocClaimTaxAmt"]
      """  The tax of the claim in the claim currency.  """  
      self.DocClaimAmt:int = obj["DocClaimAmt"]
      """  The amount of the claim in the claim currency.  """  
      self.DocTotalClaimAmt:int = obj["DocTotalClaimAmt"]
      """  The total amount of the claim in the claim currency.  This value includes taxes.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.DocExpWithholdAmt:int = obj["DocExpWithholdAmt"]
      """  Expense Withholding Tax Amount.  """  
      self.DocClaimWithholdAmt:int = obj["DocClaimWithholdAmt"]
      """  Claim Withholding Tax Amount.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.DocChargeTaxAmt:int = obj["DocChargeTaxAmt"]
      """  The tax of the claim in the charge currency.  """  
      self.DocTotalChargeAmt:int = obj["DocTotalChargeAmt"]
      """  The total charge amount in the charge currency.  This value includes taxes.  """  
      self.ClaimToBaseExchangeRate:int = obj["ClaimToBaseExchangeRate"]
      """  The exchange rate between the claim currency and the base currency.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the misc charge jobmtl record  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number of the misc charge jobmtl record  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence of the misc charge jobmtl record  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates if the expense has been invoiced.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpCommentInstr:str = obj["ExpCommentInstr"]
      """  Expense Comment Instruction  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Indicates that this record has been process by the project analysis build process  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.VoucherReceiptNo:str = obj["VoucherReceiptNo"]
      """  The voucher or receipt number reference.  """  
      self.VoucherReceiptDate:str = obj["VoucherReceiptDate"]
      """  The date for the voucher/receipt reference  """  
      self.DocAdvanceBalance:int = obj["DocAdvanceBalance"]
      """  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  """  
      self.DocMatchedClaimAmt:int = obj["DocMatchedClaimAmt"]
      """  The amount that has been matched from advance requests to this expense.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this expense is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this expense is linked to  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order that this expense is linked to  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.UnitsLabel:str = obj["UnitsLabel"]
      """  The label value for Units field.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  A list of people who have approved the expense  """  
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      """  A list of people who need to approve the expense  """  
      self.DisplayStatus:str = obj["DisplayStatus"]
      """  External field to display a descriptive status of the record  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.IsSelected:bool = obj["IsSelected"]
      """  Indicates if this record is selected to be submitted  """  
      self.DispClaimAmt:int = obj["DispClaimAmt"]
      """  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.InvoiceStatus:str = obj["InvoiceStatus"]
      """  If invoiced, the status of the invoice.  """  
      self.ExpWeek:str = obj["ExpWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  """  
      self.ExpDay:str = obj["ExpDay"]
      """  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  """  
      self.ExpMonth:str = obj["ExpMonth"]
      """  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      """  Indicates if the record has been submitted or not  """  
      self.DispTotalClaimAmt:int = obj["DispTotalClaimAmt"]
      """  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.MultiCurrency:bool = obj["MultiCurrency"]
      """  Indicates if multi-currency is licensed  """  
      self.ExpenseDisableDelete:bool = obj["ExpenseDisableDelete"]
      self.ExpenseDisableUpdate:bool = obj["ExpenseDisableUpdate"]
      self.EnableClaimLockRate:bool = obj["EnableClaimLockRate"]
      self.APInvLineAmt:int = obj["APInvLineAmt"]
      self.APInvLineTaxAmt:int = obj["APInvLineTaxAmt"]
      self.APInvLineTotAmt:int = obj["APInvLineTotAmt"]
      self.EnableUnitRate:bool = obj["EnableUnitRate"]
      """  Indicates if UnitRate is enabled  """  
      self.EnableClaimCurrencyCode:bool = obj["EnableClaimCurrencyCode"]
      self.ExpenseCurrencyList:str = obj["ExpenseCurrencyList"]
      self.DispClaimTaxAmt:int = obj["DispClaimTaxAmt"]
      """  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user retrieving the record has access to view the row or not.  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available in approval entry  """  
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open approval task.  """  
      self.ChargeCurrencyBaseCurr:bool = obj["ChargeCurrencyBaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.ChargeCurrencyCurrencyID:str = obj["ChargeCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.ChargeCurrencyDocumentDesc:str = obj["ChargeCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ChargeCurrencyCurrName:str = obj["ChargeCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.ChargeCurrencyCurrDesc:str = obj["ChargeCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.ChargeCurrencyCurrSymbol:str = obj["ChargeCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.ChargeRateTypeDescription:str = obj["ChargeRateTypeDescription"]
      """  Description  """  
      self.ClaimCurrencyDocumentDesc:str = obj["ClaimCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ClaimCurrencyCurrName:str = obj["ClaimCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.ClaimCurrencyCurrDesc:str = obj["ClaimCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.ClaimCurrencyCurrSymbol:str = obj["ClaimCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.ClaimCurrencyCurrencyID:str = obj["ClaimCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.ClaimCurrencyBaseCurr:bool = obj["ClaimCurrencyBaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      """  Description  """  
      self.EmpBasicName:str = obj["EmpBasicName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      """  Last name of employee  """  
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      """  First name of employee.  """  
      self.ExpCurrencyCurrSymbol:str = obj["ExpCurrencyCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.ExpCurrencyCurrencyID:str = obj["ExpCurrencyCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.ExpCurrencyDocumentDesc:str = obj["ExpCurrencyDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.ExpCurrencyCurrName:str = obj["ExpCurrencyCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.ExpCurrencyCurrDesc:str = obj["ExpCurrencyCurrDesc"]
      """  Description of the currency  """  
      self.ExpCurrencyBaseCurr:bool = obj["ExpCurrencyBaseCurr"]
      """  Indicates if this is the base currency.  Only one base currency is allowed  """  
      self.PayMethodReimbursable:bool = obj["PayMethodReimbursable"]
      """  Reimbursable  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.ProjectDescription:str = obj["ProjectDescription"]
      """  Full description of Project Management Code.  """  
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      """  Description  """  
      self.PurMiscExpChargeable:bool = obj["PurMiscExpChargeable"]
      """  When an expense charge, indicates if the code is chargeable.  """  
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.PurMiscExpUnitBased:bool = obj["PurMiscExpUnitBased"]
      """  When an expense charge, indicates if the code is unit based.  """  
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      """  Description of the task set.  """  
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      """  The type of workflow of this task set.  Possible values are "CRM" - CRM related tasks and "ECO" - ECO tasks  """  
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      """  Full description for the Tax Region.  """  
      self.VendorCountry:str = obj["VendorCountry"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Third address line of the Supplier  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  First address line of the Supplier  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.VendorVendorID:str = obj["VendorVendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  """  
      self.VendorCity:str = obj["VendorCity"]
      """  City portion of the address of the Supplier  """  
      self.VendorState:str = obj["VendorState"]
      """  Can be blank.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Second address line of the Supplier  """  
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.VendorZIP:str = obj["VendorZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpExpenseListTableset:
   def __init__(self, obj):
      self.EmpExpenseList:list[Erp_Tablesets_EmpExpenseListRow] = obj["EmpExpenseList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpExpenseRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.ExpenseDate:str = obj["ExpenseDate"]
      """  The date of the expense.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the expense.  Can be used to group expense entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the expense record.  """  
      self.Indirect:bool = obj["Indirect"]
      """  Indicates if the expense is related to a project.  A value of true indicates the record is not related to a project.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  The project the expense is related to.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  The project phase the expense is related to.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the expense.  """  
      self.Units:int = obj["Units"]
      """  The number of units of this expense.  """  
      self.UnitRate:int = obj["UnitRate"]
      """  Rate per unit of the expense.  """  
      self.UBFromEffectiveDate:str = obj["UBFromEffectiveDate"]
      """  The FromEffectiveDate from ExpenseTypeUnitBased that was used to determine default values for Units and UnitRate.  This combined with ExpenseTypeCode point to a unique ExpenseTypeUnitBased record.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      """  The currency the expense occurred in.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Region for this expense.  """  
      self.DocExpenseTaxAmt:int = obj["DocExpenseTaxAmt"]
      """  The tax of the expense in the expense currency.  """  
      self.DocExpenseAmt:int = obj["DocExpenseAmt"]
      """  The amount of the expense in the expense currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  Indicates if the expense amount includes tax.  """  
      self.DocTotalExpenseAmt:int = obj["DocTotalExpenseAmt"]
      """  The total amount of the expense in the expense currency.  This value includes taxes.  """  
      self.ExpenseStatus:str = obj["ExpenseStatus"]
      """   The status of the expense.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.ChargeCurrencyCode:str = obj["ChargeCurrencyCode"]
      """  The charge currency.  This is derived from the currency on the related project.  """  
      self.ChargeExchangeRate:int = obj["ChargeExchangeRate"]
      """  The charge exchange rate.  This is derived from the exchange rate on the related project.  """  
      self.ChargeRateGrpCode:str = obj["ChargeRateGrpCode"]
      """  The charge rate group code.  This is derived from the rate group code on the related projec.t  """  
      self.DocChargeAmt:int = obj["DocChargeAmt"]
      """  The charge amount of the expense in the charge currency.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the expense received final approval.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The supplier number used on the employee of the expense.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  The ap invoice number the expense was invoiced on.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  The invoice line created for this expense.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.IsReversal:bool = obj["IsReversal"]
      """  Indicates if this expense is a reversal (full or partial) of an existing expense.  """  
      self.ReversedExpenseNum:int = obj["ReversedExpenseNum"]
      """  Reversed Expense Number  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ClaimExchangeRate:int = obj["ClaimExchangeRate"]
      """  The exchange rate between the claim currency and the base currency based on expense date.  """  
      self.ClaimLockRate:bool = obj["ClaimLockRate"]
      """  Used with the currency module.  When TRUE the claim currency rate can be changed by the user and cannot be changed by the system.  """  
      self.ClaimRateGrpCode:str = obj["ClaimRateGrpCode"]
      """  The claim rate group code.  """  
      self.DocClaimTaxAmt:int = obj["DocClaimTaxAmt"]
      """  The tax of the claim in the claim currency.  """  
      self.DocClaimAmt:int = obj["DocClaimAmt"]
      """  The amount of the claim in the claim currency.  """  
      self.DocTotalClaimAmt:int = obj["DocTotalClaimAmt"]
      """  The total amount of the claim in the claim currency.  This value includes taxes.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  The miscellaneous charge code for this expense.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The user who submitted the expense  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  Indicates if the record is tax exempt.  If field is non-blank it is considered exempt.  """  
      self.GetDfltTaxIds:bool = obj["GetDfltTaxIds"]
      """  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the expense before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  """  
      self.TaxConnectCalc:bool = obj["TaxConnectCalc"]
      """  If true, the EmpExpenseTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  """  
      self.DocExpWithholdAmt:int = obj["DocExpWithholdAmt"]
      """  Expense Withholding Tax Amount.  """  
      self.DocClaimWithholdAmt:int = obj["DocClaimWithholdAmt"]
      """  Claim Withholding Tax Amount.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  Indicates if the expense is reimbursable.  """  
      self.DocChargeTaxAmt:int = obj["DocChargeTaxAmt"]
      """  The tax of the claim in the charge currency.  """  
      self.DocTotalChargeAmt:int = obj["DocTotalChargeAmt"]
      """  The total charge amount in the charge currency.  This value includes taxes.  """  
      self.ClaimToBaseExchangeRate:int = obj["ClaimToBaseExchangeRate"]
      """  The exchange rate between the claim currency and the base currency.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the misc charge jobmtl record  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence number of the misc charge jobmtl record  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material sequence of the misc charge jobmtl record  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  Indicates if the expense has been invoiced.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Expense Comment  """  
      self.ExpCommentInstr:str = obj["ExpCommentInstr"]
      """  Expense Comment Instruction  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Indicates that this record has been process by the project analysis build process  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.VoucherReceiptNo:str = obj["VoucherReceiptNo"]
      """  The voucher or receipt number reference.  """  
      self.VoucherReceiptDate:str = obj["VoucherReceiptDate"]
      """  The date for the voucher/receipt reference  """  
      self.DocAdvanceBalance:int = obj["DocAdvanceBalance"]
      """  The remaining balance of the advance.  For advance request expense category, is initially set to the claim amount; will be zero for other categories.  Is reduced when other expenses that match the advance amount are invoiced.  """  
      self.DocMatchedClaimAmt:int = obj["DocMatchedClaimAmt"]
      """  The amount that has been matched from advance requests to this expense.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  The Sales order that this expense is linked to.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The line number of the sales order that this expense is linked to  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The release number of the sales order that this expense is linked to  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PartTranSysRowID:str = obj["PartTranSysRowID"]
      """  PartTranSysRowID  """  
      self.ExpenseAutoSubmit:bool = obj["ExpenseAutoSubmit"]
      """  ExpenseAutoSubmit  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.MobileExpense:bool = obj["MobileExpense"]
      """  MobileExpense  """  
      self.APInvLineAmt:int = obj["APInvLineAmt"]
      self.APInvLineTaxAmt:int = obj["APInvLineTaxAmt"]
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  A list of people who have approved the expense  """  
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open approval task.  """  
      self.DispClaimAmt:int = obj["DispClaimAmt"]
      """  The claim amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.DispClaimTaxAmt:int = obj["DispClaimTaxAmt"]
      """  The claim tax amount displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim tax amount.  """  
      self.DisplayStatus:str = obj["DisplayStatus"]
      """  External field to display a descriptive status of the record  """  
      self.DispTotalClaimAmt:int = obj["DispTotalClaimAmt"]
      """  The claim amount total displayed to the user.  If the expense is non-reimbursable, the user will see zero for the claim amount.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.EnableClaimCurrencyCode:bool = obj["EnableClaimCurrencyCode"]
      self.EnableClaimLockRate:bool = obj["EnableClaimLockRate"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available in approval entry  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EnableUnitRate:bool = obj["EnableUnitRate"]
      """  Indicates if UnitRate is enabled  """  
      self.ExpDay:str = obj["ExpDay"]
      """  Text to show the day of the week that corresponds to the EmpExpense.ExpenseDate (Sunday, Monday, etc)  """  
      self.ExpenseCurrencyList:str = obj["ExpenseCurrencyList"]
      self.ExpenseDisableDelete:bool = obj["ExpenseDisableDelete"]
      self.ExpenseDisableUpdate:bool = obj["ExpenseDisableUpdate"]
      self.ExpMonth:str = obj["ExpMonth"]
      """  Text to show the month  (January, February, etc) that corresponds to the EmpExpense.ExpenseDate  """  
      self.ExpWeek:str = obj["ExpWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the EmpExpense.ExpenseDate such as "5/2/2009 - 5/9/2009"  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user retrieving the record has access to view the row or not.  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the expense detail has attachments  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the expense detail has comments  """  
      self.InvoiceStatus:str = obj["InvoiceStatus"]
      """  If invoiced, the status of the invoice.  """  
      self.IsSelected:bool = obj["IsSelected"]
      """  Indicates if this record is selected to be submitted  """  
      self.MultiCurrency:bool = obj["MultiCurrency"]
      """  Indicates if multi-currency is licensed  """  
      self.NewDifDateFlag:bool = obj["NewDifDateFlag"]
      self.NotSubmitted:bool = obj["NotSubmitted"]
      """  Indicates if the record has been submitted or not  """  
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      """  A list of people who need to approve the expense  """  
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnitsLabel:str = obj["UnitsLabel"]
      """  The label value for Units field.  """  
      self.XRateLabel:str = obj["XRateLabel"]
      """  Exchange Rate Label  """  
      self.APInvLineTotAmt:int = obj["APInvLineTotAmt"]
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates of the row is selected for submit or recall  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.AppointmentIsAllDay:bool = obj["AppointmentIsAllDay"]
      """  Is calendar appointment all day  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ChargeCurrencyCurrSymbol:str = obj["ChargeCurrencyCurrSymbol"]
      self.ChargeCurrencyCurrDesc:str = obj["ChargeCurrencyCurrDesc"]
      self.ChargeCurrencyCurrName:str = obj["ChargeCurrencyCurrName"]
      self.ChargeCurrencyCurrencyID:str = obj["ChargeCurrencyCurrencyID"]
      self.ChargeCurrencyDocumentDesc:str = obj["ChargeCurrencyDocumentDesc"]
      self.ChargeCurrencyBaseCurr:bool = obj["ChargeCurrencyBaseCurr"]
      self.ChargeRateGrpDescription:str = obj["ChargeRateGrpDescription"]
      self.ClaimCurrencyCurrName:str = obj["ClaimCurrencyCurrName"]
      self.ClaimCurrencyBaseCurr:bool = obj["ClaimCurrencyBaseCurr"]
      self.ClaimCurrencyDocumentDesc:str = obj["ClaimCurrencyDocumentDesc"]
      self.ClaimCurrencyCurrSymbol:str = obj["ClaimCurrencyCurrSymbol"]
      self.ClaimCurrencyCurrDesc:str = obj["ClaimCurrencyCurrDesc"]
      self.ClaimCurrencyCurrencyID:str = obj["ClaimCurrencyCurrencyID"]
      self.CurrRateGrpDescription:str = obj["CurrRateGrpDescription"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.ExpCurrencyDocumentDesc:str = obj["ExpCurrencyDocumentDesc"]
      self.ExpCurrencyCurrSymbol:str = obj["ExpCurrencyCurrSymbol"]
      self.ExpCurrencyBaseCurr:bool = obj["ExpCurrencyBaseCurr"]
      self.ExpCurrencyCurrName:str = obj["ExpCurrencyCurrName"]
      self.ExpCurrencyCurrDesc:str = obj["ExpCurrencyCurrDesc"]
      self.ExpCurrencyCurrencyID:str = obj["ExpCurrencyCurrencyID"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodReimbursable:bool = obj["PayMethodReimbursable"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ProjPhaseDescription:str = obj["ProjPhaseDescription"]
      self.PurMiscExpUnitBased:bool = obj["PurMiscExpUnitBased"]
      self.PurMiscExpChargeable:bool = obj["PurMiscExpChargeable"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.TaskSetWorkflowType:str = obj["TaskSetWorkflowType"]
      self.TaskSetTaskSetDescription:str = obj["TaskSetTaskSetDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.VendorAddress1:str = obj["VendorAddress1"]
      self.VendorCurrencyCode:str = obj["VendorCurrencyCode"]
      self.VendorVendorID:str = obj["VendorVendorID"]
      self.VendorAddress2:str = obj["VendorAddress2"]
      self.VendorTermsCode:str = obj["VendorTermsCode"]
      self.VendorAddress3:str = obj["VendorAddress3"]
      self.VendorState:str = obj["VendorState"]
      self.VendorCountry:str = obj["VendorCountry"]
      self.VendorZIP:str = obj["VendorZIP"]
      self.VendorCity:str = obj["VendorCity"]
      self.VendorDefaultFOB:str = obj["VendorDefaultFOB"]
      self.VendorName:str = obj["VendorName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_EmpExpenseTableset:
   def __init__(self, obj):
      self.EmpExpense:list[Erp_Tablesets_EmpExpenseRow] = obj["EmpExpense"]
      self.EmpExpenseAttch:list[Erp_Tablesets_EmpExpenseAttchRow] = obj["EmpExpenseAttch"]
      self.EmpExpenseComment:list[Erp_Tablesets_EmpExpenseCommentRow] = obj["EmpExpenseComment"]
      self.EmpExpenseTax:list[Erp_Tablesets_EmpExpenseTaxRow] = obj["EmpExpenseTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_EmpExpenseTaxRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  The employee the expense record is for.  """  
      self.EmpExpenseNum:int = obj["EmpExpenseNum"]
      """  Internal identifier of the EmpExpense record.  This with EmpID makes the record unique.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Rate code  """  
      self.ECAcquisitionSeq:int = obj["ECAcquisitionSeq"]
      """   Used to allow a second tax record using the same tax code on an expense.  When the sales tax field EcAquisition is checked then 2 expense tax records are created.
NOTE:  This field is now used in VAT Reverse Charge logic.  If an invoice line is marked for Reverse Charge, a second line is created just like in the ECAcquisition logic. To distinguish the two scenarios, the ReverseCharge flag will be set to true if the second line is for Reverse Charge.  """  
      self.ExpReportableAmt:int = obj["ExpReportableAmt"]
      """  The reportable amount to the tax jurisdiction in the expense currency.  """  
      self.ClaimReportableAmt:int = obj["ClaimReportableAmt"]
      """  The reportable amount to the tax jurisdiction in the claim currency.  """  
      self.ExpTaxableAmt:int = obj["ExpTaxableAmt"]
      """  Taxable Amount for this expense in the expense currency  """  
      self.ClaimTaxableAmt:int = obj["ClaimTaxableAmt"]
      """  Taxable Amount for this expense in the claim currency.  """  
      self.Percent:int = obj["Percent"]
      """  The tax percentage rate that is used for this expense. This is defaulted from the SalesTax.Percent.  """  
      self.ExpTaxAmt:int = obj["ExpTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in the expense currency.  """  
      self.ClaimTaxAmt:int = obj["ClaimTaxAmt"]
      """  Sales Tax amount for the corresponding taxable sales amount in the claim currency  """  
      self.Manual:bool = obj["Manual"]
      """  Indicates if the tax calculations are to be performed manually.  When this field is set the Reportable, Taxable, and TaxAmount fields are enabled.  When it is NOT set these fields are DISABLED and the system will perform all of the Reportable, Taxable, and TaxAmount calculations.  Defaults from the SalesTax.Manual field.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date that the record was last changed  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time that the record was last change (seconds since midnight)  """  
      self.ReverseCharge:bool = obj["ReverseCharge"]
      """  Reverse Charge.  """  
      self.CollectionType:int = obj["CollectionType"]
      """  Collection Type  """  
      self.Timing:int = obj["Timing"]
      """  Timing of when to report taxes  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Resolution number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Resolution Date  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Tax Rate Date  """  
      self.ExpDefTaxableAmt:int = obj["ExpDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment.  In expense currency  """  
      self.ClaimDefTaxableAmt:int = obj["ClaimDefTaxableAmt"]
      """  Balance of the Taxable amount that has been deferred until payment.  In claim currency.  """  
      self.ExpDefTaxAmt:int = obj["ExpDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment.  In expense currency.  """  
      self.ClaimDefTaxAmt:int = obj["ClaimDefTaxAmt"]
      """  Balance of the Tax amount that has been deferred until payment.  In claim currency  """  
      self.ManAdd:bool = obj["ManAdd"]
      """  This record was manually added (not in Liability) but will use the standard calculations  """  
      self.ExpDedTaxAmt:int = obj["ExpDedTaxAmt"]
      """  Deducatable Tax Amount in expense currency  """  
      self.ClaimDedTaxAmt:int = obj["ClaimDedTaxAmt"]
      """  Deducatable Tax Amount in claim currency  """  
      self.ExpFixedAmount:int = obj["ExpFixedAmount"]
      """  Fixed Tax Amount in expense currency  """  
      self.ClaimFixedAmount:int = obj["ClaimFixedAmount"]
      """  Document Fixed Tax Amount in claim currency  """  
      self.TextCode:str = obj["TextCode"]
      """  Unique Identifier for Legal Text  """  
      self.ExpTaxAmtVar:int = obj["ExpTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate in expense currency  """  
      self.ClaimTaxAmtVar:int = obj["ClaimTaxAmtVar"]
      """  Difference between tax calculated in document rate less tax calculated in tax rate in claim currency  """  
      self.SysCalcClaimTaxableAmt:int = obj["SysCalcClaimTaxableAmt"]
      """  System calculated Taxable amount for this expense in the claim currency  """  
      self.SysCalcExpTaxableAmt:int = obj["SysCalcExpTaxableAmt"]
      """  System calculated Taxable amount for this expense in the expense currency.  """  
      self.SysCalcExpReportableAmt:int = obj["SysCalcExpReportableAmt"]
      """  System calculated reportable amount to the tax jurisdiction in the expense currency  """  
      self.SysCalcClaimReportableAmt:int = obj["SysCalcClaimReportableAmt"]
      """  System calculated reportable sales amount to the tax jurisdiction expressed in the claim currency.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ExpCurrencyCode:str = obj["ExpCurrencyCode"]
      self.ExpCurrencyDesc:str = obj["ExpCurrencyDesc"]
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      self.ClaimCurrencyDesc:str = obj["ClaimCurrencyDesc"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RateCodeDescription:str = obj["RateCodeDescription"]
      self.TaxCodeDescription:str = obj["TaxCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.SendAlertComplete:bool = obj["SendAlertComplete"]
      """  Completion of the task will send a Global Alert  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.TaskComment:str = obj["TaskComment"]
      """  Contains comments about the Task.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.NextTaskID:str = obj["NextTaskID"]
      """  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  Indentifies the nest milestone task sequence.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Link to the Task Set Detail  """  
      self.CreateOrder:bool = obj["CreateOrder"]
      """  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  """  
      self.SendAlertCreate:bool = obj["SendAlertCreate"]
      """  Creation of the task will send a Global Alert  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Defines the type of task this is.  From the TaskType table.  """  
      self.TaskVendorNum:int = obj["TaskVendorNum"]
      """  The Vendor number associated with this task.  """  
      self.TaskPurPoint:str = obj["TaskPurPoint"]
      """  The Vendor purchase point related to this task.  """  
      self.TaskPrcConNum:int = obj["TaskPrcConNum"]
      """  The purchasing contact person associated with this task.  """  
      self.TaskMktgCampaignID:str = obj["TaskMktgCampaignID"]
      """  Link to the Marketing Campaign related to this Task.  """  
      self.OtherSalesRepCode:str = obj["OtherSalesRepCode"]
      """  A salesperson that the assigned salesperson needs to contact to complete this task  """  
      self.CustomerCategory:bool = obj["CustomerCategory"]
      """  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  """  
      self.EngineeringCategory:bool = obj["EngineeringCategory"]
      """  Defines if this task is included in the Engineering category.  """  
      self.VendorCategory:bool = obj["VendorCategory"]
      """  Defines if this task is included in the Vendor category.  """  
      self.PersonalCategory:bool = obj["PersonalCategory"]
      """  Defines if this task is included in the Personal category.  """  
      self.ManagementCategory:bool = obj["ManagementCategory"]
      """  Defines if this task is included in the Management category.  """  
      self.OtherCategory:bool = obj["OtherCategory"]
      """  Defines if this task is included in the Other category.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  EmployeeName  """  
      self.TimeOrExp:str = obj["TimeOrExp"]
      """   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID, used only by Task Time and Expense search as a search results grid.  """  
      self.TransDate:str = obj["TransDate"]
      """  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum, used only by task time and expense approbal search as search results grid  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListTableset:
   def __init__(self, obj):
      self.TaskList:list[Erp_Tablesets_TaskListRow] = obj["TaskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtEmpExpenseTableset:
   def __init__(self, obj):
      self.EmpExpense:list[Erp_Tablesets_EmpExpenseRow] = obj["EmpExpense"]
      self.EmpExpenseAttch:list[Erp_Tablesets_EmpExpenseAttchRow] = obj["EmpExpenseAttch"]
      self.EmpExpenseComment:list[Erp_Tablesets_EmpExpenseCommentRow] = obj["EmpExpenseComment"]
      self.EmpExpenseTax:list[Erp_Tablesets_EmpExpenseTaxRow] = obj["EmpExpenseTax"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpExpenseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpExpenseTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpExpenseTableset] = obj["returnObj"]
      pass

class GetListExpenses_input:
   """ Required : 
   ipEmpID
   ipClaimRef
   ipExpenseStatus
   ipInvoiceNum
   ipInvoiceStatus
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipEmpID:str = obj["ipEmpID"]
      """  Employee id  """  
      self.ipClaimRef:str = obj["ipClaimRef"]
      """  Claim Reference  """  
      self.ipExpenseStatus:str = obj["ipExpenseStatus"]
      """  Expense Status  """  
      self.ipInvoiceNum:str = obj["ipInvoiceNum"]
      """  Invoice Number  """  
      self.ipInvoiceStatus:str = obj["ipInvoiceStatus"]
      """  Invoice Status  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  the absolute page  """  
      pass

class GetListExpenses_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpExpenseListTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_EmpExpenseListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEmpExpenseAttch_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class GetNewEmpExpenseAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpExpenseComment_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      pass

class GetNewEmpExpenseComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpExpenseForDate_input:
   """ Required : 
   empID
   expenseDate
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      self.expenseDate:str = obj["expenseDate"]
      """  Expense Date  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class GetNewEmpExpenseForDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpExpenseTax_input:
   """ Required : 
   ds
   empID
   empExpenseNum
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.empExpenseNum:int = obj["empExpenseNum"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewEmpExpenseTax_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewEmpExpense_input:
   """ Required : 
   ds
   empID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      pass

class GetNewEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRateCodeInfo_input:
   """ Required : 
   rateCode
   ds
   """  
   def __init__(self, obj):
      self.rateCode:str = obj["rateCode"]
      """  Proposed RateCode value  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class GetRateCodeInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsTran_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_TaskListTableset] = obj["ds"]
      pass

class GetRowsTran_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpExpenseTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseEmpExpense
   whereClauseEmpExpenseAttch
   whereClauseEmpExpenseComment
   whereClauseEmpExpenseTax
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseEmpExpense:str = obj["whereClauseEmpExpense"]
      self.whereClauseEmpExpenseAttch:str = obj["whereClauseEmpExpenseAttch"]
      self.whereClauseEmpExpenseComment:str = obj["whereClauseEmpExpenseComment"]
      self.whereClauseEmpExpenseTax:str = obj["whereClauseEmpExpenseTax"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpExpenseTableset] = obj["returnObj"]
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

class MobileGetRowsTran_input:
   """ Required : 
   includeComments
   includeAttachments
   ds
   """  
   def __init__(self, obj):
      self.includeComments:bool = obj["includeComments"]
      self.includeAttachments:bool = obj["includeAttachments"]
      self.ds:list[Erp_Tablesets_TaskListTableset] = obj["ds"]
      pass

class MobileGetRowsTran_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_EmpExpenseTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecallEmpExpense_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class RecallEmpExpense_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecallFromApprovalBySelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class RecallFromApprovalBySelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RecallFromApproval_input:
   """ Required : 
   ipSalesRepCode
   ds
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class RecallFromApproval_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SubmitForApprovalBySelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class SubmitForApprovalBySelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.messageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class SubmitSelected_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class SubmitSelected_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEmpExpenseTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtEmpExpenseTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_EmpExpenseTableset] = obj["ds"]
      pass

      """  output parameters  """  

